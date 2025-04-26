import tkinter as tk

# Function to interpolate between two colors
def interpolate_color(c1, c2, factor):
    return tuple(int(a + (b - a) * factor) for a, b in zip(c1, c2))

# Function to convert RGB tuple to hex
def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# Smooth background animation
def smooth_background(step=0):
    global current_color, target_color, fade_steps

    if step >= fade_steps:
        # Choose a new target color
        current_color = target_color
        target_color = random_color()
        step = 0

    factor = step / fade_steps
    new_color = interpolate_color(current_color, target_color, factor)
    hex_color = rgb_to_hex(new_color)

    root.configure(bg=hex_color)
    label.configure(bg=hex_color)
    button.configure(bg=hex_color)

    root.after(50, smooth_background, step + 1)  # 50ms per step

# Random color generator
def random_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# Animate Hello World text
def animate_text(index=0):
    text = "Hello, World!"
    if index <= len(text):
        label.config(text=text[:index])
        root.after(100, animate_text, index + 1)
    else:
        label.config(fg="white")

# On button click
def on_click():
    label.config(text="", fg="white")
    animate_text()

# Setup
import random
root = tk.Tk()
root.title("Super Smooth Hello World")

root.geometry("500x300")

label = tk.Label(root, text="", font=("Arial", 26), bg="white", fg="white")
label.pack(pady=40)

button = tk.Button(root, text="Click Me for Magic!", command=on_click, font=("Arial", 16), bg="white")
button.pack(pady=10)

# Initial colors
current_color = random_color()
target_color = random_color()
fade_steps = 50

# Start the smooth background animation
smooth_background()

# Run
root.mainloop()
