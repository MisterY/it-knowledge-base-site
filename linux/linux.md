# Linux

Everything here refers mainly to OpenSuse with Gnome although the settings are similar for other linux systems.

## Tips

Here are some tips that need to be sorted:

- to disable Auto-Login: Yast - Security and Users - User/Group Management - Expert Options >Login Settings 
- Locale: 
    - in terminal, run `locale` to see the locale. `localectl` to see and modify. Use `sudo localectl set-locale LANG=en_IE.utf8`. [Ref](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)
    - Yast, Language, Detailed settings allows the same.
- Open With: to set the default application, Alt+Enter in file browser.
