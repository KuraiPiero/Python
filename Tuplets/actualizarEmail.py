def updateEmail(email):
    oldDomain = "hotmail.com"
    newDomain = "gmail.com"

    if "@" + oldDomain in email:
        index = email.index("@" + oldDomain)
        newEmail = email[:index] + "@" + newDomain
        return newEmail
    return email


print(updateEmail("eduardo@gmail.com"))
print(updateEmail("miguel@hotmail.com"))

