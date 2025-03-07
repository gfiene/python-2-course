nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

indexNum1 = 0
indexNum2 = 0

array = [0] * (len(nums1) + len(nums2))

while True:
    if nums1[indexNum1] > nums2[indexNum2]:
        array[indexNum1 + indexNum2] = nums2[indexNum2]
        indexNum2 += 1
    else: 
        array[indexNum1 + indexNum2] = nums1[indexNum1]
        indexNum1 += 1
    print(indexNum1, indexNum2, len(nums1), len(nums2))
    if indexNum2 >= len(nums2) or indexNum1 >= len(nums1):
        break

for indexNum2 in range(indexNum2, len(nums2)):
    array[indexNum2 + indexNum1] = nums2[indexNum2]
for indexNum1 in range(indexNum1, len(nums1)):
    array[indexNum2 + indexNum1] = nums1[indexNum1]
print (array)
