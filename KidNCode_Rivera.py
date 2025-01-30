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
    # Variables
    unique = [] # Make empty list to keep track of unique parents
    tempName = "" # Temporary parent name holder
    largest = 0 # Init largest kids number
    parent = "" # Init parent 'tuple'
    totalKids = 0 # Counter for kid amounts

    # For loop to iterate through tuple list
    for i in range(len(familyCount)):
        
        # Comparative values
        tempName = familyCount[i][0]
        largest = familyCount[i][1]

        # For loop to find unique parents
        for j in range(len(familyCount)):
            # Leave loop if we're looking at the same index
            if (j==i):
                break

            # If current parent has the same name as the parent we're comparing to
            elif (familyCount[j][0] == tempName):

                # AND if parent's number of kids is greater than the initial stored value
                if (familyCount[j][1] > largest):
                    largest = familyCount[j][1]

            # Create tuple of parent name and number of kids
            parent = tempName, largest

        # Add parent + largest kid amount to unique list
        if parent:
            unique.append(parent)

    # For loop to sum up number of kids
    for family in unique:
        totalKids = totalKids + family[1]
            
    totalParents = len(unique)  # Total number of parents
    print("Total parents signed up: ", totalParents, "\nTotal kids attending: ", totalKids)



'''
> Automate tracking of the performance of students
> Input:
    > Dictionary scores -- Dictionary of student names and their corresponding quiz scores
> Returns:
    > N/A
'''
def performance(scores):
    # Variables
    studentAverage = 0
    classAverage = 0
    topScore = 0
    topStudent = ""

    for name, quizScores in scores.items():

        # Find average score of current student
        studentAverage = round(sum(quizScores)/len(quizScores), 2)
        # Check if current average is greater than the top score
        if (studentAverage > topScore):
            # Set current average as the new top score
            topScore = studentAverage
            topStudent = name

        # Add current average to the total class score sum
        classAverage = classAverage + studentAverage

        # Print student's scores
        print(name, "'s average score: ", studentAverage)

    # Find class average and print value
    classAverage = round(classAverage / len(scores), 2)
    print("\nClass average: ", classAverage)

    # Print Top student
    print("Top-performing student: ", topStudent, " with an average score of ", topScore)



'''
> Main Function
'''
def main():
    # Question 1
    studentNames = ["Alice", "Bob", "Charlie", "Alice", "Bob"]
    attendance(studentNames)

    print("---------------------------------------------------------------------------------")

    # Question 2
    parents = [("John", 2), ("Jane", 3), ("John", 4), ("Alice", 1)]
    managingSignups(parents)

    print("---------------------------------------------------------------------------------")

    # Question 3
    scores = {
        "Alice": [85, 90, 78],
        "Bob": [70, 75, 80],
        "Charlie": [95, 88, 92]
        }
    performance(scores)



if __name__ == "__main__":
    main()
