# Text Recognition

## Uses of the app
As we have transitioned into more of an online environment because of COVID-19, the need for working with digital notes and files has greatly increased. Unfortunately, many of us still possess handwritten notes from school or work that cannot be easily transfered online. This TextRecognition application allows you to save your notes as a text document right next to all your other files.

## How to use
- Select an image
- Click "Detect Words" button at the top (displays an image with the words surrounded by boxes)
- Fix any mistakes in the text input (not 100% accurate, so there will be typos or random characters)
- Save the file as a text document

<p align="center">
<img src="https://github.com/Shayan925/TextRecognition/blob/main/image_2021-07-06_204610.png" height="600" width="1200"/>
</p>

<p align="center">
<img src="https://github.com/Shayan925/TextRecognition/blob/main/image_2021-07-06_204831.png" height="600" width="1200"/>
</p>

## Requirements
```
pip install tesseract
pip install pytesseract
pip install plyer
pip install opencv-python
pip insatll kivy
```
Link the tesseract.exe file inside the program (if there are still problems with imports)

## Optional
If you would like support for multiple languages and math equations download the 
language packs from tesseract and add them to the program.

## Image types
Supports images of the following types:
- JPG
- PNG
- TIF
