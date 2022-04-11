
# The data we need to retrieve
# 1. The total number of voters cast
# 2. A compete list of candidates whp receive vote
# 3. The percentage of votes each candidate won
# 4. Teh total number of votes each candidate won
# 5. The winned of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# County options and county votes.
county_options = []
county_votes = {}
# Track the largest county by votes, vote count, and percentage.
largest_county = ""
county_count = 0
county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county, add the
        # the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that counties voter count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            largest_county = county
            county_percentage = vote_percentage
    # Print the winning county results to the terminal.
    winning_county_summary = (
        
        f"-------------------------\n"
        f"\nLargest County Turnout: {largest_county}\n"
        f"\n-------------------------\n")
    print(winning_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)