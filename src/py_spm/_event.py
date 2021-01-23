from py_spm.utils import empty_to_none


class Event:
    def __init__(self, type_, value, duration, time, offset):
        self.type = type_
        self.value = value
        self.duration = empty_to_none(duration)
        self.time = time
        self.offset = offset
        self.end_time = time + (0 if self.duration is None else self.duration)

        self.sample = None
        self.end_sample = None

    @classmethod
    def from_dict(cls, event_dict):
        if "type" in event_dict:
            event_dict["type_"] = event_dict.pop("type")
        return cls(**event_dict)

    def to_dict(self):
        return {
            "type_": self.type,
            "value": self.value,
            "duration": self.duration,
            "time": self.time,
            "offset": self.offset,
        }

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(type_='{self.type}', "
            f"value={self.value}, "
            f"duration={self.duration}, "
            f"time={self.time}, "
            f"offset={self.offset})"
        )
