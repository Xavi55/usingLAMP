#!/bin/bash
#Kevin Gamez CS288 F2017
mkdir html xhtml #csv
    #loop x60
for((k=0; k<1; k++));
do
	FILENAME=`date +"%Y-%m-%e-%I-%M-%S"` #date and time
	wget http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html -O html/"$FILENAME.html"
	#printf "created file #$k\n\n"

	$(`java -jar tagsoup-1.2.1.jar --files html/"$FILENAME.html"`)
	$(mv html/*.xhtml xhtml/) #move all to another folder
	#process data
	python script.py xhtml/"$FILENAME.xhtml" #> csv/$FILENAME.csv output & write to csv file
	#sleep 60 #seconds
done
