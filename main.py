from flask import *
from imageMaker import makeImage

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        Text = {
            "text": request.form["text"],
            # Hello World
            "fontSize": int(request.form["fontSize"]),
            # 200
            "color": list(map(int, [request.form["textR"], request.form["textG"], request.form["textB"]])),
            # 255, 255, 0
            "textPosition": list(map(int, [request.form["textPositionW"], request.form["textPositionH"]]))
            # 10, 10
        }

        Background = {
            "color": list(map(int, [request.form["bgR"], request.form["bgG"], request.form["bgB"]]))
            # 73, 109, 137
        }

        photoWidth = int(request.form["photoWidth"])
        # 1920
        photoHeight = int(request.form["photoHeight"])
        # 1080

        makeImage(photoWidth, photoHeight, Background, Text)

        return render_template('index.html')

    else:
        return "Unknown method..."

app.run()