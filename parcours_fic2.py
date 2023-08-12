from path import Path  ## nécessite pip install path.py

p = Path("/") / "etc"
print("Parcours de %s " % p)
for l in p.walkfiles(errors="ignore"):
    print(l)
