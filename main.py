import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os
import webbrowser
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False


DB_PATH = os.path.join(os.getcwd(), "magizh.db")

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            service TEXT
        )
    """)
    conn.commit()
    conn.close()


root = tk.Tk()
root.title("Magizh Construction")
root.geometry("850x550")
root.configure(bg="white")
root.resizable(False, False)

create_db()

content = tk.Frame(root, bg="white")
content.pack(fill="both", expand=True)

def clear_page():
    for w in content.winfo_children():
        w.destroy()
    if hasattr(root, 'image_refs'):
        root.image_refs = []


def home_page():
    clear_page()

    def whatsapp():
        webbrowser.open("https://wa.me/918680965606")

    def call_now():
        messagebox.showinfo("Call Now", "Call: +91 86809 65606")

    contact = tk.Frame(content, bg="white")
    contact.pack(pady=10)

    tk.Button(contact, text="WhatsApp Us",
              bg="#25D366", fg="white",
              width=15, command=whatsapp).grid(row=0, column=0, padx=10)

    tk.Button(contact, text="Call Now",
              bg="#2196F3", fg="white",
              width=15, command=call_now).grid(row=0, column=1, padx=10)

    tk.Label(content, text="MAGIZH CONSTRUCTION",
             font=("Arial", 34, "bold"),
             fg="orange", bg="white").pack(pady=20)

    tk.Label(content, text="Water Proofing Tech",
             font=("Arial", 18),
             fg="orange", bg="white").pack()

    tk.Label(content, text="Quality You Can Trust",
             fg="orange", bg="white").pack(pady=10)

    btns = tk.Frame(content, bg="white")
    btns.pack(pady=20)

    tk.Button(btns, text="Add Customer",
              bg="orange", fg="white",
              width=15, command=add_customer).grid(row=0, column=0, padx=10)

    tk.Button(btns, text="View Customers",
              bg="orange", fg="white",
              width=15, command=view_customers).grid(row=0, column=1, padx=10)

    tk.Label(content, text="Our Services",
             font=("Arial", 22, "bold"),
             bg="white").pack(pady=15)

    frame = tk.Frame(content, bg="white")
    frame.pack()

    def service_card(title, col):
        card = tk.Frame(frame, bg="#F5F5F5",
                        width=220, height=120,
                        bd=1, relief="solid")
        card.grid(row=0, column=col, padx=15)
        card.pack_propagate(False)
        tk.Label(card, text=title,
                 font=("Arial", 12, "bold"),
                 bg="#F5F5F5").pack(expand=True)

    service_card("Waterproofing", 0)
    service_card("Repair & Renovation", 1)
    service_card("Grouting Work", 2)


def services_page():
    clear_page()

    services = [
        ("Waterproofing", "images/1.jpg"),
        ("Waterproofing", "images/3.jpg"),
        ("Grouting Work", "images/11.jpg"),
        ("Grouting Work", "images/22.jpg"),
        ("Grouting Work", "images/33.jpg"),
        ("Renovation Work", "images/111.jpg")
    ]

    
    root.image_refs = []  
    img_frame = tk.Frame(content, bg="white")
    img_frame.pack(pady=10)
    for i, (title, img_path) in enumerate(services):
        service_frame = tk.Frame(img_frame, bg="white")
        service_frame.grid(row=i//3, column=i%3, padx=10, pady=5)
        if PIL_AVAILABLE:
            try:
                img = Image.open(img_path)
                img = img.resize((200, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                root.image_refs.append(photo)
                img_label = tk.Label(service_frame, image=photo, bg="white")
                img_label.pack()
                title_label = tk.Label(service_frame, text=title, font=("Arial", 12, "bold"), bg="white")
                title_label.pack()
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
                tk.Label(service_frame, text=f"{title}\nImage not found", font=("Arial", 12), bg="white").pack()
        else:
            tk.Label(service_frame, text=f"{title}\nImage: {img_path}", font=("Arial", 12), bg="white").pack()

    points = [
        "• Waterproofing",
        "• Repair & Renovation",
        "• Grouting Work",
        "• Terrace & Bathroom Waterproofing",
        "• Basement & Water Tank Leakage Repair",
        "• Crack Repair",
        "• Epoxy Flooring",
        "• Pressure Grouting & PU Injection"
    ]

    for p in points:
        tk.Label(content, text=p,
                 font=("Arial", 14),
                 bg="white",
                 anchor="w").pack(fill="x", padx=80, pady=4)

    tk.Label(content, text="Our Services",
             font=("Arial", 22, "bold"),
             bg="white").pack(pady=15)

    frame = tk.Frame(content, bg="white")
    frame.pack()

    def service_card(title, col):
        card = tk.Frame(frame, bg="#F5F5F5",
                        width=220, height=120,
                        bd=1, relief="solid")
        card.grid(row=0, column=col, padx=15)
        card.pack_propagate(False)
        tk.Label(card, text=title,
                 font=("Arial", 12, "bold"),
                 bg="#F5F5F5").pack(expand=True)

    service_card("Waterproofing", 0)
    service_card("Repair & Renovation", 1)
    service_card("Grouting Work", 2)


def about_page():
    clear_page()
    tk.Label(content, text="About Company",
             font=("Arial", 22, "bold"),
             bg="white").pack(pady=20)

    info = (
        "Company Name : Magizh Construction\n\n"
        "Location     : Ramanathapuram, Tamil Nadu, India\n\n"
        "Contact No   : +91 86809 65606\n\n"
        "Email        : magizhconstruction@gmail.com\n\n"
        "Specialist   : Construction Services & Waterproofing"
    )

    tk.Label(content, text=info,
             font=("Arial", 14),
             justify="left",
             bg="white").pack(pady=10)


def contact_page():
    clear_page()
    tk.Label(content, text="Contact Us",
             font=("Arial", 22, "bold"),
             bg="white").pack(pady=20)

    tk.Label(content,
             text="Phone : +91 86809 65606\n"
                  "Email : magizhconstruction@gmail.com\n"
                  "WhatsApp Available",
             font=("Arial", 14),
             bg="white").pack(pady=10)

    btns = tk.Frame(content, bg="white")
    btns.pack(pady=20)

    tk.Button(btns, text="WhatsApp",
              bg="#25D366", fg="white",
              width=12,
              command=lambda: webbrowser.open("https://wa.me/918680965606")
              ).grid(row=0, column=0, padx=10)

    tk.Button(btns, text="Call",
              bg="#2196F3", fg="white",
              width=12,
              command=lambda: messagebox.showinfo("Call", "+91 86809 65606")
              ).grid(row=0, column=1, padx=10)


def add_customer():
    win = tk.Toplevel(root)
    win.title("Add Customer")
    win.geometry("400x320")
    win.configure(bg="#FFF3E0")
    win.resizable(False, False)

    tk.Label(win, text="Add Customer",
             font=("Arial", 16, "bold"),
             bg="#FFF3E0").pack(pady=10)

    tk.Label(win, text="Name", bg="#FFF3E0").pack()
    e1 = tk.Entry(win, width=30)
    e1.pack()

    tk.Label(win, text="Phone", bg="#FFF3E0").pack()
    e2 = tk.Entry(win, width=30)
    e2.pack()

    tk.Label(win, text="Service", bg="#FFF3E0").pack()
    e3 = tk.Entry(win, width=30)
    e3.pack()

    def save():
        if e1.get() == "" or e2.get() == "" or e3.get() == "":
            messagebox.showwarning("Error", "All fields required")
            return
        if not e2.get().isdigit():
            messagebox.showerror("Error", "Phone must be numbers only")
            return

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO customer (name, phone, service) VALUES (?,?,?)",
            (e1.get(), e2.get(), e3.get())
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer Saved")
        win.destroy()

    tk.Button(win, text="Save",
              bg="orange", fg="white",
              width=15, command=save).pack(pady=15)


def view_customers():
    win = tk.Toplevel(root)
    win.title("Customer List")
    win.geometry("600x350")

    cols = ("ID", "Name", "Phone", "Service")
    table = ttk.Treeview(win, columns=cols, show="headings")

    for c in cols:
        table.heading(c, text=c)
        table.column(c, width=140)

    table.pack(fill="both", expand=True)

    scroll = ttk.Scrollbar(win, orient="vertical", command=table.yview)
    table.configure(yscroll=scroll.set)
    scroll.pack(side="right", fill="y")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")
    for row in cur.fetchall():
        table.insert("", tk.END, values=row)
    conn.close()


menubar = tk.Menu(root)
menubar.add_command(label="Home", command=home_page)
menubar.add_command(label="About", command=about_page)
menubar.add_command(label="Services", command=services_page)
menubar.add_command(label="Contact", command=contact_page)

root.config(menu=menubar)

home_page()
root.mainloop()