from flask import Flask, request, jsonify, render_template
import random
import os

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start_game():
    global secret_number
    secret_number = random.randint(1, 100)
    return jsonify({"message": "Game started! Guess 1-100 🎯"})

@app.route('/guess', methods=['POST'])
def guess():
    global secret_number
    data = request.get_json()
    user_guess = int(data.get("guess"))

    if user_guess == secret_number:
        msg = "Correct! 🎉 New number generated."
        secret_number = random.randint(1, 100)
    elif user_guess < secret_number:
        msg = "Too low 📉"
    else:
        msg = "Too high 📈"

    return jsonify({"result": msg})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)