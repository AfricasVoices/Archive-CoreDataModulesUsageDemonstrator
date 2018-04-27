FROM python:2.7-slim

WORKDIR /app

ADD . /app

# Copy the private GitHub key to the container.
ADD .gh_rsa /root/.ssh/id_rsa

# Install the tools we need.
RUN apt-get update && apt-get install -y git ssh
RUN pip install pipenv

# Test that the ssh key works with GitHub.
RUN ssh -o StrictHostKeyChecking=no -vT git@github.com 2>&1 | grep -i auth

# Install project dependencies.
RUN pipenv sync

# Remove all the ssh keys that were copied earlier. /app/.gh_rsa was copied by the first ADD . /app stage.
RUN rm -rf /root/.ssh /etc/ssh /app/.gh_rsa

# Double check those directories were deleted. If they weren't, fail the build.
RUN if [ -d "/root/.ssh" ] || [ -d "/etc/ssh" ] || [ -d "app/.gh_rsa" ]; then exit 1 ;fi

CMD pipenv run python demo.py
