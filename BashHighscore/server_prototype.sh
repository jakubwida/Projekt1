#!/bin/bash

checko()
{
if [ -s receptor ]
then
	echo "henlo!"
	echo `cat receptor`
	: > receptor
fi
}



while true
do
	nc -l -p 1234 > receptor
	echo "?"
	checko
done
