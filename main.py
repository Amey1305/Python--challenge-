import os
import csv

#set path to open the csv file
election = os.path.join("election_data.csv")
final_analysis = os.path.join("election_analysis.txt")


# Read the CSV file and initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""
percent_votes= 0
# Read the CSV file
with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    # Process each row in the CSV file
    for row in csv_reader:
        # Count the total number of votes
        total_votes += 1

        # Extract the candidate name from the row
        candidate = row[2]

        # Update the candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Check if the current candidate is the new winner
        if candidates[candidate] > winner_votes:
            winner_votes = candidates[candidate]
            winner = candidate


# Calculate the percentage of votes each candidate won
percent_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percent = percent_votes[candidate]
    print(f"{candidate}: {percent:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#write election result in txt 
with open("election_analysis.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percent = percent_votes[candidate]
        txt_file.write(f"{candidate}: {percent:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")
