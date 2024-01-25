Edit the PostgreSQL configuration file
- Open the PostgreSQL installation directory and locate the postgresql.conf file. By default, the configuration file for PostgreSQL (version 14) is located at C:\Program Files\PostgreSQL\14\data\postgresql.conf.
- Make a backup of the file before making any changes.
- Open the postgresql.conf file in a text editor.
- Find the line that reads #listen_addresses = 'localhost' and uncomment it if it is commented (remove the ‘#’ character at the beginning of the line). Next, to ensure that PostgreSQL is configured to accept connections from any address, check the value of “listen_addresses” – it should be set to “*”.
- Edit the pg_hba.conf file to allow remote connections
- Open the PostgreSQL installation directory and locate the pg_hba.conf file. By default, it is located at C:\Program Files\PostgreSQL\14\data\pg_hba.conf (for PostgreSQL 14).
- Make a backup of the file before making any changes.
- Open the pg_hba.conf file in a text editor.
- Add a new line at the end of the file to allow remote connections. The line should have the following format:

host all all 0.0.0.0/0 md5

Create PostgreSQL admin User
- under PostgreSQL server, right click and select Create - Login/Group Role
- set username, under privileges, select admin privileges

![image](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/b48dd0fc-2ffc-4027-b033-42e4393d146a)

![image](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/82b8a2d6-d8f9-4d68-85c6-ef19bc145c9c)

