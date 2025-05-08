import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)


def click(value):
    entry.insert(tk.END, value)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == '=':
            btn = tk.Button(frame, text=char, font=("Arial", 18), bg="lightgreen", command=calculate)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=lambda ch=char: click(ch))
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

tk.Button(root, text="Clear", font=("Arial", 18), bg="red", fg="white", command=clear).pack(fill="both", padx=10, pady=10)
root.mainloop()
