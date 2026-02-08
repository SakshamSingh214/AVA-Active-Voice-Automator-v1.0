import threading
import time
import math
import subprocess
import webbrowser
import customtkinter as ctk
from tkinter import Canvas
from pynput import keyboard
import speech_recognition as sr
import pyttsx3
import random
import psutil
App=None
Running=True
logic_worker=None
MODE_PROCESS_MAP = {
    "VALORANT": ["VALORANT.exe", "RiotClientServices.exe"],
    "WARFRAME": ["Warframe.x64.exe", "steam.exe"],
    "WASTELAND": ["AVAMain.exe"],
    "STORY": ["ROTTR.exe"],
    "RACING": ["NFS13.exe"],
    "DRIFTING":["JDM.exe","Game-Win64-Shipping.exe","UE4-Win64-Shipping.exe"],
    "PROJECTS": ["Code.exe"],
    "WHATSAPP":["WhatsApp.exe"]
}
voice_engine=pyttsx3.init()
voice_engine.setProperty('rate', 145)      # Speed of speech (words per minute)
voice_engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)
voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[1].id)
webbrowser.register('brave',None,webbrowser.BackgroundBrowser(r"C:\Users\91882\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"))
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
#Ava Main Speech
def speak(text):
    if not Running:
        return
    voice_engine.say(text)
    voice_engine.runAndWait()
# ===================== SYSTEM STATE =====================
class AvaState:
    def __init__(self):
        self.system_status = "IDLE"      # IDLE | LISTENING | EXECUTING | ERROR
        self.current_mode = "NONE"
        self.message = "Waiting for input..."
        self.lock = threading.Lock()

    def update(self, status=None, mode=None, message=None):
        with self.lock:
            if status is not None:
                self.system_status = status
            if mode is not None:
                self.current_mode = mode
            if message is not None:
                self.message = message


STATE = AvaState()

# ===================== VOICE =====================

failure = pyttsx3.init('sapi5')
failure.setProperty("rate", 125)
failure.setProperty("volume", 1.0)
voices = failure.getProperty("voices")
failure.setProperty("voice", voices[1].id)
def release_audio():
    global voice_engine, recognizer
    try:
        voice_engine.stop()
    except:
        pass
    try:
        recognizer.pause_threshold = 999  # effectively disables listening
    except:
        pass
def humiliate(text):
    failure.say(text)
    failure.runAndWait()

# ===================== RECOGNITION =====================

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
def listen_for_command():
    STATE.update(status="LISTENING", message="Listening for command…")
    with sr.Microphone() as source:
        try:
            voice = recognizer.listen(source, timeout=30, phrase_time_limit=10)
            text = recognizer.recognize_google(voice).lower()
            return text
        except:
            return ""

# ===================== MODE IDENTIFICATION =====================

def identify_modes(command):
    modes = []
    if "wake" in command and "up" in command:
        modes.append("DEMO")
    if "toxic" in command or "valorant" in command or "valo" in command:
        modes.append("VALORANT")
    if "binge" in command or "netflix" in command:
        modes.append("NETFLIX")
    if "chill" in command or "netmirror" in command:
        modes.append("NETMIRROR")
    if "college" in command or "boring" in command:
        modes.append("COLLEGE")
    if "wasteland" in command or "survive" in command or "survival" in command:
        modes.append("WASTELAND")
    if "story" in command or "relaxing" in command or "relax" in command:
        modes.append("STORY")
    if "projects" in command or "actual work" in command:
        modes.append("PROJECTS")
    if "farm" in command or "farming" in command or "ninja" in command:
        modes.append("WARFRAME")
    if "race" in command or "racing" in command or "speed" in command:
        modes.append("RACING")
    if "drift" in command or "drifting" in command or "style" in command or "japan" in command:
        modes.append("DRIFTING")
    if "music" in command or "songs" in command:
        modes.append("MUSIC")
    if "videos" in command or "shorts" in command:
        modes.append("YT")
    if "chats" in command or "whatsapp" in command or "messages" in command or "videocalls" in command:
        modes.append("WHATSAPP")
    if "zen" in command or "flow" in command or "focus" in command or "note" in command:
        modes.append("ZEN")
    return modes

# ===================== MODE EXECUTION =====================

def execute_mode(modes):
    if len(modes) != 1:
        STATE.update(
            status="ERROR",
            message="Mode collision or no valid mode"
        )
        speak("Mode collision detected")
        return False

    mode = modes[0]
    STATE.update(
        status="EXECUTING",
        mode=mode,
        message=f"{mode} mode active"
    )

    # ---------------- DEMO ----------------
    if mode == "DEMO":
        speak("Welcome back Sir")
        time.sleep(1.5) 
        webbrowser.get('brave').open("https://open.spotify.com/track/57bgtoPSgt236HzfBOd8kj") 
        time.sleep(39) 
        subprocess.Popen(r"D:\Microsoft VS Code\Code.exe")

    # ---------------- VALORANT ----------------
    elif mode == "VALORANT":
        if(is_running("VALORANT")):
            speak("Valorant is already running Sir. Aborting launch.")
            return False
        speak("Attention Sir. This mode will toast and roast your mental peace. Do you really want to proceed?")
        decision=listen_for_choice(mode)
        if(decision is True):
            speak("Affirmative. Toxic Mode. Opening Valorant. Good luck Sir, you would need that")
            subprocess.Popen(
            ["cmd", "/c", "start", "",
             r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk"],
            shell=True
        )
            return True
        elif(decision is False):
            speak("Affirmative Sir Toxic Mode Offline. Good Decision")
            STATE.update(status="IDLE", message="Toxic mode cancelled")
            return False
        else:
            speak("No clear confirmation received.")
            return False
    # ---------------- NETFLIX ----------------
    elif mode == "NETFLIX":
        speak("Affirmative. Netflix Mode. Opening Netflix.")
        subprocess.Popen([
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            "https://www.netflix.com/browse"
        ])

    # ---------------- NETMIRROR ----------------
    elif mode == "NETMIRROR":
        subprocess.Popen([
        r"C:\Users\91882\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe",
        "--new-window",
        "https://netmirror.gg/2/en"
    ])
    # ---------------- COLLEGE ----------------
    elif mode == "COLLEGE":
        speak("Affirmative. College Mode Online. Initializing.")
        subprocess.Popen([
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "--profile-directory=Default",
            "--new-window",
            "https://leetcode.com",
            "https://www.onlinegdb.com"
        ])

    # ---------------- WASTELAND ----------------
    elif mode == "WASTELAND":
        if(is_running("WASTELAND")):
            speak("Wasteland Mode is already running Sir. Aborting launch.")
            return False
        speak("Affirmative. Wasteland Mode Online.")
        subprocess.Popen(
        [r"D:\Games\Mad Max\AVAMain.exe"],
        cwd=r"D:\Games\Mad Max",
        shell=False
    )

    # ---------------- STORY ----------------
    elif mode == "STORY":
        if(is_running("ROTTR")):
            speak("Story Mode is already running Sir. Aborting launch.")
            return False
        speak("Affirmative. Story Mode Online. Launching.")
        subprocess.Popen(
             ["cmd", "/c", "start", "",
             r"C:\Users\91882\Desktop\Games\Rise of the Tomb Raider.lnk"],
            shell=True
        )

    # ---------------- PROJECTS ----------------
    elif mode == "PROJECTS":
        speak("Affirmative. Projects Mode Online. Initializing work environment.")
        webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1E8PxNPCVYuc4e")
        webbrowser.open("https://chatgpt.com/")
        time.sleep(10)
        subprocess.Popen(
            r"D:\Microsoft VS Code\Code.exe"
        )

    # ---------------- WARFRAME ----------------
    elif mode == "WARFRAME":
        if(is_running("WARFRAME")):
            speak("Warframe Mode is already running Sir. Aborting launch.")
            return False
        speak("Affirmative. Farming Mode. Opening Warframe.")
        subprocess.Popen(
    ["cmd", "/c", "start", "", "steam://rungameid/230410"],
    shell=True
)   

    # ---------------- RACING ----------------
    elif mode == "RACING":
        if(is_running("RACING")):
            speak("Racing Mode is already running Sir. Aborting launch.")
            return False
        speak("Affirmative. Racing Mode Online. Drive Safe and Fast Sir")
        subprocess.Popen(
            ["cmd", "/c", "start", "",
             r"C:\Users\91882\Desktop\Games\Need for Speed - Most Wanted.lnk"],
        shell=True
        )
     # ---------------- DRIFTING ----------------
    elif mode=="DRIFTING":
        if(is_running("DRIFTING")):
            speak("Drifting Mode is already running Sir. Aborting launch.")
            return False
        speak("Affirmative. Drifting Mode Online. Drive with style and vibes Sir")
        subprocess.Popen(
            ["cmd", "/c", "start", "",
             r"C:\Users\91882\Desktop\Games\JDM.exe - Shortcut.lnk"],
            shell=True
        )
    # ---------------- MUSIC ----------------
    elif mode == "MUSIC":
        speak("Affirmative. Music Mode. Opening Spotify.")
        webbrowser.open("https://open.spotify.com")

    # ---------------- YOUTUBE ----------------
    elif mode == "YT":
        speak("Affirmative. YT mode. Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif mode=="WHATSAPP":
        speak("Affirmative. Messaging Mode. Opening WhatsApp")
        subprocess.Popen("explorer.exe shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        STATE.update(mode="WHATSAPP",message="WHATSAPP")
        # ---------------- ZEN ----------------
    elif mode=="ZEN":
        speak("Affirmative. Zen Mode. Initializing Flow State")
        webbrowser.open("https://youtube.com/playlist?list=PLpBBJSUzF6aiyfMq-8rGxyHY064CEGyAK&si=ztvMTau1NrAbHoyT")
        webbrowser.open("https://www.onlinegdb.com/")
        webbrowser.open("https://chatgpt.com/c/6985895f-f2b4-8322-b988-cfdb316ef26e")
    else:
        speak("No Valid Mode Identified")
        STATE.update(status="ERROR", message="Unknown mode")
        return False
    STATE.update(
        status="IDLE",
        message=f"{mode} mode launched"
    )
    return True


# ===================== MAIN LOGIC THREAD =====================

def logic_thread():
    global Running
    while Running:
        if not App or not App.winfo_exists():
            break
        speak("Enter the combination")
        combo = {keyboard.KeyCode(char="w"), keyboard.KeyCode(char="u")}
        pressed = set()
        combo_detected = threading.Event()
        def on_press(key):
            if not Running:
                return False
            pressed.add(key)
            if combo.issubset(pressed):
                combo_detected.set()
                return False  # stop listener
        def on_release(key):
            pressed.discard(key)
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        listener.start()
        while Running and not combo_detected.is_set():
            time.sleep(0.05)
        try:
            listener.stop()  # safe stop
        except:
            pass
        if not Running:
            break
    # ---- ONLY REACHES HERE AFTER REAL COMBO ----
        speak("Combination verified")
        attempts=0
        while attempts<4:
            speak("Speak the command")
            command = listen_for_command()
            modes = identify_modes(command)
            if not modes:
                attempts+=1
                speak("No valid mode identified")
                continue
            success=mode_switch(modes[0])
            break
        else:
            if not Running:
                break
            STATE.update(status="ERROR",message="Access Denied")
            humiliate("Four strikes.")
            time.sleep(0.25)
            humiliate("This is not a one tap system.")
            time.sleep(0.25)
            humiliate("You lack precision.")
            time.sleep(0.4)
            humiliate("Now run.")
            shutdown(silent=True)
#Shutdown
def shutdown(silent=False):
    global Running
    if not Running:
        return
    Running=False
    if not silent:
        try:
            voice_engine.say("Ava is shutting down. Good Day Sir.")
            voice_engine.runAndWait()
        except:
            pass
    if App and App.winfo_exists():
        App.after(100,App.destroy)
#UI
BG = "#01080f"
CYAN = "#4cc9f0"
CYAN_LOW = "#0a2a3a"
TEXT = "#e1eef6"
class AvaJarvisFinal(ctk.CTk):
    def __init__(self):
        super().__init__()
        global App
        App=self
        self.protocol("WM_DELETE_WINDOW",shutdown)
        # Window Setup
        self.title("AVA")
        self.geometry("1200x800")
        self.configure(fg_color=BG)

        self.angle_outer = 0
        self.angle_inner = 0
        self.pulse = 0
        self.is_maximized = False
        
        self.canvas = Canvas(self, bg=BG, highlightthickness=0, bd=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.build_ui()
        self.animate_hologram()
        
        # FIX: Only call the one that actually has the code in it
        self.update_ui_from_logic()
        self.after(200,self.lift)
        self.after(250,lambda:
        self.attributes("-topmost",True))
        self.after(400,lambda:
        self.attributes("-topmost",False))
    def build_ui(self):
        self.identity = ctk.CTkLabel(self, text="AVA", font=("Orbitron", 48, "bold"), text_color=TEXT)
        self.identity.place(relx=0.5, rely=0.5, anchor="center")

        self.meta = ctk.CTkLabel(self, text="// SYSTEM STANDBY //", font=("JetBrains Mono", 12), text_color=CYAN)
        self.meta.place(relx=0.5, rely=0.70, anchor="center")

    def minimize_window(self):
        # FIX: More reliable minimize for borderless windows
        self.update_idletasks()
        self.state('iconic')

    def toggle_maximize(self):
        if not self.is_maximized:
            self.state("zoomed")
            self.max_btn.configure(text="❐")
            self.is_maximized = True
        else:
            self.state("normal")
            self.max_btn.configure(text="▢")
            self.is_maximized = False

    def draw_hologram(self):
        self.canvas.delete("holo")
        cx, cy = self.winfo_width() // 2, self.winfo_height() // 2
        self.angle_outer += 0.5
        self.angle_inner -= 0.8
        self.pulse += 0.05
        
        pulse_r = 250 + math.sin(self.pulse) * 15
        self.canvas.create_oval(cx-pulse_r, cy-pulse_r, cx+pulse_r, cy+pulse_r, 
                                outline=CYAN_LOW, width=1, tags="holo")

        self.draw_segmented_ring(cx, cy, 210, self.angle_outer, 4, 30)
        self.draw_segmented_ring(cx, cy, 185, self.angle_inner, 2, 60)

        for i in range(8):
            a = (self.pulse * 0.2) + (i * (math.pi * 2 / 8))
            dist = 280 + math.sin(self.pulse + i) * 10
            nx, ny = cx + math.cos(a) * dist, cy + math.sin(a) * dist
            self.canvas.create_rectangle(nx, ny, nx+3, ny+3, fill=CYAN, outline="", tags="holo")

    def draw_segmented_ring(self, cx, cy, r, angle, width, extent):
        for i in range(3):
            start = angle + (i * 120)
            self.canvas.create_arc(cx-r, cy-r, cx+r, cy+r, outline=CYAN, 
                                   width=width, style="arc", extent=extent, 
                                   start=start, tags="holo")

    def animate_hologram(self):
        self.draw_hologram()
        self.after(20, self.animate_hologram)

    def update_ui_from_logic(self):
        with STATE.lock:
            mode_text = STATE.current_mode if STATE.current_mode != "NONE" else "AVA"
            self.identity.configure(text=mode_text)
            self.meta.configure(text=f"// {STATE.message.upper()} //")
        self.after(200, self.update_ui_from_logic)
#Specially for Valorant
def listen_for_choice(mode):
        STATE.update(status="LISTENING", message="Listening for command…")
        yes_words = {
    "yes", "yeah", "yep", "sure", "why not", "go ahead", "do it", "hell yeah"
        }
        no_words = {
        "no", "nope", "nah", "no way", "nein", "cancel", "stop","nopes"
        }
        with sr.Microphone() as source:
            try:
                voice = recognizer.listen(source, timeout=30,phrase_time_limit=10)
                choice = recognizer.recognize_google(voice).lower()
                for word in yes_words:
                    if word in choice:
                        return True
                for word in no_words:
                    if word in choice:
                        return False
                return None  # unclear response
            except:
                return None
#For checking if Game Modes or Projects Mode aren't already running
def is_running(mode):
    processes = MODE_PROCESS_MAP.get(mode, [])
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in processes:
            return True
    return False
#Exit for Game Modes and Projects Mode
def exit_mode(mode):
    processes=MODE_PROCESS_MAP.get(mode,[])
    if not processes:
        return
    speak(f"Exiting {mode} mode")
    STATE.update(message=f"Closing {mode} mode")
    for process in psutil.process_iter(['name','pid']):
        try:
            if(process.info['name'] in processes):
                parent=psutil.Process(process.info['pid'])
                for child in parent.children(recursive=True):
                    try:
                        child.kill()
                    except:
                        pass
                try:
                    parent.kill()
                except:
                    pass
        except(psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    time.sleep(1)
#Switches Game Modes or switches to Game Modes from Projects Mode and vice-versa
def mode_switch(new_mode):
    with STATE.lock:
        current_mode=STATE.current_mode
        if(new_mode==current_mode):
            speak(f"{new_mode} mode is already active")
            return False
    if(current_mode!="NONE"):
        exit_mode(current_mode)
    speak(f"Switching to {new_mode}")
    STATE.update(
        status="EXECUTING",
        mode=new_mode,
        message=f"Switching to {new_mode}"
    )
    return execute_mode([new_mode]) 
#Main Function
if __name__ == "__main__":
    app = AvaJarvisFinal()
    logic_worker = threading.Thread(target=logic_thread)
    logic_worker.start()
    app.mainloop()