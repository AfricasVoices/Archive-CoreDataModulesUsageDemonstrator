#!/bin/bash

set -e

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ] || [ -z "$5" ]; then
    echo "Usage: sh docker-run.sh <path_to_GitHub_key> <user> <gender-col> <input-file> <output-file>"
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

# Create a container from the image that was just built.
container="$(docker container create --env USER="$2" --env GENDER_COL="$3" core-data-demo)"

# Copy input data into the container
docker cp "$4" "${container}:/app/data/input.json"

# Run the image as a container.
docker start -a -i "$container"

# Copy the output data back out of the container
docker cp "${container}:/app/data/output.json" "$5"
