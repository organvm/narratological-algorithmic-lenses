"""FastAPI application for narratological analysis."""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from narratological_api.routes import analysis, billing, diagnostics, studies


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
app.include_router(billing.router, prefix="/billing", tags=["billing"])


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
