#import modules 
import csv
import os

#path to csv
election_csv = os.path.join("./Resources/election_data.csv")

total_votes = 0 
votes_khan = 0 
votes_correy = 0 
votes_li = 0 
votes_otooley = 0 

#read csv
with open(election_csv, newline='') as votes_csv:

    #specify delimiter & variable 
    csvreader = csv.reader(votes_csv, delimiter=',')

    #read and skip header 
    header=next(votes_csv)

    #read ea. row after header
    for row in csvreader: 

        #calculate total votes
        total_votes += 1

        #calculate ea. candidate votes 
        if (row[2] == "Khan"): 
            votes_khan += 1
        elif (row[2] == "Correy"):
            votes_correy += 1
        elif (row[2] == "Li"): 
            votes_li += 1 
        else: 
            votes_otooley += 1 
        
    #calculate ea. candidate vote percentages 
    p_khan = votes_khan / total_votes
    p_correy = votes_correy / total_votes
    p_li = votes_li / total_votes
    p_otooley = votes_otooley / total_votes

    #calculate election winner
    election_winner = max(votes_khan, votes_correy, votes_li, votes_correy)

    if election_winner == votes_khan:
        winner_is = "Khan"
    elif election_winner == votes_correy:
        winner_is = "Correy"
    elif election_winner == votes_li:
        winner_is = "Li"
    else: 
        winner_is = "O'Tooley"

#print values
print("Election Results")
print("----------------------")
print("Total Votes: " + str(total_votes))
print("----------------------")
print(f"Khan: {p_khan:.3%} ({votes_khan})")
print(f"Correy: {p_correy:.3%} ({votes_correy})")
print(f"Li: {p_li:.3%} ({votes_li})")
print(f"O'Tooley: {p_otooley:.3%} ({votes_otooley})")
print("----------------------")
print("Winner: " +str(winner_is))
print("----------------------")

#txt file 
PyPoll = open("./Analysis/election_results.txt", "w+")
PyPoll.write("Election Results")
PyPoll.write('\n' "----------------------")
PyPoll.write('\n' + "Total Votes: " + str(total_votes))
PyPoll.write('\n' + "----------------------")
PyPoll.write('\n' + (f"Khan: {p_khan:.3%} ({votes_khan}"))
PyPoll.write('\n' + (f"Correy: {p_correy:.3%} ({votes_correy}"))
PyPoll.write('\n' + (f"Li: {p_li:.3%} ({votes_li}"))
PyPoll.write('\n' + (f"O'Tooley: {p_otooley:.3%} ({votes_otooley}"))
PyPoll.write('\n' "----------------------")
PyPoll.write('\n' + "Winner: " + str(winner_is))
PyPoll.write('\n' "----------------------")