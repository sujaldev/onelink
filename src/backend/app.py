from flask import Flask, redirect, request
from pastebin.api import API
from schedule_parser import Parser, ParserException
from json import JSONDecodeError

app = Flask(__name__)

pastebin_api = API()


@app.route("/g/<copy_code>", methods=['GET'])
def copy_code_redirect(copy_code):
    try:
        raw_config = pastebin_api.copy(copy_code)
    except JSONDecodeError:
        return "<h1>JSON Decode Error</h1><p>Your copy code does not match with a valid json file</p>"

    try:
        redirect_url = Parser(raw_config).parsed.now()
    except ParserException:
        return "<h1>Parser Exception</h1><p>Your copy code does not contain a valid raw_config</p>"

    return redirect(redirect_url)


@app.route("/store", methods=['POST'])
def post_data():
    copy_code = pastebin_api.paste(request.data.decode())
    return {"copy_code": copy_code}


if __name__ == "__main__":
    app.run(debug=True)
