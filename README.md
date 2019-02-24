# PurpleAmerica

This program displays the United States by creating a list of regions and fills in each region with a ratio of blue for democratic voters, ratio of red for republican voters, or ratio of green if another party was voted for. It draws these regions by using coordinates in CSV format of the form

COUNTY,STATE,LONG1,LAT1,LONG2,LAT2,...,LONGN,LATN

where each successive pair of LONG,LAT values form a point on the polygon defining a particular region.
The election data comes from a CSV format of the form

COUNTY,STATE,REPUBLICAN_VOTES,DEMOCRATIC_VOTES,OTHER_VOTES.

To run this code, you will need to have installed the pillows imaging library first and then type in
```
python3 election.py election-data/results/US2012.csv election-data/boundaries\/US.csv output.png 1024 GRAD
```
on the command line!
