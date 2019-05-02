#!/bin/bash
# THIS IS JUST AN EXAMPLE SCRIPT: MODIFY TO YOUR NEEDS!

JOURNAL=~/journal.json /home/olof/prj/github/JJ/main.py $1

if [[ $# -eq 0 ]] ; then
	echo Syncing...
	cd ~/prj/bitbucket/journal
	git pull
	git add .
	git commit -m 'autocommit'
	git push
