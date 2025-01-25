from dataclasses import dataclass, asdict

@dataclass
class Data:
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_tuple(cls, obj: tuple) -> 'Data':
        return cls(*obj)
