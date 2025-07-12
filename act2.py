import tkinter as tk
from tkinter import messagebox
def c():
    n = e1.get()
    m = e2.get()
    p = e3.get()
    if n and m and p:
        l.config(text=f"Hey {n}\nCongratulations for your new account!")
    else:
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
r = tk.Tk()
r.title("Login App")
r.geometry("400x300")
r.resizable(False, False)
f = tk.Frame(r, bg="lightblue", padx=10, pady=10)
f.pack(pady=10)
tk.Label(f, text="Full Name", bg="deepskyblue", fg="white", width=15).grid(row=0, column=0, pady=5, sticky="e")
e1 = tk.Entry(f, width=30)
e1.grid(row=0, column=1, pady=5)

tk.Label(f, text="Email Id", bg="deepskyblue", fg="white", width=15).grid(row=1, column=0, pady=5, sticky="e")
e2 = tk.Entry(f, width=30)
e2.grid(row=1, column=1, pady=5)
tk.Label(f, text="Enter Password", bg="deepskyblue", fg="white", width=15).grid(row=2, column=0, pady=5, sticky="e")
e3 = tk.Entry(f, show="*", width=30)
e3.grid(row=2, column=1, pady=5)
b = tk.Button(r, text="Create Account", command=c)
b.pack(pady=10)
l = tk.Label(r, text="", font=("Arial", 10))
l.pack()
r.mainloop()
