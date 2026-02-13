# Server Health Monitor CLI 🚀

A production-ready Command Line Interface (CLI) tool designed to monitor critical server metrics in real-time. Built for DevOps engineers and system administrators, it provides configurable thresholds, structured JSON output, and automation-friendly exit codes for seamless CI/CD or cron job integration.

---

## 🛠 Features

* **Comprehensive Monitoring:** Tracks CPU, Memory, Disk usage, and System Uptime.
* **Granular Control:** Use flags to run specific checks or monitor everything at once.
* **Custom Thresholds:** Set your own alert levels for different environments.
* **Structured Output:** Toggle between human-readable text and machine-parseable JSON.
* **Automation Ready:** Returns specific exit codes based on system health status.
* **Metadata:** Every report includes a `hostname` and `timestamp`.

---

## 💻 Installation

### Recommended (via pipx)
For a clean, isolated installation that is available globally:
```bash
pipx install --editable ~/Desktop/Projects/server-health-monitor


server-health-monitor/
├── monitor/
│   ├── __init__.py
│   ├── cli.py         # Argument parsing logic
│   ├── checker.py     # System metric logic (psutil)
│   └── formatter.py   # JSON & Text formatting
├── tests/             # Unit tests
├── setup.py           # Installation script
└── README.md
