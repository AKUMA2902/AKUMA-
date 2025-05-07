
import tkinter as tk
from PIL import Image, ImageTk

def check_system():
    status_label.config(text="Система чиста", fg="lime")

root = tk.Tk()
root.title("AKUMA AntiCheat")
root.configure(bg="#111")

# Окно во весь экран
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, False)

frame = tk.Frame(root, bg="#111", padx=50, pady=50)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Баннер
try:
    img = Image.open("akuma_banner.png")
    img = img.resize((200, 200))
    banner_img = ImageTk.PhotoImage(img)
    banner = tk.Label(frame, image=banner_img, bg="#111")
    banner.image = banner_img
    banner.pack(pady=(0, 20))
except:
    pass

tk.Label(frame, text="AKUMA", font=("Arial", 36, "bold"), fg="red", bg="#111").pack()
tk.Label(frame, text="ANTICHEAT", font=("Arial", 18), fg="red", bg="#111").pack(pady=(0, 30))

btn = tk.Button(frame, text="НАЧАТЬ ПРОВЕРКУ", font=("Arial", 16), bg="red", fg="white", command=check_system)
btn.pack(pady=20)

status_label = tk.Label(frame, text="", font=("Arial", 16), fg="white", bg="#111")
status_label.pack()

root.mainloop()
