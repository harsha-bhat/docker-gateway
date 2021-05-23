from gateway import stats


def test_request_counts():
    assert stats.get_stats()["requests_count"]["success"] == 0
    assert stats.get_stats()["requests_count"]["error"] == 0

    stats.update_success()
    stats.update_success()
    stats.update_error()

    assert stats.get_stats()["requests_count"]["success"] == 2
    assert stats.get_stats()["requests_count"]["error"] == 1


def test_latency():
    assert stats.get_stats()["latency_ms"]["average"] == 0
    assert stats.get_stats()["latency_ms"]["p95"] == 0
    assert stats.get_stats()["latency_ms"]["p99"] == 0

    for i in range(1, 101):
        stats.update_time(i)

    assert abs(stats.get_stats()["latency_ms"]["average"] - 50) < 1
    assert abs(stats.get_stats()["latency_ms"]["p95"] - 95) < 1
    assert abs(stats.get_stats()["latency_ms"]["p99"] - 99) < 1
