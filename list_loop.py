list1 = [3, 9, 17, 15, 19]
list2 = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list1, list2):
    print max(a, b)
    print "Done"
