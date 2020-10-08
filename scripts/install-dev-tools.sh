#!/bin/bash
 
# update package manager
sudo apt-get update
# install node js
sudo apt-get -y install nodejs npm
# install sqlite3 to use the dbshell
sudo apt-get -y install sqlite3 libsqlite3-dev
# install the dev python requiremnts
pip install --user -r requirements/dev.txt