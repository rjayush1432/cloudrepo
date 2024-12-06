from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ayushraj(2201330100080)'

if __name__ == '__main__':
    app.run(port=5000)
