# Software Maintenance

On OpenSuse, PackageKit takes care of system updates. This can be annoying as it downloads them on system start and can not be easily controlled by the user. Packagekitd can be killed as the root user.

### Zypper

`zypper ps -s` lists processes that need to be restarted.
`zypper packages --orphaned` shows orphaned packages.
`sudo zypper remove --clean-deps nodejs` to remove and clean-up the dependencies.

## References

- [Zypper Cookbook](https://codeghar.wordpress.com/2014/07/23/zypper-cookbook-autoremove-packages-and-remove-orphaned-packages/)

