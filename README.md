# Gemini Screen Voice Agent 🖥️🔊

A Python-based **Screen Analysis Agent** that captures your screen using a hotkey, sends the image to **Google Gemini**, and **explains what’s on the screen using text + voice**.

This project is useful for:
- Accessibility (screen narration)
- Learning AI vision
- Automation demos
- AI portfolio projects

---

## ✨ Features

- 📸 Capture screen using a keyboard shortcut  
- 🧠 Analyze screen content using **Gemini Vision**
- 🗣️ Speak the explanation using text-to-speech
- ⌨️ Hotkey-based activation (no continuous capture)
- 🔐 API key via environment variable (safe for GitHub)

---

## 🎮 Hotkeys

| Action | Shortcut |
|------|---------|
| Analyze screen | **Ctrl + Shift + Q** |
| Exit program | **Ctrl + C** |

---

## 🧰 Tech Stack

- Python 3.10+
- Google Gemini API (`google-genai`)
- Pillow (screen capture)
- Keyboard (hotkeys)
- pyttsx3 (text-to-speech)

---
gemini_screen_agent/
│
├── agent.py # Main application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── run_agent.bat # (Optional) Windows launcher
└── .gitignore


---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

bash
git clone https://github.com/your-username/gemini_screen_agent.git
cd gemini_screen_agent

2️⃣ Create a virtual environment
python -m venv .venv


Activate it:

Windows (PowerShell):

.\.venv\Scripts\Activate.ps1


Linux / macOS:

source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set Gemini API Key (IMPORTANT)

Get your API key from:
👉 https://ai.google.dev/

Windows (PowerShell):

$env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"


Linux / macOS:

export GOOGLE_API_KEY="YOUR_API_KEY_HERE"


⚠️ Never hardcode your API key in agent.py

▶️ Run the Agent
python agent.py


You should see:

✅ Gemini Screen Voice Agent READY
👉 Press Ctrl + Shift + Q to analyze screen
👉 Press Ctrl + C to exit

## 📁 Project Structure

<img width="902" height="290" alt="image" src="https://github.com/user-attachments/assets/4f593dd4-afe4-42ae-9129-27f8eeaa9383" />
