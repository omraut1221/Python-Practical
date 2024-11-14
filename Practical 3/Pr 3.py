#Array
import array

arr1 = array.array('i', [12, 2, 34, 23])
arr2 = array.array('i', [3, 4, 5])

# append()
arr1.append(45)
print("Appended array: ", arr1)

# copy()
arr3 = arr1[:]
print("Copied array: ", arr3)

# count()
print("Count : ", arr1.count(12))

# extend()
arr1.extend(arr2)
print("Extended array: ", arr1)

# index()
print("Index : ", arr1.index(34))

# insert()
arr1.insert(2, 99)
print("After inserting : ", arr1)

# reverse()
arr1.reverse()
print("Reversed array: ", arr1)

# remove()
arr1.remove(34)
print("After removing : ", arr1)

# pop()
popped_element = arr1.pop()
print("Popped element: ", popped_element)
print("After popping: ", arr1)

# tolist()
arr_list = arr1.tolist()
print("Array converted to list: ", arr_list)

# buffer_info()
print("Buffer info: ", arr1.buffer_info())

# typecode
print("Array typecode: ", arr1.typecode)


#Implementation of List
l1=[1,12,3,4,"Python","Java","C++"]
l2=[10,15,4,50,5,2,8,9]
print(l1)
print(l1[5])
l1.append(70)
print(l1.pop(2))
print(l1)
print("The Length of the List is: ")
print(len(l1))
l1.clear()
print("The List Before Sorting: ",l2)
l2.sort()
print("The List After Sorting: ",l2)
print()

#Implementation of Tuple
t1=(10,20,30,40,50,60,25,10,80,5,45,30)
t2=("C","C++","Java","Python","Android","Javascript")
print("The Length of the tuple is: ")
print(len(t1))
print(t1.count(10))
print(t1.index(30))
print(t1+t2)
print(t1*2)
print()
