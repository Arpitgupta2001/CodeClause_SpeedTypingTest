import tkinter as tk
import random
import time

def start_typing_test():
    text = "The quick brown fox jumps over the lazy dog"
    words = text.split()
    random.shuffle(words)
    display_text.config(text=' '.join(words))
    entry.delete(0, tk.END)
    entry.focus()
    start_button.config(state=tk.DISABLED)
    global start_time
    start_time = time.time()

def finish_typing_test():
    user_text = entry.get()
    entry.delete(0, tk.END)
    entry.config(state=tk.DISABLED)
    elapsed_time = time.time() - start_time
    words = user_text.split()
    num_words = len(words)
    accuracy = calculate_accuracy(words, display_text['text'])
    wpm = calculate_wpm(num_words, elapsed_time)
    result_label.config(text=f"Accuracy: {accuracy}%   WPM: {wpm}")
    start_button.config(state=tk.NORMAL)

def calculate_accuracy(user_words, display_text):
    correct = 0
    total = len(user_words)
    display_words = display_text.split()
    for i in range(total):
        if i < len(display_words) and user_words[i] == display_words[i]:
            correct += 1
    accuracy = (correct / total) * 100
    return round(accuracy, 2)

def calculate_wpm(num_words, elapsed_time):
    minutes = elapsed_time / 60
    wpm = num_words / minutes
    return round(wpm)

# Create the main window
window = tk.Tk()
window.title("Speed Typing Test")

# Create and pack the widgets
display_text = tk.Label(window, text="", font=("Arial", 16), wraplength=400)
display_text.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)
entry.bind('<Return>', lambda e: finish_typing_test())

start_button = tk.Button(window, text="Start", command=start_typing_test)
start_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
