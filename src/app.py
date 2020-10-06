import logging

from flask import Flask, jsonify, request
from flask_cors import CORS

from .model import TextBot

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

chat_bot = TextBot()


@app.route('/chatbot', methods=['GET', 'POST'])
def chat_response():
    usr_msg = request.get_json().get('text')
    message = chat_bot.start_api(usr_msg)
    # print(f'message is {usr_msg}', type(message))
    return jsonify({'text': message, 'author': 'bot'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
