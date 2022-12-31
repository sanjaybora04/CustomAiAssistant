from flask import Flask, render_template, jsonify, request
import assistant
import json

app = Flask(__name__,static_folder="./client/webClient/static",template_folder="./client/webClient/templates")

@app.route('/',methods=["GET"])
def home():
        if request.method == "GET":
                return render_template('index.html')

@app.route('/assistant', methods=["POST"])
def chatbot_msg():
        if request.method == "POST":
                user_data = json.loads(request.data)

                sentence = user_data['msg']

                return jsonify(msg=assistant.reply(sentence))



if __name__ == '__main__':
        app.run(port=5000, debug=True)
