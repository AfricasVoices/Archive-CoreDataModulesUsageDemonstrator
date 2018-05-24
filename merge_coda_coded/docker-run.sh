#!/bin/bash

set -e

if [ $# -ne 7 ]; then
    echo "Usage: sh docker-run.sh <path_to_GitHub_key> <user> <raw-col> <code-col> <input-file> <coda-input-file> <output-file>"
    exit
fi

GH_KEY=$1
USER=$2
RAW_COL=$3
CODE_COL=$4
INPUT_FILE=$5
CODA_INPUT_FILE=$6
OUTPUT_FILE=$7

# Copy key from the specified location to here, so that Docker can access it when building the image.
cp "$GH_KEY" .gh_rsa

function finish {
	# Delete the copy of the user's key we made in this directory.
    rm -f .gh_rsa
}
trap finish EXIT

# Build an image for this project, called "core-data-demo".
docker build -t core-data-demo .

# Create a container from the image that was just built.
container="$(docker container create --env USER="$USER" --env RAW_COL="$RAW_COL" --env CODE_COL="$CODE_COL" core-data-demo)"

# Copy input data into the container
docker cp "$INPUT_FILE" "$container:/app/data/input.json"
docker cp "$CODA_INPUT_FILE" "$container:/app/data/coda_import.txt"

# Run the image as a container.
docker start -a -i "$container"

# Copy the output data back out of the container
docker cp "$container:/app/data/output.json" "$OUTPUT_FILE"
