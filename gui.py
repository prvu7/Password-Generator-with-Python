import tkinter as tk
from tkinter import ttk
from main import gen_random_password  

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")

def update_password():
    length = int(spinbox_length.get()) 
    
    use_digits = var_numbers.get()      
    use_uppercase = var_uppercase.get() 
    use_lowercase = var_lowercase.get() 
    use_special = var_special.get()     

    try:
        generated_password = gen_random_password(length, use_digits, use_uppercase, use_lowercase, use_special)
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generated_password)
        password_entry.config(state="readonly")
    except ValueError as e:
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, f"Error: {e}")
        password_entry.config(state="readonly")

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()


label_customize = tk.Label(root, text="Customize your password", font=("Arial", 18), anchor="w")
separator_top = ttk.Separator(root, orient="horizontal")

label_length = tk.Label(root, text="Password Length:", font=("Arial", 14), anchor="w")
spinbox_length = tk.Spinbox(root, from_=1, to=20, width=5, font=("Arial", 14))

frame_options = tk.Frame(root)
var_numbers = tk.IntVar()
var_uppercase = tk.IntVar()
var_lowercase = tk.IntVar()
var_special = tk.IntVar()

checkButton_numbers = tk.Checkbutton(frame_options, text="Include Numbers", font=("Arial", 12), variable=var_numbers)
checkButton_upper = tk.Checkbutton(frame_options, text="Include Uppercase Letters", font=("Arial", 12), variable=var_uppercase)
checkButton_lower = tk.Checkbutton(frame_options, text="Include Lowercase Letters", font=("Arial", 12), variable=var_lowercase)
checkButton_special = tk.Checkbutton(frame_options, text="Include Special Characters", font=("Arial", 12), variable=var_special)

separator_bottom = ttk.Separator(root, orient="horizontal")

password_entry = tk.Entry(root, font=("Arial", 14), width=30, state="readonly")
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

btn_generate = tk.Button(root, text="Generate", font=("Arial", 14), bg="#4CAF50", fg="white", command=update_password)
btn_copy = tk.Button(root, text="Copy Password", font=("Arial", 14), bg="#2196F3", fg="white", command=copy_password)

# Positioning
label_customize.grid(row=0, column=0, padx=10, pady=10, sticky="w")
separator_top.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

label_length.grid(row=2, column=0, padx=10, pady=10, sticky="w")
spinbox_length.grid(row=2, column=1, padx=10, pady=10, sticky="w")

frame_options.grid(row=3, column=1, padx=10, pady=10, sticky="w")

checkButton_numbers.pack(anchor="w", pady=2)
checkButton_upper.pack(anchor="w", pady=2)
checkButton_lower.pack(anchor="w", pady=2)
checkButton_special.pack(anchor="w", pady=2)

separator_bottom.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

btn_generate.grid(row=6, column=0, padx=10, pady=10, sticky="w")
btn_copy.grid(row=6, column=1, padx=10, pady=10, sticky="w")

root.mainloop()