from datetime import datetime

api_key = None
raise_for_status = True
_api_requests = []


def initialize(key: str, ignore_exceptions: bool = True) -> None:
    global api_key, raise_for_status
    api_key = key
    raise_for_status = ignore_exceptions


def api_request_rate(seconds: int):
    request_count = 0
    now = datetime.utcnow()
    for request in reversed(_api_requests):
        if (now - request).total_seconds() > seconds:
            break
        request_count += 1
    return request_count


def _api_request():
    _api_requests.append(datetime.utcnow())
    if len(_api_requests) > 10000:  # Seems reasonable
        _api_requests.pop(0)
