import binascii
import re
import string
import random


# encode with crc-32 checksum
# the hash consists of characters (a-z) and numbers (0-9) with length 8
# possible combinations = n^k = (26+10)^8 = 2.82*e^12
def encode_url(url: str, new_domain: str) -> str:
    hash = hex(binascii.crc32(str.encode(url)))
    new_url = new_domain + hash[2:]
    return new_url


# using random string generation to create even shorter url
# possible combinations n^k = 67^6 = 90,458,382,169
def encode_url_v2(url: str, new_domain: str) -> str:
    allowed_letters = (
        "_-.#~"  # additional allowed letters in urls and which are not reserved
    )
    characters = string.ascii_letters + string.digits + allowed_letters
    rand_string = "".join(random.choice(characters) for i in range(6))
    new_url = new_domain + rand_string
    return new_url


# validate request body
def check_request(req: dict) -> (str, str):
    if "url" not in req:
        return "", "url key not found in request body"

    url = req["url"]

    valid = is_valid_url(url)
    if not valid:
        return (
            "",
            "invalid url, please provide a valid url which starts with http:// or https://",
        )

    return url, ""


# regex is from django: https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
# I copied it according to the motto “A little copying is better than a little dependency”
def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url)
