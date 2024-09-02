first_number = int(input())
password = []

for i in range(20):
    for j in range(20):
        if (i and j in password) or (i == 0 or j == 0) or (i == j):
            continue
        if i + j == first_number or first_number % (i + j) == 0:
            password.append(i)
            password.append(j)

password_str = str(password)
password_str_del = ''
for k in password_str:
    if k == '[' or k == ']' or k == ',' or k ==' ':
        continue
    else:
        password_str_del += k

password_end = int(password_str_del)
print(password_end)
