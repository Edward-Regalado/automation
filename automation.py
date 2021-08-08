from locale import locale_encoding_alias
from typing import Text
from faker import Faker
import re

# fake = Faker()
 
# content = ''

re_phone = re.compile(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?")

re_email = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")



all_numbers = []
all_emails = []
     
# read and filter out numbers from our note.txt file
with open('assets/potential-contacts.txt', 'r+') as f:
    content = f.readlines()
    for line in content:
        if re_phone.search(line):
            found_phone_number = re_phone.search(line)
            found_phone_number = found_phone_number.group()
            # find_number = re.findall(re_phone, line)
            all_numbers.append(found_phone_number)
            # print(all_numbers)
    for line in content:
        if re_email.search(line):
            found_email = re_email.search(line)
            found_email = found_email.group()
            all_emails.append(found_email)


with open('assest/emails.txt', 'r+') as f:
    

   
        
# write filtered out numbers to our phone_numbers.txt 
with open('assets/phone_numbers.txt', 'w+') as f:
    for numbers in all_numbers:
        f.write(f'{numbers}\n')
        
                
#write filterd emails to our emails.txt file
with open('assets/emails.txt', 'w+') as f:
    content = f.readlines()
    for email in all_emails:
        f.write(f'{email}\n')
    
        

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
 # for i in range(10):
    # content += fake.sentence(5)
    # content += fake.email() + '\n'
    # content += fake.paragraph()
    # content += fake.phone_number()
    # content += fake.paragraph()
    # content += '\n'
    # print(content)
    
# content = f'{paragraph} {}'

# write/create a new file in our assets folder  
# with open('assets/notes.txt', 'w+') as f:
#     f.write(content)

# read note.text and filter our data with regex        

    

# copy and move our notes file (copy takes two positional args.. what to copy and where)
# shutil.copy('assets/.txt', '.')
