import json


class UserJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {"id": o.id, "name": o.name}
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
