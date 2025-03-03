GitHub Actions Workflow
=======================

A GitHub Actions workflow (located at ``.github/workflows/test_and_deploy.yml``) is configured to run:

- **Linting checks** via pre-commit.
- **Testing** if linting passes.
- **Deployment to PyPI** if a Git tag is present and tests pass (requires the ``TWINE_API_KEY`` in repository secrets).

This automation ensures that each commit or pull request is validated and that releases are published only when all checks pass.
