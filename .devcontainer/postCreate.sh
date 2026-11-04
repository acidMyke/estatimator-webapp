#!/bin/sh
set -e

echo "=== 1. GitHub CLI Authentication ==="
if ! gh auth status >/dev/null 2>&1; then
  gh auth login
else
  echo "Already authenticated with GitHub CLI."
fi

echo ""
echo "=== 2. Git User Identity Setup ==="
CURRENT_NAME=$(git config --global user.name || true)
CURRENT_EMAIL=$(git config --global user.email || true)

if [ -z "$CURRENT_NAME" ]; then
  printf "Enter your Git user.name: "
  read -r GIT_NAME
  git config --global user.name "$GIT_NAME"
else
  echo "Git user.name already configured as: $CURRENT_NAME"
fi

if [ -z "$CURRENT_EMAIL" ]; then
  printf "Enter your Git user.email: "
  read -r GIT_EMAIL
  git config --global user.email "$GIT_EMAIL"
else
  echo "Git user.email already configured as: $CURRENT_EMAIL"
fi

echo ""
echo "=== 3. GPG Commit Signing Setup ==="
CURRENT_GPG=$(git config --global user.signingkey || true)

if [ -z "$CURRENT_GPG" ]; then
  printf "Do you want to configure GPG commit signing? (y/N): "
  read -r CONFIGURE_GPG
  case "$CONFIGURE_GPG" in
    [Yy]*)
      echo "Available GPG secret keys:"
      gpg --list-secret-keys --keyid-format=long || true
      echo ""
      printf "Enter your GPG Key ID (or leave blank to skip): "
      read -r GPG_KEY_ID
      if [ -n "$GPG_KEY_ID" ]; then
        git config --global user.signingkey "$GPG_KEY_ID"
        git config --global commit.gpgsign true
        echo "GPG commit signing enabled for key: $GPG_KEY_ID"
      fi
      ;;
    *)
      echo "Skipping GPG configuration."
      ;;
  esac
else
  echo "GPG signing key already configured as: $CURRENT_GPG"
fi