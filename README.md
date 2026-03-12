# 📱 WhatsApp Message Scheduler (Python + Twilio + CustomTkinter)

A **desktop application built with Python** that allows users to **schedule WhatsApp messages to be sent automatically at a specific date and time**.
The project uses the **Twilio API for WhatsApp messaging** and a **modern GUI built with CustomTkinter** to provide a user-friendly interface.

---

# 🚀 Features

* ⏰ **Schedule WhatsApp Messages**
* 🖥️ **Modern Desktop UI**
* 🌙 **Dark Mode Interface**
* 📅 **Date & Time Based Scheduling**
* 🔄 **Background Threading for Scheduling**
* 📲 **WhatsApp Messaging via Twilio API**
* 👤 **User Input Form for Message Details**

---

# 🛠️ Tech Stack

* **Python**
* **Twilio API**
* **CustomTkinter (Modern Python GUI)**
* **Threading**
* **Datetime Module**

---

# 📸 Application Workflow

1. Enter the **recipient name**
2. Enter **WhatsApp number with country code**
3. Type the **message**
4. Select the **date and time**
5. Click **Schedule Message**
6. The message will automatically be sent at the scheduled time

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Bittu169/WhatsApp_Chat_Automation.git
cd whatsapp-message-scheduler
```

Install dependencies:

```bash
pip install twilio customtkinter
```

---

# 🔑 Twilio Setup

1. Create an account at https://www.twilio.com
2. Get your **Account SID** and **Auth Token**
3. Replace them in the Python script:

```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
```

4. Join the **Twilio WhatsApp Sandbox** and verify your number.

---

# ▶️ Run the Application

```bash
python main.py
```

---

# 🖥️ Application Preview

<p align="center">
  <img src="https://github.com/Bittu169/WhatsApp_Chat_Automation/blob/979d3946530a40a7d8b4578287e4862040209aaf/Screenshot%202026-03-12%20174455.png?raw=true" width="700">
</p>


---

# 📂 Project Structure

```
whatsapp-message-scheduler
│
├── main.py
├── README.md
└── screenshots
    └── ui.png
```

---

# 📈 Future Improvements

* 📅 Calendar Date Picker
* 📁 Send Messages to Multiple Contacts (CSV)
* 💾 Store Scheduled Messages in SQLite Database
* 📊 Dashboard for Scheduled Messages
* 📦 Convert into Desktop EXE Application

---

# 👨‍💻 Author

**Bittu Mondal**
MCA Student | Aspiring Full-Stack Developer & AI/ML Engineer

* LinkedIn: https://linkedin.com/in/bittu-mondal-a06258313
* GitHub: https://github.com/Bittu169

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
