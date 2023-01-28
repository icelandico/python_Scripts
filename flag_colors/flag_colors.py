import json
import logging
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Button, Label

import extcolors
from PIL import Image

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

img_extensions = ['.jpeg', '.jpg', '.gif', '.png']
file_errors = []
error_labels = []

def get_image_details(directory):
    collection = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            img_path = os.path.abspath(os.path.join(dirpath, f))
            if not is_file_supported(img_path):
                file_errors.append({'file': Path(f).stem, 'error': f'Error: {Path(f)}. Extension not supported'})
                continue
            colors = get_colors(img_path)
            file_name = Path(f).stem
            file_dict = create_image_entry(colors, file_name)
            collection.append(file_dict)
    return collection


def get_colors(img_path):
    img = Image.open(img_path).convert("RGBA")
    return extcolors.extract_from_image(img, tolerance=33, limit=10)

def is_file_supported(file):
    file_ext = Path(file).suffix
    return file_ext in img_extensions


def create_image_entry(colors, file_name):
    total_pixels = colors[1]
    image_dict = {'file_name': file_name}

    image_colors = [{'colorCode': str(index), 'percent': round(color / total_pixels * 100)} for index, color in colors[0] if round(color / total_pixels * 100) >= 1]
    image_dict['img_colors'] = image_colors

    return image_dict

def browse_folder():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    label_directory.config(text=f'Directory: {filename}')
    extract_button.config(state='normal')
    remove_error_labels()

def extract_json():
    collection = get_image_details(folder_path.get())
    with open("result1.json", "w") as outfile:
        json.dump(collection, outfile)
    messagebox.showinfo('Info', 'Process completed!')
    generate_errors()
    reset_app_state()

def reset_app_state():
    folder_path.set(None)
    label_directory.config(text='No folder selected')
    extract_button.config(state='disabled')

def remove_error_labels():
    for label in error_labels:
        label.destroy()

def generate_errors():
    count = 0
    for error_msg in file_errors:
        error_labels.append(Label(window, text=error_msg['error'], foreground="#ff0000"))
        error_labels[count].place(bordermode='outside', x=20, y=90 + count * 20)
        count += 1


window = tk.Tk()
window.title('Color extractor')
window.geometry('400x200')

folder_path = tk.StringVar()

browse_button = Button(window, text="Browse", command=browse_folder)
browse_button.place(bordermode='outside', x=20, y=20, height=30, width=100)

extract_button = Button(window, text="Extract", command=extract_json, state='disabled')
extract_button.place(bordermode='outside', x=150, y=20, height=30, width=100)

label_directory = Label(window, text='No folder selected')
label_directory.place(bordermode='outside', x=20, y=60)


window.mainloop()
