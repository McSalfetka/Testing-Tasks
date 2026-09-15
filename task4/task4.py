import argparse


parser = argparse.ArgumentParser(
        description='Выравнивание массива'
)
parser.add_argument(
    'list_info',
    help='Выравниевымый массив'
)
args = parser.parse_args()

with open(args.list_info, 'r') as file:
    line = list(map(int, file.readline().split()))

nums = line
nums.sort()
center = nums[len(nums) // 2]


index = 0
count = 0
while True:
    if center == nums[index]:
        index += 1

    if nums[index] > center:
        nums[index] -= 1
        count += 1
    elif nums[index] < center:
        nums[index] += 1
        count += 1

    repeats = 0
    for j in range(len(nums)):
        if nums[j] == center:
            repeats += 1
    if repeats == len(nums):
        print(count)
        break
    elif count == 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        break

print(nums)
