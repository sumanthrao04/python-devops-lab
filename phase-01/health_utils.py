def check_health(usage, threshold):
    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"