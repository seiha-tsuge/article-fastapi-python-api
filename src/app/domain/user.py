from dataclasses import asdict, dataclass
from typing import Dict


@dataclass(frozen=True)
class User:
    id: int
    name: str

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(**d)

    def to_dict(self) -> Dict:
        return asdict(self)
