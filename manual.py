import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess


def open_final_pred():
    try:
        subprocess.Popen(["python", "final_pred.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch detection script: {e}")


def main():
    root = tk.Tk()
    root.title("Sign Language Detection Application")
    root.configure(bg="#FFE4E1")  # Light pink background

    title = tk.Label(root, text="Sign Language Detection Application",
                     font=("Helvetica", 24, "bold"),
                     bg="#FFE4E1", fg="#880E4F")
    title.pack(pady=30)

    style = ttk.Style()
    style.configure("Pink.TButton",
                    font=("Helvetica", 16, "bold"),
                    padding=10,
                    background="#F48FB1",
                    foreground="#000000",  # black text
                    relief="raised",
                    anchor="center")
    style.map("Pink.TButton",
              background=[("active", "#F06292"), ("pressed", "#EC407A")],
              foreground=[("active", "#000000"), ("pressed", "#000000")])

    start_button = ttk.Button(root, text="Start Sign Language Detection",
                              command=open_final_pred, style="Pink.TButton")
    start_button.pack(pady=20, ipadx=15, ipady=8)

    # Open and display image at original aspect ratio, no forced resizing
    image_path = "signs.png"
    try:
        img = Image.open(image_path)
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=img_tk, bg="#FFE4E1")
        img_label.image = img_tk
        # pack with expand and fill so image fully displays and window expands accordingly
        img_label.pack(pady=20, expand=True, fill='both')
        # Resize window dynamically according to image size + padding
        root.geometry(f"{img.width + 60}x{img.height + 150}")
    except FileNotFoundError:
        error_label = tk.Label(root, text="Error: Hand gestures image not found.",
                               fg="red", bg="#FFE4E1")
        error_label.pack(pady=20)
        # Set default size if image missing
        root.geometry("800x600")

    root.mainloop()


if __name__ == "__main__":
    main()
