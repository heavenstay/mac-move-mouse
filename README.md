# **Mac Move Mouse** 🖱️  
A simple macOS app that moves your mouse automatically to keep your status **active** on Microsoft Teams—because sometimes, managers value **"online"** more than actual work.  

## **🚀 How It Works**  
This script **moves your mouse** periodically to prevent Teams from marking you as **"Away."**  
Instead of using complicated automation tools, this guide will show you how to **turn it into a simple Mac app** that you can launch with one click.  

---

## **🛠️ Setup Instructions**  

### **1️⃣ Install Dependencies**  
Open a terminal and install `pyautogui`:  
```sh
pip install pyautogui
```

---

### **2️⃣ Create the Script**  
Create a Python script called **`ToxicManagerSaver.py`** and add the following code:  

```python
import pyautogui
import time

while True:
    pyautogui.moveRel(1, 0, duration=0.2)  # Move slightly
    pyautogui.moveRel(-1, 0, duration=0.2) # Move back
    time.sleep(60)  # Wait 60 seconds
```
This will **move the mouse every minute** to keep Teams active.

---

### **3️⃣ Create a Mac App to Run It**  
Instead of running the script manually, we’ll **turn it into a Mac app** so you can launch it with one click.

#### **🔹 Open Automator**  
1. Press `Cmd + Space`, type **Automator**, and hit **Enter**.  
2. Click **"New Document"** → Select **"Application"** → Click **Choose**.  

#### **🔹 Add a Shell Script Action**  
1. In the **search bar** (top left), type **"Run Shell Script"**.  
2. Drag **"Run Shell Script"** into the workflow area.  
3. In the script box, select:  
   - **Shell:** `/bin/bash`  
   - **Pass input:** "to stdin"  

4. Paste this inside:
   ```sh
   /usr/bin/python3 /path/to/ToxicManagerSaver.py
   ```
   **Replace `/path/to/ToxicManagerSaver.py`** with the actual path of your script.

#### **🔹 Save It as an App**  
1. Go to **File → Save**.  
2. Name it **"MouseMover.app"**.  
3. Save it in **Applications** for easy access.  

---

## **🎯 How to Use It**  
- **Run the app**: Just double-click **MouseMover.app** to start the script.  
- **Stop it**: Open **Activity Monitor**, find `python3 ToxicManagerSaver.py`, and quit it.  

### **(Optional) Start It Automatically on Login**  
1. **System Settings → Users & Groups → Login Items.**  
2. Click `+`, select **MouseMover.app**, and add it.  
3. Now, it will start **automatically when you log in**.

---

## **⚠️ Disclaimer**  
This is for **educational purposes only.** If your manager **judges productivity by an "active" status,** maybe it's time to look for a better job. 😆  