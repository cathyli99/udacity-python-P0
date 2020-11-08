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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

non_tele = []
outgoing = []
receiving = []

for text in texts:
    non_tele.append(text[0])
    non_tele.append(text[1])
# print ('\n'.join(sorted(set(non_tele))))

for call in calls:
    receiving.append(call[1])
    if call[0] not in non_tele and call[0] not in receiving:
        outgoing.append(call[0])
        
print("These numbers could be telemarketers: ")
print ('\n'.join(sorted(set(outgoing))))

%time