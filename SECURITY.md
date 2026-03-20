# Security Policy

## Overview

The llm-benchmarking-py project is committed to maintaining the security and integrity of our codebase and protecting the privacy of our users. This document outlines our security practices, vulnerability reporting procedures, and known limitations.

## Reporting Security Vulnerabilities

### Responsible Disclosure

We take security vulnerabilities seriously and appreciate responsible disclosure. If you discover a security vulnerability in this project, please report it privately rather than disclosing it publicly on GitHub issues.

**Please do NOT create public GitHub issues for security vulnerabilities.**

### How to Report

To report a security vulnerability, please send a detailed email to:

```
matthew.truscott@turintech.ai
```

Include the following information in your report:

- **Description**: A clear description of the vulnerability
- **Affected Component**: Which module or function is affected (e.g., `llm_benchmark.sql`, `llm_benchmark.algorithms`)
- **Impact**: Potential impact and severity (Critical, High, Medium, Low)
- **Proof of Concept**: Steps to reproduce, code snippet, or proof-of-concept demonstration
- **Suggested Fix**: If available, your suggested remediation (optional)
- **Your Contact Information**: Your email and name for follow-up communication

### Response Timeline

We aim to respond to security reports within **48 hours** of receipt. Our team will:

1. **Acknowledge** receipt of your report and provide a tracking reference
2. **Investigate** the vulnerability and assess its impact
3. **Develop** a fix or mitigation strategy
4. **Notify** you of our findings and expected timeline for a release
5. **Release** a patched version with appropriate security updates
6. **Credit** you in the release notes (unless you prefer to remain anonymous)

**Expected Resolution Timeline:**
- **Critical vulnerabilities**: Fix and release within 7 days
- **High severity**: Fix and release within 14 days
- **Medium severity**: Fix and release within 30 days
- **Low severity**: Address in the next planned release

## Security Best Practices

This project follows these security best practices:

### 1. Code Quality and Testing

- **Static Analysis**: Code is analyzed using:
  - **mypy**: Type checking to catch type-related errors early
  - **black**: Code formatting to maintain consistency
  - **isort**: Import sorting to ensure proper module organization
  
- **Testing**: Comprehensive unit tests via pytest to catch logic errors and edge cases
- **Benchmarking**: Performance tests to identify unexpected behavior changes

### 2. Dependency Management

- **Minimal Dependencies**: The project intentionally maintains a minimal dependency footprint to reduce supply chain risks
- **Python 3.8+**: Targets stable Python versions with long-term support
- **Regular Updates**: Dependencies are reviewed and updated regularly
- **Lock Files**: Poetry lock files (`poetry.lock`) ensure reproducible builds

### 3. Input Validation and Error Handling

- All user inputs are validated before processing
- Error handling is implemented to prevent information disclosure
- Exceptions are logged appropriately without exposing sensitive details
- Database queries use parameterized statements to prevent SQL injection

### 4. Logging and Data Handling

- **Logging**: Structured logging is implemented with appropriate log levels
- **No Sensitive Data**: Log files do not contain passwords, API keys, or personal information
- **Log File Security**: Log files are stored in a dedicated `logs/` directory
- **Graceful Failures**: Errors are handled gracefully to avoid leaking stack traces to end users

### 5. Database Security

- **SQLite Usage**: The project uses SQLite as the database, which is suitable for development and benchmarking
- **Query Parameterization**: All database queries use parameterized statements to prevent SQL injection
- **No Hardcoded Credentials**: Database credentials are never hardcoded in the source code
- **Development-Only Data**: Default databases contain only benchmark data, not user or sensitive information

## Known Limitations and Out-of-Scope Concerns

This project has the following known limitations and security considerations:

### 1. Project Scope

This is a **benchmarking and algorithm testing tool**, not a production security-critical system. The primary use cases are:

- Algorithm performance analysis
- Benchmarking LLM implementations
- Educational purposes
- Local development and testing

### 2. Database Design

- **Development-Focused**: The embedded SQLite database is designed for development and testing, not production use
- **Single-User**: Not designed for multi-user concurrent access with fine-grained permissions
- **No Encryption**: SQLite databases are not encrypted at rest; do not store sensitive production data
- **File-Based**: Database files are stored as local files without network protection

### 3. Access Control

- **No Built-In Authentication**: This project does not implement user authentication or authorization
- **Trust Boundary**: Assumes all code execution occurs within a trusted environment
- **Local Execution**: Designed for local development use, not exposed to untrusted networks

### 4. Deployment Considerations

- **Not for Production Use**: This tool is not intended for production deployment without additional security hardening
- **Network Isolation**: Should be run on isolated systems or development machines
- **User Responsibility**: Developers using this tool are responsible for securing their own environments

### 5. Third-Party Content

- **External Data**: Any external data used for benchmarking should be validated by the user
- **Algorithm Implementations**: Educational implementations may not include all production hardening

## Security Update Notification Process

### Staying Informed

To receive notifications about security updates:

1. **Watch Releases**: Enable release notifications on the GitHub repository
2. **Check README**: The README.md file lists the current version and latest updates
3. **Review Changelog**: Check BENCHMARK_RESULTS.md and related documentation for known issues

### Applying Updates

To update to the latest version:

```bash
poetry update
poetry install
```

## Security Scanning and Analysis

This project uses the following tools to identify and prevent security issues:

### Current Implementation

- **mypy**: Static type checking to catch type-related errors
- **black**: Code formatter for consistency and reduced complexity
- **isort**: Import organization to improve code clarity
- **pytest**: Unit testing framework for logic validation
- **pytest-benchmark**: Performance benchmarking to detect anomalies

### Recommended Tools (Future Integration)

The following tools are recommended for deployment and production use:

- **bandit**: Security issue scanner for Python code
- **safety**: Dependency vulnerability scanner
- **pylint**: Code analysis tool for additional checks

## Security Checklist for Contributors

When contributing to this project, please ensure:

- [ ] Code follows the project's style guide (enforced by `black` and `isort`)
- [ ] All inputs are validated and sanitized
- [ ] Error messages do not expose sensitive system information
- [ ] No hardcoded secrets, API keys, or credentials are committed
- [ ] Changes are covered by unit tests
- [ ] Type hints are provided for new functions (`mypy` compliance)
- [ ] Documentation is updated for security-relevant changes
- [ ] No new dependencies are added without security review

## Disclosure Coordination

Once a security fix is ready, we will:

1. Create a private GitHub security advisory (if applicable)
2. Coordinate the announcement with the researcher who reported the issue
3. Publish the fix and security advisory simultaneously
4. Announce the update across project documentation

## Questions or Concerns?

If you have questions about the security of this project or our policies, please contact:

```
matthew.truscott@turintech.ai
```

Thank you for helping us keep the llm-benchmarking-py project secure!

---

**Last Updated**: 2024

**Version**: 1.0
