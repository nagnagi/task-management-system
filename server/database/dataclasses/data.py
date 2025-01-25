from dataclasses import dataclass

@dataclass
class Data:
    @classmethod
    def from_tuple(cls, obj: tuple) -> 'Data':
        return cls(*obj)
