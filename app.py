import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = os.getenv(FACEIT_API_KEY)

HEADERS = {
    Authorization fBearer {API_KEY}
}

PLAYERS = [
    s-chilla,
    donk666
    degst3r
]

def is_in_match(nickname)
    try
        player_res = requests.get(
            fhttpsopen.faceit.comdatav4playersnickname={nickname},
            headers=HEADERS
        )

        if player_res.status_code != 200
            return Ошибка player

        player_id = player_res.json().get(player_id)
        if not player_id
            return Не найден

        match_res = requests.get(
            fhttpsopen.faceit.comdatav4players{player_id}matchestype=ongoing&limit=1,
            headers=HEADERS
        )

        if match_res.status_code != 200
            return Ошибка match

        matches = match_res.json().get(items, [])

        return 🔴 В матче if matches else 🟢 Не в матче

    except
        return Ошибка

@app.route()
def status()
    result = {}
    for player in PLAYERS
        result[player] = is_in_match(player)
    return jsonify(result)

if __name__ == __main__
    app.run(host=0.0.0.0, port=3000)
