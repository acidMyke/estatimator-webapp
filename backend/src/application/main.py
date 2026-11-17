from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

import uvicorn

BACKEND_DIR = Path(__file__).resolve().parents[2]


def serve() -> None:
    """Start the API server."""
    uvicorn.run(
        "application.server:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        reload_excludes=[
            "openapi.json",
            "openapi.json.sha256",
        ],
    )


def main():
    parser = ArgumentParser(
        description="Backend development and maintenance commands.",
    )
    parser.add_argument(
        "command",
        choices=["serve"],
    )

    args = parser.parse_args()

    commands = {
        "serve": serve,
    }

    commands[args.command]()


if __name__ == "__main__":
    main()
