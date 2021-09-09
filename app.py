import random

from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

# Add some jokes
jokes = []
with open("jokes.txt") as jokeFile:
    for line in jokeFile:
        jokeParts = line.split("<>")
        joke = {}
        joke["opener"] = jokeParts[0].strip()
        joke["punchline"] = jokeParts[1].strip()
        jokes.append(joke)


# Define home endpoint
@app.route("/", methods=["GET"])
def home():
    response = {}
    response["text"] = "Dear visitor, welcome to my website! " \
                       "My name is Marin Milina and I'm a software developer from Croatia. " \
                       "If you came to this website accidentally, at least you can have a dad joke :)"
    response["linkedin"] = "https://www.linkedin.com/in/marin-milina-4216a8151"
    response["github"] = "https://github.com/marinco"
    response["email"] = "marin.milina96@gmail.com"
    response["joke"] = random.choice(jokes)
    return jsonify(response)


serve(app, host="0.0.0.0", port=8080)
