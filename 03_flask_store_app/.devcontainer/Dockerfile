
ARG VARIANT=3.12-bookworm

FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

ARG POETRY_VERSION=1.8.4

RUN pip3 install poetry==${POETRY_VERSION}

USER root