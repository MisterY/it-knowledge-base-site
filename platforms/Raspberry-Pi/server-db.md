# Database Server

## MariaDB

MariaDB is a fork of MySQL. It is installed with Raspbian by default.

Install with 

`sudo apt-get install mariadb-server`

Log in using `mysql -u user -p`.
Remove the default root user. Create a new user, grant all privileges. Use this user as the new root account.

### GUI

A Web-based GUI for MariaDB administration: PHY MyAdmin.

`sudo apt-get install phpmyadmin`

To configure Apache, run `sudo nano /etc/apache2/apache2.conf` and append `Include /etc/phpmyadmin/apache.conf`. 

Save and restart Apache `sudo /etc/init.d/apache2 restart` or `sudo service apache2 restart`.

Connect