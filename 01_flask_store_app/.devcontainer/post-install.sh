#!/bin/bash
set -ex

# Create alias
echo 'alias fig="docker-compose"' >> $HOME/.bashrc


# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

# Change some Poetry settings to better deal with working in a container
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true

# Now install all dependencies
poetry install

source ${WORKSPACE_DIR}/.venv/bin/activate

echo "Done!"