#imoprting os module to create file paths across operating systems
# Module for reading CSV files
import os
import csv

#finding the path to collect data from the resource file
csvpath = os.path.join("Resources","election_data.csv")
outputpath = os.path.join("analysis","results.txt")

#declaring variables
results = ""

total_votes=0
winner_name=""
winner_votes=0

#reading csv file and specifying ',' as delimiter
with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    candidate_dict={}

    #to skip the header
    for idx,row in enumerate(csvreader):
      if idx==0:
        continue

      candidate_name=str(row[2])
      county=str(row[1])
    
    #using dictionary to hold the candidates' names, votes earned by each candidate and the percentage of vote earned.
      if candidate_name in candidate_dict.keys():
        candidate_dict[candidate_name]=candidate_dict[candidate_name]+1
      else:
        candidate_dict[candidate_name]=1

    #calculating total votes using sum function.
    total_votes=sum(candidate_dict.values())
    #assigning all the results to a variable
    results = results + "Election Results" + "\n"
    results = results + "-------------------------" + "\n"
    results = results + "Total Votes: "+str(total_votes) + "\n"
    results = results + "-------------------------" + "\n"

    #calculating the percentage of votes earned by each candidate
    for candidate,votes in candidate_dict.items():
      vote_percent=(votes/total_votes)*100
      results = results + candidate+": "+str(round(vote_percent,3))+"% ("+str(votes)+")" + "\n"
    
    #if condition to findthe candidate with most votes
      if votes>winner_votes:
        winner_votes=votes
        winner_name=candidate

    results = results + "-------------------------"+"\n"
    results = results + "Winner: "+winner_name+"\n"
    results = results + "-------------------------"+"\n"
#printing the resluts to the terminal and also exporting the results to a text file
    print(results)
    with open(outputpath,'w') as f:
        f.write(results)