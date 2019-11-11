import attr

from ._registry import register
from .VelbusMessage import VelbusMessage
from ._types import Enum, UInt, Temperature


@register
@attr.s(slots=True, auto_attribs=True)
class SensorSettings1(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        SensorSettings_part1 = 0xE8
    _command: Command = Command.SensorSettings_part1

    current_temperature_set: Temperature(0.5) = 0
    comfort_temperature_set_for_heating: Temperature(0.5) = 0
    day_temperature_set_for_heating: Temperature(0.5) = 0
    night_temperature_set_for_heating: Temperature(0.5) = 0
    anti_frost_temperature_set_for_heating: Temperature(0.5) = 0
    boost_temperature_difference_set: Temperature(0.5) = 0
    # ToDo: https://github.com/velbus/moduleprotocol/blob/master/protocol_vmbel1_2_4.pdf P9
    # 5Bit
    hysteresis_temperature: Temperature(0.5) = float(0)


@register
@attr.s(slots=True, auto_attribs=True)
class SensorSettings2(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        SensorSettings_part2 = 0xE9
    _command: Command = Command.SensorSettings_part2

    comfort_temperature_set_for_cooling: Temperature(0.5) = 0
    day_temperature_set_for_cooling: Temperature(0.5) = 0
    night_temperature_set_for_cooling: Temperature(0.5) = 0
    save_temperature_set_for_cooling: Temperature(0.5) = 0
    default_sleep_timer: UInt(16) = 0
    """
    Special cases:
     Timer between (0x0001) 1 and (0xfeff) 65279 minutes
     Timer == 0xffffff: manual mode selected
    """
    send_temperature_interval: UInt(8) = 0


@register
@attr.s(slots=True, auto_attribs=True)
class SensorSettings3(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        SensorSettings_part3 = 0xC6
    _command: Command = Command.SensorSettings_part3

    temperature_alarm_1: Temperature(0.5) = 0
    temperature_alarm_4: Temperature(0.5) = 0
    lower_temperature_range_cooling: Temperature(0.5) = 0
    upper_temperature_range_heating: Temperature(0.5) = 0
    calibration_offset_factor: Temperature(0.5) = 0
    zone_number: UInt(8) = 0
    calibration_gain_factor: UInt(8) = 0


@register
@attr.s(slots=True, auto_attribs=True)
class SensorSettings4(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        SensorSettings_part4 = 0xB9
    _command: Command = Command.SensorSettings_part4

    min_switching_time: UInt(8) = 0
    pump_delay_on_time: UInt(8) = 0
    pump_delay_off_time: UInt(8) = 0
    temperature_alarm_2: Temperature(0.5) = 0
    temperature_alarm_3: Temperature(0.5) = 0
    lower_temperature_range_heating: Temperature(0.5) = 0
    upper_temperature_range_cooling: Temperature(0.5) = 0
