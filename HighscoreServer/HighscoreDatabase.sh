#!/usr/bin/env bash

DATABASE="result_base.txt"
TEMP="temp.txt"

# $1= name, $2 = score
# data is added here, not in python
function insert
	{
	name=$1
	score=$2
	date=`date '+%Y-%m-%d %H:%M:%S'`
	echo "$name $score $date" >> $DATABASE
	tempo=`sort -u -t" " -k1,1 -k2,2 $DATABASE`
	echo "$tempo" > $DATABASE
	}
#insert "hello" "15"

# $1= top/bottom $2=month/week/all/day $3= username (optional)
function get
	{
	#time:
	if [ $2 = "week" ]
		then
			startdate=`date --date='-1 week' +'%Y-%m-%d %H:%M:%S'`
	elif [ $2 = "month" ]
		then
			startdate=`date --date='-1 month' +'%Y-%m-%d %H:%M:%S'`
	elif [ $2 = "day" ]
		then
			startdate=`date --date='-1 day' +'%Y-%m-%d %H:%M:%S'`
		else
			startdate='0000-00-00 00:00:00'
		fi

	currdate=`date '+%Y-%m-%d %H:%M:%S'`
	first=`awk '{a=$3" "$4; if (a > '"\"$startdate\""' ) print;}' result_base.txt`

	if [ $1 = "top" ]
		then
			second=`echo "$first" | sort -t" " -k1,1 -k2,2 -k3,3`
		else
			second=`echo "$first" | sort -r -t" " -k1,1 -k2,2 -k3,3`
		fi

	if [ -n "$3" ]
		then
			#echo "hello there: $3"
			second=`echo "$second" | awk ' $1 =='"\"$3\""' {print}'`
		fi
	echo "$second" | head
	}
#get "top" "week"


if [ "$1" = "-h" ]
	then
	echo "This script serves as a database manager for GameLauncher highscores."
	echo "This script is ment to be run through a Python 'GameLauncher.py' script, not seperately. It will now terminate."
	exit
elif [ "$1" = "insert" ]
	then
		insert "$2" "$3"
elif [ "$1" = "get" ]
	then
		get "$2" "$3" "$4"
fi
