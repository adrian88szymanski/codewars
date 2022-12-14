'''
Write a function that returns all of the sublists of a list/array.

Example:

power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]power([1,2,3]); => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
For more details regarding this, see the power set entry in wikipedia.
'''


def power(a):
    result = [[]]
    for x in a:
        result.extend([subset + [x] for subset in result])
    return result