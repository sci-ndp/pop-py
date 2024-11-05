# Contributing to Point Of Presence (pointofpresence)

Thank you for your interest in contributing to **Point Of Presence**! We welcome contributions from the community. Below are some guidelines to help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Fork the Repository](#fork-the-repository)
  - [Clone the Repository](#clone-the-repository)
  - [Create a New Branch](#create-a-new-branch)
  - [Make Your Changes](#make-your-changes)
  - [Commit Your Changes](#commit-your-changes)
  - [Push Your Changes to GitHub](#push-your-changes-to-github)
  - [Create a Pull Request](#create-a-pull-request)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Reporting Bugs and Suggesting Features](#reporting-bugs-and-suggesting-features)
- [Running Tests](#running-tests)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report any unacceptable behavior to [u6061931@utah.edu ](mailto:u6061931@utah.edu).

## How to Contribute

### Fork the Repository

1. Navigate to the [PointOfPresence GitHub repository](https://github.com/sci-ndp/pop-py).
2. Click the **Fork** button in the top-right corner of the page to create a copy of the repository under your GitHub account.

### Clone the Repository

3. Clone your forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your_username/pointofpresence.git
   cd pointofpresence
   ```

### Create a New Branch

4. Create a new branch for your feature or bugfix. It's good practice to use a descriptive name:

   ```bash
   git checkout -b feature/new-feature
   ```

   Or for bug fixes:

   ```bash
   git checkout -b fix/bug-description
   ```

### Make Your Changes

5. Make the necessary changes to the codebase. Ensure that your changes adhere to the [Coding Standards](#coding-standards) outlined below.

### Commit Your Changes

6. Commit your changes with clear and descriptive messages. Follow the [Commit Message Guidelines](#commit-message-guidelines).

   ```bash
   git add .
   git commit -m "feat(auth): add token renewal method"
   ```

### Push Your Changes to GitHub

7. Push your branch to your forked repository on GitHub:

   ```bash
   git push origin feature/new-feature
   ```

### Create a Pull Request

8. Navigate to your forked repository on GitHub.
9. Click the **Compare & pull request** button.
10. Provide a clear and concise description of the changes you've made and why they are necessary.
11. Submit the Pull Request.

## Coding Standards

- **PEP 8 Compliance**: Follow the [PEP 8](https://pep8.org/) style guide for Python code.
- **Descriptive Names**: Use clear and descriptive names for variables, functions, and classes.
- **Documentation**: Document your functions and classes using docstrings.
- **Type Annotations**: Use type annotations where possible to improve readability and maintainability.
- **Modularity**: Keep your code modular by breaking down large functions into smaller, reusable ones.

## Commit Message Guidelines

To maintain a clear and understandable commit history, please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for your commit messages.

### Common Types

- **feat**: Add a new feature.
- **fix**: Fix a bug.
- **docs**: Documentation changes.
- **style**: Code style changes (formatting, missing semi-colons, etc.) that do not affect the meaning of the code.
- **refactor**: Code changes that neither fix a bug nor add a feature.
- **test**: Add or modify tests.
- **chore**: Changes to the build process or auxiliary tools and libraries.

### Examples

- `feat(auth): add token renewal method`
- `fix(get_method): handle empty responses correctly`
- `docs(readme): update installation instructions`
- `style(base_client): format code according to PEP 8`
- `refactor(client): simplify initialization logic`
- `test(post_method): add tests for POST requests`
- `chore: update dependencies`

## Reporting Bugs and Suggesting Features

If you encounter a bug or have an idea for a new feature, please open an [Issue](https://github.com/sci-ndp/pop-py/issues) in the repository.

### How to Report a Bug

1. **Provide a Descriptive Title**: Summarize the issue in one line.
2. **Detailed Description**:
   - **Steps to Reproduce**: List the steps required to reproduce the issue.
   - **Expected Behavior**: Describe what you expected to happen.
   - **Actual Behavior**: Describe what actually happened.
3. **Additional Context**: Include any other relevant information, such as error messages, screenshots, or your environment setup.

### How to Suggest a Feature

1. **Provide a Descriptive Title**: Summarize the feature in one line.
2. **Detailed Description**:
   - **Motivation**: Explain why this feature is important.
   - **Description**: Provide a clear description of the feature.
3. **Examples**: If possible, include examples of how the feature would be used.

## Running Tests

Before submitting a Pull Request, ensure that all tests pass and that your changes do not introduce any new issues.

1. **Install Dependencies**:

   Ensure you have **pytest** installed. If not, install it using:

   ```bash
   pip install -r requirements.txt
   ```
2. **Run Tests**:

   Execute the tests using the following command from the project root:

   ```bash
   pytest
   ```
3. **Add Tests for New Features**:

   If you've added a new feature, include corresponding tests to verify its functionality.
4. **Check Code Coverage**:

   Aim to maintain high code coverage to ensure the reliability of the project.

## Acknowledgements

Thank you for contributing to **pop-py**! Your efforts help improve this library for everyone.
