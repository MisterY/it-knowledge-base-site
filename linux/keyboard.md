# Keyboard

Setting up keyboard:

- Enable Compose key to easily enter special characters. See the [list](https://fsymbols.com/keyboard/linux/compose/).
- Enable switching layouts with Alt+Shift.
- [Dvorak <> Qwerty](https://github.com/tbocek/dvorak) for Ctrl+key shortcuts in Qwerty. (see below)


## Dvorak

- Get [dvorak](https://github.com/tbocek/dvorak). Build (make dvorak).
- add your user to the "input" group
- add the [udev rule](https://github.com/tuomasjjrasanen/python-uinput/blob/master/udev-rules/40-uinput.rules). To run the rules manually, execute `sudo udevadm control --reload`.
- Run it in Startup Applications using `./dvorak /dev/input/by-id/usb-Microsoft_Wired_Keyboard_400-event-kbd`. This command can be stored in a .sh file and run on logon.
