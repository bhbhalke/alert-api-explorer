def generate_explanation(alert) -> str:
    if alert.metric_value > alert.threshold:
        relationship = "exceeded"
    elif alert.metric_value < alert.threshold:
        relationship = "fell below"
    else:
        relationship = "reached"

    next_steps = {
        "critical": "Investigate immediately and take corrective action.",
        "warning": "Review the affected system and monitor the metric closely.",
        "info": "Review the metric and confirm whether any action is needed.",
    }

    return (
        f'This {alert.severity} alert from {alert.source} is titled "{alert.title}". '
        f"The {alert.metric_name} metric {relationship} its threshold: the current value is "
        f"{alert.metric_value}, compared with a threshold of {alert.threshold}. "
        f"Recommended next step: {next_steps[alert.severity]}"
    )