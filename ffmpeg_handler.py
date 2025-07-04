# ffmpeg_handler.py
from datetime import datetime
import time
import subprocess
import os

ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
output_file = f"recording_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mkv"
recording_process = None

def start_recording():
    global recording_process

    if recording_process:
        return False, "⚠️ Recording is already in progress."

    command = [
    ffmpeg_path,
    "-y",
    "-f", "gdigrab",
    "-framerate", "30",
    "-i", "desktop",
    "-f", "dshow",
    "-i", "audio=Voicemeeter Out B1 (VB-Audio Voicemeeter VAIO)",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-preset", "ultrafast",
    "-c:a", "aac",
    "-b:a", "192k",
    output_file
    ]



    try:
        recording_process = subprocess.Popen(command)
        return True, f"🔴 Recording started with system audio... Saving to `{output_file}`"
    except Exception as e:
        return False, f"❌ Failed to start recording: {e}"



def stop_recording():
    global recording_process

    if not recording_process:
        return False, "⚠️ No recording is currently running."

    try:
        recording_process.terminate()
        time.sleep(1.5)  # Allow FFmpeg to flush buffers
        recording_process.communicate()
        recording_process = None
    except Exception as e:
        return False, f"❌ Error stopping recording: {e}"

    if os.path.exists(output_file) and os.path.getsize(output_file) > 100000:
        return True, output_file
    else:
        return False, "❌ Recording file is corrupted or too small to play."
    
def is_recording():
    return recording_process is not None
