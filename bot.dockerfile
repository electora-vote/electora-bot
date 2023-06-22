ARG environment_type=production

################################################################################
# Dependencies builder
################################################################################
FROM python:3.11 AS builder
WORKDIR /app

# Extra python env
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m venv /venv
RUN /venv/bin/pip install --upgrade pip

RUN /venv/bin/pip install flit

COPY pyproject.toml requirements.txt ./
RUN /venv/bin/pip install -r requirements.txt

################################################################################
# Production virtual environment builder
################################################################################
FROM builder as production-builder

# Copy in the source code tree
COPY pyproject.toml LICENSE ./
COPY electora_bot ./electora_bot/

# Build a wheel and install it into the virtual env
RUN /venv/bin/python -m flit build \
&&  /venv/bin/pip install dist/*.whl

################################################################################
# Base image for dev and production
################################################################################
FROM python:3.11-slim AS base
WORKDIR /app

# Extra python env
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/venv/bin:$PATH"

################################################################################
# Development image
################################################################################
FROM base as development

# Copy in the virtual environment from the builder stage
# This does not include the electora_bot library.
COPY --from=builder /venv /venv


################################################################################
# Production image
################################################################################
FROM base as production

# Copy in the virtual environment from the production builder stage
# This includes the electora_bot library installed via wheel.
COPY --from=production-builder /venv /venv


################################################################################
# Final image
################################################################################
FROM ${environment_type} as bot
