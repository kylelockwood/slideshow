#! python3

"""Display a slideshow from a list of filenames"""

import os
import tkinter
from itertools import cycle
from PIL import Image, ImageTk

def main():
    """Set inital variables and start the slideshow"""
    # Set delay and image folder
    delay = 2500
    path = 'C:\\Users\\User\\Pictures\\'
    slides = load_images(path)

    # start the slideshow
    slideshow = Slideshow(slides, delay)
    slideshow.start()


def load_images(path):
    """ Returns a list of path + images"""
    # Only return files in the folder with the follosing extensions
    exts = ['jpg', 'bmp', 'png', 'gif', 'jpeg']
    files = [path + fn for fn in os.listdir(path) if any(fn.lower().endswith(ext) for ext in exts)]
    return files


class Slideshow(tkinter.Tk):
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, delay):
        tkinter.Tk.__init__(self)
        # Escape key quits script
        self.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit(), self.destroy()))
        self.geometry("+0+0")
        self.delay = delay
        self.images = None
        self.image = None
        self.image_name = None
        self.set_images(images)
        self.slide = tkinter.Label(self)
        self.slide.pack(expand=True, fill='both')

    def set_images(self, images):
        """Cycle through images"""
        self.images = cycle(images)

    def set_image(self):
        """Setup image to be displayed"""
        self.image_name = next(self.images)
        original_image = Image.open(self.image_name)
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        # Remove window controls
        self.overrideredirect(True)
        self.geometry("%dx%d+0+0" % (w, h))
        # Resize image to fit screen
        imgWidth, imgHeight = original_image.size
        if imgWidth > w or imgHeight > h:
            ratio = min(w/imgWidth, h/imgHeight)
            imgWidth = int(imgWidth*ratio)
            imgHeight = int(imgHeight*ratio)
            original_image = original_image.resize((imgWidth, imgHeight), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(original_image)

    def main(self):
        """Display the images"""
        self.set_image()
        self.slide.config(image=self.image, bg='black')
        self.after(self.delay, self.start)

    def start(self):
        """Start method"""
        self.main()
        self.mainloop()


if __name__ == "__main__":
    main()
