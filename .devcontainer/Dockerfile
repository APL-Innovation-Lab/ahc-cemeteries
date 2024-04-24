FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsqlite3-mod-spatialite \
    spatialite-bin \
    # Any other dependencies you might need
    && rm -rf /var/lib/apt/lists/*
