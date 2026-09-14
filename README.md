# Flask Microservice CI/CD Pipeline

![CI/CD Pipeline](https://github.com/Sonelooo77/devops-flask-microservice-ci/actions/workflows/ci.yml/badge.svg)

A simple DevOps hands-on project demonstrating an automated **Continuous Integration (CI)** pipeline for a Python Flask API using **GitHub Actions**, **Docker**, and **DevSecOps** best practices.

## Project Overview
This repository contains a lightweight Flask REST API designed to simulate a health-check monitoring service. The main goal of this project is not the application logic itself, but building a production-grade CI pipeline to validate code quality, unit tests, and container security on every push.

### Key Features
- **REST API (`Flask`)**: Exposes `/` and `/health` endpoints for monitoring.
- **Unit Testing (`pytest`)**: Automated HTTP endpoint tests.
- **Code Quality (`flake8`)**: Syntax checking and PEP8 compliance.
- **Containerization (`Docker`)**: Multi-stage/lightweight build running Python 3.10-slim.
- **DevSecOps Security Scanning (`Trivy`)**: Automated container vulnerability scanning for CVEs.
- **Integration Testing (`cURL`)**: Health check validation inside the running container.

---

## Pipeline Architecture

The GitHub Actions workflow (`.github/workflows/ci.yml`) is split into two sequential jobs:

```text
 ┌────────────────────────────────────────┐
 │ Job 1: code-quality-and-tests          │
 │ ├── Linting (flake8)                   │
 │ └── Unit Tests (pytest)                │
 └───────────────────┬────────────────────┘
                     │ (needs)
                     ▼
 ┌────────────────────────────────────────┐
 │ Job 2: docker-build-and-security       │
 │ ├── Docker Build                       │
 │ ├── Security Scan (Trivy)              │
 │ ├── Container Startup                  │
 │ └── Integration Test (cURL /health)    │
 └────────────────────────────────────────┘

