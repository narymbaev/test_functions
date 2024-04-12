import datetime
import json
from decimal import Decimal
from enum import Enum

from core import errors


class Dictionarizable:
    def dict(self) -> dict:
        raise NotImplementedError()


class JsonSerializable:
    def json(self) -> str:
        raise NotImplementedError()


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (str, int, float, type(None))):
            return obj
        elif isinstance(obj, datetime.datetime):
            return int(obj.timestamp())
        elif isinstance(obj, datetime.date):
            return int(datetime.datetime.combine(obj, datetime.time(0, 0, 0)).timestamp())
        elif isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, errors.Error):
            return obj.toDict()

        return str(obj)

        # return super(DateTimeEncoder, self).default(obj)


encoder = JSONEncoder(separators=(',', ':'))
