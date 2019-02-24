# PurpleAmerica

Jonathan Carraso-Noriega
This code will map out the United States by using coordinates in CSV format.
It has the form COUNTY,STATE,LONG1,LAT1,LONG2,LAT2,...,LONGN,LATN
where each successive pair of LONG,LAT values form a point on the polygon defin\
ing a particular region.
The election data is also in CSV format and has the form
COUNTY,STATE,REPUBLICAN_VOTES,DEMOCRATIC_VOTES,OTHER_VOTES.

This project then uses this data to map out the United States and creates a list of regions.
From this, it extracts the minimum and maximum longitude and latitude and begins to draw each region
using my Plot instance, filling in the region a ratio of blue for democratic voters, red for republican
voters, or green if another party was voted for.

To run this code, you will need to have installed the pillows imaging library first and then type in
$ python3 election.py election-data/results/US2012.csv election-data/boundaries\/US.csv output.png 1024 GRAD
on the command line!
