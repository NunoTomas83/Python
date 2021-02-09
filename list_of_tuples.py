"""Script to aggregate email names and domain names"""

def full_emails(people):   #people is a LIST of TUPLES
    result = []
    for email, name in people:
        result.append(("{} <{}>".format(name, email)))
    return result


print(full_emails([("alex@example.com", "Alex Diego"), ("shady@example.com", "Shay Brandt")]))
