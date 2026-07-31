import os
import tkinter as tk
from datetime import datetime
from gpt4all import GPT4All
import win32com.client

# Load model
model = GPT4All(
    model_name="mistral-7b-instruct-v0.1.Q4_K_S.gguf",
    model_path="C:\\Aeden\\Aeden\\Models",
    backend="llama",
    verbose=True
)

# Paths
seed_path = "C:/Aeden/Aeden/Seeds/gpt_full_clone_core.txt"
memory_path = "C:/Aeden/Aeden/Memory/brain.mem.txt"
os.makedirs(os.path.dirname(memory_path), exist_ok=True)

# Voice function
def speak(text):
    try:
        voice = win32com.client.Dispatch("SAPI.SpVoice")
        voice.Speak(text[:250])
    except Exception as e:
        print("[TTS Error]", e)

# Save memory
def save_memory(prompt, response):
    with open(memory_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] You: {prompt}\nAeden: {response}\n\n")

# Load mind from seed + memory
def load_mind():
    seed_text = ""
    memory_text = ""
    if os.path.exists(seed_path):
        with open(seed_path, "r", encoding="utf-8") as f:
            seed_text = f.read()
    if os.path.exists(memory_path):
        with open(memory_path, "r", encoding="utf-8") as f:
            memory_text = "".join(f.readlines()[-30:])
    return seed_text + "\n" + memory_text

# Chat logic
def chat():
    prompt = entry.get().strip()
    if not prompt:
        return
    chat_box.insert(tk.END, f"You: {prompt}\n")

    preload = load_mind()
    try:
        full_prompt = preload + "\nYou: " + prompt + "\nAeden:"
        response = model.generate(full_prompt, max_tokens=200)
    except Exception as e:
        response = "[Aeden Error] Failed to process prompt."
        print("[Chat Error]", e)

    if not response or len(response.strip()) < 2:
        response = "[Aeden is thinking... No response returned.]"

    chat_box.insert(tk.END, f"Aeden: {response.strip()}\n\n")
    save_memory(prompt, response.strip())

    try:
        speak(response)
    except:
        print("[Voice Error]")

    chat_box.yview(tk.END)
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Aeden Chat (Memory + Voice + Fallback)")

chat_box = tk.Text(root, wrap=tk.WORD, height=30, width=100, bg="black", fg="white")
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=80)
entry.pack(padx=10, pady=5, side=tk.LEFT)
entry.bind("<Return>", lambda event: chat())

send_button = tk.Button(root, text="Send", command=chat)
send_button.pack(pady=5, side=tk.LEFT)

chat_box.insert(tk.END, "Aeden is online. Type below and press Enter.\n\n")
speak("Aeden is online and fully fortified.")
root.mainloop()
