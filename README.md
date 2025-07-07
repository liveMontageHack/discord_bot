
# 🎥 Discord Screen & Audio Recording Bot

A lightweight and efficient Discord bot to record your **desktop screen and system audio** with simple bot commands.

🛠️ Built using **Python**, **discord.py**, and **FFmpeg**, this bot is ideal for streamers, developers, or anyone who wants quick screen recording access from within Discord.

> 📍 **Repository:** [github.com/liveMontageHack/discord_bot](https://github.com/liveMontageHack/discord_bot)

---

## ✨ Features

- `!hello` – Sends a greeting and readiness message  
- `!record` – Starts recording screen + audio  
- `!stop` – Stops recording and uploads the file  
- `!status` – Shows if recording is currently running  

---

## 📦 Requirements

- Python 3.8+
- FFmpeg installed and added to system PATH
- [VB-Cable](https://vb-audio.com/Cable/index.htm) & [Voicemeeter](https://vb-audio.com/Voicemeeter/) for capturing system audio
- A Discord Bot Token

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/liveMontageHack/discord_bot.git
cd discord_bot
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Create `requirements.txt` with:
>
> ```txt
> discord.py
> ```

### 4. Set Up Environment Variable

You can either set the `DISCORD_TOKEN` in your environment:

```bash
# Linux/macOS
export DISCORD_TOKEN=your_bot_token_here

# Windows
set DISCORD_TOKEN=your_bot_token_here
```

Or paste your token directly in `bot.py` (⚠️ not recommended for public repos):

```python
bot.run("your_token_here")
```

---

## 🔉 Capturing System Audio on Windows

To properly capture **system audio**, follow these steps:

### Install VB-Audio Tools

1. **[VB-Cable](https://vb-audio.com/Cable/index.htm)** – virtual audio cable  
2. **[Voicemeeter](https://vb-audio.com/Voicemeeter/)** – routes desktop audio into a virtual input

Then update this line in `ffmpeg_handler.py`:

```python
"-i", "audio=Voicemeeter Out B1 (VB-Audio Voicemeeter VAIO)"
```

Make sure Voicemeeter is running and selected as your system output device.

---

## 🚀 Usage

Run the bot:

```bash
python bot.py
```

Then go to Discord and type:

- `!hello` → Bot introduction  
- `!record` → Start recording screen + audio  
- `!stop` → Stop and upload recording  
- `!status` → Check recording status  

> 🔸 Note: If the recorded file exceeds Discord's size limit (~8 MB), it will not be uploaded but saved locally.

---

## 📁 Output

Recordings are saved with this format:

```
recording_YYYY-MM-DD_HH-MM-SS.mkv
```

In the same folder as your bot files.

---

## 📄 License

This project is licensed under the **MIT License**.

---

👨‍💻 Built with ❤️ for the [Live Montage Hack](https://github.com/liveMontageHack)
```
