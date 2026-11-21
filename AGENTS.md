# AGENTS.md

Guidance for AI coding agents working in this repository. Read this before making changes.

## Project Overview

**Estimator Web Application** (`hdbeeprice`) is a monorepo containing two independently-run subprojects:

| Layer                 | Path        | Stack                                                                                                                                                                       |
| --------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Backend (Python)      | `./backend` | Python ≥3.14 (toolchain pinned to 3.15), FastAPI, SQLModel + SQLAlchemy 2.0 (sync engine), Alembic, PostgreSQL (`psycopg`), managed with `uv`, formatted/linted with `ruff` |
| Frontend (TypeScript) | `./web_app` | React 19, Vite via pnpm, TanStack Router (file-based) + TanStack Query + TanStack Form, Tailwind CSS v4, shadcn/ui (Base UI flavor), `orval`, `oxfmt`/`oxlint`, Vitest      |

The backend owns the API contract. On startup it writes an OpenAPI spec (`backend/openapi/spec.json`), and the frontend generates its typed API client from that spec via `orval`. **Treat the backend OpenAPI spec as the single source of truth for API types.** In production the backend also serves the built SPA from `backend/web_app_dist`; in development Vite serves the app and proxies `/api` to the backend.

**This app is designed to be developed inside the Dev Container** (`.devcontainer/`), which already provisions Python/Node toolchains and the database/mail services — see "Development Environment (devcontainer)" below.

## Development Environment (devcontainer)

Open the repository with **"Reopen in Container"** (VS Code / Dev Containers) and work from `/hdbeeprice` inside it. Do not replicate the toolchain on the host, and do not `docker compose up` the stack yourself — the container starts it.

| Piece        | Details                                                                                                                                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Container    | `ghcr.io/astral-sh/uv:python3.15-trixie` + Node 24 / pnpm, `gh`, `jq`/`yq`, git, zsh; compose service `dev-container`, workspace folder `/hdbeeprice`                                                                                   |
| Services     | `postgis` (`postgis/postgis:17-3.5-alpine`, container `5432`, host `5433`, volume `pgdata`), `pgadmin` (`http://localhost:5050`, pre-wired to PostGIS), `mailpit` (SMTP `1025`, UI `http://localhost:8025`)                             |
| Injected env | `POSTGRES_USER=postgres`, `POSTGRES_PASSWORD` (compose default, override with the `POSTGRES_PASSWORD` host variable), `POSTGRES_DB=localdb`, `POSTGRES_HOST=postgis`, `POSTGRES_PORT=5432`, `MAILPIT_HOST=mailpit`, `MAILPIT_PORT=8025` |
| Lifecycle    | `postCreateCommand`: `zsh .devcontainer/postCreate.sh`; `postStartCommand`: `zsh .devcontainer/postStart.sh`                                                                                                                            |

- **Connect to PostgreSQL as `postgis:5432` from inside the container.** `localhost:5433` only works from the host. Because `POSTGRES_*` and `MAILPIT_*` are injected by compose, `backend/.env` only needs the settings that compose doesn't provide (`JWT_SECRET_KEY`, `DEBUG`, `ADMIN_ALLOWED_EMAIL_DOMAINS`, Mailjet keys, ...).
- `postCreate.sh` is an **interactive one-time setup**: GitHub CLI web login, git `user.name`/`user.email`, an SSH commit-signing key uploaded to GitHub, `origin` → `https://github.com/acidMyke/estatimator-webapp.git`, `uv tool install --with ipykernel jupyterlab`, and a generated `JWT_SECRET_KEY` written into `backend/.env`. If it aborts, rerun it from the repo root (`zsh .devcontainer/postCreate.sh`); it is safe to re-run.
- `postStart.sh` runs `uv sync` (backend) and `pnpm install --frozen-lockfile` (web_app) on **every** container start. Keep `pyproject.toml`/`uv.lock` and `package.json`/`pnpm-lock.yaml` in sync and committed, otherwise the container cannot install dependencies on start.
- Ports used inside the container: Vite dev server `127.0.0.1:5001` (`pnpm dev`), FastAPI `127.0.0.1:5000`, PostgreSQL `postgis:5432`. Mailpit UI (`:8025`) and pgAdmin (`:5050`) are published on the host. No `forwardPorts` are declared — VS Code forwards listening ports automatically.
- Agents: run every `uv`/`pnpm`/`ruff` command **inside** the container (that is where the toolchains and services live), and prefer the container's env over hardcoding connection strings.

## Repository Layout

```
hdbeeprice/
├── AGENTS.md                        # this file
├── README.md                        # root setup pointers
├── .agents/skills/                  # agent skills (see "Available Skills")
│   ├── router-query-integration/
│   ├── shadcn/
│   └── sqlmodel-orm-dbhelper/
├── .devcontainer/                   # primary dev environment (see "Development Environment")
│   ├── devcontainer.json            # compose-based; uv python:3.15 image + node/pnpm/gh features
│   ├── dev-compose.yml              # dev-container + postgis + pgadmin + mailpit
│   ├── postCreate.sh                # gh login, git identity + signing key, JWT secret
│   ├── postStart.sh                 # uv sync + pnpm install --frozen-lockfile
│   └── devcontainer-lock.json
├── .vscode/settings.json            # oxc + ruff + vitest wiring; routeTree.gen.ts marked read-only
├── backend/                         # Python backend (project/distribution name: `application`)
│   ├── .env / .env.example          # settings for every `core/settings` class (never commit .env)
│   ├── .python-version              # 3.15
│   ├── pyproject.toml               # deps + ruff config + `application` console script
│   ├── uv.lock
│   ├── alembic.ini                  # script_location = alembic, post-write hook runs `uv run ruff format`
│   ├── alembic/
│   │   ├── env.py                   # uses database_engine + application.models.target_metadata
│   │   └── versions/                # migration scripts
│   ├── openapi/
│   │   ├── spec.json(+.sha256)      # GENERATED at startup — do not hand-edit
│   │   └── external/                # vendored third-party specs (mailjet.json, filtered-mailjet.json)
│   ├── src/
│   │   ├── application/
│   │   │   ├── main.py              # `uv run application` → uvicorn application.server:app on 0.0.0.0:5000
│   │   │   ├── server.py            # FastAPI app, /api router wiring, SPA route registration
│   │   │   ├── lifespan.py          # writes OpenAPI spec + hash, regenerates the orval client
│   │   │   ├── models.py            # imports every feature model; target_metadata = SQLModel.metadata
│   │   │   ├── core/
│   │   │   │   ├── database.py      # sync engine + DatabaseSession dependency
│   │   │   │   ├── models.py        # IdMixin / TimestampMixin / SoftDeleteMixin
│   │   │   │   ├── security.py      # argon2 hashing, JWT encode/decode, session tokens
│   │   │   │   ├── mailer.py        # Mailjet sending via the generated client
│   │   │   │   ├── pathings.py      # repo paths (openapi spec, web_app/, web_app_dist/)
│   │   │   │   ├── spa.py           # serves the built SPA in prod, redirects / to /docs in dev
│   │   │   │   └── settings/        # pydantic-settings: base, database, security, email, datasource
│   │   │   ├── clients/             # generated Mailjet client (openapi-python-client)
│   │   │   └── features/
│   │   │       └── <feature>/{models,service,router,deps}.py
│   │   └── ml/                      # separate top-level module shipped in the same distribution
│   └── web_app_dist/                # frontend build output (gitignored)
└── web_app/                         # TypeScript frontend
    ├── package.json                 # scripts: dev, build, preview, generate-routes, test, lint, fmt, check
    ├── vite.config.ts               # dev server 127.0.0.1:5001, /api proxy → :5000, build → ../backend/web_app_dist
    ├── .oxfmtrc.json                # formatter config (OXC)
    ├── .oxlintrc.json               # linter config (OXC, type-aware)
    ├── orval.config.ts              # generates src/api from ../backend/openapi/spec.json
    ├── components.json              # shadcn/ui config (base-vega, Base UI, `#` aliases)
    ├── tsconfig.json                # strict TS, `#`-prefixed path aliases (no `@/*`)
    └── src/
        ├── main.tsx                 # createRouter + RouterProvider (defaultPreload 'intent')
        ├── router.tsx               # getRouter() factory (same defaults + defaultPreloadStaleTime: 0)
        ├── routeTree.gen.ts         # GENERATED — do not edit
        ├── styles.css               # Tailwind v4 entry, theme tokens, fonts
        ├── routes/                  # file-based routes (__root.tsx, index.tsx, ...)
        ├── api/                     # GENERATED by orval — do not edit
        ├── components/
        │   ├── ui/                  # shadcn/ui components (CLI-generated)
        │   └── form/                # pre-bound TanStack Form field components
        ├── hooks/                   # form-context.ts + form.ts (useAppForm)
        └── lib/utils.ts             # `cn` re-export
```

## Backend — `backend`

### Setup & run

Run all commands from `backend/`.

```sh
uv sync                     # install/update deps
cp .env.example .env        # inside the devcontainer postCreate.sh at least writes JWT_SECRET_KEY into backend/.env
uv run uvicorn application.server:app --reload \
  --reload-exclude "openapi/spec.json" --reload-exclude "openapi/spec.json.sha256"
uv run application          # equivalent console script (application.main:main, 0.0.0.0:5000, reload on)
```

- The project/distribution name is **`application`** and the src layout is `backend/src/application/`, so the ASGI import path is **`application.server:app`**. `backend/README.md` still shows `app.main:app` — that is stale.
- Startup runs `application/lifespan.py`: it serializes `app.openapi()` to `openapi/spec.json`, writes `openapi/spec.json.sha256`, and shells out to `pnpm orval` inside `web_app/` when the hash changed (or `web_app/src/api/` is empty). Keep the reload excludes above, otherwise the watcher restarts on every spec write.
- `IS_PROD=false` (default) makes `core/spa.py` redirect `/` to `/docs`; with `IS_PROD=true` it serves `backend/web_app_dist` (SPA fallback) and `/assets` from the build.

### Environment / settings

Settings are one `.env` read by several `BaseAppSettings` subclasses in `src/application/core/settings/`:

| Module          | Settings                                                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base.py`       | `IS_PROD`, `DEBUG`                                                                                                                                                                   |
| `database.py`   | `POSTGRES_USER`, `POSTGRES_PASSWORD` (**required**), `POSTGRES_DB`, `POSTGRES_HOST`, `POSTGRES_PORT`, `SQL_ECHO` → builds `sync_connection_string` / `async_connection_string`       |
| `security.py`   | `JWT_SECRET_KEY` (**required**, ≥64 hex chars), `JWT_ISSUER`, `JWT_ALGORITHM`, `USER_SESSION_TOKEN_EXPIRE_DAYS`, `ADMIN_SESSION_TOKEN_EXPIRE_MINUTES`, `ADMIN_ALLOWED_EMAIL_DOMAINS` |
| `email.py`      | `MAILJET_API_KEY`, `MAILJET_API_SECRET`, `FROM_EMAIL`, `FROM_NAME`, `MAILPIT_HOST`, `MAILPIT_PORT` (Mailjet sending is skipped while the API key/secret are unset)                   |
| `datasource.py` | placeholder for future data.gov.sg / OneMap / URA tokens                                                                                                                             |

Add a new env var as a field on the relevant settings class **and** to `.env.example`; new variables must also be provisioned in the deployed environment.

### Lint & format

```sh
uv run ruff check .          # lint
uv run ruff check . --fix    # autofix
uv run ruff format .         # format
```

Ruff config lives in `pyproject.toml` (`src = ["src"]`, first-party `application`, `ignore = ["EXE002"]`). Alembic runs `uv run ruff format` on every generated revision (`[post_write_hooks]` in `alembic.ini`).

### Database migrations (Alembic)

`alembic/env.py` imports `application.core.database.database_engine`, `application.core.settings.database.database_settings` and `application.models.target_metadata`. To pick up a new model in autogenerate you **must** import it in `src/application/models.py`.

```sh
uv run alembic revision --autogenerate -m "describe change"
uv run alembic upgrade head
uv run alembic downgrade -1
```

### Architecture & conventions

- **Feature-oriented structure**: each domain lives in `src/application/features/<feature>/` with these file roles:
  - `models.py` — SQLModel tables + request/response schemas
  - `service.py` — business logic operating on a `Session`
  - `router.py` — FastAPI `APIRouter` endpoints
  - `deps.py` — FastAPI dependencies (auth, current user, ...)
  - Some features only need a subset (`users`/`admin` have `models` + `service`).
- **Router wiring happens in `application/server.py`**, not `main.py`: a single `api_router = APIRouter(prefix="/api")` mounts each feature router with an explicit `prefix=` and `tags=[...]` (e.g. `auth` → `/api/auth`, `admin_auth` → `/api/admin/auth`). Tags drive orval grouping; `features/health/router.py` is mounted with `include_in_schema=False`.
- **Models**: SQLModel-first. Use the shared mixins from `core/models.py`:
  - `IdMixin` → UUID primary key (`uuid4`)
  - `TimestampMixin` → `created_at` / `updated_at` (UTC)
  - `SoftDeleteMixin` → `deleted_at` (nullable, indexed)
  - Prefer soft deletes (`deleted_at == None` filters) over hard deletes.
  - Use `TYPE_CHECKING` imports to avoid circular imports between `users`/`admin` and `auth`/`admin_auth` models.
- **Database is synchronous**: `core/database.py` uses `create_engine` + `sqlmodel.Session` and injects it via `DatabaseSession = Annotated[Session, Depends(...)]`. `sqlalchemy[asyncio]`/`greenlet` are installed and `database_settings.async_connection_string` exists, but nothing uses an async engine today — do **not** introduce `AsyncSession`/async engine without coordinating, it would break Alembic and the existing services.
- **Pydantic schemas** (request/response bodies) live alongside the models; base "table-less" models are plain `SQLModel` classes, table models set `table=True`.
- **Security** (`core/security.py`): argon2 for password/OTP hashing, PyJWT for ephemeral tokens and short verification flows, opaque random `secrets.token_urlsafe` session tokens stored in httpOnly, `secure`, `samesite="lax"` cookies. Do not leak secrets to logs.
- **Email** (`core/mailer.py`): sends through the generated Mailjet client in `src/application/clients/mailjet_send/`, produced with `openapi-python-client` from `openapi/external/filtered-mailjet.json`. Regenerate that client instead of hand-editing it; `application/clients/__init__.py` re-exports `MailjetClient`.
- **Paths** (`core/pathings.py`): the one place that resolves repo-relative locations (`openapi/spec.json`, `web_app/`, `web_app_dist/`). Use it instead of recomputing `Path(__file__).parents[...]`.
- **`src/ml/`** is a second top-level module shipped in the same distribution (`[tool.uv.build-backend] module-name = ["application", "ml"]`). Keep it import-light so it can be used without pulling the FastAPI app in.

### Backend guardrails

These files carry an explicit "discuss with the maintainer (JJ) before changing" header — changes there may be refactored or reverted:

- `src/application/core/database.py`
- `src/application/core/security.py`

In `src/application/core/settings/` only **add** fields/classes (plus `.env.example` entries) — don't restructure the package.

## Frontend — `web_app`

### Setup & run

Run all commands from `web_app/`. The toolchain is **`pnpm`**.

```sh
pnpm install               # install deps
pnpm dev                   # vite dev server: 127.0.0.1:5001 (strictPort), proxies /api → 127.0.0.1:5000
pnpm build                 # production build → ../backend/web_app_dist (gitignored)
pnpm preview               # serve the build
pnpm generate-routes       # tsr generate (the router plugin also regenerates on the fly in dev)
pnpm test / pnpm test:run  # vitest (script exists; there is no vitest config or test file yet)
pnpm exec orval            # regenerate src/api/* from the backend OpenAPI spec
```

> The dev server runs on a fixed port because the backend CORS/proxy setup expects it; `strictPort` means it fails instead of silently moving to another port. If `tsr` / `orval` report "not found in node_modules/.bin", the install is incomplete — re-run `pnpm install`. `pnpm dlx <package>` can run a binary without adding it as a dependency.

### Format & lint

Formatting and linting use the **OXC toolchain**, configured in `web_app/.oxfmtrc.json` and `web_app/.oxlintrc.json` (not Prettier/ESLint, and no longer inside `vite.config.ts`). VS Code is wired to the OXC extension via `.vscode/settings.json`.

```sh
pnpm fmt           # format (oxfmt) — rewrites files
pnpm fmt:check     # verify formatting
pnpm lint          # oxlint (type-aware, tsgolint enabled)
pnpm lint:fix      # oxlint --fix
pnpm check         # oxfmt --check && oxlint && tsc --noEmit
```

Formatting rules (`.oxfmtrc.json`): `printWidth: 120`, single quotes including JSX, `arrowParens: "avoid"`, trailing commas, sorted imports, `quoteProps: "consistent"`; ignores `dist/**` and `*.gen.ts`. `pnpm check` must pass before finishing.

### Path aliases

`tsconfig.json` only defines **`#`-prefixed** aliases — there is no `@/*` mapping, so `@/components/...` will **not** resolve:

| Alias                                                               | Target                       |
| ------------------------------------------------------------------- | ---------------------------- |
| `#/*`                                                               | `./src/*`                    |
| `#api/*`, `#components/*`, `#ui/*`, `#form/*`, `#lib/*`, `#hooks/*` | matching `./src/*` subfolder |
| `#utils`                                                            | `./src/lib/utils`            |

Use these (or relative imports within the same folder, e.g. `./field-errors`). shadcn's `components.json` aliases point at `#components`, `#ui`, `#lib`, `#hooks`, `#utils`, so CLI-added components already use this style.

### Architecture & conventions

- **File-based routing** (TanStack Router). Add routes as files under `src/routes/`; `src/routeTree.gen.ts` is generated by `@tanstack/router-plugin` — never edit it (also read-only in `.vscode/settings.json`). `src/main.tsx` creates the router (`defaultPreload: 'intent'`, `scrollRestoration`) and renders `RouterProvider`; `src/router.tsx` exposes an equivalent `getRouter()` factory (plus `defaultPreloadStaleTime: 0`) for tooling/SSR-style usage. `src/routes/__root.tsx` mounts the router + form devtools.
- **Data fetching**: TanStack Query. Follow the `router-query-integration` skill — define `queryOptions` helpers, prefetch in route loaders with `queryClient.ensureQueryData(...)`, then consume with `useQuery`/`useSuspenseQuery`. Generated hooks live in `src/api/`.
- **Forms**: use the composed `useAppForm` hook — see "Forms (TanStack Form)" below. Don't call `useForm` directly in routes.
- **TypeScript is strict**: `strict`, `noUnusedLocals`, `noUnusedParameters`, `noFallthroughCasesInSwitch`, `noUncheckedSideEffectImports`, `verbatimModuleSyntax` are enabled. Type-only imports must use `import type`.
- **Styling**: Tailwind CSS v4 via `@tailwindcss/vite`; the entry is `src/styles.css` (`@import 'tailwindcss'`, `tw-animate-css`, `shadcn/tailwind.css`, Geist Mono + Manrope fonts, theme tokens). `cn` lives in `src/lib/utils.ts` and is a re-export of the `cn` package.
- **shadcn/ui**: components live in `src/components/ui/` and are CLI-generated — add new ones with the `shadcn` skill/CLI rather than hand-writing, and prefer wrapping them in `src/components/` for app-specific composition.

### Forms (TanStack Form)

The app uses a **composition layer** over TanStack Form, so routes never wire inputs by hand:

- `src/hooks/form-context.ts` — `createFormHookContexts()` (exports `fieldContext`, `formContext`, `useFieldContext`, `useFormContext`). It is a separate module on purpose: field components consume `useFieldContext` without creating an import cycle with `form.ts`.
- `src/hooks/form.ts` — `createFormHook(...)` exporting `useAppForm` (plus `withForm`, `withFieldGroup`, `useTypedAppFormContext`, `extendForm`) and re-exporting the contexts. Registered components:
  - `fieldComponents`: `TextField`, `TextareaField`, `NumberField`, `SelectField`, `CheckboxField`, `SwitchField`
  - `formComponents`: `SubmitButton`
- `src/components/form/` — the pre-bound components. Each one reads `useFieldContext<T>()`, wraps a shadcn `Field` (label, optional description, error) around a `#components/ui` control, binds `value`/`onChange` (or `checked`/`onCheckedChange`) and `onBlur`, and renders `FieldError` once the field is touched. `field-errors.tsx` holds the shared `useFieldErrorState` (reactive through `useSelector(field.store, ...)`) and `toErrorMessages`, which normalizes string/`{ message }`/`Error` errors into what `FieldError` expects.

Expected field value types:

| Component                      | Field value                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TextField`, `TextareaField`   | `string` (empty input stays `''`)                                                                                                                                   |
| `NumberField`                  | `number \| null` — empty/invalid input writes `null`; type the default as `null as number \| null` so the key is not inferred as `null` and dropped from `DeepKeys` |
| `CheckboxField`, `SwitchField` | `boolean`                                                                                                                                                           |
| `SelectField`                  | the `TValue` union of the `options` (`value` of the selected option; it is generic and type-checked against the field)                                              |

Usage:

```tsx
const form = useAppForm({
  defaultValues: { name: '', role: 'admin' as 'admin' | 'user' },
  onSubmit: ({ value }) => {
    /* call the generated API mutation */
  },
});

<form
  onSubmit={event => {
    event.preventDefault();
    void form.handleSubmit();
  }}
>
  <form.AppField name='name' children={field => <field.TextField label='Name' />} />
  <form.AppField
    name='role'
    children={field => <field.SelectField label='Role' options={[{ label: 'Admin', value: 'admin' }]} />}
  />
  <form.AppForm>
    <form.SubmitButton>Save</form.SubmitButton>
  </form.AppForm>
</form>;
```

Form components (e.g. `SubmitButton`) read the form context from `<form.AppForm>` — rendering `<form.SubmitButton>` outside that wrapper throws `` `formContext` only works when within a `formComponent` passed to `createFormHook` ``. `SubmitButton` renders `pendingLabel` (default `Submitting...`) and sets `disabled`/`aria-busy` while the form is submitting.

Adding a field component:

1. Create `src/components/form/<name>-field.tsx` (no barrel file — import it as `#form/<name>-field`).
2. Type props as `Omit<ComponentProps<typeof Control>, 'id' | 'value' | 'onChange' | 'onBlur'>` (plus `label`/`description`), spread caller props **first** and then the bound props so the hook wiring always wins.
3. Register it under `fieldComponents` in `src/hooks/form.ts`.

### Generated code — do not edit by hand

- `src/routeTree.gen.ts` — generated by `@tanstack/router-plugin` (also marked read-only in `.vscode/settings.json`)
- `src/api/*.ts` and `src/api/index.zod.ts` — generated by `orval` from the backend OpenAPI spec

If a generated API type or endpoint is wrong, change the backend and regenerate — do not patch the generated files.

## API Contract Workflow

The two subprojects are coupled only through the OpenAPI spec:

1. Backend startup → `application/lifespan.py` serializes `app.openapi()` to `backend/openapi/spec.json`, writes the sha256 to `backend/openapi/spec.json.sha256`, and when the hash changed (or `web_app/src/api/` is empty) runs `pnpm orval` in `web_app/`.
2. `web_app/orval.config.ts` reads `../backend/openapi/spec.json` and generates into `src/api/`:
   - one React Query + axios client file per FastAPI tag (`mode: 'tags'`, `useSkipToken` for queries, custom `operationName` that prefixes the verb/tag)
   - a single Zod v4 **mini** schema file, `src/api/index.zod.ts`
   - formatted with `oxfmt`; the `System` tag is filtered out
3. Regenerate the client after any backend API change (restart the backend or run `pnpm exec orval`), then commit the updated generated files.

When adding an endpoint, use clear FastAPI `tags` and `response_model`s — orval groups output by tag and derives TypeScript types from the Pydantic schemas.

## Available Skills

Project-specific skills live in `.agents/skills/`. Invoke them when relevant instead of improvising:

- **`sqlmodel-orm-dbhelper`** — use for designing/modifying SQLModel models, engine/session configuration, relationships, timestamps, and indexing in `backend` (models live under `backend/src/application/features/<feature>/models.py`, with `application/models.py` as the registry). References under `.agents/skills/sqlmodel-orm-dbhelper/references/` cover relationships, engine config, performance, field types, and migrations.
- **`router-query-integration`** — use when wiring TanStack Router loaders to TanStack Query (prefetching, `queryOptions`, avoiding waterfalls) in `web_app`.
- **`shadcn`** — use for shadcn/ui work in `web_app`: adding/searching components, composing UI, and design-system/token work. Initialized via `web_app/components.json` (`style: base-vega`, `baseColor: mauve`, `iconLibrary: tabler`, aliases `#components` / `#utils` / `#ui` / `#lib` / `#hooks`), on the **Base UI flavor** (`@base-ui/react` + `render`, not Radix `asChild`). `cn` lives in `src/lib/utils.ts` (re-export from the `cn` package). Design preset: `b6C24NuyWY` (vega/mauve, sky theme, small radius, Geist Mono + Manrope). Components already generated in `src/components/ui/` include button, card, checkbox, dialog, dropdown-menu, field, input, label, select, separator, skeleton, sonner, switch, table, tabs, textarea, tooltip — treat them as CLI output (regenerate/extend via the CLI, don't restructure). App-level composition lives in `src/components/` (e.g. `src/components/form/` for TanStack Form fields). Rules under `.agents/skills/shadcn/rules/` cover styling, forms, composition, icons, and base-vs-radix differences.

## General Conventions

- Work inside the **Dev Container** (`.devcontainer/`): it provides the Python/Node toolchains and the PostgreSQL/Mailpit services. Don't recreate that environment on the host, and check `git status` of lock files (`uv.lock`, `pnpm-lock.yaml`) before finishing so the next container start can install.
- Keep changes scoped to the relevant subproject; don't mix backend and frontend concerns in one change unless the API contract is shifting.
- Match existing naming: Python `snake_case` (SQLModel fields, functions), TypeScript `camelCase` for values / `PascalCase` for components and types.
- Run the relevant formatter/linter before finishing:
  - Backend: `uv run ruff check . && uv run ruff format .`
  - Frontend: `pnpm check` (format check + lint + `tsc --noEmit`)
- Regenerate and commit derived artifacts when inputs change: Alembic migrations, `backend/openapi/spec.json` (+ `.sha256`), `web_app/src/routeTree.gen.ts`, and `web_app/src/api/*`.
- Do not commit secrets. `backend/.env` holds real credentials; `backend/.env.example` documents the expected variables.
- Prefer ASCII/UTF-8 text; keep files free of `__pycache__`/build output (already gitignored). Note `.vscode/settings.json` is committed and configures the editor toolchain.
