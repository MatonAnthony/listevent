class HTTPError(Exception):
    """ Exception used for network related exception such as HTTP 500 """
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message

class FormatError(Exception):
    def __init__(self, content_type, message):
        self.content_type = content_type
        self.message = message