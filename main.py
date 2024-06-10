import tkinter as tk
from tkinter import messagebox
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

# Load translations from JSON file
def load_translations():
    try:
        with open('translations.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save translations to JSON file
def save_translations(translations):
    with open('translations.json', 'w') as file:
        json.dump(translations, file, indent=4)

# Translate text
def translate_text(origin, target, text):
    if not origin:
        origin = "English"  # Assume English if origin is not entered
    completion = send_prompt(origin, target, text)
    return completion

# Send prompt to OpenAI API
def send_prompt(origin, target, prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language translator named Tongs. You will receive the origin language, target language, and prompt to be translated. You will reply only with the translation of the prompt."},
            {"role": "user", "content": f"{origin} to {target}: {prompt}"}
        ]
    )
    return completion.choices[0].message.content

# Show translation history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Translation History")
    history_text = tk.Text(history_window, height=20, width=50)
    history_text.pack()

    for translation in translations:
        history_text.insert(tk.END, f"Origin: {translation['origin']}\n")
        history_text.insert(tk.END, f"Target: {translation['target']}\n")
        history_text.insert(tk.END, f"Text: {translation['text']}\n")
        history_text.insert(tk.END, f"Translation: {translation['translation']}\n\n")

# Translate button click event
def translate():
    origin = origin_entry.get()
    target = target_entry.get()
    text = text_entry.get("1.0", "end-1c")

    if not target or not text:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    translation = translate_text(origin, target, text)
    translation_label.config(text=translation)

    # Save translation to JSON file
    translations.append({
        'origin': origin,
        'target': target,
        'text': text,
        'translation': translation
    })
    save_translations(translations)

# Main window
root = tk.Tk()
root.title("Language Translator")

# Load translations
translations = load_translations()

# Origin language entry
tk.Label(root, text="Origin Language:").pack()
origin_entry = tk.Entry(root)
origin_entry.pack()

# Target language entry
tk.Label(root, text="Target Language:").pack()
target_entry = tk.Entry(root)
target_entry.pack()

# Text entry
tk.Label(root, text="Text to Translate:").pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

# Translation label
translation_label = tk.Label(root, text="")
translation_label.pack()

# History button
history_button = tk.Button(root, text="Show History", command=show_history)
history_button.pack()

root.mainloop()
