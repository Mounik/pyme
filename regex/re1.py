import re

fichier = '/etc/group'

pattern = r'[-\w]*:\w:\d*:\w*'

with open(fichier) as f:
    for lig in f:
        if re.match(pattern, lig):
            pass # ne faitrien si cela 'matche'
        else:
            print("Ligne hors motif : %s " % lig)
