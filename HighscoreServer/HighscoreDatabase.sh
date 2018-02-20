#!/usr/bin/env bash

DATABASE="result_base.txt"
TEMP="temp.txt"

if [ "$1" = "-h" ]
	then
	echo "This script serves as a database manager for GameLauncher highscores."
	echo "This script is ment to be run through a Python 'GameLauncher.py' script, not seperately. It will now terminate."
	exit
	fi



# format insertu:
# name score
# data jest dodwawana tutaj, nie w pythonie
function insert
	{
	name=$1
	score=$2
	date=`date '+%Y-%m-%d %H:%M:%S'`
	echo "$name $score $date" >> $DATABASE
	sort -u -t" " -k1,1 -k2,2 $DATABASE > $TEMP
	cp $TEMP $DATABASE
	rm $TEMP
	}

#insert "hello" "5"


# $1= top/bottom $2=month/week/all/day, $3 = user - not forced
function get
	{

	}
