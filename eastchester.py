import requests
from bs4 import BeautifulSoup
import codecs
import re 

eastchester_scrape = get requests("https://www.eufsdk12.org/Domain/76")
soup = BeautifulSoup(eastchester_scrape.text, "html.parser")
email_elements = soupfindAll("li", class_="staffemail")
decoded_emails = []

for element in email_elements:
    script = element.find('script').string if element.find('script') else None
    if script:
        matches = re.findall(r"swrot13\('([^']+)'\)", script)
        if matches:
            encoded_email = matches[0]
            decoded_email = codecs.decode(encoded_email,'rot_13')
            decoded_emails.append(decoded _email)
for email in decoded_emails:
    print(email)