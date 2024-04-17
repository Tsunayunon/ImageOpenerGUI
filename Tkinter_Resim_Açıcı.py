import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def dosya_ac():
    print("Dosya aç fonksiyonu çalıştı.")  # Debug mesajı
    resim = filedialog.askopenfilename(title="Resim seçiniz",
                                       filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    print("Seçilen resim:", resim)  # Seçilen dosya yolu
    if resim:
        try:
            pil_image = Image.open(resim)
            tk_image = ImageTk.PhotoImage(pil_image)

            # Yeni bir pencere oluştur
            new_window = tk.Toplevel(root)
            new_window.title("Resim Penceresi")
            new_window.geometry(f"{tk_image.width()}x{tk_image.height()}")

            # Bu pencerede bir canvas oluştur ve resmi ekle
            canvas = tk.Canvas(new_window, width=tk_image.width(), height=tk_image.height())
            canvas.pack()
            canvas.create_image(0, 0, anchor="nw", image=tk_image)

            # ImageTk.PhotoImage nesnesini saklamak önemli
            canvas.image = tk_image

        except Exception as e:
            messagebox.showerror("Hata", f"Resim yüklenirken bir hata oluştu: {e}")

root = tk.Tk()
root.title("Manzara Penceresi")
root.geometry("300x200")

btn_open = tk.Button(root, text="Resim Aç", command=dosya_ac)
btn_open.pack(pady=20)

root.mainloop()
