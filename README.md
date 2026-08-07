# Git-Scope 🛡️
> **Real-Time Repo Security & Credential Leak Interceptor**

## Description
**Git-Scope** is a developer-first security interception tool designed to detect and prevent hardcoded credentials, API keys, and insecure data flows before code reaches public version control.

---

## Features
* Local pre-push hook interceptor to block leaks before they reach remote.
* AST behavioral taint analysis to track data flow into risky sinks.
* CI/CD integration via GitHub Actions for server-side validation and releases.

---

## Getting Started

### Download prebuilt binaries (recommended)
Prebuilt binaries are published on GitHub Releases. Replace `v1.0.0` with the release you want.

- Linux (amd64):

  ```bash
  curl -L -o git-scope-linux-amd64 \
    https://github.com/ehtishamiqbal433-cell/Git-Scope/releases/download/v1.0.0/git-scope-linux-amd64
  chmod +x git-scope-linux-amd64
  ./git-scope-linux-amd64 --version
  ```

- Linux (arm64):

  ```bash
  curl -L -o git-scope-linux-arm64 \
    https://github.com/ehtishamiqbal433-cell/Git-Scope/releases/download/v1.0.0/git-scope-linux-arm64
  chmod +x git-scope-linux-arm64
  ./git-scope-linux-arm64 --version
  ```

- macOS (darwin/amd64):

  ```bash
  curl -L -o git-scope-darwin-amd64 \
    https://github.com/ehtishamiqbal433-cell/Git-Scope/releases/download/v1.0.0/git-scope-darwin-amd64
  chmod +x git-scope-darwin-amd64
  ./git-scope-darwin-amd64 --version
  ```

- macOS (darwin/arm64):

  ```bash
  curl -L -o git-scope-darwin-arm64 \
    https://github.com/ehtishamiqbal433-cell/Git-Scope/releases/download/v1.0.0/git-scope-darwin-arm64
  chmod +x git-scope-darwin-arm64
  ./git-scope-darwin-arm64 --version
  ```

- Windows (amd64):

  Download and run `git-scope-windows-amd64.exe` from:
  https://github.com/ehtishamiqbal433-cell/Git-Scope/releases/download/v1.0.0/git-scope-windows-amd64.exe

Releases page: https://github.com/ehtishamiqbal433-cell/Git-Scope/releases

> Note: release assets are created by the GitHub Actions workflow (see Releases page). If your platform is not listed, build from source below.

### Verify release asset integrity (recommended)
It's best practice to verify downloaded binaries with SHA256.

- Generate checksum locally:

  ```bash
  sha256sum git-scope-linux-amd64
  # or on macOS
  shasum -a 256 git-scope-darwin-amd64
  ```

- We do not currently publish checksums in the release notes. To add verified checksums to a release yourself:
  1. Compute the checksum locally (commands above).
  2. Add the checksum to the release body via the GitHub UI or include a `checksums.txt` asset.

> If you want, you can ask the maintainers to add automated checksum generation to CI; guidelines are in the Contributing section below.

### Build from source (Go)
Requirements: Go 1.22+ (the release workflow uses Go 1.22).

```bash
git clone https://github.com/ehtishamiqbal433-cell/Git-Scope.git
cd Git-Scope
# ensure modules are tidy
go mod tidy
# build
go build -o git-scope ./cmd/git-scope
./git-scope --version
```

### What the binary currently supports
The shipped `git-scope` binary currently prints an informational banner and supports a `--version` flag. The main entrypoint is `cmd/git-scope/main.go`.

If you expected a full interactive TUI or a Python CLI, note:
- The previous README referenced a `cli/requirements.txt` (Python). That directory is not present in this repository — README has been updated to reflect the Go-based binary and how to use it.
- The interactive/dashboard functionality mentioned in older docs is not implemented in `main.go` at present. If you need the TUI, open an issue or submit a PR with the implementation.

### CI / Release notes
- The repository uses a GitHub Actions workflow to build and publish releases (see `.github/workflows/release.yml`).
- Example Actions run (build + release):
  https://github.com/ehtishamiqbal433-cell/Git-Scope/actions/runs/31151099891/job/92781489033#step:4:52

### Contributing
- To add automated checksum publishing to releases, add a workflow step that computes SHA256 sums and either appends them to the release body or uploads a `checksums.txt` asset to the release.
- If you want the Python CLI restored, either:
  - add the `cli/` directory and `cli/requirements.txt` mentioned in historic docs, or
  - remove the Python CLI instructions completely (this README now documents the Go binary path).

### Issues
Please open issues for:
- Missing features (TUI/CLI),
- Incorrect release assets or checksums,
- CI build failures.

---

If you'd like, I can:
- open a PR that adds a GitHub Actions job to compute SHA256 checksums and upload `checksums.txt` to each release,
- publish a second commit that adds example checksum lines (computed by me if you grant permission to download assets), or
- add a short TUI stub under `internal/` and expand `cmd/git-scope/main.go` to launch it.

Which of these should I do next?
