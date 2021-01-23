from py_spm._event import Event


class Trial:
    def __init__(self, label, events, onset, bad, tag, repl):
        self.label = label
        self.events = [Event.from_dict(event_dict) for event_dict in events]
        self.onset = onset
        self.bad = bad
        self.tag = tag
        self.repl = repl

    def _event_property(self, property_):
        return [getattr(event, property_) for event in self.events]

    @property
    def event_types(self):
        return self._event_property("type")

    @property
    def event_values(self):
        return self._event_property("value")

    @property
    def event_durations(self):
        return self._event_property("duration")

    @property
    def event_times(self):
        return self._event_property("time")

    @property
    def event_offsets(self):
        return self._event_property("offset")
