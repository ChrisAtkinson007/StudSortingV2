Students=[['Greg',24],['John',22],['Andy',21],['Jim',23],['Phil',22],['Bob',23],['Chip',23],['Tim',24]]

print(Students)

#Create a unique set of possible ages from original array
#Time complexity of iterating of the list is O(n) and adding each element to the hash set is O(1)
unique_set=set([Stud[1] for Stud in Students])

#Group the students by their ages, not in order.
#O(n) time complexity for iterating over list of students, O(1) for fetching value from hashset
names_grouped=[[Stud for Stud in Students if Stud[1]==val] for val in unique_set]
print(names_grouped)

#If you want the list in the original ungrouped format
ListFinal=[]
for list in names_grouped:
    ListFinal.extend(list)

#Final time complexity resolves to O(n)
print(ListFinal)