from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "it works!! good job !! hello world!! \n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
