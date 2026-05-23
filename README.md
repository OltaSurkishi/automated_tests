QA Automation Project (Playwright + Python)

This project contains simple UI automated tests using Playwright.

------------------------------------------------------------

SETUP

1. Install Python
python --version

If not installed:
https://www.python.org/downloads/

------------------------------------------------------------

2. Install Playwright
pip install playwright

------------------------------------------------------------

3. Install browsers
python -m playwright install

------------------------------------------------------------

RUN TEST
python automated_test.py

------------------------------------------------------------

PROJECT STRUCTURE

solution25 automated test case/
├── automated_test.py
├── README.md

------------------------------------------------------------

WHAT THIS DOES
- Opens website
- Runs search test
- Checks results
- Prints PASS/FAIL

------------------------------------------------------------

ISSUES

If Playwright not found:
python -m playwright install

If pip issue:
python -m pip install playwright