from flask import Flask, render_template
import random

app = Flask(__name__)

# List of jokes
jokes = [
    # "Why don't scientists trust atoms? Because they make up everything!",
    # "Why don't skeletons fight each other? They don't have the guts!",
    # "Why did the scarecrow win an award? Because he was outstanding in his field!",
    # "Why did the bicycle fall over? It was two-tired!"

    "What did the Java Code say to the C code? You’ve got no class",
    "Why do programmers prefer dark mode? Because light attracts bugs",
    "Why did the programmer quit her job? Because she didn’t get arrays",
    "Programming is 10% writing code and 90% understanding why it’s not working",
    "; The Ultimate Hide and Seek Champion"
]

def get_random_joke():
    return random.choice(jokes)

@app.route('/')
def index():
    joke = get_random_joke()
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001) #if we didn't mention any port, the flask development server will listen on port 5000