Using Linux , Apache, mySQL*, and PHP ... (LAMP)

*but with postgreSQL

LINUX SETUP:
* install virtualenv AND/OR use : `source env/bin/activate`
    OR install the 'psycopg2' Python module 
    
* get PostgreSQL or mySQL/mysqlite and edit both the Python / PHP scripts accordingly
* install apache2, configure it to recognize PHP files with: 
    `sudo nano /etc/apache2/mods-enabled/dir.conf`
    add 'index.php' to the DirectoryIndex line
    `sudo system ctl restart apache2 && systemctl status apache2`
*place the PHP script in var/www/html/

------

* run command to make executable ...`chmod +X script.sh`
* execute the script.sh to gather stock HTML data with ... `./script.sh`
    * within there's a python script, reading XML, and injecting data into the DB