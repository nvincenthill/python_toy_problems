# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e

# tests


print(find_uniq([1, 1, 1, 2, 1, 1]) == 2)
print(find_uniq([0, 0, 0.55, 0, 0]) == 0.55)
print(find_uniq([3, 10, 3, 3, 3]) == 10)
