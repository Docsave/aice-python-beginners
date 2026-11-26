#messy name
name = "  saviour ISIDORE  "
email_address = "SAVIOURisidore02@GMAIL.com"
phone_number = "+234-816-388-1255"

#clean and format each field
clean_name = name.strip().title()
clean_email = email_address.lower()
clean_phone = phone_number.replace("-","")

print(f"Name: {clean_name}")
print(f"Email: {clean_email}")
print(f"Phone Number: {clean_phone}")

#validation check
print(f"Name Length Valid (>3): {len(clean_name) > 3}")
print(f"Email Contain @: {"@" in clean_email}")
