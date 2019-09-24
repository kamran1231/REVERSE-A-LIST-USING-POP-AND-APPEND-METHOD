
def reverse_list(l):
    list1 = []
    for i in range(len(l)):
        popped_item = l.pop()
        list1.append(popped_item)
    return list1

l = [6,9,5,2,69,3]
print(reverse_list(l))