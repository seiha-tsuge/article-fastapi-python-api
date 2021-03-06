from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class User:
    id: int
    name: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return asdict(self)
