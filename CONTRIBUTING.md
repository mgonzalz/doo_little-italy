# Contributing Guidelines.

We appreciate your interest in contributing to **Doo Little Italy**. This document outlines the processes and standards for contributing to the project. By adhering to these guidelines, you help ensure a high-quality, cohesive codebase and an efficient collaboration process.

## Table of Contents.

1. [Contribution Types](#contribution-types)
   - [Bug Reports](#bug-reports)
   - [Feature Requests](#feature-requests)
   - [Code Contributions](#code-contributions)
2. [Development Standards](#development-standards)
   - [Code Style](#code-style)
   - [Testing](#testing)
   - [Documentation](#documentation)
3. [Development Workflow](#development-workflow)
   - [Environment Setup](#environment-setup)
   - [Branching Strategy](#branching-strategy)
   - [Submitting Pull Requests](#submitting-pull-requests)
4. [Contact and Support](#contact-and-support)

## Contribution Types.

### Bug Reports.

- Ensure the issue has not been reported already by searching the [issue tracker](https://github.com/mgonzalz/doo_little-italy/issues).
- Include:
  - A clear and concise title summarizing the issue.
  - Steps to reproduce the problem.
  - Observed behavior and the expected outcome.
  - Relevant logs, screenshots, or error messages.
  - Environment details (OS, Python version, dependencies).

### Feature Requests.

- Verify similar suggestions have not been raised in the [issue tracker](https://github.com/mgonzalz/doo_little-italy/issues).
- Provide:
  - A comprehensive explanation of the proposed feature.
  - Potential use cases and benefits to the project.
  - References, diagrams, or examples (if applicable).

### Code Contributions.

- Before beginning work, consider raising an issue or starting a discussion to avoid duplication of effort.
- All code must follow the development standards outlined below.

## Development Standards.

### Code Style.

- Adhere to [PEP 8](https://peps.python.org/pep-0008/) guidelines for Python code.
- Ensure consistency with existing patterns and architecture.
- Use type annotations where applicable.
- Run code formatting tools before submission:
  ```bash
  black .
  ```

### Testing.

- All new features and bug fixes must include corresponding unit tests.
- Execute the full test suite before submitting changes:
  ```bash
  python manage.py test
  ```

### Documentation.

- Update or create relevant documentation for your changes, including:
  - Inline comments for complex logic.
  - Modifications to `README.md` or relevant sections.
  - API documentation where applicable.

## Development Workflow.

### Environment Setup.

1. Clone the repository:
   ```bash
   git clone https://github.com/mgonzalz/doo_little-italy.git
   cd doo_little-italy
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your `.env` file:
   - Create a `.env` with the API Keys.

### Branching Strategy.

- Follow the naming conventions:
  - `feature/<short-description>` for new features.
  - `bugfix/<short-description>` for bug fixes.
  - `hotfix/<short-description>` for critical fixes.
- Always branch from `main`.

### Submitting Pull Requests.

- Ensure your branch is up to date:
  ```bash
  git fetch origin
  git rebase origin/main
  ```
- Push your branch:
  ```bash
  git push origin <branch-name>
  ```
- Open a pull request in GitHub:
  - Use a descriptive title.
  - Include a summary of changes and their impact.
  - Link any related issues.

## Contact and Support.

For questions, discussions, or to report issues not covered above:

- Open an issue in the [issue tracker](https://github.com/mgonzalz/doo_little-italy/issues).
- Direct inquiries to the repository maintainers via GitHub Discussions (if enabled).

By contributing, you agree to follow these guidelines and adhere to the project's licensing and community standards.

Thank you for your contributions!
