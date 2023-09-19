## 0x14-mysql

**0. Install MySQL** >> Installing MySQL (a 5.7.x distribution) on both `web-01` and `web-02` servers.

**1. Let us in!** >> Creating a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`; to be able to access the replication status on both servers. User `holberton_user` has permission to check the primary/ replica status of the databases.

**2. If only you could see what I've seen with your eyes** >> Creating a database called `tyrell_corp`, within which a table named `nexus6` is created and at least one entry added. The user `holberton_user` has `SELECT` permissions on the table to check that the table exists and is not empty.

**3. Quite an experience to live in fear, isn't it?** >> Creating a new user `replica_user` with the host name set to `%`, with the appropriate permissions to replicate the primary MySQL server. User `holberton_user` is given SELECT privileges on the `mysql.user` table in order to check that `replica_user` is created with the correct permissions.

**4. Setup a Primary-Replica infrastructure using MySQL** `[4-mysql_configuration_primary, 4-mysql_configuration_replica]` >> MySQL primary is hosted on `web-01` (not using the `bind-address`) and MySQL replica is hosted on `web-02`. Replcation for a MySQL database named `tyrell_corp` is also setup.

**5. MySQL backup** `[5-mysql_backup]` >> Bash script that generates a MySQL dump and creates a compressed archive out of it. The MySQL dump is named `backup.sql` and contains all the MySQL databases. It is compressed to a `tar.gz` archive named in the format `day-month-year.tar.gz`. The bash script accepts only one argument, which is the password used to connect to the MySQL database.
