'''
Script to create groups from student ids.
'''

import random

num_students = int(input('How many students are present? '))
group_size = int(input('What size do you want the groups to be? '))

num_groups = num_students // group_size # how many times does group_size go into num_students (ignore remainder for now)

student_ids = list(range(1, num_students + 1)) # generate a list of student ids
random.shuffle(student_ids) # randomize the order of the ids

groups = list() # create a list of groups
for group_num in range(num_groups):
  group = list()
  for _ in range(group_size):
    group.append(student_ids.pop(0))
  groups.append(group) # add group the list of groups

# add any remaining students to the groups
if len(student_ids) > 0:
  # if the remaining students can form a group of size near the target size, then just make a new group
  if len(student_ids) == group_size - 1 > 1:
    groups.append(student_ids)
  else: # otherwise, distribute the remainder across the existing groups
    for idx, student in enumerate(student_ids):
      groups[idx].append(student)

# print groups
print() # add some whie space
for idx, group in enumerate(groups):
  print(f'Group {idx + 1}: {group}')
