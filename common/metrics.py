from prometheus_client import Counter

REQ = Counter("requests_total", "Total Requests")
