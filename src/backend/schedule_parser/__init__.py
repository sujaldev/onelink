from weekday_schedule.parser import WeekdayScheduleParser


class Parser:
    def __init__(self, raw_config):
        self.raw_config = raw_config
        self.parsed = self.parse()

    def parse(self):
        config_type = self.raw_config["type"]
        if config_type == "weekdays":
            parser = WeekdayScheduleParser
        elif config_type == "daily":
            parser = None  # not implement yet
        else:
            raise Exception("Invalid config type, can either be 'weekdays' or 'daily'")

        raw_schedule = self.raw_config["schedule"]
        return parser(raw_schedule).parsed
