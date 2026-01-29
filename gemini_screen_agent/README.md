# Gemini Screen Agent

Advanced AI agent that continuously monitors your screen, detects changes, and speaks descriptions of what's happening.

## Features

✨ **Smart Screen Monitoring**
- Continuous agent loop running every 5 seconds
- Automatic screen change detection using image hashing
- Only calls Gemini API when screen changes (saves quota!)

🎥 **Screen Analysis**
- Real-time screenshot capture
- Sends to Gemini Vision API for understanding
- Gets concise 1-2 sentence descriptions

🔊 **Spoken Feedback**
- Converts descriptions to natural speech
- Plays audio immediately
- No internet required for text-to-speech

📊 **Performance Optimized**
- Minimizes API calls with change detection
- Perceptual hashing for fast comparison
- Error handling and logging throughout

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Gemini API key
Create a `.env` file in this directory:
```
GEMINI_API_KEY=your_api_key_here
```

Or set the environment variable directly:
```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# Windows (CMD)
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

```bash
python agent.py
```

The agent will:
1. Start monitoring your screen every 5 seconds
2. Detect when screen content changes
3. Send changes to Gemini Vision API
4. Speak descriptions of what changed
5. Continue monitoring (press Ctrl+C to stop)

### Example Output
```
[INFO] ✓ Screen Agent initialized
[INFO] ▶️ Starting agent loop (checking every 5s)
[INFO] 🔍 First capture - storing baseline
[INFO] 🎬 Screen changed detected (diff: 23)
[INFO] 🤖 Calling Gemini Vision API...
[INFO] 📝 You've opened VS Code with a Python file displayed. The editor shows line numbers and syntax highlighting.

[INFO] 🔊 Converting to speech...
[INFO] ✓ Speech completed
[INFO] ⏸️ No change (diff: 2)
```

## Requirements
- Python 3.8+
- Windows/Mac/Linux
- Gemini API key (get from https://ai.google.dev)
