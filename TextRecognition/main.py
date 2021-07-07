from kivy.config import Config
Config.set("graphics", "width", "1800")
Config.set("graphics", "height", "900")
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from plyer import filechooser
from pytesseract import Output
from process_image import get_greyscale, resize_with_aspect_ratio
from tkinter import *
import tkinter.filedialog
import pytesseract
import cv2

# If there are troubles with importing pytesseract try specifying the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\USER\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

class ScreenDisplay(GridLayout):

    output_text = StringProperty("")
    file_path = StringProperty("")

    # Default language is English 
    # For more languages download the tesseract language packs
    language = StringProperty("eng")

    def select_image(self):
        try:
            self.file_path = filechooser.open_file(title="Pick an Image..", filters=[("Image", "*.jpg", "*.png", "*.tif")])[0]
        except IndexError as e:
            self.file_path = ""

    def detect_words(self):

        if self.file_path != "":

            # Read image 
            img = cv2.imread(self.file_path)
            img_draw_boxes = get_greyscale(img)
            img_predict = get_greyscale(img)

            # Draw boxes around words
            data = pytesseract.image_to_data(img_draw_boxes, output_type = Output.DICT)
            n_boxes = len(data["text"])
            for i in range(n_boxes):
                if float(data["conf"][i]) > 60:
                    # Detects the dimensions of the box that needs to be drawn
                    (x, y, w, h) = (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
                    # Draws a green box around the word
                    img = cv2.rectangle(img_draw_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

            resize = resize_with_aspect_ratio(img_draw_boxes, height=900)
            cv2.imshow("Detected Words", resize)
            
            # Find words in image and turn it into a string
            custom_config = f"-l {self.language} --oem 1 --psm 3"
            text = pytesseract.image_to_string(img_predict, config=custom_config)

            self.output_text = text

    def save_file(self, text):
        root = Tk()
        root.withdraw()
        name = tkinter.filedialog.asksaveasfile(filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
        if name is not None:
            name.write(text)
            name.close()


class TextRecognitionApp(App):
    pass

TextRecognitionApp().run()
