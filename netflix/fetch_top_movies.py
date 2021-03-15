'''
    Question: Every country has a list of movies, we need to find the top rated movies in all given countries

    Answer: We basically assume that the first list is always the final list. We will compare
    that list to the second list. We will sort these two lists and store the result in list 1, then compare list1 to list3.
    Again, the result will still be in list1. We will continue doing that until we have no more
    lists to compare our list1 to

    Complexity:
        let n be the number of lists and k be the number of movies in a list.

        Time: O(NxK) -> We are counting list of movies and its list that contains movies.

        Space O(1) -> We are making our changes in place without allocating any extra memory.

'''
from LinkedList import *


def merge_two_lists(l1, l2):
    head = LinkedListNode(-1)

    previous = head

    while l1 and l2:
        if l1.data <= l2.data:
            previous.next = l1
            l1 = l1.next
        else:
            previous.next = l2
            l2 = l2.next
        previous = previous.next
    if l1 is not None:
        previous.next = l1
    else:
        previous.next = l2

    return head.next


def mergeK_movies(movies_list):
    if len(movies_list) > 0:
        result = movies_list[0]
        for i in range(1, len(movies_list)):
            result = merge_two_lists(result, movies_list[i])
        return result
    return


if __name__ == '__main__':
    # Driver code
    a = create_linked_list([11, 41, 51])
    b = create_linked_list([21, 23, 42])
    c = create_linked_list([25, 56, 66, 72])

    print("All movie ID's from best to worse are:")
    display(mergeK_movies([a, b, c]))
