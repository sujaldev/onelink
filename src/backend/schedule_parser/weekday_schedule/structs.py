from datetime import datetime


def abbreviate_long_string(s, max_length=15):
    if len(s) > max_length:
        return s[:max_length - 3] + "..."
    return s


def current_time():
    fmt = "%d %H:%M"
    time = datetime.now().strftime("0%u %H:%M")
    return datetime.strptime(time, fmt)


class WeekSchedule:
    def __init__(self):
        self.days = []

    def now(self, time=None):
        if not time:
            time = current_time()

        day_index = time.day - 1
        day = self.days[day_index]
        event = day.match_time_with_event(time)
        if event:
            return event.redirect_url
        day = day.previous_day
        event = day.match_time_with_last_event(time)
        if event:
            return event.redirect_url

    def __getitem__(self, item):
        return self.days[item]

    def __repr__(self):
        buffer = ""
        for day in self.days:
            buffer += str(day) + "\n\n\n"
        return buffer


class DaySchedule:
    def __init__(self, day_num):
        self.day_num = day_num
        self.day_name = datetime.strptime(f"0{self.day_num}", "%d").strftime("%a")

        self.previous_day = None
        self.next_day = None
        self.events = []

    def match_time_with_event(self, time):
        for event in self.events:
            if event.start <= time <= event.end:
                return event

    def match_time_with_last_event(self, time):
        try:
            event = self.events[-1]
            if event.start <= time <= event.end:
                return event
        except IndexError:
            return None

    def __repr__(self):
        table = ""
        top_bottom_lines = "+" + ("-" * 56) + "+"
        heading = "|" + self.day_name.center(56) + "|"
        table += f"{top_bottom_lines}\n{heading}\n{top_bottom_lines}\n"
        for event in self.events:
            table += "|" + str(event) + "|\n"
        table += top_bottom_lines
        return table


class Event:
    def __init__(self, redirect_url):
        self.start = None
        self.end = None
        self.redirect_url = redirect_url

    def __repr__(self):
        start = self.start.strftime("%a %H:%M")
        end = self.end.strftime("%a %H:%M")
        url = abbreviate_long_string(self.redirect_url)
        fmt = f"[{start:^15}][{url:^20}][{end:^15}]"
        return fmt

    def __lt__(self, other):
        return self.start < other.start

    def __le__(self, other):
        return self.start <= other.start

    def __gt__(self, other):
        return self.start > other.start

    def __ge__(self, other):
        return self.start >= other.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self.__eq__(other)
