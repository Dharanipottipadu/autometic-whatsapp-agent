import tkinter as tk
from tkinter import messagebox
import threading
import pywhatkit
import pyautogui
import time
from datetime import datetime

# ==============================
# FUNCTION TO SEND MESSAGE
# ==============================
def send_message():
    def task():
        try:
            number = entry_number.get().strip()
            message = text_message.get("1.0", "end").strip()
            hour = int(entry_hour.get())
            minute = int(entry_minute.get())

            # Validation
            if not number.startswith("+"):
                messagebox.showerror("Error", "Use +91 format")
                return

            if message == "":
                messagebox.showerror("Error", "Message cannot be empty")
                return

            now = datetime.now()

            # Ensure time is at least 2 minutes ahead
            if (hour == now.hour and minute <= now.minute + 1) or hour < now.hour:
                messagebox.showerror("Error", "Set time at least 2 minutes ahead")
                return

            status_label.config(text="Waiting for scheduled time...", fg="blue")

            # Schedule message
            pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=20)

            # Wait for WhatsApp Web to fully load
            time.sleep(25)

            # Ensure focus on chat
            pyautogui.click()

            # Press ENTER multiple times to ensure send
            for _ in range(3):
                pyautogui.press("enter")
                time.sleep(1)

            status_label.config(text="Message Sent Successfully ✅", fg="green")

        except Exception as e:
            status_label.config(text="Failed ❌", fg="red")
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task).start()


# ==============================
# GUI SETUP
# ==============================
root = tk.Tk()
root.title("WhatsApp Automation Agent")
root.geometry("400x500")
root.resizable(False, False)

# Title
tk.Label(root, text="WhatsApp Automation Agent", font=("Arial", 14, "bold")).pack(pady=10)




# Phone Number
tk.Label(root, text="Phone Number (+91...)").pack()
entry_number = tk.Entry(root, width=30)
entry_number.pack(pady=5)

# Message
tk.Label(root, text="Message").pack()
text_message = tk.Text(root, height=5, width=30)
text_message.pack(pady=5)

# Hour
tk.Label(root, text="Hour (24 format)").pack()
entry_hour = tk.Entry(root)
entry_hour.pack(pady=5)

# Minute
tk.Label(root, text="Minute").pack()
entry_minute = tk.Entry(root)
entry_minute.pack(pady=5)

# Button
tk.Button(root, text="Schedule Message", command=send_message,
          bg="green", fg="white", width=20).pack(pady=20)

# Status
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()