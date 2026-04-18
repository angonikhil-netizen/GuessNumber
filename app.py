from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


game_state = {
    "secret_number": random.randint(1, 100),
    "attempts": 0
}

@app.route('/')
def index():
    # Reset game when the page is refreshed
    game_state["secret_number"] = random.randint(1, 100)
    game_state["attempts"] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    user_guess = int(data.get('guess'))
    game_state["attempts"] += 1
    
    if user_guess < game_state["secret_number"]:
        return jsonify({"message": "Too Low! Try a higher number. ↑", "status": "hint"})
    elif user_guess > game_state["secret_number"]:
        return jsonify({"message": "Too High! Try a lower number. ↓", "status": "hint"})
    else:
        msg = f"CORRECT! You found {game_state['secret_number']} in {game_state['attempts']} tries!"
        return jsonify({"message": msg, "status": "win"})

if __name__ == '__main__':
    app.run(debug=True)