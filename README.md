
# Server Health Monitor CLI 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-production--ready-success)](https://github.com/)

A production-ready Command Line Interface (CLI) tool designed to monitor critical server metrics in real-time. Built for **DevOps engineers** and **System Administrators**, it provides configurable thresholds, structured JSON output, and automation-friendly exit codes for seamless integration into CI/CD pipelines or monitoring stacks.

---

## 🛠 Features

* **Key Metrics:** Real-time tracking of CPU, Memory, Disk usage, and System Uptime.
* **Granular Control:** Toggle specific checks using flags (e.g., check *only* CPU or *only* Disk).
* **Custom Thresholds:** Define your own "Warning" and "Critical" levels via CLI arguments.
* **Dual-Mode Output:** * **Human-Readable:** Clean, formatted text for manual checks.
    * **JSON:** Machine-parseable data for logs and dashboards.
* **File Logging:** Export reports directly to a `.json` file using the `--output` flag.
* **Automation Ready:** Returns standardized exit codes (0, 1, 2) based on health status.

---

## 💻 Installation

### Recommended (via pipx)
For a clean, isolated installation that is available globally without messing up your global Python environment:

```bash
pipx install --editable ~/Desktop/Projects/server-health-monitor

```

### Alternative (Virtual Environment)

```bash
# Clone the project
cd ~/Desktop/Projects/server-health-monitor

# Setup environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .

```

---

## ⚡ Usage & Flags

### Basic Flags

| Flag | Description |
| --- | --- |
| `--all` | Run all available health checks |
| `--cpu` | Check CPU usage percentage |
| `--memory` | Check Memory usage percentage |
| `--disk` | Check Disk usage percentage |
| `--uptime` | Check System uptime in hours |

### Configuration & Output

| Flag | Description | Default |
| --- | --- | --- |
| `--threshold-cpu` | Set CPU warning limit | 50% |
| `--threshold-memory` | Set Memory warning limit | 60% |
| `--threshold-disk` | Set Disk warning limit | 80% |
| `--threshold-uptime` | Set Uptime alert limit (hrs) | 24 |
| `--json` | Format output as JSON | False |
| `--output <file>` | Save results to a file | None |

---

## 📖 Examples

### 1. Standard Health Check

```bash
server-monitor --all

```

**Output:**

```text
HOSTNAME: my-server.local
TIMESTAMP: 2026-02-13T12:45:25
OVERALL STATUS: OK

CPU: Usage: 1.4%, Status: OK
MEMORY: Usage: 57.4%, Status: OK
DISK: Usage: 2.3%, Status: OK
UPTIME: Uptime: 23.78 hours, Status: OK

```

### 2. Export to JSON

Perfect for piping into tools like `jq` or sending to a logging server.

```bash
server-monitor --all --json

```

### 3. Custom Threshold (Automation Example)

If the CPU usage exceeds 1%, the tool will return a `WARNING` and an **Exit Code 1**.

```bash
server-monitor --cpu --threshold-cpu 1

```

---

## 🤖 Automation-Friendly Exit Codes

This tool is designed to be used in shell scripts or Cron jobs. You can check the exit status using `echo $?`.

| Exit Code | Status | Meaning |
| --- | --- | --- |
| **0** | **OK** | All metrics are within safe limits. |
| **1** | **WARNING** | One or more metrics exceeded thresholds. |
| **2** | **CRITICAL** | System-level failure or critical threshold reached. |

---

## 🏗 Project Structure

```text
server-health-monitor/
├── monitor/
│   ├── __init__.py
│   ├── cli.py         # Argument parsing logic
│   ├── checker.py     # System metric logic (psutil)
│   └── formatter.py   # JSON & Text formatting
├── tests/             # Unit tests
├── setup.py           # Installation script
└── README.md

```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Built with ❤️ for the DevOps Community.**

```

---

### Would you like me to:
1.  **Add a "Troubleshooting" section** for common `psutil` installation issues?
2.  **Generate a `requirements.txt`** content to go along with this?
3.  **Create a sample `GitHub Action`** workflow so you can show how this runs automatically?

```
