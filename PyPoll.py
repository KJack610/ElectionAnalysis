# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote.
# Assign a variable for the file to looad and the path.
#file_to_load = 'Resources/election_results.csv'
# open the election results and read the file.
#election_data = open(file_to_load, 'r')
# to do: perform analysis
#close the file 
#election_data.close()
#open the election results and read the file
#with open(file_to_load, "r") as election_data:
#print the file object
#print(election_data)
#Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis1.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#assign a variable to save the file to a path
#file_to_save = os.path.join("Analysis", "election_analysis1.txt")
#Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as outfile:
# Write some data to the file.
   #outfile.write( "Hello World")
   #outfile.close()
#using the with statemnt open the file as a text file.
#with open(file_to_save, "w") as txt_file:
   #txt_file.write("Hello World")
#Write three countries to the file.Newline escapres sequence to the end of the first two county names so that the code looks like this:
   #txt_file.write("\nArapahoe\nDenver\nJefferson")
#open the election results and read the file
 #To do: read and analyze the data here.m#Read the file object with the reader function
import csv
import os
file_to_load = 'Resources/election_results.csv'
file_to_save = os.path.join("Analysis", "election_analysis1.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load, "r") as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   for row in file_reader:
      total_votes =+ 1
      candidate_name = row[2]
      if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] =+ 1
with open(file_to_save, "w") as txt_file:
      election_results = (
         f"\nElection Results\n"
         f"------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"------------------\n")
      print(election_results, end ="")
      txt_file.write(election_results)
      for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/ float(total_votes) * 100
            candidate_results = (
                  f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            if (votes > winning_count) and (vote_percentage > winning_percentage):
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name
            winning_candidate_summary = (
               f"-----------------------------\n"
               f"Winner: {winning_candidate}\n" 
               f"Winning Vote COunt: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"-----------------------------\n" )
            print(winning_candidate_summary)
            txt_file.write(winning_candidate_summary)
