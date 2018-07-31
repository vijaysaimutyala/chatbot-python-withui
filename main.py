from flask import Flask, render_template, request, jsonify
# import aiml
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return render_template('chatnew.html')

# @app.route("/ask", methods=['POST'])
# def ask():
# 	message = request.form['messageText'].strip()
# 	print("the message is ",str(message))
# 	return jsonify({'status':'OK','answer':message})

	# # kernel = aiml.Kernel()

	# if os.path.isfile("bot_brain.brn"):
	#     kernel.bootstrap(brainFile = "bot_brain.brn")
	# else:
	#     kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	#     kernel.saveBrain("bot_brain.brn")

	# # kernel now ready for use
	# while True:
	#     if message == "quit":
	#         exit()
	#     elif message == "save":
	#         kernel.saveBrain("bot_brain.brn")
	#     else:
	#         bot_response = kernel.respond(message)
	#         # print bot_response

if __name__ == "__main__":
    app.run(debug=True)
