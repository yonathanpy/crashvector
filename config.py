LOG_FILE = "logs/crashvector.log"

RISK_WEIGHTS = {
    "stack_overflow": 3,
    "heap_overflow": 3,
    "use_after_free": 4,
    "missing_canary": 2,
    "missing_nx": 2,
    "missing_pie": 2
}
