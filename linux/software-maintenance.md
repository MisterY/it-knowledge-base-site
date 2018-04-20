# Software Maintenance

On OpenSuse, PackageKit takes care of system updates. This can be annoying as it downloads them on system start and can not be easily controlled by the user. Packagekitd can be killed as the root user.

### Zypper

`zypper ps -s` lists processes that need to be restarted.

