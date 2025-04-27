import tkinter as tk
import math

# Functions
def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ("sin", "cos", "tan", "sqrt", "log"):
        try:
            if text == "sin":
                result = math.sin(math.radians(float(current)))
            elif text == "cos":
                result = math.cos(math.radians(float(current)))
            elif text == "tan":
                result = math.tan(math.radians(float(current)))
            elif text == "sqrt":
                result = math.sqrt(float(current))
            elif text == "log":
                result = math.log10(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#1e1e1e")
        entry.config(bg="#333333", fg="white", insertbackground="white")
        for button in buttons_list:
            button.config(bg="#333333", fg="white", activebackground="#555555", activeforeground="white")
        toggle_btn.config(text="Light Mode", bg="#333333", fg="white", activebackground="#555555", activeforeground="white")
    else:
        root.config(bg="#f0f0f0")
        entry.config(bg="white", fg="black", insertbackground="black")
        for button in buttons_list:
            button.config(bg="white", fg="black", activebackground="#d1d1d1", activeforeground="black")
        toggle_btn.config(text="Dark Mode", bg="white", fg="black", activebackground="#d1d1d1", activeforeground="black")

# Main Window
root = tk.Tk()
root.title("Scientific Calculator with Theme Toggle")
root.geometry("400x550")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.FLAT, justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

# Toggle theme button
toggle_btn = tk.Button(root, text="Dark Mode", font="Arial 12", command=toggle_theme)
toggle_btn.grid(row=6, column=0, columnspan=5, pady=10)

# Buttons layout
button_texts = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'sqrt',
    'C', '(', ')', '**', 'log'
]

buttons_list = []
row_val = 1
col_val = 0

for text in button_texts:
    button = tk.Button(root, text=text, font="Arial 16", width=5, height=2)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", click)
    buttons_list.append(button)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Theme settings
dark_mode = False
toggle_theme()

# Run the app
root.mainloop()
