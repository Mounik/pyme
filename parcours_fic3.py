from pathlib import Path


p = Path.cwd().rglob('*')
print("Parcours de %s" % p)
for l in p:
    print(l)

fichier_csv = Path('/tmp/data').glob('*.csv')
