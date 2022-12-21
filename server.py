from flask import Flask, render_template, jsonify, request
import chatbot

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=["POST"])
def chatbot_msg():
	if request.method == "POST":
		user_data = request.json

		sentence = user_data['message']
		
		return jsonify(answer=chatbot.chat.reply(sentence))


if __name__ == '__main__':
	app.run(port=5000, debug=True)