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

Our code will then open the CSV file and begin to read through the data. We ask our code to loop through each row of data keep track of the following items: After the header row, count each row as an additional vote cast for the total votes count, determine which candidate the vote was cast for, check if this is a new candidate or not (if they are a new candidate add them to the list of candidates) and increase the vote count for that candidate by 1, determine which county the vote was cast from, check if this is a new county or not (if it is a new county add it to the list of counties) and increase the vote count for that county by 1. An example of this is shown below, where reader is a variable created to store information row by row of the CSV file as our code reads through it The code below demonstrates the vote total increase and the candidate vote increase. The same process is used for the county increase. 

     for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
The code is then asked to print the total number of votes cast in the election and save that number to the text file we created. 

Next, now that our code has sucessfully read through all the data in the CSV file and stored it within the variables we preset, we ask our code to run through our variables, perform some quick math for us, and compile the information into a format we can print and read. The code below demonstrates this process for the county information. The basic play-by-play is we are asking the computer to look at the data we stored from the CSV file for each different county, compare the number of votes that were cast in each county to the total number of votes to find the percentage of total votes cast from that county, provide us that information and save it in our text file, then determine if the vote for that county is the largest we have seen so far (if it is, we store the name of that county as the county with the largest voter turnout). This process is later repeated in our code for the candidates.

    for county_name in election_info:
        # 6b: Retrieve the county vote count.
        vote_count = election_info[county_name]
        # 6c: Calculate the percentage of votes for the county.
        count_percentage = float(vote_count) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {count_percentage:.1f}% ({vote_count:,})\n"
        )
        print(county_results, end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if election_info[county_name] > largest_count:
            largest_count = election_info[county_name]
            largest_turnout = county_name
            
### Use of Code in Future Elections

This code should be able to determine the results of elections for any election moving forward in the same format that this analysis provided, as long as a few certain details are heeded.
- The data we ask the code to sort through must be in a CSV file for this code to be able to read it. The data should be formatted in three columns, the first column can be anything representing the vote as unique from all others, the second column must be the county name from which the vote was cast, and the third column must be the candidate name for which the vote was cast. If the data is not in a CSV file, or it is not formatted as described, this code may need modifying in order to get the desired results.
- Even with the aforementioned considerations, this code will likely need some small adjustments to work properly with your computer and data. These involve the names of files and folders that you store your data in and want the text file to be saved to. There are three instances in the code where you may need to make changes if your folder and/or file names do not match the file and folder names we used for this project.

        # Add a variable to load a file from a path.
        file_to_load = os.path.join("Resources", "election_results.csv")
        # Add a variable to save the file to a path.
        file_to_save = os.path.join("analysis", "election_results.txt")

As previosly mentioned, the code above shows us creating a path to load the data from the CSV file named, "election_results" in a folder named, "Resources". Similarly, the last line in the clip above is creating a path to save the results from our analysis to a text file named, "election_results" in a folder named, "analysis". The file and folder names in the code must match what is on your computer, so that will need to be considered when using this code in future elections. 

Lastly, the syntax and formatting of the information this code stores in the text file and displays in the terminal can be adapted in any way the person asking for results may desire. For example, the code for the summary at the end of our analysis regarding the winning candidate looks like this:

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
The indented statements between the quotation marks can be freely edited to display the results in almost any way you would prefer. Let's take the second indented statement, which stores to our text file and prints to the terminal, "Winner: {winning_candidate}" where the name of the winning candidate will be placed where the {winning_candidate} text is. We can modify this statement to read, "The winning candidate of this election was {candidate_name}! Congratulations {winning_candidate}!" instead by adapting that line of code to look as follows:

    f"The winning candidate of this election was {winning_candidate}! Congratulations {winning_candidate}!\n"
    
This goes for any of the statements we have the code printing for us to display results, the format of what the computer tells back to us can be edited freely without breaking the code, provided it is within the quotation marks and the portions that we use to call variables are formatted correctly.

