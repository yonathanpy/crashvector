def analyze_crash(signal_name):
    if signal_name == "SIGSEGV":
        return "Segmentation fault: invalid memory access"
    if signal_name == "SIGABRT":
        return "Abort signal: possible heap corruption"
    if signal_name == "SIGBUS":
        return "Bus error: unaligned memory access"
    return "Unknown crash signal"
