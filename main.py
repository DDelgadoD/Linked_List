from LinkedList import LinkedList


def create_linked_lists(list_of_lists):
    """
    Function that returns a set of linked lists.
    :param: list_of_lists: list of lists of integers that want to become to linked lists e.g : [[1,2],[2,4,5]]
    :return: lls: A list of linked lists e.g. [[1->2][2->4->5]]
    """

    if type(list_of_lists) is not list:
        raise TypeError("Your input isn't a list e.g =  [[1,2],[2,4,5]]")
    
    lls = []
    for i in range(len(list_of_lists)):
        if type(list_of_lists[i]) is list:
            lls.append(LinkedList())
            for n in list_of_lists[i]:
                if type(n) is int:
                    lls[i].append(n)
                else:
                    raise TypeError("Your lists aren't composed only for integers e.g = [[1,2],[2,4,5]]")
        else:   
            raise TypeError("Your list isn't composed only for lists e.g = [[1,2],[2,4,5]]")
    
    return lls


# We can do the input from command line but for is more confortable in this case do the input directly
# input_ = input()

input_ = [[1, 4, 5], [1, 3, 4], [2, 6]]

lists = create_linked_lists(input_)

print("Input:")
for linked in lists:
    print("        "+str(linked))

for ln in range(1, len(lists)):
    lists[0].merge(lists[ln])

lists[0].sort()

print(f"Output:\n        {lists[0]}")
