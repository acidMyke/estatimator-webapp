import uvicorn


def main():
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


if __name__ == "__main__":
    main()
