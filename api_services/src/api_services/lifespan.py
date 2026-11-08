import subprocess
from contextlib import asynccontextmanager
from hashlib import sha256
from json import dumps
from pathlib import Path

from fastapi import FastAPI

BACKEND_ROOT, REPO_ROOT = Path(__file__).resolve().parents[2:4]
OPENAPI_SPEC_PATH = BACKEND_ROOT / "openapi" / "spec.json"
OPENAPI_HASH_PATH = OPENAPI_SPEC_PATH.with_suffix(".json.sha256")
FRONTEND_DIR = REPO_ROOT / "web_app"
FRONTEND_CLIENT_PATH = FRONTEND_DIR / "src" / "api"


@asynccontextmanager
async def lifespan(app: FastAPI):
    spec_changed = write_openapi_spec_and_hash(app)
    client_api_empty = not FRONTEND_CLIENT_PATH.is_dir() or not any(
        FRONTEND_CLIENT_PATH.iterdir()
    )
    if spec_changed or client_api_empty:
        print("openapi spec changed: regenerating ovral client")
        generate_orval_client()

    yield


def write_openapi_spec_and_hash(app: FastAPI) -> bool:
    openapi_spec = app.openapi()
    serialized_spec = dumps(openapi_spec, indent=2, sort_keys=True) + "\n"
    current_hash = sha256(serialized_spec.encode("utf-8")).hexdigest()

    previous_hash = None
    if OPENAPI_HASH_PATH.exists():
        previous_hash = OPENAPI_HASH_PATH.read_text(encoding="utf-8").strip() or None

    OPENAPI_SPEC_PATH.parent.mkdir(parents=True, exist_ok=True)
    OPENAPI_SPEC_PATH.write_text(serialized_spec, encoding="utf-8")
    OPENAPI_HASH_PATH.write_text(f"{current_hash}\n", encoding="utf-8")

    return current_hash != previous_hash


def generate_orval_client():
    try:
        subprocess.run(
            ["vp", "exec", "orval"],
            check=True,
            cwd=FRONTEND_DIR,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )
    except (
        FileNotFoundError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        PermissionError,
    ):
        print("failed to generate orval client")
