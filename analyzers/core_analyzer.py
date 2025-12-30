import subprocess

def analyze_core(binary_path, core_path):
    try:
        cmd = [
            "gdb",
            "--batch",
            "-ex", "info signals",
            "-ex", "bt",
            binary_path,
            core_path
        ]

        output = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            text=True
        )

        if "SIGSEGV" in output:
            return "SIGSEGV", "Segmentation fault from invalid memory access"

        if "SIGABRT" in output:
            return "SIGABRT", "Abort signal, possible heap corruption"

        return "UNKNOWN", "Unknown crash signal"

    except Exception as e:
        return "ERROR", str(e)
