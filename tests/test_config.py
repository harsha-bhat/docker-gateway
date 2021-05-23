from gateway import config


def test_config():
    parsed = config.load_config("tests/test.yml")

    assert len(parsed["routes"]) == 2
    assert parsed["default_response"]
    assert len(parsed["backends"]) == 2
