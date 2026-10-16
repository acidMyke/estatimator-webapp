# Web Application

## Setup (One-Time)

### Check if vp is installed

```sh
  vp -V
```

- **If it says "command not found":** You need to install vp, continue
- else, skip to [Application startup](#)

### vp installation

#### macOS / Linux

```bash
curl -fsSL https://vite.plus | bash
```

#### Windows

```powershell
irm https://vite.plus/ps1 | iex
```

Alternatively, download and run [`vp-setup.exe`](https://setup.viteplus.dev)

## Application Startup

Update dependencies

```sh
  vp install
```

Start the web app

```sh
  vp dev
```
