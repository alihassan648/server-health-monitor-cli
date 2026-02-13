import argparse
import json
import socket
from datetime import datetime
from .checks.cpu import check_cpu
from .checks.memory import check_memory
from .checks.disk import check_disk
from .checks.uptime import check_uptime
from .report import generate_report  # Ensure generate_report accepts only results, json/text output

# Status priority for exit codes and overall status
STATUS_PRIORITY = {
    "OK": 0,
    "WARNING": 1,
    "ALERT": 1,
    "CRITICAL": 2
}

def create_parser():
    parser = argparse.ArgumentParser(
        description="Server Health Monitoring CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--all", action="store_true", help="Run all checks")
    parser.add_argument("--cpu", action="store_true", help="Check CPU usage")
    parser.add_argument("--memory", action="store_true", help="Check memory usage")
    parser.add_argument("--disk", action="store_true", help="Check disk usage")
    parser.add_argument("--uptime", action="store_true", help="Check uptime")
    parser.add_argument("--threshold-cpu", type=float, help="CPU usage threshold")
    parser.add_argument("--threshold-memory", type=float, help="Memory usage threshold")
    parser.add_argument("--threshold-disk", type=float, help="Disk usage threshold")
    parser.add_argument("--threshold-uptime", type=float, help="Uptime threshold in hours")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    parser.add_argument("--output", type=str, help="Output file (JSON or text)")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    # Build threshold dictionary safely
    thresholds = {
        "cpu": args.threshold_cpu,
        "memory": args.threshold_memory,
        "disk": args.threshold_disk,
        "uptime": args.threshold_uptime
    }

    # Run checks
    results = {}
    if args.cpu or args.all:
        results["cpu"] = check_cpu(threshold=thresholds["cpu"])
    if args.memory or args.all:
        results["memory"] = check_memory(threshold=thresholds["memory"])
    if args.disk or args.all:
        results["disk"] = check_disk(threshold=thresholds["disk"])
    if args.uptime or args.all:
        # Guard against None threshold
        results["uptime"] = check_uptime(
            threshold=thresholds["uptime"] if thresholds["uptime"] is not None else float('inf')
        )

    # Determine overall status
    overall_status = "OK"
    for stat in results.values():
        if STATUS_PRIORITY[stat["status"]] > STATUS_PRIORITY[overall_status]:
            overall_status = stat["status"]

    # Build output data
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "overall_status": overall_status,
        **results
    }

    # Generate output string
    if args.json:
        report_str = json.dumps(output_data, indent=4)
    else:
        report_lines = [
            f"HOSTNAME: {output_data['hostname']}",
            f"TIMESTAMP: {output_data['timestamp']}",
            f"OVERALL STATUS: {output_data['overall_status']}\n"
        ]
        for key, val in results.items():
            if key == "uptime":
                report_lines.append(f"{key.upper()}: Uptime: {val['uptime_hours']} hours, Status: {val['status']}")
            else:
                report_lines.append(f"{key.upper()}: Usage: {val['usage']}%, Status: {val['status']}")
        report_str = "\n".join(report_lines)

    # Print output
    print(report_str)

    # Save to file if requested
    if args.output:
        with open(args.output, "w") as f:
            f.write(report_str)
        print(f"\nReport saved to {args.output}")

    # Return proper exit code
    exit_code = STATUS_PRIORITY[overall_status]
    return exit_code

if __name__ == "__main__":
    import sys
    sys.exit(main())
