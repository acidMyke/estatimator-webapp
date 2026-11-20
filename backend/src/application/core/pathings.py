from pathlib import Path

BACKEND_ROOT, REPO_ROOT = Path(__file__).resolve().parents[3:5]

OPENAPI_SPEC_PATH = BACKEND_ROOT / "openapi" / "spec.json"
OPENAPI_HASH_PATH = OPENAPI_SPEC_PATH.with_suffix(".json.sha256")

FRONTEND_DIR = REPO_ROOT / "web_app"
FRONTEND_CLIENT_PATH = FRONTEND_DIR / "src" / "api"
FRONTEND_BUILD_DIR = BACKEND_ROOT / "web_app_dist"
FRONTEND_BUILD_ASSET_DIR = FRONTEND_BUILD_DIR / "assets"
