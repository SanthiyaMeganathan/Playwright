# Playwright + Pytest Learning Project (Python)

This project is a beginner-friendly automation testing setup using:

- **Python**
- **Pytest**
- **Playwright (Python)**

It is written so even a new learner can open, run, and study the tests easily.

---

## What this project does

Automated tests open a browser, perform actions (like searching in Google), and verify results.

Example from this project:
- Open Google
- Accept cookie popup (if shown)
- Search for `playwright`
- Verify page title contains `playwright`

---

## Current project structure

```text
playwright/
└── tests/
    └── test_google.py
```

> As you add more tests/files, update this section.

---

## Prerequisites

Install these first:

1. **Python 3.10+**  
   https://www.python.org/downloads/

2. (Recommended) **VS Code**  
   https://code.visualstudio.com/

3. Verify Python and pip:
```powershell
python --version
pip --version
```

---

## Setup (Windows PowerShell)

### 1) Create virtual environment
```powershell
python -m venv .venv
```

### 2) Activate virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3) Install required packages
```powershell
pip install pytest playwright pytest-playwright
```

### 4) Install Playwright browsers
```powershell
python -m playwright install
```

---

## How to run tests

### Run all tests
```powershell
pytest
```

### Run tests with detailed output
```powershell
pytest -v
```

### Run only the Google test file
```powershell
pytest tests\test_google.py -v
```

---

## Understanding the current test

File: `tests/test_google.py`

What it does in simple words:

1. Opens `https://www.google.com/`
2. Tries to click **Accept all** cookie button  
   - If popup does not appear, test continues
3. Types `playwright` in the search box
4. Presses Enter
5. Checks page title contains `playwright` (case-insensitive)

---

## Learning notes for beginners

- `page` is provided by **pytest-playwright fixture**
- `expect(...)` is used for assertions
- `get_by_role(...)` is a reliable locator strategy
- `re.IGNORECASE` means uppercase/lowercase does not matter

---

## Common issues and fixes

### `ModuleNotFoundError: No module named 'playwright'`
```powershell
pip install playwright pytest-playwright
```

### Browser executable missing
```powershell
python -m playwright install
```

### `pytest` command not found
Use:
```powershell
python -m pytest -v
```

### PowerShell script execution blocked (venv activation)
Run PowerShell as user and execute:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## Suggested next improvements

- Add more test files inside `tests/`
- Use clearer test names (example: `test_google_search`)
- Add screenshots on failure
- Add HTML reporting with pytest plugins

---

## Quick command cheat sheet

```powershell
# create venv
python -m venv .venv

# activate venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install pytest playwright pytest-playwright

# install browsers
python -m playwright install

# run tests
pytest -v
```

---

## Last updated

**18-Mar-2026**

fixture is the reusable code , if we use same code again and again in so many times
then we can put in conftest and reuse when ever its needed.!

to install everything in this project run:
pip install -r requirements.txt