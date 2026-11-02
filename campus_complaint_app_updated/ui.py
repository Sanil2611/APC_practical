import hashlib
import hmac #-it is used to compare the hashed password and stored password  
import tkinter as tk #used to create gui of our system
from datetime import datetime
from tkinter import filedialog, messagebox, ttk

from config import CATEGORIES, DEMO_USERS, PAPER, INK, PLUM, CORAL, MUTED, STATUSES
from storage import load_complaints, save_complaints, load_users, save_users
from analytics import render_chart

try:
    import pandas as pd
except ImportError:
    pd = None


class CampusComplaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Campus Complaint Desk")
        self.geometry("1120x760")
        self.minsize(760, 560)
        self.configure(bg=PAPER)
        self.username = None
        self.role = None
        self.complaints = load_complaints()
        self.users = load_users()
        self.search_var = tk.StringVar()
        self._style()
        self.show_login()

    def persist_complaints(self):
        try:
            save_complaints(self.complaints)
            return True
        except OSError as exc:
            messagebox.showerror("Save failed", f"Your changes could not be saved.\n\n{exc}", parent=self)
            return False

    def _style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TFrame", background=PAPER)
        style.configure("Card.TFrame", background="white")
        style.configure("TLabel", background=PAPER, foreground=INK, font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Georgia", 23, "bold"), foreground=INK)
        style.configure("Sub.TLabel", foreground=MUTED)
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=36, background="#fffdf9", fieldbackground="#fffdf9", foreground=INK)
        style.configure("Treeview", rowheight=34)
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#f0e5d8", foreground=PLUM, padding=10)
        style.map("Treeview", background=[("selected", "#f6d6c7")], foreground=[("selected", INK)])
        style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=(12, 8), background="#f1dfd1", foreground=PLUM)
        style.map("TButton", background=[("active", "#e9c8b6")])

    def clear(self):
        for child in self.winfo_children():
            child.destroy()

    def show_login(self):
        self.unbind("<Return>")
        self.username = self.role = None
        self.clear()
        self.configure(bg=PLUM)
        shell = ttk.Frame(self, padding=24)
        shell.place(relx=.5, rely=.5, anchor="center")
        card = tk.Frame(shell, bg="white", padx=32, pady=30, highlightthickness=1, highlightbackground="#eadbcb")
        card.pack()
        tk.Frame(card, bg=CORAL, height=5).pack(fill="x", pady=(0, 22))
        tk.Label(card, text="THE CAMPUS NOTICEBOARD", bg="white", fg=PLUM,
                 font=("Georgia", 11, "bold")).pack(anchor="w")
        tk.Label(card, text="Speak up. We’ll follow up.", bg="white", fg=INK,
                 font=("Georgia", 23, "bold")).pack(anchor="w", pady=(8, 0))
        tk.Label(card, text="Sign in to report and track campus issues", bg="white", fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 22))
        tk.Label(card, text="Username", bg="white", font=("Segoe UI", 10)).pack(anchor="w")
        self.user_entry = ttk.Entry(card, width=38)
        self.user_entry.pack(pady=(5, 13))
        tk.Label(card, text="Password", bg="white", font=("Segoe UI", 10)).pack(anchor="w")
        self.pass_entry = ttk.Entry(card, width=38, show="●")
        self.pass_entry.pack(pady=(5, 18))
        ttk.Button(card, text="Sign in", command=self.login).pack(fill="x")
        ttk.Button(card, text="Create student account", command=self.create_account).pack(fill="x", pady=(8, 0))
        tk.Label(card, text="Demo: admin / admin123   ·   student / student123",
                 bg="white", fg="#64748b", font=("Segoe UI", 9)).pack(anchor="w", pady=(18, 0))
        tk.Label(card, text="Demo credentials are for learning only. Change them before real use.",
                 bg="white", fg="#9a5b19", font=("Segoe UI", 8)).pack(anchor="w", pady=(5, 0))
        self.user_entry.focus_set()
        self.bind("<Return>", lambda _e: self.login())
        self.bind("<Escape>", lambda _e: self.show_login())

    def login(self):
        name = self.user_entry.get().strip().lower()
        password = self.pass_entry.get()
        account = DEMO_USERS.get(name) or self.users.get(name)
        if not account:
            messagebox.showerror("Sign in failed", "Check your username and password.")
            return
        stored_password = account["password"]
        if account.get("password_hashed"):
            valid = hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(), stored_password)
        else:
            valid = hmac.compare_digest(password, stored_password)
        if not valid:
            messagebox.showerror("Sign in failed", "Check your username and password.")
            return
        self.username, self.role = name, account["role"]
        self.show_dashboard()

    def create_account(self):
        win = tk.Toplevel(self)
        win.title("Create student account")
        win.geometry("380x300")
        win.transient(self)
        win.grab_set()
        frame = ttk.Frame(win, padding=22)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Create student account", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 14))
        ttk.Label(frame, text="Username").pack(anchor="w")
        username = ttk.Entry(frame)
        username.pack(fill="x", pady=(4, 12))
        ttk.Label(frame, text="Password (at least 8 characters)").pack(anchor="w")
        password = ttk.Entry(frame, show="●")
        password.pack(fill="x", pady=(4, 12))
        ttk.Label(frame, text="Confirm password").pack(anchor="w")
        confirm = ttk.Entry(frame, show="●")
        confirm.pack(fill="x", pady=(4, 16))

        def submit():
            name, secret = username.get().strip().lower(), password.get()
            if len(name) < 3 or not name.replace("_", "").isalnum():
                messagebox.showwarning("Invalid username", "Use at least 3 letters or numbers; underscores are allowed.", parent=win)
                return
            if name in DEMO_USERS or name in self.users:
                messagebox.showwarning("Username taken", "Choose a different username.", parent=win)
                return
            if len(secret) < 8:
                messagebox.showwarning("Password too short", "Use at least 8 characters.", parent=win)
                return
            if secret != confirm.get():
                messagebox.showwarning("Passwords do not match", "Enter the same password in both fields.", parent=win)
                return
            self.users[name] = {"password": hashlib.sha256(secret.encode()).hexdigest(),
                                "password_hashed": True, "role": "student"}
            try:
                save_users(self.users)
            except OSError as exc:
                messagebox.showerror("Could not create account", str(exc), parent=win)
                return
            win.destroy()
            messagebox.showinfo("Account created", "Your account is ready. Sign in with your new credentials.", parent=self)
            self.user_entry.delete(0, "end")
            self.user_entry.insert(0, name)
            self.pass_entry.focus_set()

        actions = ttk.Frame(frame)
        actions.pack(fill="x", pady=(2, 0))
        ttk.Button(actions, text="Cancel", command=win.destroy).pack(side="right", padx=(8, 0))
        ttk.Button(actions, text="Create account", command=submit).pack(side="right")
        username.focus_set()
        win.bind("<Return>", lambda _event: submit())
        win.bind("<Escape>", lambda _event: win.destroy())

    def show_dashboard(self):
        self.unbind("<Return>")
        self.unbind("<Escape>")
        self.clear()
        top = ttk.Frame(self, padding=(22, 16))
        top.pack(fill="x")
        self.configure(bg=PAPER)
        ttk.Label(top, text="The Campus Noticeboard", style="Title.TLabel").pack(side="left")
        ttk.Label(top, text=f"{self.username.title()} · {self.role.title()}", style="Sub.TLabel").pack(side="right", padx=12)
        #This line displays the logged-in user's name and role on the right side of the window.
        ttk.Button(top, text="Log out", command=self.show_login).pack(side="right")
        tk.Frame(self, bg=CORAL, height=3).pack(fill="x", padx=22)
        body = ttk.Frame(self, padding=22)
        body.pack(fill="both", expand=True)
        if self.role == "student":
            self.student_view(body)
        else:
            self.admin_view(body)
        # it tells which module should open 

    def make_table(self, parent, rows):
        wrap = ttk.Frame(parent)
        wrap.pack(fill="both", expand=True, pady=(10, 0))
        columns = ("id", "date", "category", "title", "status")
        tree = ttk.Treeview(wrap, columns=columns, show="headings", selectmode="browse")
        labels = {"id": "ID", "date": "Date", "category": "Category", "title": "Complaint", "status": "Status"}
        widths = {"id": 65, "date": 145, "category": 130, "title": 380, "status": 125}
        for col in columns:
            tree.heading(col, text=labels[col])
            tree.column(col, width=widths[col], minwidth=55, anchor="w", stretch=(col == "title"))
        scroll = ttk.Scrollbar(wrap, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        for item in rows:
            tree.insert("", "end", iid=str(item["id"]), values=(item["id"], item["created_at"], item["category"], item["title"], item["status"]))
        tree.tag_configure("Submitted", foreground="#9a5b19")
        tree.tag_configure("In Progress", foreground="#55345f")
        tree.tag_configure("Resolved", foreground="#397044")
        for item in rows:
            tree.item(str(item["id"]), tags=(item.get("status", ""),))
        return tree

    def student_view(self, parent):
        head = ttk.Frame(parent)
        head.pack(fill="x")
        ttk.Label(head, text="My complaints", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(head, text="＋ New complaint", command=self.new_complaint).pack(side="right")
        mine = [c for c in self.complaints if c["student"] == self.username]
        if not mine:
            empty = ttk.Frame(parent, style="Card.TFrame", padding=24)
            empty.pack(fill="x", pady=(24, 10))
            ttk.Label(empty, text="No complaints yet", font=("Segoe UI", 15, "bold")).pack(anchor="w")
            ttk.Label(empty, text="Use ‘New complaint’ to report an issue. You can track its progress here.", style="Sub.TLabel").pack(anchor="w", pady=(6, 0))
            self.student_tree = None
            return
        self.student_tree = self.make_table(parent, mine)
        ttk.Label(parent, text="Select a row to read the full description.", style="Sub.TLabel").pack(anchor="w", pady=8)
        ttk.Button(parent, text="View details", command=self.view_student_detail).pack(anchor="w")

    def new_complaint(self):
        win = tk.Toplevel(self)
        win.title("New complaint")
        win.geometry("480x470")
        win.transient(self)
        win.grab_set()
        frame = ttk.Frame(win, padding=22)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Submit a complaint", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 16))
        ttk.Label(frame, text="Category").pack(anchor="w")
        category = ttk.Combobox(frame, values=CATEGORIES, state="readonly")
        category.current(0)
        category.pack(fill="x", pady=(4, 12))
        ttk.Label(frame, text="Short title").pack(anchor="w")
        title = ttk.Entry(frame)
        title.pack(fill="x", pady=(4, 12))
        ttk.Label(frame, text="Description").pack(anchor="w")
        desc = tk.Text(frame, height=9, wrap="word", font=("Segoe UI", 10))
        desc.pack(fill="both", expand=True, pady=(4, 14))

        def submit():
            subject, details = title.get().strip(), desc.get("1.0", "end").strip()
            if not subject or not details:
                messagebox.showwarning("Missing information", "Enter a title and description.", parent=win)
                return
            entry = {"id": max((c["id"] for c in self.complaints), default=0) + 1,
                     "student": self.username, "category": category.get(), "title": subject,
                     "description": details, "status": "Submitted",
                     "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")}
            self.complaints.append(entry)
            if not self.persist_complaints():
                self.complaints.pop()
                return
            win.destroy()
            self.show_dashboard()
        ttk.Button(frame, text="Submit complaint", command=submit).pack(anchor="e")

    def view_student_detail(self):
        if self.student_tree is None:
            return
        selected = self.student_tree.selection()
        if not selected:
            messagebox.showinfo("Select a complaint", "Choose a complaint first.")
            return
        item = next(c for c in self.complaints if str(c["id"]) == selected[0])
        messagebox.showinfo(item["title"], f"Category: {item['category']}\nStatus: {item['status']}\n\n{item['description']}")

    def admin_view(self, parent):
        ttk.Label(parent, text="Complaint administration", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        controls = ttk.Frame(parent)
        controls.pack(fill="x", pady=(10, 0))
        ttk.Label(controls, text="Search:").pack(side="left")
        search = ttk.Entry(controls, textvariable=self.search_var, width=24)
        search.pack(side="left", padx=(6, 12))
        ttk.Label(controls, text="Update selected status:").pack(side="left")
        self.status_choice = ttk.Combobox(controls, values=STATUSES, state="readonly", width=18)
        self.status_choice.set("In Progress")
        self.status_choice.pack(side="left", padx=8)
        ttk.Button(controls, text="Save status", command=self.update_status).pack(side="left")
        ttk.Button(controls, text="View details", command=self.view_admin_detail).pack(side="left", padx=8)
        ttk.Button(controls, text="Export CSV", command=self.export_csv).pack(side="right")
        ttk.Button(controls, text="📊 View analytics", command=self.open_chart).pack(side="right", padx=8)
        self.admin_tree = self.make_table(parent, self.complaints)
        self.search_var.trace_add("write", self._search_changed)

    def _search_changed(self, *_args):
        self.filter_admin_table()

    def filter_admin_table(self):
        if not hasattr(self, "admin_tree") or not self.admin_tree.winfo_exists():
            return
        query = self.search_var.get().strip().casefold()
        for row in self.admin_tree.get_children():
            self.admin_tree.delete(row)
        for item in self.complaints:
            searchable = " ".join(str(item.get(key, "")) for key in ("id", "student", "created_at", "category", "title", "status"))
            if query and query not in searchable.casefold():
                continue
            self.admin_tree.insert("", "end", iid=str(item["id"]), values=(item["id"], item["created_at"], item["category"], item["title"], item["status"]))

    def update_status(self):
        selected = self.admin_tree.selection()
        if not selected:
            messagebox.showinfo("Select a complaint", "Choose a complaint first.")
            return
        complaint = next(c for c in self.complaints if str(c["id"]) == selected[0])
        original_status = complaint["status"]
        complaint["status"] = self.status_choice.get()
        if not self.persist_complaints():
            complaint["status"] = original_status
            return
        self.show_dashboard()

    def view_admin_detail(self):
        selected = self.admin_tree.selection()
        if not selected:
            messagebox.showinfo("Select a complaint", "Choose a complaint first.")
            return
        item = next(c for c in self.complaints if str(c["id"]) == selected[0])
        messagebox.showinfo(item["title"], f"Student: {item['student']}\nCategory: {item['category']}\nStatus: {item['status']}\nDate: {item['created_at']}\n\n{item['description']}")

    def open_chart(self):
        if not render_chart(self, self.complaints):
            messagebox.showinfo("Matplotlib required", "Install Matplotlib to view analytics:\n\npython -m pip install matplotlib")
    def export_csv(self):
        if not self.complaints:
            messagebox.showinfo("Nothing to export", "There are no complaints yet.")
            return
        filename = filedialog.asksaveasfilename(title="Export complaints", defaultextension=".csv",
                                                 filetypes=[("CSV file", "*.csv")], initialfile="campus_complaints.csv")
        if not filename:
            return
        records = [{"ID": c["id"], "Student": c["student"], "Date": c["created_at"],
                    "Category": c["category"], "Title": c["title"], "Description": c["description"], "Status": c["status"]}
                   for c in self.complaints]
        try:
            if pd is not None:
                pd.DataFrame(records).to_csv(filename, index=False, encoding="utf-8-sig")
            else:
                import csv
                with open(filename, "w", newline="", encoding="utf-8-sig") as f:
                    writer = csv.DictWriter(f, fieldnames=records[0].keys())
                    writer.writeheader()
                    writer.writerows(records)
            messagebox.showinfo("Export complete", f"Saved {len(records)} complaints to:\n{filename}")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc))



