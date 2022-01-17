# Election Analysis Challenge

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Calculate the total number of votes and percentage of votes from each county.
6. Determine which county had the highest turnout.
7. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, Visual Studio Code, 1.63.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The counties participating in the election and their voter turnout were:
    - Jefferson County had 38,855 votes, 10.5% of the total votes.
    - Denver County had 306,055 votes, 82.8% of the total votes.
    - Arapahoe County had 24,801 votes, 6.7% of the total votes.
    - Denver County had the largest number of votes 
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was: 
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Challenge Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

The results of this election were analyzed by using a script of code in Python and run through Visual Studio Code. The code takes in the raw data we recieved from the Colorado Board of Elections via a CSV file. The CSV file contained data on every vote cast, inlcuding the ballot ID, the county from which the vote was cast, and the candidate the vote was casted for. We then created a blank text file to have the code write the results of the analysis to so that we can save the results of the analysis and access them without having to run the code every time we need them.

Before the code reads the data from the CSV file provided, we initialize a handful of variables to store information we recieve from the CSV file in order to perform analysis on that information without editing or deleting any information from the CSV file. These variables can be seen below, and they are all set to be empty or equal to 0 until the code assigns them values from the CSV file. 

total_votes = 0
candidate_options = []
candidate_votes = {}
counties_list = []
election_info = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_turnout = ""
largest_count = 0

