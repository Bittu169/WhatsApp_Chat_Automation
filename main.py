import customtkinter as ctk
from twilio.rest import Client
from datetime import datetime
import time
import threading
from tkinter import messagebox

# Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Send message function
def send_whatsapp_message(rec_no, msg_body):
    try:
        msg = client.messages.create(
            from_='whatsapp:+Enter_Twilio_WhatsApp_Number',
            body=msg_body,
            to=f'whatsapp:{rec_no}'
        )
        messagebox.showinfo("Success", f"Message Sent!\nSID: {msg.sid}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Background scheduler
def wait_and_send(delay, rec_no, msg_body):
    time.sleep(delay)
    send_whatsapp_message(rec_no, msg_body)


# Schedule button function
def schedule_message():

    name = name_entry.get()
    number = number_entry.get()
    message = message_box.get("1.0", "end")
    date = date_entry.get()
    time_str = time_entry.get()

    try:
        schedule_time = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
        current_time = datetime.now()

        delay = (schedule_time - current_time).total_seconds()

        if delay <= 0:
            messagebox.showerror("Error", "Please enter a future time.")
            return

        messagebox.showinfo("Scheduled", f"Message scheduled for {name}")

        threading.Thread(target=wait_and_send, args=(delay, number, message)).start()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ---------------- #

app = ctk.CTk()
app.title("WhatsApp Message Scheduler")
app.geometry("500x520")

title = ctk.CTkLabel(app, text="WhatsApp Message Scheduler", font=("Arial", 24, "bold"))
title.pack(pady=20)

name_entry = ctk.CTkEntry(app, placeholder_text="Recipient Name", width=350)
name_entry.pack(pady=10)

number_entry = ctk.CTkEntry(app, placeholder_text="WhatsApp Number (+CountryCode)", width=350)
number_entry.pack(pady=10)

date_entry = ctk.CTkEntry(app, placeholder_text="Date (YYYY-MM-DD)", width=350)
date_entry.pack(pady=10)

time_entry = ctk.CTkEntry(app, placeholder_text="Time (HH:MM)", width=350)
time_entry.pack(pady=10)

message_box = ctk.CTkTextbox(app, width=350, height=120)
message_box.pack(pady=10)

schedule_btn = ctk.CTkButton(app, text="Schedule Message", command=schedule_message)
schedule_btn.pack(pady=20)

app.mainloop()