from prometheus_client import Counter
from prometheus_client import Histogram

REQUEST_COUNT = Counter(
    "request_count",
    "Total API Requests"
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "API Latency"
)