from flask import Flask, render_template, request, jsonify
# import aiml
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = request.form['messageText'].strip()
	print("the message is ",str(message))
	return jsonify({'status':'OK','answer':message})

if __name__ == "__main__":
    app.run(debug=True,port=8000)
