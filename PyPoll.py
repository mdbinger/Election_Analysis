# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Add the total vote counter
total_votes = 0

#Candidate options
candidate_options = []

#Create a dictionary to hold candidate names and votes
candidate_votes = {}

#Create an empty string to hold the value of the winning candidate, and variables to help determine the winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Print the header row
    headers = next(file_reader)

    #Print each row inthe CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list if it has not already been added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

#Use a for loop to iterate through the candidate_options list
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
#print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
#Use the open statement to open the file as a text file
# with open(file_to_save, "w") as txt_file