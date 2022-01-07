from .structs import *


def interlink_nodes(prev_node, current_node):
    prev_node.next_day = current_node
    current_node.previous_day = prev_node


def time_object_from_string(time_string):
    time_fmt = "%d %H:%M"
    return datetime.strptime(time_string, time_fmt)


class WeekdayScheduleParser:
    def __init__(self, raw_schedule):
        self.raw_schedule = raw_schedule
        self.parsed = WeekSchedule()
        self.parse()

    def _get_parsed_day(self, day_num):
        day_index = day_num - 1  # datetime module counts from 1(monday) but list index counts from 0
        day_schedule = self.raw_schedule[day_index]
        return DayScheduleParser(day_schedule, day_num).parsed

    def _link_monday_with_sunday(self):
        sunday, monday = self.parsed.days[-1], self.parsed.days[0]
        interlink_nodes(sunday, monday)

    def parse(self):
        prev_day_node = None
        for day_num in range(1, 8):
            current_day_node = self._get_parsed_day(day_num)
            self.parsed.days.append(current_day_node)
            if prev_day_node:
                interlink_nodes(prev_day_node, current_day_node)
            prev_day_node = current_day_node

        self._link_monday_with_sunday()


class DayScheduleParser:
    def __init__(self, day_schedule, day_num):
        self.day_schedule = day_schedule
        self.day_num = day_num

        self.parsed = DaySchedule(self.day_num)
        self.parse()

    def parse(self):
        for raw_event in self.day_schedule:
            current_event = EventParser(raw_event, self.day_num).parsed
            self.parsed.events.append(current_event)


class EventParser:
    def __init__(self, raw_event, day_num):
        self.raw_event = raw_event
        self.day_num = day_num

        self.start = raw_event["start"]
        self.end = raw_event["end"]
        self.redirect_url = raw_event["redirect_url"]

        self.parsed = Event(self.redirect_url)
        self.parse()

    def parse(self):
        default_day_prefix = f"0{self.day_num} "
        try:
            end_day_override_prefix = self.raw_event['override_end_day'] + " "
        except KeyError:
            end_day_override_prefix = None

        start_time_string = default_day_prefix + self.start
        self.parsed.start = time_object_from_string(start_time_string)

        end_time_string = (end_day_override_prefix or default_day_prefix) + self.end
        self.parsed.end = time_object_from_string(end_time_string)
