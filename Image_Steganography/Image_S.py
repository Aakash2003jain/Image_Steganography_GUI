import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button, Text
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import os

# Global Variable
selected_file = None

def on_drop(event):
    """Handles drag-and-drop functionality for selecting an image file."""
    global selected_file
    file_path = event.data.strip()

    # Remove curly braces on Windows (TkinterDnD wraps paths with spaces in {})
    if file_path.startswith('{') and file_path.endswith('}'):
        file_path = file_path[1:-1]

    if file_path.lower().endswith((".png", ".bmp")):
        selected_file = file_path
        update_preview(file_path)
    else:
        messagebox.showerror("Error", "Invalid file type! Please select a PNG or BMP image.")

def upload_image():
    """Opens file dialog to select an image for encoding/decoding."""
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    
    if file_path:
        selected_file = file_path
        update_preview(file_path)

def update_preview(file_path):
    """Updates the image preview in the GUI."""
    img = Image.open(file_path)
    img.thumbnail((150, 150))  # Resize for preview
    img = ImageTk.PhotoImage(img)
    
    image_label.config(image=img)
    image_label.image = img

def encode_text_into_image():
    """Encodes the entered text into the selected image."""
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "No image selected!")
        return

    text = text_entry.get("1.0", "end-1c")
    if not text:
        messagebox.showerror("Error", "No text entered to encode!")
        return

    try:
        image = Image.open(selected_file)
        binary_text = ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # End delimiter
        pixels = image.load()
        width, height = image.size
        index = 0
        
        for y in range(height):
            for x in range(width):
                if index < len(binary_text):
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(binary_text[index])  # Modify the least significant bit
                    pixels[x, y] = (r, g, b)
                    index += 1
                else:
                    output_path = os.path.splitext(selected_file)[0] + "_encoded.png"
                    image.save(output_path)
                    messagebox.showinfo("Success", f"Text encoded successfully! Saved as {output_path}")
                    return
    except Exception as e:
        messagebox.showerror("Error", f"Encoding failed: {str(e)}")

def decode_text_from_image():
    """Decodes hidden text from the selected image."""
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "No image selected!")
        return

    try:
        image = Image.open(selected_file)
        pixels = image.load()
        width, height = image.size
        binary_text = ""
        
        for y in range(height):
            for x in range(width):
                r, _, _ = pixels[x, y]
                binary_text += str(r & 1)
                if binary_text.endswith('1111111111111110'):
                    binary_text = binary_text[:-16]  # Remove delimiter
                    decoded_text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
                    text_entry.delete("1.0", "end")
                    text_entry.insert("1.0", decoded_text)
                    messagebox.showinfo("Success", "Text decoded successfully!")
                    return
        messagebox.showerror("Error", "No hidden text found!")
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed: {str(e)}")

# GUI Setup
root = TkinterDnD.Tk()  # Use TkinterDnD for Drag & Drop support
root.title("Image Steganography")
root.geometry("450x400")

# Image Upload Section
Label(root, text="Drag & Drop an Image (.png , .bmp) or Click 'Upload'").pack()
image_label = Label(root)
image_label.pack()

# Drag and Drop Area
drop_area = Label(root, text="Drop Image Here", relief="groove", width=30, height=2, bg="lightgray")
drop_area.pack(pady=5)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

# Buttons for Upload & Drag-Drop
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Text Input Section
Label(root, text="Enter text to encode:").pack()
text_entry = Text(root, height=5, width=50)
text_entry.pack()

# Encode & Decode Buttons
Button(root, text="Encode Text into Image", command=encode_text_into_image).pack()
Button(root, text="Decode Text from Image", command=decode_text_from_image).pack()
Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
