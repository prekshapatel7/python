'''Accept contact details from the user and create a vcard
that we can directly store in our mobile'''
def create_vcard(name, phone, email, filename="contact.vcf"):
    vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD
"""

    with open(filename, "w") as file:
        file.write(vcard_data)

    print(f"vCard saved as '{filename}' — you can now transfer it to your phone.")

# Accept contact details
name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

create_vcard(name, phone, email)
