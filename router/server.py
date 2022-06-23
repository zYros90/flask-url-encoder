from flask import Flask, request, jsonify
from router.utils import encode_url, encode_url_v2, check_request

app = Flask(__name__)

memory_store = {}


def set_encode_domain(encode_domain: str):
    global domain
    domain = encode_domain


@app.route("/encode", methods=["POST"])
def encode_route():
    decoded_url, error_msg = check_request(request.json)
    if error_msg != "":
        return jsonify({"error": error_msg}), 400

    encoded_url = encode_url(decoded_url, domain)
    memory_store[encoded_url] = decoded_url

    return jsonify({"encoded_url": encoded_url}), 200


@app.route("/decode", methods=["POST"])
def decode_route():
    encoded_url, error_msg = check_request(request.json)
    if error_msg != "":
        return jsonify({"error": error_msg}), 400

    if encoded_url in memory_store.keys():
        decoded_url = memory_store[encoded_url]
        return jsonify({"decoded_url": decoded_url}), 200

    return jsonify({"error": "url not found"}), 400


@app.route("/", methods=["GET"])
def liveness_probe():
    return "ok", 200