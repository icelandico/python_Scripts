import json
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Button, Label

import extcolors
from PIL import Image


class FlagColors(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Color extractor')
        self.geometry('500x200')

        self.img_extensions = ['.jpeg', '.jpg', '.gif', '.png']
        self.file_errors = []
        self.error_labels = []
        self.folder_path = tk.StringVar()

        self.browse_button = Button(self, text="Browse", command=self.browse_folder)
        self.browse_button.place(bordermode='outside', x=20, y=20, height=30, width=100)

        self.extract_button = Button(self, text="Extract", command=self.extract_json, state='disabled')
        self.extract_button.place(bordermode='outside', x=150, y=20, height=30, width=100)

        self.label_directory = Label(self, text='No folder selected')
        self.label_directory.place(bordermode='outside', x=20, y=60)

    def get_image_details(self, directory):
        collection = []
        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                img_path = os.path.abspath(os.path.join(dirpath, f))
                if not self.is_file_supported(img_path):
                    self.file_errors.append(
                        {'file': Path(f).stem, 'error': f'Error: {Path(f)}. Extension not supported'})
                    continue
                colors = self.get_colors(img_path)
                file_name = Path(f).stem
                file_dict = self.create_image_entry(colors, file_name)
                collection.append(file_dict)
        return collection

    def get_colors(self, img_path):
        img = Image.open(img_path).convert("RGBA")
        return extcolors.extract_from_image(img, tolerance=33, limit=10)

    def is_directory_empty(self, directory):
        directory_files = os.listdir(directory)
        return len(directory_files) == 0

    def is_file_supported(self, file):
        file_ext = Path(file).suffix
        return file_ext in self.img_extensions

    def create_image_entry(self, colors, file_name):
        total_pixels = colors[1]
        image_dict = {'file_name': file_name}
        image_colors = [{'colorCode': str(index), 'percent': round(color / total_pixels * 100)} for index, color in
                        colors[0] if round(color / total_pixels * 100) >= 1]
        image_dict['img_colors'] = image_colors

        return image_dict

    def browse_folder(self):
        directory = filedialog.askdirectory()
        if self.is_directory_empty(directory):
            messagebox.showerror("Error", "Directory is empty")
            return
        self.folder_path.set(directory)
        self.label_directory.config(text=f'Directory: {directory}')
        self.extract_button.config(state='normal')
        self.remove_error_labels()

    def extract_json(self):
        collection = self.get_image_details(self.folder_path.get())
        with open("result1.json", "w") as outfile:
            json.dump(collection, outfile)
        messagebox.showinfo('Info', 'Process completed!')
        self.generate_errors()
        self.reset_app_state()

    def reset_app_state(self):
        self.folder_path.set(None)
        self.label_directory.config(text='No folder selected')
        self.extract_button.config(state='disabled')

    def remove_error_labels(self):
        for label in self.error_labels:
            label.destroy()

    def generate_errors(self):
        count = 0
        for error_msg in self.file_errors:
            self.error_labels.append(Label(self, text=error_msg['error'], foreground="#ff0000"))
            self.error_labels[count].place(bordermode='outside', x=20, y=90 + count * 20)
            count += 1


flag_colors_app = FlagColors()
flag_colors_app.mainloop()
