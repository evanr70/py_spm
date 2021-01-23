import numpy as np
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
        return np.array([getattr(event, property_) for event in self.events])

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

    @property
    def event_end_times(self):
        return self._event_property("end_time")

    @property
    def event_samples(self):
        return self._event_property("sample")

    @property
    def event_end_samples(self):
        return self._event_property("end_sample")

    def calculate_samples(self, sample_frequency):
        for event in self.events:
            event.sample = round(event.time * sample_frequency)
            event.end_sample = round(event.end_time * sample_frequency)
