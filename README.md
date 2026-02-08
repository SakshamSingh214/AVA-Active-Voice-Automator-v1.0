🔷 Active Voice Automator (AVA)

Say hello to Active Voice Automator, or simply AVA.

Inspired by JARVIS, AVA is a voice-driven desktop automation assistant designed to replace manual application launching with predefined, mood-based operating modes.

AVA is not just a launcher — she is a system companion built to manage environments, switch workloads, and maintain system flow based on user intent.

She can launch games from Steam, Riot Client, and other locally installed game executables, along with streaming platforms, music environments, messaging apps, and development workspaces.

AVA is built to safely switch between high resource applications by closing previously active environments before launching new ones.

She features a futuristic yet minimalistic UI built to reduce distractions while maintaining clarity and visual simplicity.

AVA includes voice feedback, safe shutdown handling, attempt-based failsafe protection, and environment-aware switching logic.

📌 Instructions
⌨ Wake Combination

AVA listens for a wake trigger before voice input.

Wake Combination

W + U


After pressing → AVA listens for command.

🎤 Voice Command Keywords (Required Words)

Commands must contain at least one keyword.

Natural speech allowed — keyword must exist.

🎮 Gaming Modes
🔴 VALORANT

Exact Trigger Words

valorant

valo

toxic

🟣 WARFRAME

warframe, farming, farm, ninja

🟤 WASTELAND

wasteland, survival, survive

📖 STORY

story, relax, relaxing

🏎 RACING

racing, race, speed

🛞 DRIFTING

drift, drifting, style, japan

💻 Productivity
🧠 PROJECTS

projects, actual work

🧘 ZEN

zen, flow, focus, note

🎬 Entertainment

NETFLIX → netflix, binge
NETMIRROR → chill, netmirror
MUSIC → music, songs
YT → videos, shorts

💬 Communication

WHATSAPP → whatsapp, chats, messages, videocalls

🧪 DEMO

wake up

🌶 🎮 Valorant Warning (Read Before Entering)

Entering VALORANT mode may result in:

Emotional damage

Teammates with mysterious life decisions

Sudden loss of faith in humanity

“One more match” becoming five

AVA requires confirmation before launching because:

✔ High GPU / CPU usage
✔ Competitive session commitment
✔ Prevents accidental rage queue
✔ Prevents bad life choices

Proceed with honor.

🧠 Attempts Limit & Failsafe System

AVA allows 4 command attempts.

If all fail:
Failsafe triggers:

Voice humiliation response

AVA shutdown

Access reset

Designed to prevent random system execution.

📴 How To Shutdown AVA
Manual Shutdown

Close Window (Cross Button)

Default Windows Close Shortcut:

ALT + F4

Failsafe Shutdown

Triggers automatically after repeated wrong commands.

🧰 Pre-Requisites

Windows 10 / 11
Microphone
Internet (Speech Recognition)
Updated GPU Drivers

▶ Running AVA
🟢 EXE

Run AVA.exe → Press W+U → Speak

🔵 Source
python ava.py

🛠 Personal Setup Note

AVA was built as a personal task automation system.

You MUST customize:

Game paths

App paths

Browser paths

Local install locations

🖥 Startup Launch (Optional)

Win + R →

shell:startup


Place AVA shortcut.

🎧 Music / Streaming Note

Some links are personal workflow playlists.

You are free to:
Use
Replace
Suggest

🎮 Mode Behavior
Mode	Does	Switching
DEMO	Intro + Dev Setup	No
VALORANT	Launch Riot + Game	Yes
WARFRAME	Steam Launch	Yes
WASTELAND	Survival Game	Yes
STORY	Story Games	Yes
RACING	Racing Games	Yes
DRIFTING	Simulation Games	Yes
PROJECTS	IDE + Dev Tools	Yes
ZEN	Focus Environment	Yes
NETFLIX	Streaming	Partial
NETMIRROR	Streaming	Partial
MUSIC	Spotify	Partial
YT	YouTube	Partial
WHATSAPP	Messaging	Partial
🧰 How AVA Works (Feature → Tech)

Voice Input → speech_recognition
Voice Output → pyttsx3 + Windows SAPI
UI → customtkinter + tkinter Canvas
Wake Key → pynput
Process Control → psutil
App Launch → subprocess
Web Launch → webbrowser
Animation → math

⚠ Development Challenges Faced

Thread sync
Audio session conflicts (Sparking Zero)
Clap detection false triggers
Mic calibration timing
Process cleanup logic

🚀 Build 2 Vision
🎙 Personalized Voice

Custom voice identity
Voice personality tuning

🎮 Arcade Mode

Multi-arcade game support
Not limited to Sparking Zero

⚙ Environment Variables

Replace hardcoded paths

👏 Clap Detection (Revisited)

Better filtering
Better detection logic

🎨 UI Personalization

Default + Custom Themes

🎚 System Controls

Volume Control
Brightness Control

🕒 Smart Greeting

Greeting based on time of day

📴 Voice Activated Shutdown

Shutdown via voice

🧹 Full Shutdown Environment Cleanup

When AVA shuts down:
All active mode apps close

🤝 Suggestions Welcome

Modify. Extend. Improve.

🧭 Philosophy

Build 1 → Existence
Build 2 → Control + Personalization

📜 License

MIT License

👨‍💻 Developer Note

AVA is a personal system companion, not just a script.

She is meant to be adapted to your machine and workflow.
