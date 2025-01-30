'''
> Handling Student Attendance
> Input:
    > list studentNames -- A List of strings to be iterated through
> Returns:
    > N/A
'''
def attendance(studentNames):

    # Take the length of the list to find how many names/students are in attendance
    total = len(studentNames)

    # Make empty list to keep track of unique names
    unique = []

    # Use for loop to find all unique names
    for name in studentNames: # Iterate through each name within studentNames

        if name not in unique: # if name isn't in unique name list, add it
            unique.append(name)

    # Take the length of the list to find out how many names are in attendance AND unique
    uniqueTotal = len(unique)

    # Print 
    print("Total students attended: ", total, "\nUnique stuents: ", uniqueTotal)



'''
> Managing Parent Sign-Ups for "Parents' Night Out"
> Input:
    > list familyCount -- List of tuples that contains the Parent's name and the number of kids
> Returns:
    > N/A
'''
def managingSignups(familyCount):
    print("------------------------------------------------------")

    
    totalKids = 0
    totalParents = 0

    # Make empty list to keep track of unique parents
    unique = []
    tempName = ""
    largest = 0
    parent = ""
    for i in range(len(familyCount)):
        
        tempName = familyCount[i][0]
        largest = familyCount[i][1]

        for j in range(len(familyCount)):
            if (j==i):
                break
            elif (familyCount[i][0] == familyCount[j][0]):

                if (familyCount[j][1] > familyCount[i][1]):
                    largest = familyCount[j][1]
                else:
                    largest = familyCount[i][1]

            parent = tempName, largest

        # Add parent + largest kid amount to unique list
        unique.append(parent)

    totalKids = sum(unique[1])  # Total number of kids
    totalParents = len(unique)  # Total number of parents
    print("Total parents signed up: ", totalParents, "\nTotal kids attending: ", totalKids)




'''
> Main Function
'''
def main():
    # Question 1
    studentNames = ["Alice", "Bob", "Charlie", "Alice", "Bob"]
    attendance(studentNames)

    # Question 2
    parents = [("John", 2), ("Jane", 3), ("John", 4), ("Alice", 1)]
    managingSignups(parents)

if __name__ == "__main__":
    main()