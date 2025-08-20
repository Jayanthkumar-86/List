my_list=["Jayanth","Pranav","Dumbu","Bunny"]
search_word="Jayanth"
replace_word="God"
for i in range(len(my_list)):
    if my_list[i]==search_word:
        my_list[i]=replace_word
        print(my_list)
        
        