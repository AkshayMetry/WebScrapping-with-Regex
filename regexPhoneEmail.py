# import re
# fptr = open("web.txt", "r+")
# str = fptr.read()  #string
# # #type(str)  #list

# #------------------------------------------------------------------------------
# #Read File Line By Line
# file = open("output.txt","w+")

# with open("web.txt","r") as textfile:
#     for line in textfile:
#         # regexPhone = "\d{3}-\d{3}-\d{4}"
#         # phoneNum = re.findall(regexPhone, line)
#         # # print(phoneNum)     
#         # if phoneNum == []:
#         #    phoneNum.append("Mobile Number not provided")

#         regexEmail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
#         emails = re.findall(regexEmail, line)
#         # print(emails)
#         # if emails == []:
#         #     emails.append("Email Address not provided")


#         list1 = emails
#         string = str(list1)
#         file.write('%s\n' %string)


#--------
# ---------------------------------------------------------------
import re
import numpy as np
fptr = open("web.txt", "r+")
str = fptr.read() 

def unique(a):
    x = np.array(a)
    y = np.unique(x)
    return y

# regexPhone = r"((\+91 )*)((\d{10})+|([0-9]{12})+)|\d{3}([- ]*)\d{4}([- ]*)\d{4}}"
# regexPhone = r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
regexPhone =r"(\+91\d{10})"
phoneNum = re.findall(regexPhone, str)
uniquelist = unique(phoneNum)
# print(uniquelist)

phoneNumCount  = 0
file = open("output.txt","w")

for item in uniquelist:
    # print(item)
    phoneNumCount += 1
    file.write(item)
    file.write("\n")

print("No of Phone Number: ",phoneNumCount)


regexEmail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(regexEmail, str)


emailCount = 0
for item in emails:
    # print(item)
    emailCount += 1
    file.write(item)
    file.write("\n")

print("No of Emails: ",emailCount)

total = phoneNumCount + emailCount
print("Total Entries of Both Phone Number and Email: ",total)