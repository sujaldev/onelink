class MissingParserTypeParseError(Exception):
    def __init__(self):
        super().__init__("Raw config lacks a type attribute")


class InvalidParserTypeParseError(Exception):
    def __init__(self):
        super().__init__("Raw config with invalid parser type. Type attribute has to be one of 'daily' or 'weekend'")
