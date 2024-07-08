#Task 1: Email Extraction Enhancement
import re

#Added https://exclude.com to test if changes effect this string as well
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, https://exclude.com"
#Add a grouping after the @ followed by a ?! to check if the following word is NOT 'exclude'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)