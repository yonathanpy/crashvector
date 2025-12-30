def classify_pattern(description):
    description = description.lower()

    if "stack" in description:
        return "stack_overflow"

    if "heap" in description:
        return "heap_overflow"

    if "use after free" in description:
        return "use_after_free"

    return "unknown"
