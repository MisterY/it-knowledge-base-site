# Themes

- [Themes](#themes)
    - [Settings](#settings)
        - [Controls](#controls)
        - [Cursors](#cursors)
        - [Desktop](#desktop)
        - [Fonts](#fonts)
        - [Icons](#icons)
        - [Window Borders](#window-borders)
    - [Customizing](#customizing)
        - [Theme](#theme)

Sources:
- [Open Desktop](https://www.opendesktop.org/)

## Settings

### Controls

- Sierra Dark
- Adwaita Dark

This changes the toolbar buttons and other controls only in GTK apps.

Both `gtk-2.0` and `gtk-3.0` directories must be present for this.

### Cursors

- capitaine-cursors

Unpack and add to `/usr/share/icons` as root.

### Desktop

- Numix Cinnamon Transparent
- macOS High Sierra

This affects only the Desktop setting.

GTK Theme goes into `gtk-3.0` sub-directory.
Cinnamon theme goes into `cinnamon` directory.

### Fonts

Create `/usr/share/fonts/truetype/`.
Copy font files to new location.
Update your font cache: `sudo fc-cache -fv`.

### Icons

- Mist

Unpack and add to `/usr/share/icons` as root.

### Window Borders

- BiSOFT-GTK3

This affects only the toolbar buttons and the window border on non-GTK apps.

`metacity-1` directory.

## Customizing 

GTK titlebar buttons (.titlebutton) have the CSS classes .minimize, .maximize, and .close.

GTK Inspector can be used to identify UI elements. To enable, run `gsettings set org.gtk.Settings.Debug enable-inspector-keybinding true`. Then press Ctrl+Shift+D or +I to activate.

Non-GTK applications get the window border and titlebar from the Window Border setting.

To reload the list of themes, rename the theme directory.

### Theme

Custom themes are in `~/.themes/` directory. Create a sub-directory with the theme's name.
