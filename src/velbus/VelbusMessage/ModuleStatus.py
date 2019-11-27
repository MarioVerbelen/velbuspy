import attr

from ._registry import register
from .VelbusMessage import VelbusMessage
from ._types import Enum, UInt, Bitmap, Bool


# Different decodes possible
# They can be identified by their length
# VMB8PBU sends 7 data bytes; VMB6IN sends 5 data bytes; VMBELO sends 8 data bytes; VMBEL1_2_4 sends 7 data bytes


@register
@attr.s(slots=True, auto_attribs=True)
class ModuleStatus8PBU(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        ModuleStatus = 0xed
    _command: Command = Command.ModuleStatus

    channel_pressed: Bitmap(8) = Bitmap(8).zero()
    channel_enabled: Bitmap(8) = Bitmap(8).zero()
    channel_not_inverted: Bitmap(8) = Bitmap(8).zero()
    channel_locked: Bitmap(8) = Bitmap(8).zero()
    channel_program_disabled: Bitmap(8) = Bitmap(8).zero()

    # byte 7
    prog_sunset_enabled: Bool = False
    prog_sunrise_enabled: Bool = False

    class LocalGlobal(Enum(1)):
        Local = 0
        Global = 1
    alarm2: LocalGlobal = LocalGlobal.Local
    alarm2_enabled: Bool = False
    alarm1: LocalGlobal = LocalGlobal.Local
    alarm1_enabled: Bool = False

    class Program(Enum(2)):
        No = 0
        Summer = 1
        Winter = 2
        Holiday = 3
    program: Program = Program.No


@register
@attr.s(slots=True, auto_attribs=True)
class ModuleStatus6IN(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        ModuleStatus = 0xed
    _command: Command = Command.ModuleStatus

    input_status: Bitmap(8) = Bitmap(8).zero()
    leds_on: Bitmap(8) = Bitmap(8).zero()
    leds_slow_blink: Bitmap(8) = Bitmap(8).zero()
    leds_fast_blink: Bitmap(8) = Bitmap(8).zero()


@register
@attr.s(slots=True, auto_attribs=True)
class ModuleStatusVMBELO(VelbusMessage):
    _priority: UInt(2) = 3

    class Command(Enum(8)):
        ModuleStatus = 0xed
    _command: Command = Command.ModuleStatus

    channel_pressed: Bitmap(8) = Bitmap(8).zero()
    channel_enabled: Bitmap(8) = Bitmap(8).zero()

    # DATABYTE4
    open_collector_output_on: Bool = False
    open_collector_output_locked: Bool = False
    open_collector_output_program_disabled: Bool = False
    temperature_sensor_program_disabled: Bool = False
    edge_colod_inhibited: Bool = False

    ignore_bit1: Bool = False
    ignore_bit2: Bool = False
    ignore_bit3: Bool = False

    channel_locked: Bitmap(8) = Bitmap(8).zero()
    channel_program_disabled: Bitmap(8) = Bitmap(8).zero()

    # byte 7
    prog_sunset_enabled: Bool = False
    prog_sunrise_enabled: Bool = False

    class LocalGlobal(Enum(1)):
        Local = 0
        Global = 1
    alarm2: LocalGlobal = LocalGlobal.Local
    alarm2_enabled: Bool = False
    alarm1: LocalGlobal = LocalGlobal.Local
    alarm1_enabled: Bool = False

    class Program(Enum(2)):
        No = 0
        Summer = 1
        Winter = 2
        Holiday = 3
    program: Program = Program.No

    # byte 8
    class DisplayOnOff(Enum(1)):
        On = 1
        Off = 0
    display: DisplayOnOff = DisplayOnOff.Off

    class ScreensaverOnOff(Enum(1)):
        On = 1
        Off = 0
    screen_saver: ScreensaverOnOff = ScreensaverOnOff.Off

    menu_page: Bool = False

    class Page(Enum(5)):
        Button_page_1 = 0
        Button_page_2 = 1
        Button_page_3 = 2
        Button_page_4 = 3
        Button_page_5 = 4
        Button_page_6 = 5
        Button_page_7 = 6
        Button_page_8 = 7
        Counter_page_1 = 8
        Counter_page_2 = 9
        Counter_page_3 = 10
        Counter_page_4 = 11
        Local_temperature_page = 12
        Remote_temperature_page_1 = 13
        Remote_temperature_page_2 = 14
        Remote_temperature_page_3 = 15
        Remote_temperature_page_4 = 16
        Remote_temperature_page_5 = 17
        Remote_temperature_page_6 = 18
        Remote_temperature_page_7 = 19
        Remote_temperature_page_8 = 20
        Remote_temperature_page_9 = 21
        Remote_temperature_page_10 = 22
        Remote_temperature_page_11 = 23
        Remote_temperature_page_12 = 24
        Analog_sensor_page_1 = 25
        Analog_sensor_page_2 = 26
        Analog_sensor_page_3 = 27
        Analog_sensor_page_4 = 28
        Clock_page = 29
    page: Page = Page.Button_page_1
