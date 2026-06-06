import json
import subprocess
import sys
import time
import urllib.request


def main():
    print("Starting FastAPI server...")
    proc = subprocess.Popen(
        ["uv", "run", "uvicorn", "narratological_api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for server to start
    time.sleep(3)

    # Check if process is still running
    if proc.poll() is not None:
        print("Error: FastAPI server failed to start.")
        stdout, stderr = proc.communicate()
        print("STDOUT:", stdout.decode())
        print("STDERR:", stderr.decode())
        sys.exit(1)

    endpoints = [
        ("Root", "/"),
        ("Health", "/health"),
        ("Stats", "/stats"),
        ("Studies", "/studies/"),
        ("Diagnostic Metrics", "/diagnostics/metrics")
    ]

    success = True
    for name, path in endpoints:
        url = f"http://127.0.0.1:8000{path}"
        print(f"Testing {name} ({url})... ", end="")
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = response.read().decode('utf-8')
                    # Parse json to verify it's valid
                    parsed = json.loads(data)
                    print(f"PASS (keys: {list(parsed.keys()) if isinstance(parsed, dict) else len(parsed) if isinstance(parsed, list) else type(parsed)})")
                else:
                    print(f"FAIL (status {response.status})")
                    success = False
        except Exception as e:
            print(f"FAIL with exception: {e}")
            success = False

    print("Stopping FastAPI server...")
    proc.terminate()
    proc.wait()
    print("Server stopped.")

    if success:
        print("All API endpoints smoke-tested successfully!")
        sys.exit(0)
    else:
        print("Some API endpoints failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
