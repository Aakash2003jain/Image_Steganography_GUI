# Image Steganography GUI

A simple **Image Steganography** application built using Python and Tkinter. This tool allows users to **hide (encode) text into an image** and **retrieve (decode) the hidden text** from an image. It supports **drag-and-drop** functionality for seamless user experience.

## Features

#### ✅ **Drag & Drop Support** – Easily upload images by dragging them into the interface.
#### ✅ **Text Encoding** – Hide a secret message inside a `.png` or `.bmp` image using LSB (Least Significant Bit) technique.
#### ✅ **Text Decoding** – Retrieve hidden messages from encoded images.
#### ✅ **User-Friendly GUI** – Built with Tkinter for an intuitive experience.
#### ✅ **Error Handling** – Provides clear messages for incorrect file formats or missing inputs.

---

## Installation & Setup

### Prerequisites
Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Install Required Dependencies
Run the following command to install the required libraries:

```sh
pip install tkinterdnd2 pillow
```

### Clone the Repository
```sh
git clone https://github.com/Aakash2003jain/Image_Steganography_GUI.git
cd Image_Steganography_GUI
```

### Run the Application
```sh
python ImageS.py
```

---

## Usage Guide

1. **Select an Image**: Drag and drop an image (.png or .bmp) or click **Upload Image**.
2. **Encode Text**:
   - Enter the secret message in the text box.
   - Click **Encode Text into Image** to hide the message.
   - The encoded image will be saved automatically.
3. **Decode Text**:
   - Select an encoded image.
   - Click **Decode Text from Image** to retrieve the hidden message.

---

## Demo Video
Watch the demo video to see how the application works:  
📹 [Demo Video](https://raw.githubusercontent.com/Aakash2003jain/Image_Steganography_GUI/main/demo.mp4)

## License
   This project is licensed under the MIT License. See the LICENSE file for more details.

---

