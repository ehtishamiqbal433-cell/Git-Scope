#!/bin/sh
set -e

REPO="ehtishamiqbal433-cell/infra-scope"
BINARY_NAME="infra-scope"

print_error() {
    echo "\033[31mError: $1\033[0m" >&2
    exit 1
}

print_info() {
    echo "\033[32m[INFO] $1\033[0m"
}

OS="$(uname -s)"
case "$OS" in
    Linux*)   PLATFORM="linux";;
    Darwin*)  PLATFORM="darwin";;
    CYGWIN*|MINGW*|MSYS*) PLATFORM="windows";;
    *) print_error "Unsupported operating system: $OS" ;;
esac

ARCH="$(uname -m)"
case "$ARCH" in
    x86_64|amd64) ARCH="amd64";;
    arm64|aarch64) ARCH="arm64";;
    *) print_error "Unsupported architecture: $ARCH" ;;
esac

if [ "$PLATFORM" = "windows" ]; then
    INSTALL_DIR="/usr/local/bin"
else
    if [ "$(id -u)" -eq 0 ]; then
        INSTALL_DIR="/usr/local/bin"
    else
        INSTALL_DIR="$HOME/.local/bin"
    fi
fi

mkdir -p "$INSTALL_DIR"

RELEASE_URL="https://github.com/$REPO/releases/latest/download/${BINARY_NAME}-${PLATFORM}-${ARCH}"

print_info "Downloading $BINARY_NAME from GitHub Releases..."
if command -v curl >/dev/null 2>&1; then
    curl -sSL "$RELEASE_URL" -o "$INSTALL_DIR/$BINARY_NAME"
elif command -v wget >/dev/null 2>&1; then
    wget -qO "$INSTALL_DIR/$BINARY_NAME" "$RELEASE_URL"
else
    print_error "Neither curl nor wget is available."
fi

chmod +x "$INSTALL_DIR/$BINARY_NAME"
print_info "Successfully installed $BINARY_NAME to $INSTALL_DIR/$BINARY_NAME!"
