# Linux

Everything here refers mainly to OpenSuse with Gnome although the settings are similar for other linux systems.

- [Applications](applications)
- [AppImage](appimage)
- [Keyboard](keyboard)
- [Software](software)
- [Themes](themes)

## Tips

Here are some tips that need to be sorted:

- to set Auto-Login: Yast - Security and Users - User/Group Management - Expert Options >Login Settings 
- Locale: 
    - in terminal, run `locale` to see the locale. `localectl` to see and modify. Use `sudo localectl set-locale LANG=en_IE.utf8`. [Ref](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)
    - Yast, Language, Detailed settings allows the same.
- Open With: to set the default application, Alt+Enter in file browser.

### Folders

- /home/<user>/.local/share/gnucash = gnucash data directory
- ~/.config/autostart  = autostart applications

### Gnome on Xorg or Wayland

Edit /etc/gdm/custom.conf and set Wayland on/off for the default session by enabling/disabling the line.

### Grub Boot

Boot can be in MBR or UEFI mode.
UEFI partition is vfat, 500MB, mounted at /boot/efi as recommended by openSuse installer.

### Recovery

To mount a drive from rescue USB, see [here](https://doc.opensuse.org/documentation/leap/startup/html/book.opensuse.startup/cha.trouble.html#sec.trouble.data.recover.rescue).

Also see [this](https://www.pks.mpg.de/~mueller/docs/suse10.2/html/opensuse-manual_en/manual/sec.trouble.boot.html) for boot troubleshooting.
