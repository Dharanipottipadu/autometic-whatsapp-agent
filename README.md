# 📌 WhatsApp Automation Agent

## 🔹 Overview

WhatsApp Automation Agent is a Python-based desktop application that allows users to send scheduled WhatsApp messages automatically using WhatsApp Web. The project provides a simple GUI interface, making it easy for non-technical users to automate message sending.

---

## 🔹 Features

* 📱 Send WhatsApp messages automatically
* ⏰ Schedule messages at a specific time
* 🖥️ Simple and user-friendly GUI
* ⚡ Real-time status updates
* 📦 Executable (.exe) support for easy usage

---

## 🔹 Technologies Used

* Python
* Tkinter (GUI)
* pywhatkit
* pyautogui
* PyInstaller

---

## 🔹 Project Structure

```
whatsapp_automation_agent/
│
├── whatsapp_gui.py        # Main application file
├── whatsapp_gui.exe       # Executable file (generated)
├── README.md              # Project documentation
```

---

## 🔹 Installation (For Developers)

1. Clone the repository:

```
git clone https://github.com/your-username/whatsapp-automation-agent.git
cd whatsapp-automation-agent
```

2. Install required libraries:

```
pip install pywhatkit
pip install pyautogui
```

3. Run the application:

```
python whatsapp_gui.py
```

---

## 🔹 Usage (Executable Version)

1. Open the `.exe` file
2. Enter:

   * Phone number (with country code, e.g., +91XXXXXXXXXX)
   * Message
   * Time (24-hour format)
3. Click **Schedule Message**
4. Keep system active until message is sent

---

## 🔹 How It Works

1. User inputs required details
2. Application opens browser
3. Loads WhatsApp Web
4. Sends message automatically at scheduled time

---

## 🔹 Requirements

* Active internet connection
* WhatsApp Web login
* Desktop/Laptop system

---

## 🔹 Important Notes

* Ensure WhatsApp Web is logged in before running
* Do not use keyboard/mouse during automation
* Set time at least 2 minutes ahead
* Works best on stable internet connection

---

## 🔹 Limitations

* Depends on browser automation
* May fail if system is interrupted
* Not supported on mobile devices

---

## 🔹 Future Enhancements

* 📂 Bulk messaging (Excel support)
* 🎨 Improved UI/UX
* 🤖 AI-based auto replies
* 🌐 Selenium integration for better reliability

---

## 🔹 Author

**DHARANI P**

---

## 🔹 License

This project is for educational purposes.
