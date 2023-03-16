from flask import Flask, render_template
import platform, os
app = Flask(__name__)

@app.route('/')
def index():
    machine = platform.machine()
    processor = platform.processor()
    os = platform.system()
    return render_template('index.html', machine=machine, processor=processor, os=os)

