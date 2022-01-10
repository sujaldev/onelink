from .weekday_schedule.parser import WeekdayScheduleParser


class ParserException(Exception):
    def __init__(self):
        super().__init__("An error occurred while parsing, invalid raw_config")


class Parser:
    def __init__(self, raw_config):
        self.raw_config = raw_config
        try:
            self.parsed = self.parse()
        except KeyError:
            raise ParserException

    def parse(self):
        config_type = self.raw_config["type"]
        if config_type == "weekdays":
            parser = WeekdayScheduleParser
        elif config_type == "daily":
            parser = None  # not implement yet
        else:
            raise KeyError

        raw_schedule = self.raw_config["schedule"]
        return parser(raw_schedule).parsed
