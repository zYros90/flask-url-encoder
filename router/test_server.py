import router.server


def test_set_encode_domain():
    test_domain = "https://example.com"
    router.server.set_encode_domain(test_domain)
    assert test_domain == router.server.domain
