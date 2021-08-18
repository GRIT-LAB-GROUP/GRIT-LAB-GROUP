# Reads the students Dataset file and returns a dictionary sorted from the highest ave mark to lowest ave mark
def create_student_dict(file):
    student_dict = {}  # Create empty dictionary
    f = open(file, 'r')  # Opening student dataset file in read mode
    for line in f:  # Reading student per line
        temp_student_info = line.split(", ")  # Creating list comma delimited
        temp_student_info[4] = temp_student_info[4].rstrip("\n")  # Removing new line from last item on list
        temp_student_list = temp_student_info[1:]  # Creating new temp list without student number
        student_dict[str(temp_student_info[0])] = temp_student_list  # Creating final list with student number as key

    sorted_student_dict = sorted(student_dict.items(), key=lambda x: x[1][3], reverse=True)  # Sorting list via ave mark
    return sorted_student_dict  # Returning the sorted list to caller


def group_leaders(main_dictionary, number_of_leader):  # Create a dictionary of leaders
    leader_dict = {}  # Create empty dictionary
    for student in main_dictionary:  # Iterate through the main dictionary
        if len(leader_dict) < number_of_leader:  # Check for number of leaders to be appended to dictionary
            if student[1][2] == "Extraversion" or student[1][2] == "Conscientiousness":  # Check for leader personality
                leader_dict[student[0]] = student[1]  # Append dictionary

    if len(leader_dict) < number_of_leader:  # Check if enough leaders are appended
        for student in main_dictionary:  # Iterate through the main dictionary
            if len(leader_dict) < number_of_leader:  # Check if enough leaders are appended
                if not (student[0] in leader_dict.keys()):  # Check to make sure that student isn't already in leader_dict
                    if student[1][2] != "Neuroticism":  # Filter out Neuroticism
                        leader_dict[student[0]] = student[1]  # Append dictionary

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


def add_members(sorted_student_dictionary, min_number_of_groups, group_leaders): #Adding members to groups
    #create groups
    groups = []
    for group in range(min_number_of_groups):
        groups.append(("Group " + str((group + 1)), []))
    
    #add leaders
    index = 0
    for leader in group_leaders:
        groups[index][1].append(leader + ', ' + ', '.join(group_leaders[leader]))
        index += 1
        
    #add other members
        
    return groups

def display_groups(groups): #displaying all members with groups
    for group in groups:
        print (group[0])
        for member in group[1]:
            print (member)
        print ("")

# Main Program
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
sorted_student_list = create_student_dict("Sample data.txt")  # This actually creates a list oops
# Check number of students is more than 20
if len(sorted_student_list) >= 20:
    # Get a dictionary of group leaders
    group_leaders = group_leaders(sorted_student_list, get_min_number_of_groups(sorted_student_list))
    #add members
    groups = add_members(sorted_student_list, get_min_number_of_groups(sorted_student_list), group_leaders)
    #display groups
    display_groups(groups)
        
else:
    print("Not enough students in Student Dataset.")

