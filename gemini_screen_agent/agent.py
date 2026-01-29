import os
import keyboard
import pyttsx3
from PIL import ImageGrab
from io import BytesIO

from google import genai
from google.genai import types


# =========================
# CONFIG
# =========================
HOTKEY = "ctrl+shift+q"
MODEL_NAME = "gemini-2.0-flash"
VOICE_RATE = 170


# =========================
# VERIFY API KEY
# =========================
if not os.environ.get("GEMINI_API_KEY"):
    raise RuntimeError("❌ GEMINI_API_KEY is NOT set in environment")

client = genai.Client()   # <-- IMPORTANT: NO api_key passed here


# =========================
# TEXT TO SPEECH
# =========================
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# =========================
# SCREEN CAPTURE
# =========================
def capture_screen():
    img = ImageGrab.grab()
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


# =========================
# ANALYZE SCREEN
# =========================
def analyze_screen():
    print("\n⚡ Hotkey pressed")
    print("📸 Capturing screen...")

    image_bytes = capture_screen()

    print("🧠 Sending image to Gemini...")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                "Explain what is visible on this screen in clear, simple language. "
                                "Focus on the main application or window. "
                                "Do not read random text. "
                                "If unsure, say 'I may be mistaken'."
                            )
                        },
                        {
                            "inline_data": {
                                "mime_type": "image/png",
                                "data": image_bytes
                            }
                        }
                    ]
                }
            ]
        )

        text = response.text.strip()

        print("\n🗣️ Explanation:")
        print(text)
        print()

        speak(text)

    except Exception as e:
        print(f"\n❌ Gemini Error: {e}\n")


# =========================
# MAIN
# =========================
def main():
    print("\n✅ Gemini Screen Voice Agent READY")
    print("👉 Press Ctrl + Shift + Q to analyze screen")
    print("👉 Press Ctrl + C to exit\n")

    keyboard.add_hotkey(HOTKEY, analyze_screen)

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")


if __name__ == "__main__":
    main()
