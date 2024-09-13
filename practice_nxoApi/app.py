from generateImg import getImgUrl
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app) 

@app.route("/") # 루트 경로에 접속시 index 호출
def index():
    return render_template("index.html")

@app.route("/process", methods={"POST"})
def process():
    name = request.form["name"]
    style = request.form['style']
    summary, profile_picture_url = getImgUrl(name,style)
    print(profile_picture_url)
    return jsonify(
        {
            "summarized_text": summary,
            "picture_url": profile_picture_url
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) # 모든 사용자

