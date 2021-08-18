# GRIT-LAB-GROUP


# Write a python program that creates student groupings based on their marks and their personality. 
  
# The mark will be a single average; if their mark is 75% or above, they will be viewed as a top student,and if their mark is below 50%, they will be viewed as a weak student. The personality considerationswill consist of the Five-Factor Model of personality: extraversion, conscientiousness, neuroticism,agreeableness, and openness. The user will specify how many groups they would like to have, withthe limitations of a minimum of 20 students in the dataset (which can be read in any file format)and a minimum of 4 members per group. Each group will need a group leader; the group leader must have the personality traits ofextraversion or conscientiousness, and a group leader can also be a top student. A group cannothave two members with a personality trait of extraversion as too many members with this trait canbe disruptive in a group and if a group has two members with a leader's personality trait(extraversion and conscientiousness) or (conscientiousness and conscientiousness) then themember with the higher mark will be assigned as the group leader. If there is no member in thegroup with the personality trait of a leader then the member with the highest mark will be assignedas the leader. If a group does not have a member with a personality trait of neuroticism, it is acceptable; however,each group can only have at most one member with this trait as it is a negative and disruptive trait,and a neurotic member can also be a top/weak student but not a group leader. The remaininggroup members must have the personality trait of agreeableness or openness.
  
  
# Sample Input:
# User Input: How many students would you like to have in each group?
# Students
# Dataset
# 21904236, Ellie, Fredricksen, Agreeableness, 67
# 21792608, Cornelius, Robinson, Neuroticism, 71
# 24789033, Gordie, Gibble, Conscientiousness, 75
# 21573892, Lilo, Pelekai, Openness, 49
# 21785092, Lucille, Krunklehorn, Conscientiousness, 49
# 21589057, Imelda, Rivera, Extraversion, 71
# 21789035, Cass, Hamada, Extraversion, 73
# 21090679, Georges, Hautecourt, Openness, 43
# 21798540, Sylvia, Marpole, Extraversion, 95
# 21456378, Remy, Remington, Openness, 68
# 21572333, Delilah, Dalmatian, Conscientiousness, 84
# 21534267, Minty, Zaki, Agreeableness, 51
# 21576890, John, Smith, Neuroticism, 45
# 21689303, Anita, Radcliffe, Agreeableness, 56
# 28590169, Gunther, Magnuson, Neuroticism, 87
# 21578028, Delbert, Doppler, Conscientiousness, 76
# 21684900, David, Kawena, Extraversion, 87
# 21786792, Lizzy, Griffiths, Agreeableness, 76
# 21789900, Lavender, Bloom, Agreeableness, 56
# 21285790, Jackie, Wackerman, Neuroticism, 34
# 21357854, Li, Shang, Conscientiousness, 71
# 21902789, Benjamin, Clawhauser, Openness, 66
# 21978546, Miranda, Wright, Agreeableness, 82
# (Note: There are 23 students in this dataset)
  
  
# Sample Output:
# Group 1
# 24789033, Gordie, Gibble, Conscientiousness, 75 (Leader & Top student)
# 21576890, John, Smith, Neuroticism, 45 (Neurocrotic member & Weak student)
# 21689303, Anita, Radcliffe, Agreeableness, 56 (remaining Agreeable/Open members)
# 21902789, Benjamin, Clawhauser, Openness, 66 (remaining Agreeable/Open members)
# Group 2
# 21789035, Cass, Hamada, Extraversion, 73 (Leader)
# 21978546, Miranda, Wright, Agreeableness, 82 (Top student)
# 21792608, Cornelius, Robinson, Neuroticism, 71 (Neurocrotic member)
# 21090679, Georges, Hautecourt, Openness, 43 (Weak student & remaining Agreeable/Openmembers)
# Group 3
# 21572333, Delilah, Dalmatian, Conscientiousness, 84 (Leader)
# 21578028, Delbert, Doppler, Conscientiousness, 76 (Top student)
# 21285790, Jackie, Wackerman, Neuroticism, 34 (Neurocrotic member & Weak student)
# 21789900, Lavender, Bloom, Agreeableness, 56 (remaining Agreeable/Open members)
# Group 4
# 21798540, Sylvia, Marpole, Extraversion, 95 (Leader & Top student)
# 21785092, Lucille, Krunklehorn, Conscientiousness, 49 (Weak student)
# 21786792, Lizzy, Griffiths, Agreeableness, 76 (remaining Agreeable/Open members)
# 21456378, Remy, Remington, Openness, 68 (remaining Agreeable/Open members)
# Group 5
# 21589057, Imelda, Rivera, Extraversion, 71 (Leader)
# 28590169, Gunther, Magnuson, Neuroticism, 87 (Neurotic member & Top student)
# 21904236, Ellie, Fredricksen, Agreeableness, 67 (remaining Agreeable/Open members)
# 21534267, Minty, Zaki, Agreeableness, 51 (remaining Agreeable/Open members)
# Group 6
# 21684900, David, Kawena, Extraversion, 87 (Leader)
# 21357854, Li, Shang, Conscientiousness, 79 (Top student)
# 21573892, Lilo, Pelekai, Openness, 49 (Weak student & remaining Agreeable/Open members)
# (This group will have one less member as 23 is not equally divisble by 4)