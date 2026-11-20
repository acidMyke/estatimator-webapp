# HDBee Price

A monorepo for the fullstack application HDBee Price with a FastAPI backend and a React SPA frontend.
The backend owns the API contract; the frontend generates its typed client from the backend's OpenAPI spec.

| Layer   | Path        | Stack                                                                  |
| ------- | ----------- | ---------------------------------------------------------------------- |
| API     | `./backend` | Python 3.15 · FastAPI · SQLModel/SQLAlchemy 2.0 · Alembic              |
| Web app | `./web_app` | React 19 · Vite · TanStack Router/Query/Form · Tailwind v4 · shadcn/ui |

Toolchain:

- backend uses `uv` + `ruff`
- the web app uses `pnpm` + `oxlint`/`oxfmt`

In production the backend may also serves the built SPA from `backend/web_app_dist`  
In development Vite serves the app on `:5001` and proxies `/api` to the backend on `:5000`

## Getting started (Dev Container)

Development happens inside the Dev Container, which provides the Python/Node toolchains
plus PostgreSQL, pgAdmin, and Mailpit. Don't install the toolchain on your host.

Make sure VScode & Docker is installed

1. Open the repo in VS Code → **Reopen in Container**.
2. `postCreate.sh` runs once (interactive): GitHub CLI login, git identity + signing key, JWT secret.
3. `postStart.sh` runs on every start: `uv sync` + `pnpm install --frozen-lockfile`.

### Run the backend

```sh
cd backend
uv run application
```

Backend: <http://127.0.0.1:5000> (in dev, `/` redirects to `/docs`). Connect to Postgres
at `postgis:5432` from inside the container.

### Run the web app

```sh
cd web_app
pnpm dev        # http://127.0.0.1:5001
```

## Cheat sheet

| Task              | Backend                                       | Web app           |
| ----------------- | --------------------------------------------- | ----------------- |
| Install deps      | `uv sync`                                     | `pnpm install`    |
| Dev server        | `uv run application`                          | `pnpm dev`        |
| Lint              | `uv run ruff check .`                         | `pnpm lint`       |
| Format            | `uv run ruff format .`                        | `pnpm fmt`        |
| Full check        | `uv run ruff check . && uv run ruff format .` | `pnpm check`      |
| Tests             | —                                             | `pnpm test:run`   |
| Regenerate client | (restart backend)                             | `pnpm exec orval` |

## Database migrations (Alembic)

Autogenerate only sees models that are imported in [`backend/src/application/models.py`](/backend/src/application/models.py)
(the `target_metadata` registry), please add the imports of new feature there.

```sh
cd backend
uv run alembic revision --autogenerate -m "describe change"   # create a revision
uv run alembic upgrade head                                   # apply pending revisions
uv run alembic downgrade -1                                   # roll back the last one
```

Autogenerate diffs against the `local` database, so the `postgis` service must be up

Make sure upgrade and downgrade works first before raising pull request

## How the layers couple

1. Backend startup writes `backend/openapi/spec.json` (+ `.sha256`)
2. If the hash changed, it runs `pnpm orval` in `web_app/` directory
3. `orval` generates a typed Tanstack React Query + axios client into `web_app/src/api/` and Zod schemas into `web_app/src/api/index.zod.ts`

Change the backend schema to change the frontend types — never hand-edit generated code
(`web_app/src/api/*`, `web_app/src/routeTree.gen.ts`, `backend/openapi/spec.json`).

## Layout

```
backend/
├── alembic/versions/        # migrations
├── openapi/spec.json        # GENERATED
└── src/
    ├── application/
    │   ├── core/            # db, security, mailer, settings, paths
    │   ├── clients/         # generated Mailjet client
    │   └── features/<x>/    # models · service · router · deps
    └── ml/                  # standalone ML module (import-light)

web_app/src/
├── routes/                  # file-based TanStack Router routes
├── api/                     # GENERATED orval client
├── components/{ui,form}/    # shadcn/ui + TanStack Form fields
└── hooks/                   # useAppForm composition
```

## Conventions in one breath

- Feature folders under `features/<feature>/`, routers wired centrally in `application/server.py`
- SQLModel-first models with shared `IdMixin` / `TimestampMixin` / `SoftDeleteMixin`; prefer soft delete
- Sync DB sessions only — don't introduce an async engine
- Frontend imports use **`#`-prefixed aliases** (`#components/ui/...`), not `@/...`
- Forms go through `useAppForm` (`#hooks/form`); data fetching uses TanStack Query with `queryOptions` prefetched in route loaders
