from dataclasses import dataclass, asdict

@dataclass
class Data:
    def to_dict(self) -> dict:
        return asdict(self)

    def concat(self, other: 'Data') -> dict:
        return self.to_dict() | other.to_dict()

    @classmethod
    def from_tuple(cls, obj: tuple) -> 'Data':
        return cls(*obj)
