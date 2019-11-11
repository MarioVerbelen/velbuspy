import attr

from ._registry import register
from .VelbusMessage import VelbusMessage
from ._types import Enum, UInt


@register
@attr.s(slots=True, auto_attribs=True)
class SensorSettingsRequest(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        SensorSettingsRequest = 0xe7

    _command: Command = Command.SensorSettingsRequest
