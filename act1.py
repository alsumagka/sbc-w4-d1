my_array = ["M", "B", "D", "R", "N", "C"]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            print(my_array)

print("Sorted array:", my_array)