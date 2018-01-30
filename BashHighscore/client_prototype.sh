#!/bin/bash

echo -n '127.0.0.1  top_all bbb' | nc 127.0.0.1 1234
out=`nc -l -p 1235`
echo $out
