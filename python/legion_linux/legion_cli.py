#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
# pylint: disable=wrong-import-order
import argcomplete
import argparse
from legion import LegionModelFacade


class CLIFeatureCommand:
    def __init__(self, name: str, parser_subcommands, cmd_group: list, writeable: bool = True):
        self.name = name
        self.model = None
        status_parser = parser_subcommands.add_parser(
            f"{self.name}-status", help=f'Get current value for {self.name}')
        status_parser.set_defaults(
            func=lambda l, *args, **kwargs: self.command_status(**kwargs))

        if writeable:
            enable_parser = parser_subcommands.add_parser(
                f"{self.name}-enable", help=f'Enable {self.name}')
            enable_parser.set_defaults(
                func=lambda l, *args, **kwargs: self.command_enable(**kwargs))

            disable_parser = parser_subcommands.add_parser(
                f"{self.name}-disable", help=f'Disable {self.name}')
            disable_parser.set_defaults(
                func=lambda l, *args, **kwargs: self.command_disable(**kwargs))

        if cmd_group is not None:
            cmd_group.append(self)

    def set_model(self, model: LegionModelFacade):
        self.model = model

    # pylint: disable=no-self-use
    def command_status(self, **_) -> int:
        return 0

    # pylint: disable=no-self-use
    def command_enable(self, **_) -> int:
        return -1

    # pylint: disable=no-self-use
    def command_disable(self, **_) -> int:
        return -1


class MiniFancurveFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("minifancurve", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.fancurve_io.get_minifancuve())
        return 0

    def command_enable(self, **_) -> int:
        self.model.fancurve_io.set_minifancuve(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.fancurve_io.set_minifancuve(False)
        return 0


class LockFanControllerFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("lockfancontroller", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.lockfancontroller.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.lockfancontroller.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.lockfancontroller.set(False)
        return 0


class MaximumFanSpeedFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("maximumfanspeed", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.maximum_fanspeed.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.maximum_fanspeed.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.maximum_fanspeed.set(False)
        return 0


class BatteryConservationFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("batteryconservation", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.battery_conservation.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.battery_conservation.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.battery_conservation.set(False)
        return 0


class FnLockFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("fnlock", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.fn_lock.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.fn_lock.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.fn_lock.set(False)
        return 0


class TouchpadFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("touchpad", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.touchpad.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.touchpad.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.touchpad.set(False)
        return 0


class CameraPowerFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("camera-power", parser_subcommands, cmd_group, False)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.camera_power.get())
        return 0


class OnPowerSupplyFeatureCommand(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("on-power-supply", parser_subcommands, cmd_group, False)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.on_power_supply.get())
        return 0


class AlwaysOnUsbCharging(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("always-on-usb-charging", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.always_on_usb_charging.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.always_on_usb_charging.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.always_on_usb_charging.set(False)
        return 0


class RapidCharging(CLIFeatureCommand):
    def __init__(self, parser_subcommands, model: LegionModelFacade, cmd_group: list):
        super().__init__("rapid-charging", parser_subcommands, cmd_group)
        self.model = model

    def command_status(self, **_) -> int:
        print(self.model.rapid_charging.get())
        return 0

    def command_enable(self, **_) -> int:
        self.model.rapid_charging.set(True)
        return 0

    def command_disable(self, **_) -> int:
        self.model.rapid_charging.set(False)
        return 0


def autocomplete_install(_, **__) -> int:
    cmd = f"eval \"$(register-python-argcomplete {__file__})\""
    print("PLEASE RUN THE COMMAND:")
    print(cmd)


def fancurve_write_preset_to_hw(legion: LegionModelFacade, presetname: str, **_) -> int:
    # pylint: disable=unused-argument
    legion.fancurve_write_preset_to_hw(presetname)
    print(f'Successfully wrote preset {presetname} to hardware')
    return 0


def fancurve_write_hw_to_preset(legion: LegionModelFacade, presetname: str, **_) -> int:
    # pylint: disable=unused-argument
    legion.fancurve_write_hw_to_preset(presetname)
    print(f'Successfully wrote hardware to preset {presetname}')
    return 0


def fancurve_write_file_to_hw(legion: LegionModelFacade, filename: str, **_) -> int:
    # pylint: disable=unused-argument
    legion.fancurve_write_file_to_hw(filename)
    print(f'Successfully wrote fan curve from file {filename} to hardware')
    return 0


def fancurve_write_hw_to_file(legion: LegionModelFacade, filename: str, **_) -> int:
    # pylint: disable=unused-argument
    legion.fancurve_write_hw_to_file(filename)
    print(f'Successfully wrote fan curve from hardware to file {filename}')
    return 0


def fancurve_write_preset_for_current_profile(legion: LegionModelFacade, **_) -> int:
    # pylint: disable=unused-argument
    legion.fancurve_write_preset_for_current_profile()
    return 0


def main():
    parser = argparse.ArgumentParser(description='Legion CLI')
    parser.add_argument(
        '--donotexpecthwmon', action='store_true', help='Do not check hwmon dir when not needed', default=False)

    subcommands = parser.add_subparsers(title='subcommands', dest='subcommand')

    autocomplete_install_parser = subcommands.add_parser(
        'autocomplete-install', help='Install autocompletion in shell for this tool')
    autocomplete_install_parser.set_defaults(func=autocomplete_install)

    preset_to_hw_parser = subcommands.add_parser(
        'fancurve-write-preset-to-hw', help='Write fan curve from preset to hardware')
    preset_to_hw_parser.add_argument(
        'presetname', type=str, help='Name of the preset')
    preset_to_hw_parser.add_argument(
        '--preset-dir', type=str, help='Path of the directory with presets')
    preset_to_hw_parser.set_defaults(func=fancurve_write_preset_to_hw)

    hw_to_preset_parser = subcommands.add_parser(
        'fancurve-write-hw-to-preset', help='Write fan curve from hardware to preset')
    hw_to_preset_parser.add_argument(
        'presetname', type=str, help='Name of the preset')
    hw_to_preset_parser.add_argument(
        '--preset-dir', type=str, help='Path of the directory with presets')
    hw_to_preset_parser.set_defaults(func=fancurve_write_hw_to_preset)

    file_to_hw_parser = subcommands.add_parser(
        'fancurve-write-file-to-hw', help='Write fan curve from file to hardware')
    file_to_hw_parser.add_argument(
        'filename', type=str, help='Name of the file')
    file_to_hw_parser.set_defaults(func=fancurve_write_file_to_hw)

    hw_to_file_parser = subcommands.add_parser(
        'fancurve-write-hw-to-file', help='Write fan curve from hardware to file')
    hw_to_file_parser.add_argument(
        'filename', type=str, help='Name of the file')
    hw_to_file_parser.set_defaults(func=fancurve_write_hw_to_file)

    hw_to_file_parser = subcommands.add_parser(
        'fancurve-write-current-preset-to-hw',
        help='Write fan curve for the current profile (power mode, power supply status) to hardware')
    hw_to_file_parser.set_defaults(
        func=fancurve_write_preset_for_current_profile)

    cmd_group = []
    MiniFancurveFeatureCommand(subcommands, None, cmd_group)
    LockFanControllerFeatureCommand(subcommands, None, cmd_group)
    MaximumFanSpeedFeatureCommand(subcommands, None, cmd_group)
    BatteryConservationFeatureCommand(subcommands, None, cmd_group)
    FnLockFeatureCommand(subcommands, None, cmd_group)
    TouchpadFeatureCommand(subcommands, None, cmd_group)
    CameraPowerFeatureCommand(subcommands, None, cmd_group)
    OnPowerSupplyFeatureCommand(subcommands, None, cmd_group)
    AlwaysOnUsbCharging(subcommands, None, cmd_group)
    RapidCharging(subcommands, None, cmd_group)

    # only add autocompletion if package is installed
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        legion = LegionModelFacade(expect_hwmon=not args.donotexpecthwmon)
        for cmd in cmd_group:
            cmd.set_model(legion)
        # set global options
        if "preset_dir" in args and args.preset_dir is not None:
            legion.set_preset_folder(args.preset_dir)

        args.func(legion, **vars(args))


if __name__ == '__main__':
    main()
