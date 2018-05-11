#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "Usage: sh docker-run.sh <path_to_GitHub_key>"
    exit
fi

# Copy key from the specified location to here, so that Docker can access it when building the image.
cp "$1" .gh_rsa

function finish {
	# Delete the copy of the user's key we made in this directory.
    rm -f .gh_rsa
}
trap finish EXIT

# Build an image for this project, called "core-data-demo".
docker build -t core-data-demo .

# Run the image as a container.
docker run core-data-demo
