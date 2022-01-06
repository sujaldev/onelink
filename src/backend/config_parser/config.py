from exceptions import *
from datetime import datetime
from event_chain import EventChain, EventChainNode


# SAMPLE_CONFIG = {
#     "type": "daily",
#     "events": {
#         "01 23:30": {"end": "02 00:30", "redirect_url": "some_url"},
#         "02 06:30": {"end": "02 08:00", "redirect_url": "some_url"},
#         "02 09:30": {"end": "02 10:00", "redirect_url": "some_url"}
#     }
# }


def generate_datetime_object(string):
    return datetime.strptime(string, "%d %H:%M")


class DailyParser:
    def __init__(self, events):
        self.events = events

    def construct_event_chain(self):
        chain = None
        last_node = None
        for start, params in self.events.items():
            end, redirect_url = params.values()
            current_node = EventChainNode(
                generate_datetime_object(start),
                generate_datetime_object(end),
                redirect_url
            )

            if last_node:
                last_node.next_node = current_node  # link back to previous node
            else:
                chain = EventChain(current_node)  # chain initialization here
            last_node = current_node

        return chain


class EverydayParser:
    pass


class Config:
    def __init__(self, raw_config):
        try:
            config_type = raw_config["type"]
        except KeyError:
            raise MissingParserTypeParseError

        if config_type == "daily":
            self.parser = DailyParser(raw_config["events"])
        elif config_type == "everyday":
            self.parser = EverydayParser(raw_config["events"])
        else:
            raise InvalidParserTypeParseError

        self.parsed_chain = self.parser.construct_event_chain()

    def now(self):
        current_time_string = datetime.now().strftime("%d %H:%M")
        date_obj = generate_datetime_object(current_time_string)
        return self.parsed_chain.match_time_with_range(date_obj)
