import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
outputpath = os.path.join("analysis","results.txt")

results=""

total_months=0
total=0

with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    diff_sum = 0
    previous_value = 0

    inc_month = ""
    dec_month = ""
    lowest_month_val = 0
    highest_month_val = 0

    for idx,row in enumerate(csvreader):
      if idx==0:
        continue

      value=int(row[1])
        
      if idx>=2:
        diff = value-previous_value
        diff_sum = diff_sum + diff

        if diff > highest_month_val:
          highest_month_val=diff
          inc_month = row[0]

        if diff < lowest_month_val:
          lowest_month_val = diff
          dec_month = row[0]

      total=total+value

      total_months=idx
      previous_value = value
    average_change=diff_sum/(total_months-1)

    results = results +"Financial Analysis"+"\n"
    results = results +"----------------------------"+"\n"
    results = results +"Total Months: " +str(total_months)+"\n"
    results = results +"Total: $" +str(total)+"\n"
    results = results +"Average Change: $"+str(average_change)+"\n"
    results = results +"Greatest Increase in Profits: " +inc_month+" ("+str(highest_month_val)+")"+"\n"
    results = results +"Greatest Decrease in Profits: "+dec_month+" ("+str(lowest_month_val)+")"+"\n"

    print(results)
    with open(outputpath,'w') as f:
        f.write(results)