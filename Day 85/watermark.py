import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont

image_path = ""
original_image = None
preview_image = None
watermark_color = "white"

def upload_image():
    global image_path, original_image, preview_image

    file = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if not file:
        return

    image_path = file
    original_image = Image.open(file).convert("RGBA")

    preview = original_image.copy()
    preview.thumbnail((500, 400))

    preview_image = ImageTk.PhotoImage(preview)

    image_label.config(image=preview_image)
    image_label.image = preview_image


def choose_color():
    global watermark_color

    color = colorchooser.askcolor()[1]

    if color:
        watermark_color = color


def add_watermark():

    if original_image is None:
        messagebox.showerror("Error", "Upload an image first.")
        return

    text = watermark_entry.get().strip()

    if text == "":
        messagebox.showerror("Error", "Enter watermark text.")
        return

    font_size = int(size_spinbox.get())

    image = original_image.copy()

    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt_layer)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = image.width - text_width - 20
    y = image.height - text_height - 20

    opacity = opacity_scale.get()

    rgb = tuple(int(watermark_color[i:i+2], 16) for i in (1, 3, 5))

    draw.text(
        (x, y),
        text,
        font=font,
        fill=(rgb[0], rgb[1], rgb[2], opacity)
    )

    watermarked = Image.alpha_composite(image, txt_layer)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG", "*.png"),
            ("JPEG", "*.jpg")
        ]
    )

    if save_path:

        if save_path.endswith(".jpg") or save_path.endswith(".jpeg"):
            watermarked.convert("RGB").save(save_path)
        else:
            watermarked.save(save_path)

        messagebox.showinfo("Success", "Watermarked Image Saved!")

root = tk.Tk()
root.title("Image Watermarker")
root.geometry("700x750")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Image Watermarker",
    font=("Arial", 22, "bold")
)

title.pack(pady=10)

upload_btn = tk.Button(
    root,
    text="Upload Image",
    width=20,
    command=upload_image
)

upload_btn.pack()

image_label = tk.Label(root)
image_label.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

tk.Label(
    frame,
    text="Watermark Text"
).grid(row=0, column=0, padx=5, pady=5)

watermark_entry = tk.Entry(
    frame,
    width=30
)

watermark_entry.grid(row=0, column=1)

tk.Label(
    frame,
    text="Font Size"
).grid(row=1, column=0)

size_spinbox = tk.Spinbox(
    frame,
    from_=10,
    to=100,
    width=10
)

size_spinbox.grid(row=1, column=1, sticky="w")

color_btn = tk.Button(
    frame,
    text="Choose Color",
    command=choose_color
)

color_btn.grid(row=2, column=0, pady=10)

tk.Label(
    frame,
    text="Opacity"
).grid(row=3, column=0)

opacity_scale = tk.Scale(
    frame,
    from_=20,
    to=255,
    orient="horizontal",
    length=200
)

opacity_scale.set(120)

opacity_scale.grid(row=3, column=1)

save_btn = tk.Button(
    root,
    text="Add Watermark & Save",
    width=25,
    bg="green",
    fg="white",
    command=add_watermark
)

save_btn.pack(pady=20)

root.mainloop()
