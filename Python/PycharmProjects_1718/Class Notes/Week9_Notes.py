# Error Handling
'''
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]: ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad Index:', position)
    except Exception as other:
        print('Something else broke:', other)

try:
    f = open('username.txt')
except FileNotFoundError:
    print("The file does not exist at this location.")
except NameError:
    print("You are using an undefined variable.")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    # Why run it here than in the try block?
    # So that each potential error is caught
finally:
    print("Code is executing the stuff in the 'finally' block.")
'''

import pprint # This will allow for cleaner printing. Can use the pprint() and the pformat functions()

courses = {'CIT 200': 'Relational Databases', 'CSI 300': 'Database Systems', 'SEC 250': 'Computer & Network Security',
           'NET 215': 'TCP/IP'}
grade_avg = {'Exam 1': 90, 'Exam 2': 76, 'Exam 3': 82, 'Exam 4': 88}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in courses:
        print(courses[name] + ' is known as ' + name)
    else:
        print('I do not have course information for ' + name)
        print('What is the course?')
        cname = input()
        courses[name] = cname
        print('Courses Database Updated')

for k in grade_avg.keys():
    print(k)
for i in grade_avg.values():
    print(i)

print("I want to take " + str(courses.get('NET 215', 0)))
print("I want to take " + str(courses.get('AI', 'a course that does not exist')))

message = 'You need to register for at least 4 or you will lose your full-time status'
msg_count = {}
for character in message:
    msg_count.setdefault(character, 0)
    msg_count[character] = msg_count[character] + 1
print(msg_count)


