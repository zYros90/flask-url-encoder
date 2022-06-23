import os
import argparse
from router.server import app, set_encode_domain
from router.utils import is_valid_url
from gevent.pywsgi import WSGIServer


# parse args
def parse_args() -> (bool, int, str):
    parser = argparse.ArgumentParser("server")
    parser.add_argument(
        "-debug", "--debug", default=False, type=bool, help="run app in debug-mode"
    )
    parser.add_argument(
        "-port", "--port", default=5000, type=int, help="port of flask server"
    )
    parser.add_argument(
        "-encode_domain",
        "--encode_domain",
        default="http://abc.def/",
        type=str,
        help="domain of encoded url",
    )
    args = parser.parse_args()
    return args.debug, args.port, args.encode_domain


# read environment variables and overwrite debug, port and encode_domain
def merge_env_vars(debug, port, encode_domain) -> (bool, int, str):
    try:
        if os.environ["APP_DEBUG"] != "":
            boolStr = os.environ["APP_DEBUG"].lower()
            print()
            if boolStr == "true":
                debug = True
            else:
                debug = False
    except:
        pass
    try:
        if os.environ["APP_PORT"] != "":
            port = int(os.environ["APP_PORT"])
    except:
        pass
    try:
        if os.environ["APP_ENCODE_DOMAIN"] != "":
            encode_domain = str(os.environ["APP_ENCODE_DOMAIN"])
    except:
        pass
    return debug, port, encode_domain


# parse args and merge with environment variables
def parse_args_with_env_vars() -> (bool, int, str):
    debug, port, encode_domain = parse_args()
    return merge_env_vars(debug, port, encode_domain)


def main():
    # read in args and environment variables
    debug, port, encode_domain = parse_args_with_env_vars()

    # check and set encode_domain
    if not is_valid_url(encode_domain):
        print("please enter a valid domain which starts with http:// or https://")
        exit(1)
    if encode_domain[len(encode_domain) - 1] != "/":
        encode_domain += "/"
    set_encode_domain(encode_domain=encode_domain)

    # run app
    if debug:
        print("running server in develop mode on port: " + str(port))
        app.run(host="0.0.0.0", port=port, debug=debug)
    else:
        print("running server in production mode on port " + str(port))
        http_server = WSGIServer(("", port), app)
        http_server.serve_forever()


if __name__ == "__main__":
    main()
