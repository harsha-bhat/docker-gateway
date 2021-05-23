from tdigest import TDigest

digest = TDigest()
digest.update(0)

requests = {
    "success": 0,
    "error": 0,
}


def update_success():
    """Update succeeded request count"""
    requests["success"] += 1


def update_error():
    """Update failed request count"""
    requests["error"] += 1


def update_time(t):
    """Update request latency"""
    digest.update(t)


def get_stats():
    """Get stats about the service"""
    return {
        "requests_count": requests,
        "latency_ms": {
            "average": digest.trimmed_mean(0, 100),
            "p95": digest.percentile(95),
            "p99": digest.percentile(99),
        },
    }
