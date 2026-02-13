import psutil

def check_disk(threshold=None):
    """Check Disk usage (root partition) and return status."""
    usage = psutil.disk_usage('/').percent
    status = "OK"
    if threshold is not None and usage > threshold:
        status = "WARNING"
    return {"usage": usage, "status": status}
