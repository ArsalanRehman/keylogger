# **Keylogger with Server Logging**

## **📌 Overview**

This project consists of a **Python keylogger** that captures keystrokes and sends them to a **Node.js server**, which then stores the logs in a file (`keys.txt`). The purpose of this project is purely **educational** and aims to demonstrate how keyloggers work in terms of logging, networking, and data storage.

> **⚠ Disclaimer:** This project is for **educational purposes only**. Unauthorized use of keyloggers is illegal and unethical. I take **no responsibility** for any misuse of this code. Use it only in environments where you have explicit permission.

---

## **🛠 Features**

✅ **Real-time Key Logging** – Captures user keystrokes and stores them in memory.  
✅ **Automatic Data Transmission** – Sends logs to the server every 6 minutes (360 seconds).  
✅ **Remote Logging** – Uses an Express.js server to receive and store keystrokes in a file.  
✅ **Cross-Platform Support** – Works on Windows, macOS, and Linux.

---

## **📂 Project Structure**

```
/keylogger-project
│── server.js       # Node.js server to collect key logs
│── keylogger.py    # Python script to capture keystrokes and send them to server
│── keys.txt        # File where logs are stored
│── README.md       # Project documentation (this file)
```

---

## **🚀 Installation & Usage**

### **1️⃣ Install Dependencies**

Ensure you have **Python 3**, **Node.js**, and **pip** installed.

#### **🔹 Install Node.js Packages**

```sh
cd /path/to/project
npm install express body-parser
```

#### **🔹 Install Python Packages**

```sh
pip install pynput requests
```

---

### **2️⃣ Start the Server**

Run the **Node.js server** to receive logs:

```sh
node server.js
```

if you also wanna use ngrok to attack outside of the local network:

```sh
ngrok http 3002 --url 893f13a17c53-18320658179660089964.ngrok-free.app
```

You should see:

```
Server running on http://localhost:3002
```

---

### **3️⃣ Run the Keylogger**

Start the keylogger script in Python:

```sh
python keylogger.py
```

Now, the script will **silently capture** keystrokes and send them to the server every **6 minutes**.

---

## **🛑 Stopping the Keylogger**

To **stop** the keylogger, press **`Esc`**, or terminate the script manually:

```sh
Ctrl + C
```

---

## **⚠ Legal & Ethical Disclaimer**

This project is strictly for **educational purposes**. Unauthorized usage of keyloggers to capture **sensitive or personal data** without **explicit consent** is **illegal** in most countries.

**I am NOT responsible for any misuse of this code.** Use it only on **your own systems** or with **explicit permission**. **Misuse can lead to legal consequences.**

By using this project, you **agree to use it responsibly** and for **ethical hacking and cybersecurity learning only**.

---

## **📌 Author & Contributions**

Developed by **[ARSALAN REHMAN]** 🚀  
Feel free to contribute, open issues, or suggest improvements!

---

**💡 Enjoy learning about keylogging, but always stay ethical!** 🔐
