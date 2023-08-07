from flask import Flask
from flask import request
from flask import send_from_directory
import flask
import re
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    number = request.args.get('number')
    token="a1i0b--Zy1pIW-lkrzzJh5H8S1gSiasFEnHzH5FSh_FCdqelI8BRM6kfx6P0hlvF"
    
    def num_search(authkey, num):
        params = {'q': num, 'countryCode': '', 'type': '4', 'locAddr': '', 'placement': 'SEARCHRESULTS,HISTORY,DETAILS',
                'encoding': 'json'}
        headers = {'content-type': 'application/json; charset=UTF-8', 'accept-encoding': 'gzip',
                'user-agent': 'Truecaller/11.75.5 (Android;10)', 'clientsecret': 'lvc22mp3l1sfv6ujg83rd17btt',
                'authorization': 'Bearer ' + authkey}
        req = requests.get('https://search5-noneu.truecaller.com/v2/search', headers=headers, params=params)
        return req.content
    resp = flask.Response(num_search(token,number).decode("utf-8"))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

    
if __name__ == "__main__":
    app.run(debug=True)





