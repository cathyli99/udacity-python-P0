"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

output = set(x[0] for x in calls)
output2 = set((x[1]) for x in calls if x[1] not in list(output))
output3 = set((x[0]) for x in texts)
output4 = set((x[1]) for x in texts if x[1] not in list(output3) and list(output2) and list(output))

# print(len(output))
# print(len(output2))
# print(len(output3))
# print(len(output4))

count = len(output) + len(output2) + len(output3) + len(output4)
        
print("There are {} different telephone numbers in the records.".format(count))