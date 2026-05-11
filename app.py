from flask import Flask
import random

app = Flask(__name__)

fortunes = [
    "You will have a pleasant surprise today.",
    "Adventure awaits you around the corner.",
    "Your hard work will soon pay off.",
    "A new opportunity is coming your way.",
    "Good news will arrive this week.",
    "Someone is thinking of you right now.",
]

@app.route('/')
def fortune():
    fortune = random.choice(fortunes)
    return f"""
    🔮 Your fortune: {fortune}
    
    <a href="/">Get another fortune →</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)