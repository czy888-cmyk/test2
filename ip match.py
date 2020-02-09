import re
if re.match(r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)$","192.168.1.123"):
    print('ip vaild')
else:
    print('ip invaild')