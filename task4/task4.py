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
    line = list(map(int, file.read().split()))

nums = line
nums.sort()
center = nums[len(nums) // 2]

index = 0

count = sum(abs(x - center) for x in nums)

if count >= 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(count)
