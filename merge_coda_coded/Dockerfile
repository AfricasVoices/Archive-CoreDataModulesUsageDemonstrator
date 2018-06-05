FROM python:3.6-slim

# Install the tools we need.
RUN apt-get update && apt-get install -y git ssh
RUN pip install pipenv

# Copy dependencies file.
WORKDIR /app
ADD Pipfile.lock /app
ADD Pipfile /app

# Copy the private GitHub key to the container.
ADD .gh_rsa /root/.ssh/id_rsa

# Test that the ssh key works with GitHub.
RUN ssh -o StrictHostKeyChecking=no -vT git@github.com 2>&1 | grep -i auth

# Install project dependencies.
RUN pipenv sync

# Remove all the ssh keys that were copied earlier. /app/.gh_rsa was copied by the first ADD . /app stage.
RUN rm -rf /root/.ssh /etc/ssh /app/.gh_rsa

# Double check those directories were deleted. If they weren't, fail the build.
RUN if [ -d "/root/.ssh" ] || [ -d "/etc/ssh" ] || [ -d "app/.gh_rsa" ]; then exit 1; fi

# Copy the rest of the project
ADD . /app

# Make a directory for intermediate data
RUN mkdir /app/data

# USER, RAW_COL, and CODE_COL are environment variables which need to be set when constructing this container e.g. via
# docker run or docker container create. Use docker-run.sh to set these automatically.
CMD pipenv run python merge_coda_coded.py "$USER" "$RAW_COL" "$CODE_COL" data/input.json data/coda_import.txt data/output.json
