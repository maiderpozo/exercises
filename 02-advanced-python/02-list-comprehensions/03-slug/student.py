# Write your code here
def slug(name):
    complete= name.split(" ")
    name=complete[0]
    surnames=complete[1:]
    return "-".join(s.lower() for s in complete + [name])

print(slug('Maider Pozo'))