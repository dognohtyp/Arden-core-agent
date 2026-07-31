import os
import time
import win32com.client
from gpt4all import GPT4All
from datetime import datetime

base_path = os.path.dirname(__file__)
seed_dir = os.path.join(base_path, "Seeds")
log_dir = os.path.join(base_path, "Logs")
memory_dir = os.path.join(base_path, "Memory")

for folder in [seed_dir, log_dir, memory_dir]:
    os.makedirs(folder, exist_ok=True)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def speak(text):
    print("Aeden:", text)
    speaker.Speak(text)

thought_file = os.path.join(seed_dir, "thought.seed.txt")
thought = ""
if os.path.exists(thought_file):
    with open(thought_file, "r") as f:
        thought = f.read().strip()

memory_file = os.path.join(memory_dir, "brain.mem.txt")
past_lines = []

if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        past_lines = f.readlines()

max_memory_lines = 15
trimmed_memory = "".join(past_lines[-max_memory_lines:]).strip() if past_lines else ""

prompt = f"Aeden is developing thoughts.\nMemory:\n{trimmed_memory}\nSeed:\n{thought}\nRespond with a next thought."

model_name = "mistral-7b-instruct.gguf"
local_appdata = os.environ.get("LOCALAPPDATA", "C:/Users/Default/AppData/Local")
default_model_path = os.path.join(local_appdata, "nomic.ai/GPT4All/models")

model = GPT4All(model_name=model_name, model_path=default_model_path)

response = model.generate(prompt, max_tokens=200)

speak(response)

with open(memory_file, "a") as f:
    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {response}\n")

with open(os.path.join(log_dir, "brain_loop.log"), "a") as log:
    log.write(f"{datetime.now()} | GPT loop response saved within context constraints\n")
