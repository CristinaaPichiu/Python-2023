"""
    Write a function that receives as parameters two lists a and b and returns a list of sets containing
    (list A intersected with B, A reunited with B, A - B, B - A)
"""


def operations(list1, list2):

    # create sets from the lists
    set_a = set(list1)
    set_b = set(list2)

    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    difference_a = set_a.difference(set_b)
    difference_b = set_b.difference(set_a)

    # return the results as a list of sets
    list3 = [intersection, union, difference_a, difference_b]
    return list3


if __name__ == "__main__":

  a = [1, 2, 3, 4, 5]
  b = [3, 4, 5, 6, 7]
  result = operations(a, b)
  print(result)
