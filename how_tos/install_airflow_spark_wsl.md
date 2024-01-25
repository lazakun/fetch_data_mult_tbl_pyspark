--install ubuntu from microsoft store
--chose a username and password
--use the following cmd commands to login back to the newly installed ubuntu os
wsl -l: This command will list all of the installed WSL distributions.
wsl -d <distribution name>: This command will start a new WSL session using the specified distribution.
-- save the following lines of code as a .sh file (for example spark_installation.sh)
#!/bin/bash
# -- use 'chmod u+x scripts/spark_installation.sh' to give spark_installation.sh executable permission

sudo apt update
sudo apt install default-jdk -y
sudo apt install curl mlocate git scala -y

curl -O https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.227/aws-java-sdk-bundle-1.12.227.jar
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar

sudo tar xvf spark-3.2.0-bin-hadoop3.2.tgz
sudo mkdir /opt/spark

sudo mv spark-3.2.0-bin-hadoop3.2/* /opt/spark
sudo mv hadoop-aws-3.3.1.jar /opt/spark/jars
sudo mv aws-java-sdk-bundle-1.12.227.jar /opt/spark/jars


sudo chmod -R 777 /opt/spark
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc 
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc

--execute this command to run the contents in the above .sh file
bash scripts/spark_installation.sh
--execute commands one by one
source ~/.bashrc
start-master.sh
--validate that spark master is up using url: http://localhost:8080/home
--get the spark master and url and port from the url above
--setup a worker (attached to the master) using this command below:
start-slave.sh spark://XXXXXXXXXXXX:7077 
--XXXXXXXXXXXX is "Lazlo." based on my spark master information (do not add the double quotation marks)



--confirm python is installed on your machine using command
python3 --version
--execute commands one by one
sudo apt-get -y install python3-pip
pip install virtualenv
--add airflow home path (AIRFLOW_HOME=/home/<username>/airflow) to bashrc file using the following commands
nano ~/.bashrc

--use ctrl+s then ctrl+x to save and exit
--for example lazlo was used as username



--install apache airflow using the following command
pip install apache-airflow
--initialize airflow database using the following command
airflow db init
NB: if you get get "command not found error", close the terminal and login to your linux wsl terminal afresh using this, rerun the command in the home directory (using cd ~)
wsl -l: This command will list all of the installed WSL distributions.
wsl -d <distribution name>: This command will start a new WSL session using the specified distribution.
cd ~
--validate airflow directory is created in your home directory



--create a user to login to aiflow with the following sample information (username:admin, first name: admin, last name: admin, role: admin, email: admin@admin.com)
airflow users create  -u admin -f admin -l admin -r Admin -e admin@admin
--you would be prompted for to create an airflow pwd for the user
--create a 'dags' folder in the airflow directory



--start the airflow web server, because spark master is using the default port 8080, start airflow web server as a daemon using an alternate port(8090)
airflow webserver --port 8090 -D
--start airflow schedular with the following command
airflow scheduler
--login to airflow using localhost:8090 and confirm access
