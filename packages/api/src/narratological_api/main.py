"""FastAPI application for narratological analysis."""

from contextlib import asynccontextmanager
from typing import Any
import logging
import json
import sys

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from narratological_api.routes import analysis, diagnostics, studies

class JSONFormatter(logging.Formatter):
    """JSON structured logger formatter."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        for key, value in record.__dict__.items():
            if key not in ["args", "asctime", "created", "exc_info", "exc_text", "filename", "funcName", "levelname", "levelno", "lineno", "message", "module", "msecs", "msg", "name", "pathname", "process", "processName", "relativeCreated", "stack_info", "thread", "threadName", "taskName"]:
                log_data[key] = value
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)

# Configure logging
logger = logging.getLogger("narratological_api")
logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(JSONFormatter())
logger.addHandler(_handler)

# Ensure uvicorn/fastapi loggers also use the JSON formatter if desired,
# but for now we focus on our application logger.


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Load the compendium on startup
    from narratological.loader import load_compendium

    app.state.compendium = load_compendium()
    yield
    # Cleanup on shutdown


app = FastAPI(
    title="Narratological Algorithmic Lenses API",
    description="API for narrative analysis using formalized algorithms from master storytellers",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(studies.router, prefix="/studies", tags=["studies"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
app.include_router(diagnostics.router, prefix="/diagnostics", tags=["diagnostics"])


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning("HTTP Exception", extra={"status_code": exc.status_code, "detail": exc.detail, "path": request.url.path})
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning("Validation Error", extra={"errors": exc.errors(), "path": request.url.path})
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "message": "Input validation failed"},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {exc}", exc_info=True, extra={"path": request.url.path})
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint with API information."""
    return {
        "name": "Narratological Algorithmic Lenses API",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/stats")
async def stats() -> dict[str, Any]:
    """API statistics."""
    from narratological.loader import load_compendium

    compendium = load_compendium()

    total_axioms = sum(len(s.axioms) for s in compendium.studies.values())
    total_algorithms = sum(len(s.core_algorithms) for s in compendium.studies.values())
    total_questions = sum(len(s.diagnostic_questions) for s in compendium.studies.values())

    return {
        "study_count": len(compendium.studies),
        "total_axioms": total_axioms,
        "total_algorithms": total_algorithms,
        "total_diagnostic_questions": total_questions,
        "categories": compendium.meta.categories,
        "sequence_pairs": len(compendium.get_sequence_pairs()),
    }
