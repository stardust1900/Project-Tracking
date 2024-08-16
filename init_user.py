import re
with open('email.txt', "r", encoding="utf-8") as f:
    for line in f:
        # print(line)
        name = line.split('<')[0]
        result = re.search(r'<(.*?)>', line)
        email = result.group(1)
        login_name = email.split('@')[0]
        print("INSERT INTO user (name, login_name, password, email, dept_id, is_active, create_time, update_time) VALUES ('%s', '%s', 'scrypt:32768:8:1$wqKjBRUNtsHjgwpN$9f26116d8af458abed42e21547225096903db813379784b2a80996330d095cb58dc178893731baf3196302bcdc9f2790c162b30bf7e86f6edbaa87d01fc16760', '%s', 1, true, '2024-08-06 09:57:52', null);" % (name,login_name,email))
