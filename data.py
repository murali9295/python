d={"Delhi":5, "Jammu":9, "Gujarath":8,  "Andhra":1, "Kerala":3}
c=sorted(d.items())
print(c)
t = {x:y for x, y in c}
print(t.values())
print(t.keys())
print(t)
