import re


def fun(s):
    email_parts = re.split(';|@|\.', s)

    if not len(email_parts) == 3:
        return False

    username, website, extension = email_parts

    if len(extension) > 3:
        return False

    if len(username) == 0 and not re.match("^[A-Za-z0-9_-]*$", username):
        return False

    if len(website) == 0 and not website.isalnum():
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)