# Maintenance

Once the RPi has been set up, there are a few things that can be done to keep it running smoothly.

## Monitoring

### Logs

System messages can be seen with `cat /var/log/messages` or `dmesg`.

`systemctl status hdparm.service` and `journalctl -xe`.

## Actions

### Updates

- apt-get update
- apt-get upgrade

List available updates with `sudo apt list --upgradable`.

`sudo rpi-update` will install the very latest system, before it has reached apt-get.

Links

- [apt-get how-to ](https://help.ubuntu.com/community/AptGet/Howto)
- [rpi-update](https://github.com/Hexxeh/rpi-update)
