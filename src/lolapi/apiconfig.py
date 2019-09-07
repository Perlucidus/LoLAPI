api_key = None
raise_on_status = True


def initialize(key: str, ignore_exceptions: bool = True) -> None:
    global api_key, raise_on_status
    api_key = key
    raise_on_status = ignore_exceptions
