# server_monitor/report.py

import json

def generate_report(results, output_format="text", output_file=None, timestamp=None, hostname=None, overall_status=None):
    """
    Generate server health report in text or JSON format.
    """
    if output_format == "json":
        report_data = {
            "timestamp": timestamp,
            "hostname": hostname,
            "overall_status": overall_status,
            **results
        }
        report_str = json.dumps(report_data, indent=4)
    else:
        lines = []
        if hostname:
            lines.append(f"HOSTNAME: {hostname}")
        if timestamp:
            lines.append(f"TIMESTAMP: {timestamp}")
        if overall_status:
            lines.append(f"OVERALL STATUS: {overall_status}")
        for key, value in results.items():
            if key == "uptime":
                lines.append(f"{key.upper()}: Uptime: {value['uptime_hours']:.2f} hours, Status: {value['status']}")
            else:
                lines.append(f"{key.upper()}: Usage: {value['usage']}%, Status: {value['status']}")
        report_str = "\n".join(lines)

    if output_file:
        with open(output_file, "w") as f:
            f.write(report_str + "\n")
        print(f"Report saved to {output_file}")

    return report_str
