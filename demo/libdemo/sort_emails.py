# Take emails from emails.txt, sort unique emails and write them to sorted_emails.txt

f = open("emails.txt", "rt")  # read text
emails = set()
for line in f:
    line = line.strip()
    if len(line) == 0:   # Ignore blank line
        continue

    parts = line.split(",")
    for email in parts:
        email = email.strip()
        if len(email) > 0 and '@' in email:
            emails.add(email)

f.close()

f = open("sorted_emails.txt", "wt")
for email in sorted(emails):
    f.write(email + "\n")

f.close()
