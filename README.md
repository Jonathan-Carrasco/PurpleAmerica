# PurpleAmerica

This code will map out the United States by using coordinates in CSV format of the form
COUNTY,STATE,LONG1,LAT1,LONG2,LAT2,...,LONGN,LATN

where each successive pair of LONG,LAT values form a point on the polygon defining a particular region.
It also uses election data in CSV format of the form

COUNTY,STATE,REPUBLICAN_VOTES,DEMOCRATIC_VOTES,OTHER_VOTES.

Given these files, I map out the United States and create a list of regions in order to extract the minimum and maximum longitude and latitude and draw each region, filling in the region with blue for democratic voters, red for republican
voters, or green if another party was voted for.

To run this code, you will need to have installed the pillows imaging library first and then type in
```
python3 election.py election-data/results/US2012.csv election-data/boundaries\/US.csv output.png 1024 GRAD
```
on the command line!
