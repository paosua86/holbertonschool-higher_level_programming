#!/usr/bin/python3

nums = [1, 2, 3]

for i in range(len(nums)):
    print(nums[i])

for i, n in enumerate(nums):
    print(i, n)

print("")

nums1 = [1, 2, 3]
nums2 = [4, 5, 7]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

nums3 = [1, 2, 3]
nums3.reverse()
print(nums3)

nums3 = [5, 6, 2, 1]
nums3.sort()
print(nums3)

nums3.sort(reverse=True)
print(nums3)

arr = ["bob", "nick", "pedro", "carlos"]
arr.sort(key=lambda x: len(x))
print(arr)

print("")
arr = [i+i for i in range(5)]
print(arr)


# grids

arr = [[1] * 4 for i in range(4)]
print(arr)

s = "abc"
print(s[0:2])


print(ord("a"))

strings = ["abc", "def", "ghi"]
print("".join(strings))
