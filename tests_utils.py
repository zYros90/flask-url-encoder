import requests
import json
import random, string


class bcolors:
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"


def random_string(length):
    alphabet = string.ascii_lowercase
    return "".join(random.choice(alphabet) for i in range(length))


def test_single_encoding_decoding(
    server_host: str, encode_path: str, decode_path: str
) -> bool:
    encoded_url, decoded_url = "", ""
    original_url = "https://original-domain.xy/" + random_string(10)

    # post request to encode original_url
    resp = requests.post(server_host + encode_path, json={"url": original_url})
    try:
        encoded_url = json.loads(resp.text)["encoded_url"]
    except:
        print(bcolors.FAIL + "server response: " + resp.text)
        return False

    # decode encoded_url to decoded_url
    resp = requests.post(server_host + decode_path, json={"url": encoded_url})
    try:
        decoded_url = json.loads(resp.text)["decoded_url"]
    except:
        print(bcolors.FAIL + "server response: " + resp.text)
        return False

    # compare decoded_url with original_url
    if decoded_url != original_url:
        print(bcolors.FAIL + "decoded_url != original_url")
        return False

    return True
