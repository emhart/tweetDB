#!/usr/bin/bash


echo "Setting-up your tweet bot"
echo "Checking if DB exists"

if [ -f "$1" ]
  then
    echo "Great your database already exists"
  else
    echo "Creating your database"
    python createDB.py "$1"
fi

echo "Grabbing your search results"

python addData.py "$1" "$2"

echo "Finished"
