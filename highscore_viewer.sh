#!/bin/bash

ip="127.0.0.1"
myip=`hostname -I`

while getopts "hi:" opt; do
  case $opt in
    h)
      #echo "-a was triggered, Parameter: $OPTARG" >&2
			echo "This is a client-viewer. The server must be available at port 1234, and 1235 must be clear for communication. Follow the on-screen prompts for instrucitons."
			echo "OPTIONS"
			echo "-h: it displays this text."
			echo "-i: <optional> IP - requires parameter IP which must be a valid ip address. This address is the server target"
			echo "  default: localhost"
      exit 0
      ;;
    i)
			ipp=$OPTARG;
			if [[ ! $ipp =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
      	echo "$ipp is not valid IP address" >&2
		  	exit 1
			else
				ip=$ipp
			fi
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

#untested
# $1= input for server, echoes response
send_and_print_response_from_server()
{
#echo "$myip $1"
echo -n "$myip $1" | nc -w1 $ip 1234
out=` nc -l -w1 -p 1235`
#echo `echo $out | awk '{print $1,$2,$3,"\n"}'`
#echo "kurka!"
#echo `echo $out | awk '{print $4,$5,$6,"\n"}'`
#echo `echo $out | awk '{print $7,$8,$9}'`
#echo `echo $out | awk '{print $10,$11,$12}'`
#echo `echo $out | awk '{print $13,$14,$15}'`
out=`printf "$out" | xargs -n3`
printf "$out \n \n"
}





while true
do
echo "HIGHSCORE VIEWER:"
echo "TO SEE TOP RESULTS FROM LAST DAY or WEEK, WRITE top_day, top_week OR top_all FOR ALL TIME"
echo "TO SEE GIVEN USERS TOP RESULTS, WRITE top_by_user [username], USERNAME CANNOT HAVE SPACES"
echo "TO INSERT YOUR RESULTS, WRITE send [username]"
echo "TO END, WRITE exit"
echo "ANY OTHER COMMANDS WILL BE IGNORED"
read intr1 instr2

if [ $intr1 = "send" ] && [ -n $instr2 ]
then
	addo=`cat current_highscore.txt`
	echo $addo
	if [ -n "$addo" ]
		then
		message="$instr2 $addo"
		send_and_print_response_from_server "$intr1 $message"
		else
		echo "no current highscore exists!"
		fi
fi

if [ $intr1 = "top_day" ]
then
	send_and_print_response_from_server "$intr1 $instr2"
fi

if [ $intr1 = "top_by_user" ]
then
	send_and_print_response_from_server "$intr1 $instr2"
fi

if [ $intr1 = "top_week" ]
then
	send_and_print_response_from_server "$intr1 $instr2"
fi

if [ $intr1 = "top_month" ] #this is broken
then
	send_and_print_response_from_server "$intr1 $instr2"
fi

if [ $intr1 = "top_all" ]
then
	send_and_print_response_from_server "$intr1 $instr2"
fi

if [ $intr1 = "exit" ]
then
	exit 0
fi
#if block for interpreting commands
done


#TODO
#passing - needs to read from local highscore and pass it to the server
#this is the only untested bit right now.
