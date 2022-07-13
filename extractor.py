import re

fptr = open("sample.txt", "r+")
# str = fptr.readlines()
str = fptr.read()  #string
#type(str)  #list

# phoneRegex = re.compile(r'''(
#  (\d{3}|\(\d{3}\))?             #area code
#  (\s|-|\.)?                     #separator
#  \d{4}                          #first 4 digits
#  (\s|-|\.)                      #separator
#  \d{4}                          #last 4 digits
#  (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
#  )''', re.VERBOSE)


# phoneNum = phoneRegex.search(str[2])
# if phoneNum :
#     print(phoneNum.group())

# str = 'Your no. is 022 1111 2222   ext    34'
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))?             #area code
 (\s|-|\.)?                     #separator
 \d{4}                          #first 4 digits
 (\s|-|\.)                      #separator
 \d{4}                          #last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
 )''', re.VERBOSE)

# mo1 = phoneRegex.findall(str[2])
# print(mo1)


for line in str:
    # line1 = ''.join(line)
    # print(line1)
    phoneNum = re.findall(phoneRegex,line)
    print(phoneNum)


# phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')
# print(phoneNum.findall(str))

# emailId = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
# print(emailId.findall(str))

# a = emailId.search("jbutt@gmail.com")
# if a :
#     print("found" +a.group())

regexPhone = r"\d{3}-\d{3}-\d{4}"
phoneNum = re.findall(regexPhone, str)
print(phoneNum)

regexEmail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(regexEmail, str)
print(emails)

list1 = dict(zip(phoneNum, emails))
print(list1)