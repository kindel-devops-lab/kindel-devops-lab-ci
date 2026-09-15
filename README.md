# Flask Monitoring API and DevSecOps Pipeline

![CI/CD Pipeline](https://github.com/Sonelooo77/devops-flask-microservice-ci/actions/workflows/ci.yml/badge.svg)

This repository contains a lightweight Flask REST microservice simulating a system health monitoring endpoint. The primary objective is to demonstrate an automated continuous integration and DevSecOps workflow that validates code quality, scans container images for security vulnerabilities, and synchronizes deployment metadata with a dedicated infrastructure repository.

## Architecture and Workflow

The continuous integration pipeline is implemented using GitHub Actions and executes on every push to the main branch:

1. Code Quality: Python source code is analyzed using flake8 to enforce PEP8 standards and syntax rules.
2. Unit Testing: Automated testing is performed using pytest to validate that the endpoints respond as expected.
3. Containerization: A lightweight Docker image is built using a Python 3.10 slim base image with layer caching optimization.
4. Security Scanning: Aqua Security Trivy scans the compiled container image to detect High and Critical Common Vulnerabilities and Exposures (CVEs).
5. Registry Publication: The validated container image is pushed to a private ACR instance using Service Principal authentication with an immutable tag matching the short Git commit SHA.
6. GitOps Synchronization: The workflow checks out the infrastructure repository using a Personal Access Token, updates the image tag variable inside terraform.tfvars, and commits the modification automatically.

## API Endpoints

The service exposes two HTTP endpoints:
- GET /: Returns a basic service description and confirmation that the API is running.
- GET /health: Returns a JSON status object used by orchestration probes and smoke tests.
