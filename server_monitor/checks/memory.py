import psutil

def check_memory(threshold=None):
    """Check Memory usage and return status."""
    usage = psutil.virtual_memory().percent
    status = "OK"
    if threshold is not None and usage > threshold:
        status = "WARNING"
    return {"usage": usage, "status": status}
