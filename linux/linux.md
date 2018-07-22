# Linux

Everything here refers mainly to OpenSuse with Gnome although the settings are similar for other linux systems.

- [Applications](applications)
- [AppImage](appimage)
- [Boot](boot)
- [Keyboard](keyboard)
- [Software](software)
- [Themes](themes)

## Tips

Here are some tips that need to be sorted:

- to set Auto-Login: Yast - Security and Users - User/Group Management - Expert Options >Login Settings 
- Locale:
    - Set locale variables in .profile. i.e. `export LC_TIME=en_IE.utf8`
    - First day of week, set the LC_TIME locale variable.
    - Or, in terminal, run `locale` to see the locale. `localectl` to see and modify. Use `sudo localectl set-locale LANG=en_IE.utf8`. [Ref](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)
    - Yast, Language, Detailed settings allows the same.
- gnome shell calendar, first day of the week - go to Region and Language, set Format to en_GB.
- Open With: to set the default application, Alt+Enter in file browser.

### Folders

- /home/<user>/.local/share/gnucash = gnucash data directory
- ~/.config/autostart  = autostart applications

### Gnome on Xorg or Wayland

Edit /etc/gdm/custom.conf and set Wayland on/off for the default session by enabling/disabling the line.
