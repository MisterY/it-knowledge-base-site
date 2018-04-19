# Linux

Everything here refers mainly to OpenSuse with Gnome although the settings are similar for other linux systems.

- [Software](software)

## Tips

Here are some tips that need to be sorted:

- to set Auto-Login: Yast - Security and Users - User/Group Management - Expert Options >Login Settings 
- Locale: 
    - in terminal, run `locale` to see the locale. `localectl` to see and modify. Use `sudo localectl set-locale LANG=en_IE.utf8`. [Ref](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)
    - Yast, Language, Detailed settings allows the same.
- Open With: to set the default application, Alt+Enter in file browser.

### Keyboard

- Enable Compose key to easily enter special characters. See the [list](https://fsymbols.com/keyboard/linux/compose/).
- Enable switching layouts with Alt+Shift.
- [Dvorak <> Qwerty](https://github.com/tbocek/dvorak) for Ctrl+key shortcuts in Qwerty.

#### Dvorak

Use [dvorak](https://github.com/tbocek/dvorak) project.
To run rules manually, execute `sudo udevadm control --reload`.

### Folders

- /home/<user>/.local/share/gnucash = gnucash data directory
- ~/.config/autostart  = autostart applications

## Updates

To prevent PackageKit automatically downloading all the update packages, run
```
gsettings set org.gnome.software download-updates false
```
also, disable PackageKit service
```
systemctl stop packagekit
systemctl disable packagekit
```

Resources: 
- [Thread](https://forums.opensuse.org/showthread.php/530069-Tumbleweed-waiting-for-shared-lock-on-var-lib-rpm-Packages)
- [Fedora](https://ask.fedoraproject.org/en/question/10929/how-do-i-stop-package-kit-from-constantly-searching-for-updates/)
