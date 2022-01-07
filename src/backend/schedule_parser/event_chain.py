class EventChainNode:
    def __init__(self, start, end, redirect_url, next_node=None):
        self.start = start
        self.end = end
        self.redirect_url = redirect_url

        self.next_node = next_node

    def range_matches_time(self, time):
        return self.start <= time <= self.end

    def __repr__(self):
        start = self.start.strftime("%H:%M, %A")
        end = self.end.strftime("%H:%M, %A")
        return f"{start} to {end}: {self.redirect_url}"


class EventChain:
    def __init__(self, first_node):
        self.first_node = first_node

    def match_time_with_range(self, time):
        current_node = self.first_node
        while not current_node.range_matches_time(time):
            current_node = current_node.next_node
            if current_node is None:
                return None

        return current_node
