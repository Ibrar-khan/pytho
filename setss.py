
s = {2,4,6,2,8}
print(s)
#ye ghalat hay {} is say dict ban jata hay, awr ye () tuple. true set()
st=set()
print(type(st))

info = {"ibrar", "muazzam",9,18,9}

for value in info:
    print(value)

s1={2,4,6,8}
s2={1,3,5,7,9}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1, s2)



set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)           # Union: {1, 2, 3, 4, 5}
print(set1 & set2)           # Intersection: {3}
print(set1 - set2)  