#!/bin/sh
set -e

# If setup exits early or is interrupted, show how to resume it.
on_exit() {
  status=$?

  if [ "$status" -ne 0 ]; then
    echo ""
    echo "Setup did not complete (exit code: $status)."
    echo "To rerun the setup, execute this command from the repository root:"
    echo "  .devcontainer/postCreate.sh"
  fi
}

trap on_exit 0
trap 'exit 130' INT
trap 'exit 143' TERM

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "ERROR: This script must be run inside a Git repository."
  exit 1
fi

echo "Ello, I've pre-configure helpful quickstart setup script that will setup the following"
echo "- Github CLI sign-in (with access to set your signing keys)"
echo "- Git user.name & user.email"
echo "- SSH git commit signing keys and help to upload it to your github accounts"

echo "if you don't feel like having it automated, feel free to setup these up mannually"
echo ""
echo "=== 1. GitHub CLI Authentication ==="

if ! gh auth status --hostname github.com >/dev/null 2>&1; then
  gh auth login --hostname github.com --git-protocol https --web -s admin:ssh_signing_key
else
  echo "Already authenticated with GitHub CLI."
fi

# Configure Git to use GitHub CLI for HTTPS authentication.
gh config set git_protocol https --host github.com 
gh auth setup-git --hostname github.com

echo ""
echo "=== 2. Git User Identity Setup ==="
CURRENT_NAME=$(git config user.name || true)
CURRENT_EMAIL=$(git config user.email || true)

if [ -z "$CURRENT_NAME" ]; then
  printf "Enter your Git user.name: "
  read -r GIT_NAME
  git config --local user.name "$GIT_NAME"
else
  GIT_NAME="$CURRENT_NAME"
  echo "Git user.name configured as: $GIT_NAME"
fi

if [ -z "$CURRENT_EMAIL" ]; then
  printf "Enter your Git user.email: "
  read -r GIT_EMAIL
  git config --local user.email "$GIT_EMAIL"
else
  GIT_EMAIL="$CURRENT_EMAIL"
  echo "Git user.email configured as: $GIT_EMAIL"
fi

echo "Git identity:"
echo "  Name:  $GIT_NAME"
echo "  Email: $GIT_EMAIL"
echo ""
echo "=== 3. SSH Commit Signing Setup ==="

SSH_DIR="$HOME/.ssh"
mkdir -p "$SSH_DIR"
chmod 700 "$SSH_DIR"

# Generate a unique 6-character hexadecimal nonce.
NONCE=$(od -An -N3 -tx1 /dev/urandom | tr -d ' \n')

SSH_KEY_TITLE="Estatimator Webapp Devcon $NONCE"
SSH_KEY_PATH="$SSH_DIR/id_ed25519_estatimator_devcon_$NONCE"

echo "Generating SSH signing key: $SSH_KEY_TITLE"

ssh-keygen -t ed25519 -C "$SSH_KEY_TITLE" -f "$SSH_KEY_PATH" -N ""

# Upload the public key to GitHub specifically as a signing key.
gh ssh-key add "$SSH_KEY_PATH.pub" --type signing --title "$SSH_KEY_TITLE"

# Configure Git to use SSH for commit signing.
git config --local gpg.format ssh
git config --local user.signingkey "$SSH_KEY_PATH.pub"
git config --local commit.gpgsign true

echo "SSH commit signing successfully configured!"
echo "Key title: $SSH_KEY_TITLE"
echo "Public key: $SSH_KEY_PATH.pub"

echo ""
echo "Regarding the signing keys, they are optional keys use the sign the git commits"
echo "These doesn't grant any access to your github accounts"
echo "Feel free to delete '$SSH_KEY_TITLE' from your Github account after we get our grades"

echo ""
echo "=== 4. Git Remote Origin Setup ==="
EXPECTED_ORIGIN="https://github.com/acidMyke/estatimator-webapp.git"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$EXPECTED_ORIGIN"
  echo "Updated Git remote origin to: $EXPECTED_ORIGIN"
else
  git remote add origin "$EXPECTED_ORIGIN"
  echo "Added Git remote origin: $EXPECTED_ORIGIN"
fi