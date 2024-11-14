#String
A="Hello World"
print(A)
print(A[:5])
print(A[2:6])
print(A[-11:-2])
print(A.upper())
print(A.lower())
print(A.count('l'))
print("The Length of the String is: ",len(A))
print()

# Implementation of Dictionary
Dict1 = {
    "Brand": "BMW",
    "Model": "X6",
    "Year": 2020
}
print(Dict1)
Dict1.update({"Year": 2024})
print(Dict1)
Dict1["Colour"] = "Red"
print(Dict1)
Dict1.pop("Model")
print(Dict1)
print()

# Original sets
s1 = {"Apple", 1, "Banana", 25, "Cherry", 12, 25}
s2 = {1, 12, 3, 4, "Python", "Java", "C++"}

print("Set 1:", s1)
print("Length of Set 1:", len(s1))

s1.add("Orange")
print("Set 1 after adding 'Orange':", s1)

union_set = s1.union(s2)
print("Union of Set 1 and Set 2:", union_set)

#Returns a set, that is the intersection of two other sets
intersection_set = s1.intersection(s2)
print("Intersection of Set 1 and Set 2:", intersection_set)

#Returns a set with the symmetric differences of two sets
sym_diff_set = s1.symmetric_difference(s2)
print("Symmetric Difference of Set 1 and Set 2:", sym_diff_set)

#Frozenset

frozenset1 = frozenset([1, 2, 3, 4, 5])
frozenset2 = frozenset([4, 5, 6, 7, 8])

# union()
union_fs = frozenset1.union(frozenset2)
print("Union : ", union_fs)

# intersection()
intersection_fs = frozenset1.intersection(frozenset2)
print("Intersection : ", intersection_fs)

# difference()
difference_fs = frozenset1.difference(frozenset2)
print("Difference : ", difference_fs)

# symmetric_difference()
symmetric_difference_fs = frozenset1.symmetric_difference(frozenset2)
print("Symmetric difference : ", symmetric_difference_fs)

# issubset()
is_subset = frozenset1.issubset(frozenset2)
print("Is frozenset1 a subset of frozenset2? ", is_subset)

# issuperset()
is_superset = frozenset1.issuperset(frozenset2)
print("Is frozenset1 a superset of frozenset2? ", is_superset)

# isdisjoint()
is_disjoint = frozenset1.isdisjoint(frozenset2)
print("Are frozenset1 and frozenset2 disjoint? ", is_disjoint)

# copy()
frozenset_copy = frozenset1.copy()
print("Copy: ", frozenset_copy)

# len()
length = len(frozenset1)
print("Length : ", length)

# in
is_in = 3 in frozenset1
print("Is 3 in frozenset1? ", is_in)
