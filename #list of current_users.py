#list of current_users
current_users=['Ivan','John','Andy','Smith','William']
new_users=['Ivan','John','Yvonne','Olivia','wilson']
for new_user in new_users:
    print(new_users)
    if new_users in current_users :
       print(f"{new_users.title()} has been used already.please enter a new username ")
    else:
        print('username is available')
#fizzbuzz
    for num in range(1,100):
        if num % 3 == 0 and num % 5== 0:
            print('fizzbuzz')
        elif num % 3== 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz') 
        else:
            print(num)
           
