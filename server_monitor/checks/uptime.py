import time
import psutil

def check_uptime(threshold=24):
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = round(uptime_seconds / 3600, 2)

    status = "OK"
    if uptime_hours > threshold:
        status = "WARNING"

    return {
        "uptime_hours": uptime_hours,
        "status": status
    }
