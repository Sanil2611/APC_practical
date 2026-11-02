CAMPUS COMPLAINT DESK

Run on Windows:
1. Install Python 3.
2. Open a terminal in this folder.
3. Run: python -m pip install -r requirements.txt
4. Run: python main.py

Demo sign-ins:
Admin: admin / admin123
Student: student / student123

Students can create accounts from the sign-in screen. Registered accounts and complaints are stored in users.json and complaints.json beside the app. Admins can search complaints by ID, student, date, category, title, or status, update statuses, view analytics, and export a CSV.

Tkinter is included with most standard Python installations. Matplotlib charts are available when Matplotlib is installed; CSV export uses pandas when available and a built-in fallback otherwise.

This is a classroom demo. Demo credentials and local JSON storage are not suitable for a real deployment.
