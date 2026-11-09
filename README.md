# SecureOpShip

A Python REST API demonstrating DevSecOps practices
through automated testing, code quality validation,
and security scanning with GitHub Actions.

## CI Pipeline
 ![SecureOpShip CI](https://github.com/DarkNic/secureopship-ci/actions/workflows/ci.yml/badge.svg) uses GitHub Actions to automatically execute:

- Ruff code quality checks
- pytest automated tests
- Bandit source-code security analysis
- pip-audit dependency vulnerability auditing