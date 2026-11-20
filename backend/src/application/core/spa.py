from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from application.core.pathings import FRONTEND_BUILD_ASSET_DIR, FRONTEND_BUILD_DIR
from application.core.settings.base import common_settings


def register_spa_routes(app: FastAPI) -> None:
    if not common_settings.IS_PROD:

        @app.get("/", include_in_schema=False)
        async def redirect_to_docs():
            return RedirectResponse(url="/docs#")

        return

    if FRONTEND_BUILD_ASSET_DIR.exists():
        app.mount(
            "/assets", StaticFiles(directory=FRONTEND_BUILD_ASSET_DIR), name="assets"
        )

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(full_path: str):
        if full_path == "api" or full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="API endpoint not found")

        if full_path:
            file_path = (FRONTEND_BUILD_DIR / full_path).resolve()
            if file_path.is_relative_to(FRONTEND_BUILD_DIR) and file_path.is_file():
                return FileResponse(file_path)

        index_path = FRONTEND_BUILD_DIR / "index.html"
        if index_path.is_file():
            return FileResponse(index_path)

        raise HTTPException(status_code=500, detail="Vite build not found.")
