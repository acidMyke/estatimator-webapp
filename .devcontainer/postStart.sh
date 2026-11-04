#!/bin/bash
set -e

echo "=== Running uv sync in api_services ==="
if [ -d "api_services" ]; then
  (cd api_services && uv sync)
else
  echo "Directory 'api_services' not found. Skipping uv sync."
fi

echo ""
echo "=== Running pnpm install in web_app ==="
if [ -d "web_app" ]; then
  (cd web_app && pnpm install)
else
  echo "Directory 'web_app' not found. Skipping pnpm install."
fi