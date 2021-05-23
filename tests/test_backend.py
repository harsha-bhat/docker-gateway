from gateway import backend


def test_parse_labels():
    parsed = backend._parse_labels(["key=value"])

    assert parsed["key"] == "value"


def test_label_match():
    source = {"key": "value", "otherkey": "othervalue"}
    target = {"key": "value"}

    assert backend._match_labels(source, target) == True

    source = {"otherkey": "othervalue"}
    target = {"key": "value"}

    assert backend._match_labels(source, target) == False
