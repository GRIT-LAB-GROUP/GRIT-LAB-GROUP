# Reads the students Dataset file and returns a dictionary sorted from the highest ave mark to lowest ave mark
def create_student_dict(file):
    student_dict = {}  # Create empty dictionary
    f = open(file, 'r')  # Opening student dataset file in read mode
    for line in f:  # Reading student per line
        temp_student_info = line.split(", ")  # Creating list comma delimited
        temp_student_info[4] = temp_student_info[4].rstrip("\n")  # Removing new line from last item on list
        temp_student_list = temp_student_info[1:]  # Creating new temp list without student number
        student_dict[str(temp_student_info[0])] = temp_student_list  # Creating final list with student number as key

    sorted_student_list = sorted(student_dict.items(), key=lambda x: x[1][3], reverse=True)  # Sorting list via ave mark
    return sorted_student_list  # Returning the sorted list to caller


def group_leaders(main_dictionary, number_of_leader):  # Create a dictionary of leaders
    leader_dict = {}  # Create empty dictionary
    for student in main_dictionary:  # Iterate through the main dictionary which would be the sorted_student_list
        if len(leader_dict) < number_of_leader:  # Check for number of leaders to be appended to dictionary
            if student[1][2] == "Extraversion" or student[1][2] == "Conscientiousness":  # Check for leader personality
                leader_dict[student[0]] = student[1]  # Append dictionary

    if len(leader_dict) < number_of_leader:  # Check if enough leaders are appended in the dictionary

        for student in main_dictionary:  # Iterate through the main dictionary again
            if len(leader_dict) < number_of_leader:  # Check if enough leaders are appended on every for loop

                if not (student[0] in leader_dict.keys()):  # Check to make sure that student isn't already in leader_dict
                    if student[1][2] != "Neuroticism":  # Filter out Neuroticism
                        leader_dict[student[0]] = student[1]  # Append dictionary
            else:
                break

    if len(leader_dict) < number_of_leader:  # Final check if still not enough leaders
        return "Not enough students with leader attributes"
    else:
        return leader_dict


def get_min_number_of_groups(sorted_student_dict):  # Gets the number of groups required
    extraversion = 0
    neuroticism = 0
    for key in sorted_student_dict:
        if key[1][2] == "Extraversion":
            extraversion += 1
        if key[1][2] == "Neuroticism":
            neuroticism += 1
    import math
    temp_list = [extraversion, neuroticism, math.ceil(len(sorted_student_list) / students_in_each_group)]
    return max(temp_list)


def check_student(groups, student):  # check student in each group before adding them to a group
    found = False
    for group in groups:
        for group_student in group[1]:
            if group_student[0] == student[0]:
                found = True
                break
    return found


def check_extraversion(group):
    found = False
    for group_student in group[1]:
        if group_student[1][2] == "Extraversion":
            found = True
            break
    return found


def check_neurotic(group):
    found = False
    for group_student in group[1]:
        if group_student[1][2] == "Neuroticism":
            found = True
            break
    return found


def add_members(students_in_each_group, sorted_student_dictionary, min_number_of_groups, group_leaders):  # Adding members to groups
    # create groups
    groups = []
    for group in range(min_number_of_groups):
        groups.append(("Group " + str((group + 1)), []))
    
    # add leaders
    index = 0

    for leader in group_leaders:

        if int(group_leaders[leader][3]) >= 75:
            group_leaders[leader].append("(Leader & Top student)")
        elif int(group_leaders[leader][3]) < 50:
            group_leaders[leader].append("(Leader & Weak student)")
        else:
            group_leaders[leader].append("(Leader)")
        
        groups[index][1].append((leader, group_leaders[leader]))
        sorted_student_dictionary.remove((leader, group_leaders[leader]))

        index += 1
    
    # add others
    while len(sorted_student_dictionary) > 0:
        
        student = sorted_student_dictionary[len(sorted_student_dictionary) - 1]
        
        if len(student[1]) == 4:
            if int(student[1][3]) >= 75:
                if student[1][2] == "Agreeableness" or student[1][2] == "Openness":
                    student[1].append("(Top student & remaining Agreeable/Open members)")
                elif student[1][2] == "Neuroticism":
                    student[1].append("(Neurocrotic member & Top student)")
                else:
                    student[1].append("(Top student)")                
            elif int(student[1][3]) < 50:
                if student[1][2] == "Agreeableness" or student[1][2] == "Openness":
                    student[1].append("(Weak student & remaining Agreeable/Open members)")
                elif student[1][2] == "Neuroticism":
                    student[1].append("(Neurocrotic member & Weak student)")
                else:
                    student[1].append("(Weak student)")
            else:
                if student[1][2] == "Agreeableness" or student[1][2] == "Openness":
                    student[1].append("(remaining Agreeable/Open members)")
                elif student[1][2] == "Neuroticism":
                    student[1].append("(Neurocrotic member)")
                
        for group in groups:
            if check_student(groups, student) != (True and (len(group[1]) < students_in_each_group)):
                if student[1][2] == "Extraversion":
                    if check_extraversion(group) != True:
                        group[1].append(student)
                        sorted_student_dictionary.pop()
                elif student[1][2] == "Neuroticism":
                    if check_neurotic(group) != True:
                        group[1].append(student)
                        sorted_student_dictionary.pop()       
                else:
                    group[1].append(student)
                    sorted_student_dictionary.pop()    
    return groups


def display_groups(groups):  # displaying all members with groups
    for group in groups:
        print (group[0])
        for member in group[1]:
            print (member[0] + ", " + ', '.join(member[1]).replace(", (", " ("))
        print ("")


# Main Program
students_in_each_group = "0"  # Initialise variable

while True:
    students_in_each_group = input("How many students would you like to have in each group: ")  # User input

    if students_in_each_group.isdigit():  # Check if input is a digit.
        students_in_each_group = int(students_in_each_group)

        if students_in_each_group >= 4:  # Check if input is more than 4.
            break

        else:
            print("There is a minimum of 4 members per group.")

    else:
        print("Please enter a valid number.")

# Creating sorted list of students
sorted_student_list = create_student_dict("Sample data.txt")

# Check number of students is more than 20
if len(sorted_student_list) >= 20:

    # Get a dictionary of group leaders
    group_leaders = group_leaders(sorted_student_list, get_min_number_of_groups(sorted_student_list))

    # Catch if there is not enough leaders with leader attributes
    if group_leaders == "Not enough students with leader attributes":
        print("Error! Not enough students with leader attributes")

    else:
        # add members
        groups = add_members(students_in_each_group, sorted_student_list, get_min_number_of_groups(sorted_student_list), group_leaders)
        # display groups
        display_groups(groups)

else:
    print("Not enough students in Student Dataset.")

