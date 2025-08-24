import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        temp = float(entry.get())
        f = from_unit.get()
        t = to_unit.get()
        if f == t:
            result.set(f"{temp:.2f}")
            return
        if f == "Celsius":
            if t == "Fahrenheit":
                res = temp * 9/5 + 32
            else:
                res = temp + 273.15
        elif f == "Fahrenheit":
            if t == "Celsius":
                res = (temp - 32) * 5/9
            else:
                res = (temp - 32) * 5/9 + 273.15
        else:
            if temp < 0:
                messagebox.showerror("Error", "Kelvin cannot be negative!")
                return
            if t == "Celsius":
                res = temp - 273.15
            else:
                res = (temp - 273.15) * 9/5 + 32
        
        result.set(f"{res:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x200")
tk.Label(root, text="Temperature:").pack(pady=5)
entry = tk.Entry(root, width=15)
entry.pack()
from_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
from_unit.current(0)
from_unit.pack(pady=5)
to_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
to_unit.current(1)
to_unit.pack(pady=5)
tk.Button(root, text="Convert", command=convert).pack(pady=10)

result = tk.StringVar(value="--")
tk.Label(root, text="Result:").pack()
tk.Label(root, textvariable=result, font=("Arial", 14, "bold")).pack(pady=5)
root.mainloop()