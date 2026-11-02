"""Local JSON file storage for complaints and accounts."""
import json
from pathlib import Path
from tkinter import messagebox

DATA_FILE = Path(__file__).resolve().parent / "complaints.json"
USERS_FILE = Path(__file__).resolve().parent / "users.json"


def load_users():
    """Load registered accounts, tolerating a missing or invalid file."""
    if not USERS_FILE.exists():
        return {}
    try:
        with USERS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return {name: account for name, account in data.items()
                if isinstance(name, str) and isinstance(account, dict)
                and account.get("role") == "student" and isinstance(account.get("password"), str)}
    except (json.JSONDecodeError, OSError):
        messagebox.showerror("Data error", f"Could not read {USERS_FILE.name}. The file may be damaged.")
        return {}


def save_users(users):
    temporary = USERS_FILE.with_suffix(".tmp")
    with temporary.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
    temporary.replace(USERS_FILE)


def load_complaints():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        messagebox.showerror("Data error", f"Could not read {DATA_FILE.name}. The file may be damaged.")
        return []


def save_complaints(complaints):
    temporary = DATA_FILE.with_suffix(".tmp")
    with temporary.open("w", encoding="utf-8") as file:
        json.dump(complaints, file, indent=2, ensure_ascii=False)
    temporary.replace(DATA_FILE)


def save_json(path, data):
    """Write JSON atomically so an interrupted save does not truncate user data."""
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    temporary.replace(path)
