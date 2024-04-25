from PIL import Image 
# from pytesseract
from flask import Flask,request,render_template
import pytesseract 

app=Flask(__name__)
path_to_tesseract = r"C:\Users\samcy\anaconda3\Scripts\pytesseract.exe"

# img = Image.open('img3.png') 

pytesseract.pytesseract.tesseract_cmd = path_to_tesseract 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    img=request.files['img']
    img=Image.open(img)
    text=pytesseract.image_to_string(img)
    return render_template('index.html', text=text[:-1])

@app.route('/reset')
def reset():
    return index()

if __name__=='__main__':
    app.run(debug=True)