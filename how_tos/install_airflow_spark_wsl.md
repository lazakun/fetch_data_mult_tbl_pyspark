- install ubuntu from microsoft store
- chose a username and password
- use the following cmd commands to login back to the newly installed ubuntu os
  wsl -l: This command will list all of the installed WSL distributions.
  wsl -d <distribution name>: This command will start a new WSL session using the specified distribution.
- execute this command to run the contents in the above .sh file
bash scripts/spark_installation.sh
- execute commands one by one
source ~/.bashrc
start-master.sh
- validate that spark master is up using url: http://localhost:8080/home
- get the spark master and url and port from the url above
- setup a worker (attached to the master) using this command below:
start-slave.sh spark://XXXXXXXXXXXX:7077 
--XXXXXXXXXXXX is "Lazlo." based on my spark master information (do not add the double quotation marks)

![a](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/d264e1ba-5771-44cd-89a1-cc03974e1388)


- confirm python is installed on your machine using command
python3 --version
- execute commands one by one
sudo apt-get -y install python3-pip
pip install virtualenv
- add airflow home path (AIRFLOW_HOME=/home/<username>/airflow) to bashrc file using the following commands
nano ~/.bashrc

![b](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/6c96d187-f7e3-46a2-907c-68784d26b495)

- use ctrl+s then ctrl+x to save and exit
- for example lazlo was used as username

![c](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/3f99fcb4-4831-41f0-9ca8-056ca7e42bc6)

- install apache airflow using the following command
pip install apache-airflow
- initialize airflow database using the following command
airflow db init
NB: if you get get "command not found error", close the terminal and login to your linux wsl terminal afresh using this, rerun the command in the home directory (using cd ~)
wsl -l: This command will list all of the installed WSL distributions.
wsl -d <distribution name>: This command will start a new WSL session using the specified distribution.
cd ~
- validate airflow directory is created in your home directory

![d](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/3105240e-31e3-4c41-a0da-46b300720139)

- create a user to login to aiflow with the following sample information (username:admin, first name: admin, last name: admin, role: admin, email: admin@admin.com)
airflow users create  -u admin -f admin -l admin -r Admin -e admin@admin
- you would be prompted for to create an airflow pwd for the user
- create a 'dags' folder in the airflow directory

![e](https://github.com/lazakun/fetch_data_mult_tbl_pyspark/assets/100403369/57c1d8e1-fba8-4ae7-ad79-f33e62dda00c)

- start the airflow web server, because spark master is using the default port 8080, start airflow web server as a daemon using an alternate port(8090)
airflow webserver --port 8090 -D
- start airflow schedular with the following command
airflow scheduler
- login to airflow using localhost:8090 and confirm access
