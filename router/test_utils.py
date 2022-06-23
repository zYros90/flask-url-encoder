from router.utils import encode_url, encode_url_v2, check_request, is_valid_url


def test_encode_url():
    # check consistency of encoding
    assert (
        encode_url("https://original-domain.xy/abcdefghij", "http://abc.def/")
        == "http://abc.def/fbb1cb3e"
    )
    assert (
        encode_url("https://original-domain.xy/!$§&$/()=?0?", "http://abc.def/")
        == "http://abc.def/3851d26c"
    )

    # check if encoded_url is valid
    encoded_url = encode_url(
        "https://original-domain.xy/abcdefghij", "http://abc.def/"
    )
    assert is_valid_url(encoded_url)


def test_encode_url_v2():
    # check if encoded_url is valid
    encoded_url = encode_url_v2(
        "https://original-domain.xy/abcdefghij", "http://abc.def/"
    )
    assert is_valid_url(encoded_url)


def test_validate_url():
    # valid urls
    assert is_valid_url("https://google.com")
    assert is_valid_url("https://google.com/")
    assert is_valid_url("http://google.com")
    assert is_valid_url("http://www.google.com")
    assert is_valid_url(
        "http://www.google.com/routex?first_query_param=abc&second_query_param=xyz"
    )
    assert is_valid_url("http://localhost:5959")

    # non valid urls
    assert not is_valid_url("https://goo;gle.com/xy")
    assert not is_valid_url("https://google.c;om/xy")
    assert not is_valid_url("https://google.c?om/xy")
    assert not is_valid_url("https://google.c:om/xy")
    assert not is_valid_url("https://google.c;om/xy")
    assert not is_valid_url("https://google.c@om/xy")
    assert not is_valid_url("https://googlec@om/xy")
    assert not is_valid_url("https://googlec@om/x[y]")
    # also non valid urls: without http or https
    assert not is_valid_url("google.com")
    assert not is_valid_url("www.google.com")
    assert not is_valid_url("www.google.com")


def test_check_request():
    # valid requests
    url, error_msg = check_request({"url": "https://google.com/xyz"})
    assert error_msg == ""
    assert url == "https://google.com/xyz"

    # non valid requests
    url, error_msg = check_request({"x": "https://google.com/xyz"})
    assert error_msg == "url key not found in request body"
    assert url == ""

    url, error_msg = check_request({"url": "google.com/xyz"})
    assert (
        error_msg
        == "invalid url, please provide a valid url which starts with http:// or https://"
    )
    assert url == ""
