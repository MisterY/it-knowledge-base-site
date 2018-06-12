# Database Server

## MariaDB

MariaDB is a fork of MySQL. It is installed with Raspbian by default.

Install with 

`sudo apt-get install mariadb-server`

Create a user using `mysql -u user -p`.

### GUI

A Web-based GUI for MariaDB administration: PHY MyAdmin.

`sudo apt-get install phpmyadmin`

To configure Apache, run `sudo nano /etc/apache2/apache2.conf` and append `Include /etc/phpmyadmin/apache.conf`. Save and restart Apache `sudo /etc/init.d/apache2 restart`.
