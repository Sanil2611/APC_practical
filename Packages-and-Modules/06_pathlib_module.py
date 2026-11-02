from pathlib import Path

folder = Path(".")
print("Current folder:", folder.resolve())
print("Python files:", list(folder.glob("*.py")))
