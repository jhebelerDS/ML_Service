from flask import Flask
from flask import request
import os


app = Flask(__name__)

#http://localhost:8786/hello?name=john&location=fish
@app.route('/get', methods=['GET'])
def helloget():
    args = request.args
    name = args.get('name')
    location = args.get('location')
    print("Name: ", name, " LocatAion: ", location)
    return 'Hello, Get!'

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    #filename = secure_filename(file.filename)
    file.save( "fish.jpg")
    return("saving file")

@app.route('/post', methods=['POST'])
def hellopost():
    args = request.args
    name = args.get('name')
    location = args.get('location')
    image = args.get('image')
    print("Name: ", name, " Location: ", location)
    print("IMage: ", image)
    return 'Hello, Post!'

print('starting server...')

app.run(host = '0.0.0.0', port = 8786)