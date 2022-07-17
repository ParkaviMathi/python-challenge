import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
outputpath = os.path.join("analysis","results.txt")

results = ""

total_votes=0
winner_name=""
winner_votes=0

with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    candidate_dict={}

    for idx,row in enumerate(csvreader):
      if idx==0:
        continue

      candidate_name=str(row[2])
      county=str(row[1])

      if candidate_name in candidate_dict.keys():
        candidate_dict[candidate_name]=candidate_dict[candidate_name]+1
      else:
        candidate_dict[candidate_name]=1

    total_votes=sum(candidate_dict.values())
    results = results + "Election Results" + "\n"
    results = results + "-------------------------" + "\n"
    results = results + "Total Votes: "+str(total_votes) + "\n"
    results = results + "-------------------------" + "\n"


    for candidate,votes in candidate_dict.items():
      vote_percent=(votes/total_votes)*100
      results = results + candidate+": "+str(round(vote_percent,3))+"% ("+str(votes)+")" + "\n"

      if votes>winner_votes:
        winner_votes=votes
        winner_name=candidate

    results = results + "-------------------------"+"\n"
    results = results + "Winner: "+winner_name+"\n"
    results = results + "-------------------------"+"\n"

    print(results)
    with open(outputpath,'w') as f:
        f.write(results)