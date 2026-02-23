# TITAN Vulnerability Scanner Demo

This repository demonstrates TITAN's vulnerability detection capabilities.

## 🔴 Vulnerable Files (Should be detected)

1. **vulnerable_sqli.py** - SQL Injection vulnerability
2. **vulnerable_rce.py** - Remote Code Execution (eval, exec, os.system)
3. **vulnerable_xss.py** - Cross-Site Scripting (XSS)

## ✅ Safe Files (Should be marked safe)

1. **safe_database.py** - Parameterized SQL queries
2. **safe_commands.py** - Secure subprocess execution

## How TITAN Works

TITAN automatically scans this repository on:
- Every push to main branch
- Every pull request
- Manual workflow dispatch

Results are posted as comments on PRs and commits.
