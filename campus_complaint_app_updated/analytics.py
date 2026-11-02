"""Matplotlib analytics window."""
from config import CORAL, INK, MUTED, PAPER, STATUSES

try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
except ImportError:
    FigureCanvasTkAgg = Figure = None


def render_chart(parent, complaints):
    if not Figure or not FigureCanvasTkAgg:
        return False
    import tkinter as tk
    from tkinter import ttk

    window = tk.Toplevel(parent)
    window.title("Complaint Analytics")
    window.geometry("820x540")
    window.minsize(650, 430)
    window.configure(bg=PAPER)
    window.transient(parent)
    shell = ttk.Frame(window, padding=20)
    shell.pack(fill="both", expand=True)
    ttk.Label(shell, text="Complaint Analytics", style="Title.TLabel").pack(anchor="w")
    ttk.Label(shell, text="Live overview of complaints by current status", style="Sub.TLabel").pack(anchor="w", pady=(3, 12))
    chart_frame = ttk.Frame(shell, style="Card.TFrame", padding=10)
    chart_frame.pack(fill="both", expand=True)
    counts = [sum(1 for complaint in complaints if complaint["status"] == status) for status in STATUSES]
    #it makes the chart for the system
    figure = Figure(figsize=(8.0, 4.3), dpi=100, facecolor="white")
    axis = figure.add_subplot(111)
    bars = axis.bar(STATUSES, counts, color=["#7a5a86", CORAL, "#87a878"], width=.55, zorder=3)
    axis.set_title("Complaints by status", loc="left", fontsize=16, fontweight="bold", color=INK, pad=18)
    axis.set_ylabel("Number of complaints", color=MUTED)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color("#eadbcb")
    axis.grid(axis="y", alpha=.25, zorder=0)
    axis.set_axisbelow(True)
    axis.bar_label(bars, padding=5, fontsize=12, fontweight="bold", color="#59495d")
    axis.set_ylim(0, max(counts + [1]) * 1.25)
    figure.tight_layout()
    canvas = FigureCanvasTkAgg(figure, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    return True
