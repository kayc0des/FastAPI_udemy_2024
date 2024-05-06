''' Python Loops '''

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x < 3:
    x += 1
    for item in my_list:
        if item == 'Monday':
            continue
        print(item)