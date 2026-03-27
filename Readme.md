# Todo App - Playwright & Pytest Automation

A professional and automated UI testing suite for the [Todo Application](https://github.com/SanthiyaMeganathan/todo_project). This project uses **Playwright** and **Pytest** to ensure proper functionality of the Todo application across different scenarios.

## 📂 Project Structure

- `pages/`: Contains the Page Object Model (POM) classes for interacting with web elements.
- `tests/`: Contains the test scripts (e.g., `test_todo_scenarios.py` and `test_google.py`).
- `utils/`: Reusable utility functions and helpers.
- `conftest.py`: Configuration and global fixtures for Pytest.
- `pytest.ini`: Pytest configuration settings.
- `requirements.txt`: Python dependencies needed to run the project.

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)

## 🛠️ Installation

1. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## 🏃‍♂️ Running the Tests

To execute the test suite, simply run:
```bash
pytest
```

After the tests run, you can view the generated HTML report by opening the `report.html` file in your browser:
```bash
start report.html
```

## 🔗 Related Repository

- **Todo Application Source**: [https://github.com/SanthiyaMeganathan/todo_project.git](https://github.com/SanthiyaMeganathan/todo_project.git)
