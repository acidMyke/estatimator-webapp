#!/bin/sh
set -e

# Resolve repository root relative to the script location.
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$REPO_ROOT"

echo "=== Starting dependency installation ==="

# Python dependencies
echo ""
echo "=== Running uv sync in api_services ==="

if [ -d "api_services" ]; then
  (
    cd api_services
    uv sync
  )
  echo "Python dependencies installed successfully."
else
  echo "WARNING: Directory 'api_services' not found. Skipping."
fi

# Node.js dependencies
echo ""
echo "=== Running pnpm install in web_app ==="

if [ -d "web_app" ]; then
  (
    cd web_app
    pnpm install --frozen-lockfile
  )
  echo "Node.js dependencies installed successfully."
else
  echo "WARNING: Directory 'web_app' not found. Skipping."
fi

echo ""
echo "=== Dependency installation completed ==="