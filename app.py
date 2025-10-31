import tkinter as tk
from tkinter import messagebox

def convert():
    c = from_currency.get()
    cc = to_currency.get()
    try:
        amt = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    if c == cc:
        result.set("Invalid: Same currency.")
    elif c == "USD" and cc == "INR":
        result.set(f"{amt * 88:.2f} INR")
    elif c == "USD" and cc == "EUR":
        result.set(f"{amt * 0.94:.2f} EUR")
    elif c == "INR" and cc == "USD":
        result.set(f"{amt / 88:.2f} USD")
    elif c == "INR" and cc == "EUR":
        result.set(f"{amt / 93:.2f} EUR")
    elif c == "EUR" and cc == "USD":
        result.set(f"{amt / 0.94:.2f} USD")
    elif c == "EUR" and cc == "INR":
        result.set(f"{amt * 104.76:.2f} INR")
    else:
        result.set("Invalid combination.")
    
    animate_result()

def animate_result():
    colors = ["#e74c3c", "#f39c12", "#2ecc71", "#3498db", "#9b59b6"]
    def pulse(i=0):
        result_label.config(fg=colors[i])
        root.after(300, pulse, (i+1) % len(colors))
    pulse()

def on_enter(e):
    convert_btn.config(bg="#1abc9c", fg="white")

def on_leave(e):
    convert_btn.config(bg="#16a085", fg="white")

def animate_title():
    shades = ["#f1c40f", "#e67e22", "#e74c3c", "#9b59b6", "#2ecc71"]
    def cycle(i=0):
        title_label.config(fg=shades[i])
        root.after(400, cycle, (i+1) % len(shades))
    cycle()

# Main window
root = tk.Tk()
root.title("💱 Currency Converter")
root.geometry("450x500")
root.configure(bg="#2c3e50")

# Title
title_label = tk.Label(root, text="Currency Converter", font=("Verdana", 20, "bold"), bg="#2c3e50")
title_label.pack(pady=20)
animate_title()

# Amount Entry
tk.Label(root, text="Amount:", font=("Verdana", 12), bg="#2c3e50", fg="white").pack()
amount_entry = tk.Entry(root, font=("Verdana", 12), justify="center", width=20, bd=3, relief="groove")
amount_entry.pack(pady=10)

# Currency Options
currencies = ["USD", "EUR", "INR"]

tk.Label(root, text="From:", font=("Verdana", 12), bg="#2c3e50", fg="white").pack()
from_currency = tk.StringVar(value="USD")
tk.OptionMenu(root, from_currency, *currencies).pack(pady=5)

tk.Label(root, text="To:", font=("Verdana", 12), bg="#2c3e50", fg="white").pack()
to_currency = tk.StringVar(value="INR")
tk.OptionMenu(root, to_currency, *currencies).pack(pady=5)

# Convert Button with hover effect
convert_btn = tk.Button(root, text="Convert", command=convert, font=("Verdana", 12, "bold"),
                        bg="#16a085", fg="white", padx=10, pady=5, relief="raised", bd=3)
convert_btn.pack(pady=20)
convert_btn.bind("<Enter>", on_enter)
convert_btn.bind("<Leave>", on_leave)

# Result Display with animation
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Verdana", 18, "bold"), bg="#2c3e50")
result_label.pack(pady=30)

# Bind Enter key to trigger conversion
root.bind('<Return>', lambda event: convert())

root.mainloop()