#imoprting os module to create file paths across operating systems
# Module for reading CSV files
import os
import csv

#finding the path to collect data from the resource file
csvpath = os.path.join("Resources","budget_data.csv")
outputpath = os.path.join("analysis","results.txt")

#declaring variables
results=""

total_months=0
total=0

#reading csv file and specifying ',' as delimiter
with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    diff_sum = 0
    previous_value = 0

    inc_month = ""
    dec_month = ""
    lowest_month_val = 0
    highest_month_val = 0

    for idx,row in enumerate(csvreader):
      #condition to skip header
      if idx==0:
        continue

      value=int(row[1])
        
      if idx>=2:
        diff = value-previous_value
        diff_sum = diff_sum + diff
        #calculating greatest increase in values and the month
        if diff > highest_month_val:
          highest_month_val=diff
          inc_month = row[0]
        #calculating greatest decrease in values and the month
        if diff < lowest_month_val:
          lowest_month_val = diff
          dec_month = row[0]

      #calculating the total months,  and the average value change.
      total=total+value

      total_months=idx
      previous_value = value
    average_change=diff_sum/(total_months-1)

    #assigning all the results to a variable
    results = results +"Financial Analysis"+"\n"
    results = results +"----------------------------"+"\n"
    results = results +"Total Months: " +str(total_months)+"\n"
    results = results +"Total: $" +str(total)+"\n"
    results = results +"Average Change: $"+str(average_change)+"\n"
    results = results +"Greatest Increase in Profits: " +inc_month+" ("+str(highest_month_val)+")"+"\n"
    results = results +"Greatest Decrease in Profits: "+dec_month+" ("+str(lowest_month_val)+")"+"\n"

    #printing the resluts to the terminal and also exporting the results to a text file
    print(results)
    with open(outputpath,'w') as f:
        f.write(results)