from flask import Flask, redirect, url_for, request
import logging
import sys




import os

import openai
from flask import Flask, redirect, render_template, request, url_for
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)



@app.route("/quest", methods=("GET", "POST"))
def quest():
    if request.method == "GET":
        npc = request.args['npc_name']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt_game(npc),
            temperature=0.6,
        )
        print('---- ' + str(response.choices) + ' ++++')
        sys.stdout.flush()
        #return redirect(url_for("index", result=response.choices[0].text))
        return response.choices[0].text

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt_game(name):
    return f"""This is a fantasy world.
    I'm a brave worrier named {name}.
    please give me a quest  that invloves dragons and knights and use my name
    """



@app.route('/')
def index():
    return 'Web App with Python Flask!!!!'

@app.route('/game')
def game():
    app.logger.info(request.get_data())
    print('ori ' + str(request.headers) + ' kam')
    res = ''
    for x in request.args.items():
        res += str(x) + '\n'
    sys.stdout.flush()
    return res

@app.route('/game_post',methods = ['POST'])
def game_post():
    app.logger.info(request.get_data())
    print('--- ' + str(request.headers) + ' ++++')
    res = ''
    for x in request.form.items():
        res += str(x) + '\n'
    sys.stdout.flush()
    return res

app.run(host='0.0.0.0', port=81, debug=True)

