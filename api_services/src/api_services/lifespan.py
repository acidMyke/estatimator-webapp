from contextlib import asynccontextmanager
from hashlib import sha256
from json import dumps
from pathlib import Path

from fastapi import FastAPI

REPO_ROOT = Path(__file__).resolve().parents[2]
OPENAPI_SPEC_PATH = REPO_ROOT / "openapi" / "spec.json"
OPENAPI_HASH_PATH = OPENAPI_SPEC_PATH.with_suffix(".json.sha256")
FRONTEND_DIR = REPO_ROOT / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    spec_changed = write_openapi_spec_and_hash(app)
    if spec_changed:
        print("openapi spec changed: regenerating ovral client")
        # TODO: @acidmyke add ovral client generator

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
