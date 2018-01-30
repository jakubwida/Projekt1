#!/bin/bash

get_top_5()
{
output=`head -5 temp.txt`
echo $output
}


scores_to_tempfile_last_day()
{
[ -e temp.txt ] && rm temp.txt
now=`date +'%-Y:%-m:%-d'`
		awk '$3 == "'$now'"' result_base.txt >> temp.txt
}

#scores_to_tempfile_last_day

scores_to_tempfile_last_7d()
{
[ -e temp.txt ] && rm temp.txt
END=7
for ((i=0;i<=END;i++)); do
    dated=`date --date="$i day ago" +'%-Y:%-m:%-d'`
		awk '$3 == "'$dated'"' result_base.txt >> temp.txt
done
}

scores_to_tempfile_last_30d()
{
[ -e temp.txt ] && rm temp.txt
END=30
for ((i=0;i<=END;i++)); do
		#echo "$i"
    dated=`date --date="-$i day" +'%-Y:%-m:%-d'`
		awk '$3 == "'$dated'"' result_base.txt >> temp.txt
done
}

scores_to_tempfile_all_time()
{
[ -e temp.txt ] && rm temp.txt
cp result_base.txt temp.txt
}

#scores_to_tempfile_all_time
#scores_to_tempfile_last_30d

# $1 = username
scores_by_user_to_tempfile()
{
[ -e temp.txt ] && rm temp.txt
	awk '$1 == "'$1'"' result_base.txt >> temp.txt
}
#scores_by_user_to_tempfile "username3"

# $1= string containing entire username score date
this_score_position_in_temp()
{
out=`grep -Fn "$1" temp.txt | cut -c 1`
echo $out
}
#echo `this_score_position_in_temp "username 5 2018:1:29"`

#$1 = request_string $2 = request_value
on_request()
{
if [ $1 = 'top_all' ]
then
	scores_to_tempfile_all_time
	echo `get_top_5`
fi
#if [ $1 = "tom_month" ]
#then
#	scores_to_tempfile_last_30d
#	echo `get_top_5`
#fi
if [ $1 = "top_week" ]
then
	scores_to_tempfile_last_7d
	echo `get_top_5`
fi
if [ $1 = "top_day" ]
then
	scores_to_tempfile_last_day
	echo `get_top_5`
fi

if [ $1 = "top_by_user" ]
then
	scores_by_user_to_tempfile $2
	echo `get_top_5`
fi

if [ $1 = "send" ]
then
	echo "$2 $3 $4" >> result_base.txt
	awk '!a[$0]++' result_base.txt > temp.txt #possible removal errors while adding
	cat temp.txt > result_base.txt
	scores_to_tempfile_all_time
	num=`this_score_position_in_temp "$2 $3 $4"`
	echo "all-time position: $num"
fi
}

#echo `on_request passed "username2 1 2018:1:7"`


check_receptor()
{
if [ -s receptor ]
then
	echo "henlo!"
	echo `cat receptor`
	a=`cat receptor  | head -n1 | cut -d " " -f1`
	b=`cat receptor | awk '{print $2}'`
	c=`cat receptor | awk '{$1=""; $2=""; print }'`
	#echo "$a       $b       $c"
	response=`on_request $b $c`
	echo $response
	echo $response | nc $a 1235

	: > receptor
fi
}

run_server()
{
while true
do
	nc -l -p 1234 > receptor
	check_receptor
done
}





while getopts "h" opt; do
  case $opt in
    h)
      #echo "-a was triggered, Parameter: $OPTARG" >&2
			echo "This is a server. It must be run before the client. It features no options, as port is fixed - those are 1234 and 1235."
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

run_server


#TODO
#CLIENT
#some basic read based interface
#printing responses from server <breaking lines after 3 words>
#client_prototype has some valuable code about connection
