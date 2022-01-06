class PastebinInvalidExpireParameter(Exception):
    def __init__(self):
        super().__init__("Expire parameter must be one of these: (N, 10M, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)")


class PastebinServerOrClientError(Exception):
    def __init__(self, status_code):
        super().__init__(
            f"Server Responded with {status_code}: "
            f"Error connecting to pastebin, either bad request or server error"
        )
