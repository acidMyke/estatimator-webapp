# API Services

## Setup (One-time)

### Check if uv is installed

```sh
  uv -V
```

- **If it says "command not found":** You need to install uv, continue
- else, skip to [Application startup](#application-startup)

### uv installation

#### macOS / Linux

```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Application startup

Update dependencies

```sh
  uv sync
```

Start the api_service

```sh
  uvicorn app.main:app --reload --reload-exclude "openapi.json" --reload-exclude "openapi.json.sha256"
```
