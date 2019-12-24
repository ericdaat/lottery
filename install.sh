#!/bin/bash

# usage: ./install.sh /path/to/dir
if [ -z "$1" ] || [ ! -d $(dirname "$1") ]; then
    echo "Non valid path"
    exit 1
fi

rsync -av "$(dirname "$0")/" "$1" \
	--exclude venv \
	--exclude .git \
	--exclude docs/build \
	--exclude __pycache__ \
	--exclude instance \
	--exclude .idea \
	--exclude .pytest_cache \
	--exclude install.sh \
    --exclude README.md;

cd $1;
echo "#$(basename $1)" > README.md;
git init;

exit 0
