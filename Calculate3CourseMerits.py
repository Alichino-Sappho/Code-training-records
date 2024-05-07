# define course1, course2, course3
course1 = int(input('input the score of 1st course: '))
course2 = int(input('input the score of 2nd course: '))
course3 = int(input('input the score of 3rd course: '))

# classify three kinds of merits: course1_merit, course2_merit, course3_merit
if 0 <= course1 < 60:
    course1_merit = 0
elif 60 <= course1 < 90:
    course1_merit = 1
elif 90 <= course1 <= 100:
    course1_merit = 2
else:
    print('A wrong score was inputed.')
if 0 <= course2 < 60:
    course2_merit = 0
elif 60<= course2 < 90:
    course2_merit = 1
elif 90 <= course2 <= 100:
    course2_merit = 2
else:
    print('A wrong score was inputed.')
if 0 <= course3 < 60:
    course3_merit = 0
elif 60<= course3 < 90:
    course3_merit = 1
elif 90 <= course3 <= 100:
    course3_merit = 2
else:
    print('A wrong score was inputed.')
# calculate the total_merit
total_merit = course1_merit+course2_merit+course3_merit
print("The total merits are %d. "%(total_merit))