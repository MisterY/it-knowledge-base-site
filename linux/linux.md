# Linux

Everything here refers mainly to OpenSuse with Gnome although the settings are similar for other linux systems.

- [Software](software)

## Tips

Here are some tips that need to be sorted:

- to disable Auto-Login: Yast - Security and Users - User/Group Management - Expert Options >Login Settings 
- Locale: 
    - in terminal, run `locale` to see the locale. `localectl` to see and modify. Use `sudo localectl set-locale LANG=en_IE.utf8`. [Ref](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)
    - Yast, Language, Detailed settings allows the same.
- Open With: to set the default application, Alt+Enter in file browser.

### Keyboard

- Enable Compose key to easily enter special characters. See the [list](https://fsymbols.com/keyboard/linux/compose/).
- Enable switching layouts with Alt+Shift.
- [Dvorak <> Qwerty](https://github.com/tbocek/dvorak) for Ctrl+key shortcuts in Qwerty.

### Folders

- /home/<user>/.local/share/gnucash = gnucash data directory
- ~/.config/autostart  = autostart applications
