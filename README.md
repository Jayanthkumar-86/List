# List
Searching a word and replacing it with a new word
# List Search and Replace in Python

This is a simple Python script that searches for a specific word in a list and replaces it with another word.

## Description

The script iterates over a list of names, checks if any element matches the search word, and replaces it with the specified replacement word. It then prints the updated list.

## Code Example
#Input:
```python
my_list = ["Jayanth", "Pranav", "Dumbu", "Bunny"]
search_word = "Jayanth"
replace_word = "God"

for i in range(len(my_list)):
    if my_list[i] == search_word:
        my_list[i] = replace_word
        print(my_list)
#Output:
runfile('C:/Users/ADMIN/untitled2.py', wdir='C:/Users/ADMIN')
['God', 'Pranav', 'Dumbu', 'Bunny']

