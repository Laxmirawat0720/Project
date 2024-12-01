my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After appending 6:", my_list)

my_list.remove(3)
print("After removing 3:", my_list)

my_list.insert(1, 10)
print("After inserting 10 at the second position:", my_list)

my_list.sort(reverse=True)
print("Sorted list in descending order:", my_list)

my_tuple = ("apple", "banana", "cherry")

second_element = my_tuple[1]
print("Second element of the tuple:", second_element)

try:
    my_tuple[0] = "mango"
except TypeError as e:
    print("Error: Cannot change tuple elements:", e)
