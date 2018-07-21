# Software Maintenance

On OpenSuse, PackageKit takes care of system updates. This can be annoying as it downloads them on system start and can not be easily controlled by the user. Packagekitd can be killed as the root user.

## Preferred Applications

Run the app with the same name and set the defaults, i.e. file manager, browser, etc.

## Updates

To prevent PackageKit automatically downloading all the update packages, run
`gsettings set org.gnome.software download-updates false`
also, disable PackageKit service
```
systemctl stop packagekit
systemctl disable packagekit
```
or remove it completely.

Install updates with `zypper up` or `zypper dup`.

Resources: 
- [Thread](https://forums.opensuse.org/showthread.php/530069-Tumbleweed-waiting-for-shared-lock-on-var-lib-rpm-Packages)
- [Fedora](https://ask.fedoraproject.org/en/question/10929/how-do-i-stop-package-kit-from-constantly-searching-for-updates/)

### Zypper

`zypper ps -s` lists processes that need to be restarted.
`zypper packages --orphaned` shows orphaned packages.
`sudo zypper remove --clean-deps nodejs` to remove and clean-up the dependencies.

References:

- [Zypper Cookbook](https://codeghar.wordpress.com/2014/07/23/zypper-cookbook-autoremove-packages-and-remove-orphaned-packages/)
