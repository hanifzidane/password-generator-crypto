import tkinter as tk
from tkinter import messagebox
from database import init_db, add_password, get_passwords, delete_password
from crypto import encrypt_password, decrypt_password
import random, string
import pyperclip

# ================= INIT =================
init_db()
root = tk.Tk()
root.title("💻 Modern Password Manager")
root.geometry("600x500")
root.configure(bg="#1E1E1E")

# ================= FUNCTIONS =================
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def add_entry():
    # Modal dialog untuk input
    dialog = tk.Toplevel(root)
    dialog.title("Tambah Password")
    dialog.configure(bg="#1E1E1E")
    dialog.geometry("300x150")
    dialog.grab_set()  # fokus di sini dulu

    tk.Label(dialog, text="Website:", bg="#1E1E1E", fg="white").pack(pady=5)
    website_entry = tk.Entry(dialog, width=30)
    website_entry.pack(pady=5)

    tk.Label(dialog, text="Username:", bg="#1E1E1E", fg="white").pack(pady=5)
    username_entry = tk.Entry(dialog, width=30)
    username_entry.pack(pady=5)

    def save():
        website = website_entry.get().strip()
        username = username_entry.get().strip()
        if not website or not username:
            messagebox.showwarning("Warning", "Website dan username harus diisi!")
            return
        password = generate_password()
        enc_password = encrypt_password(password)
        add_password(website, username, enc_password)
        messagebox.showinfo("Sukses", f"Password untuk {website} disimpan!\n{password}")
        refresh_list()
        dialog.destroy()

    tk.Button(dialog, text="Simpan", command=save, bg="#2C2C2C", fg="white").pack(pady=10)

def refresh_list(search_text=""):
    listbox.delete(0, tk.END)
    for row in get_passwords():
        display_text = f"{row[0]} | {row[1]} | {row[2]}"
        if search_text.lower() in display_text.lower():
            listbox.insert(tk.END, display_text)

def show_password():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Pilih item", "Pilih password dulu")
        return
    item = listbox.get(selected[0])
    password_id = int(item.split(" | ")[0])
    enc_pass = get_passwords()[password_id-1][3]
    dec_pass = decrypt_password(enc_pass)
    pyperclip.copy(dec_pass)
    messagebox.showinfo("Password", f"Password: {dec_pass}\nSudah dicopy ke clipboard!")

def delete_entry():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Pilih item", "Pilih password dulu")
        return
    item = listbox.get(selected[0])
    password_id = int(item.split(" | ")[0])
    delete_password(password_id)
    refresh_list()

def search_entry(event):
    search_text = search_var.get()
    refresh_list(search_text)

# ================= UI =================
top_frame = tk.Frame(root, bg="#1E1E1E")
top_frame.pack(pady=10)

add_btn = tk.Button(top_frame, text="Add Password", command=add_entry, bg="#2C2C2C", fg="white")
add_btn.grid(row=0, column=0, padx=5)

show_btn = tk.Button(top_frame, text="Show Password", command=show_password, bg="#2C2C2C", fg="white")
show_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(top_frame, text="Delete Password", command=delete_entry, bg="#2C2C2C", fg="white")
del_btn.grid(row=0, column=2, padx=5)

search_var = tk.StringVar()
search_box = tk.Entry(root, textvariable=search_var, bg="#2C2C2C", fg="white")
search_box.pack(pady=5, padx=10, fill=tk.X)
search_box.bind("<KeyRelease>", search_entry)

listbox = tk.Listbox(root, width=80, bg="#2C2C2C", fg="white", selectbackground="#4A90E2")
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

refresh_list()
root.mainloop()
