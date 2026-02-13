import psutil

def check_cpu(threshold=None):
    """Check CPU usage and return status."""
    usage = psutil.cpu_percent(interval=1)
    status = "OK"
    if threshold is not None and usage > threshold:
        status = "WARNING"
    return {"usage": usage, "status": status}
