from pathlib import Path

ENTRY = "fix: retry stuck refunds hourly; forgot to mark paid, 4 ex-customers are now on payroll"

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(ENTRY.encode("utf-8"))
