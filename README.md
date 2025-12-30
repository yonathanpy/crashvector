 CRASHVECTOR

Memory Corruption & Exploitability Analysis Framework

CRASHVECTOR performs post‑crash forensic analysis on native Linux binaries.  
It evaluates real core dumps to determine crash origin, memory corruption type, binary hardening state, and practical exploitability risk.

The framework is designed for vulnerability research, crash triage, and defensive security analysis.

Capabilities
- Core dump inspection via GDB (batch)
- Crash signal classification
- Memory corruption pattern detection
- ELF hardening analysis (NX, PIE, CANARY)
- Exploitability risk scoring

 Scope
CRASHVECTOR does not exploit vulnerabilities.  
It analyzes crashes to support responsible research and mitigation.

 Requirements
Linux, Python 3.9+, GDB

## License
MIT
