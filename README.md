Server Health Monitor CLI
A production-ready CLI tool to monitor server health with configurable thresholds, JSON output, and automation-friendly exit codes. Ideal for DevOps engineers, system administrators, or portfolio projects.
Features:
Monitor key system metrics:
CPU usage
Memory usage
Disk usage
System uptime
Flexible CLI flags:
--all      # Run all checks
--cpu      # Check CPU usage only
--memory   # Check memory usage only
--disk     # Check disk usage only
--uptime   # Check uptime only
Custom thresholds (default if not set):
--threshold-cpu 50
--threshold-memory 60
--threshold-disk 80
--threshold-uptime 24
Output options:
Human-readable text (default)
JSON (--json)
Save output to file (--output filename.json)
Automation-friendly exit codes:
Status	Exit Code
OK	0
WARNING/ALERT	1
CRITICAL	2
Extra info: Adds hostname and timestamp to each run.
Installation
Recommended (via pipx):
pipx install --editable ~/Desktop/Projects/server-health-monitor
Or via virtual environment:
python -m venv venv
source venv/bin/activate
pip install -e ~/Desktop/Projects/server-health-monitor
Example Usage
Run all checks
server-monitor --all
Sample Output:
HOSTNAME: my-server.local
TIMESTAMP: 2026-02-13T12:45:25
OVERALL STATUS: OK

CPU: Usage: 1.4%, Status: OK
MEMORY: Usage: 57.4%, Status: OK
DISK: Usage: 2.3%, Status: OK
UPTIME: Uptime: 23.78 hours, Status: OK
Run all checks with JSON output
server-monitor --all --json
Sample JSON Output:
{
  "timestamp": "2026-02-13T12:45:26",
  "hostname": "my-server.local",
  "overall_status": "OK",
  "cpu": { "usage": 0.9, "status": "OK" },
  "memory": { "usage": 57.6, "status": "OK" },
  "disk": { "usage": 2.3, "status": "OK" },
  "uptime": { "uptime_hours": 23.78, "status": "OK" }
}
Save JSON report to file
server-monitor --all --json --output health_report.json
Result:
Report saved to health_report.json
Custom threshold example
server-monitor --cpu --threshold-cpu 1
Sample Output:
HOSTNAME: my-server.local
TIMESTAMP: 2026-02-13T12:34:14
OVERALL STATUS: WARNING

CPU: Usage: 1.6%, Status: WARNING
Exit code: 1 (for automation / scripts)
