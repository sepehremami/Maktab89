import re
words = ["Show must go on", "Parents pray popcorn", "kings wont surrender", "popsicle Play"]

for w in words:
        m = re.match("(?i)(P\w+)\W(P\w+)", w)
        if m:
            print(m.groups())
