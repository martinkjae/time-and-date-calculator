import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime, timedelta

# Parse time string and day into a datetime object
def parse_time_day(time_str, day_str):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_str = day_str.strip().lower()
    if day_str not in days:
        raise ValueError("Invalid day of the week.")

    # Check for 12-hour format
    match_12 = re.match(r"(\d{1,2}):?(\d{2})?\s*(AM|PM)", time_str.strip(), re.IGNORECASE)
    match_24 = re.match(r"(\d{1,2}):(\d{2})$", time_str.strip())

    if match_12:
        hour = int(match_12.group(1))
        minute = int(match_12.group(2)) if match_12.group(2) else 0
        period = match_12.group(3).upper()
        if hour == 12:
            hour = 0
        if period == "PM":
            hour += 12
    elif match_24:
        hour = int(match_24.group(1))
        minute = int(match_24.group(2))
        if hour > 23 or minute > 59:
            raise ValueError("Invalid 24-hour time format.")
    else:
        raise ValueError("Invalid time format. Use '3 PM', '3:30 PM' or '15:30'.")

    # Get the next given day
    today = datetime.now()
    today_weekday = today.weekday()  #0 index from monday
    target_weekday = days.index(day_str)
    days_ahead = (target_weekday - today_weekday) % 7
    target_date = today + timedelta(days=days_ahead)

    return target_date.replace(hour=hour, minute=minute, second=0, microsecond=0)

# Calculate the difference
def calculate_difference():
    try:
        start_time = entry_start_time.get()
        start_day = entry_start_day.get()
        end_time = entry_end_time.get()
        end_day = entry_end_day.get()

        dt1 = parse_time_day(start_time, start_day)
        dt2 = parse_time_day(end_time, end_day)

        # If end time is before start time, assume it's next week
        if dt2 <= dt1:
            dt2 += timedelta(days=7)

        diff = dt2 - dt1
        hours, remainder = divmod(diff.total_seconds(), 3600)
        minutes = remainder // 60

        result_label.config(text=f"Time difference: {int(hours)} hours and {int(minutes)} minutes")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# GUi
root = tk.Tk()
root.title("Time Until Event Calculator")

tk.Label(root, text="Start Time (e.g. 3:00 PM or 15:00):").pack()
entry_start_time = tk.Entry(root)
entry_start_time.pack()

tk.Label(root, text="Start Day (e.g. Wednesday):").pack()
entry_start_day = tk.Entry(root)
entry_start_day.pack()

tk.Label(root, text="End Time (e.g. 1:00 PM or 13:00):").pack()
entry_end_time = tk.Entry(root)
entry_end_time.pack()

tk.Label(root, text="End Day (e.g. Friday):").pack()
entry_end_day = tk.Entry(root)
entry_end_day.pack()

tk.Button(root, text="Calculate Time Difference", command=calculate_difference).pack(pady=10)

result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
result_label.pack()

root.mainloop()
