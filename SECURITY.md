# Security Policy

## Dependency Vulnerability Management

This project maintains a comprehensive dependency vulnerability management program to ensure the security of all project dependencies.

## Current Status

✅ **All Clear** - Initial vulnerability baseline scan completed with no vulnerabilities detected.

See [VULNERABILITY_BASELINE.md](./VULNERABILITY_BASELINE.md) for detailed findings.

## Scanning Tools & Configuration

### pip-audit
- **Tool:** pip-audit - Audits Python packages for known vulnerabilities
- **Configuration:** `.pip-audit.toml`
- **Databases:** PyPA Advisory Database + Open Source Vulnerability (OSV)
- **Purpose:** Identify security issues in direct and transitive dependencies

### Running Scans

Quick scan:
```bash
poetry run pip-audit
```

Scan with script:
```bash
bash artemis_scripts/vulnerability_scan.sh
```

## Documented Procedures

- **[VULNERABILITY_BASELINE.md](./VULNERABILITY_BASELINE.md)** - Initial scan results and baseline status
- **[VULNERABILITY_SCANNING.md](./VULNERABILITY_SCANNING.md)** - Complete procedures for running and interpreting scans

## Dependency Inventory

**Development Dependencies:**
- black (23.12.1) - Code formatter
- isort (5.13.2) - Import organizer
- pytest (7.4.4) - Testing framework
- pytest-benchmark (4.0.0) - Benchmarking fixture

**Transitive Dependencies:** 8 additional packages (all verified)

All dependencies are development/testing tools only. No runtime production dependencies.

## Vulnerability Response

### Severity Levels
- **Critical** → Fix within 1-7 days
- **High** → Fix within 1-2 weeks
- **Medium** → Fix within 1 month
- **Low** → Fix in regular update cycle

### Remediation Process
1. Review vulnerability details
2. Assess project impact
3. Update affected package
4. Re-scan to verify fix
5. Document resolution
6. Update baseline

## Monitoring

Recommended scanning frequency:
- **Manual:** Weekly or before releases
- **Automated:** As part of CI/CD pipeline (see next task)

## Additional Security Notes

- All dependencies are kept current with security patches
- Python version: 3.8+ (supported by all dependencies)
- No known security issues in current baseline
- Baseline established: Initial scan (2024)

## References

- [pip-audit GitHub](https://github.com/pypa/pip-audit)
- [PyPA Advisory Database](https://github.com/pypa/advisory-db)
- [OSV Database](https://osv.dev)
- [Python Security Guidelines](https://python.readthedocs.io/en/latest/library/security_warnings.html)

---

For detailed security documentation, see:
- **VULNERABILITY_BASELINE.md** - Current security status
- **VULNERABILITY_SCANNING.md** - How to run and interpret scans
