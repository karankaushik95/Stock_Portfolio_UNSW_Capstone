# capstone-project-byte_me
capstone-project-byte_me created by GitHub Classroom

NOTE: YOU MUST USE EITHER LINUX OR MAC OSX

First, clone the Github repository to your local machine. Then, open the script named “sqlite3_setup”, and uncomment the line for your operating system. 

Once you have uncommented the relevant line, save the script, and exit. In the root project directory, run the script with the command

./sqlite3_setup

This script will download the software required for SQLite to manage the database. It will create a folder to store all the requisite software tools. Then, move to the directory ‘db’ and run the file ‘user_setup.py’ to set up the databases for users.

cd db

python3  user_setup.py

Come back to the top directory ‘/capstone-project-byte_me’ and run the script ‘runlocal’.

cd ../

./runlocal

This step helps you complete all the environment configuration and run the software, including installing dependencies, setting environment variables, running flask etc.  If a similar response appears on your terminal, the software's server is running successfully.

If you want to terminate the server, press control and C simultaneously in the terminal.

Next, open your browser and go to http://127.0.0.1:5000/index.html and you will be taken to the homepage of our web application. 
