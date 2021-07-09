coins = int(input())

if coins >= 6769:
    print(f'{coins // 6769} sheep')
elif coins >= 3848:
    print(f'{coins // 3848} cow' if coins // 3848 == 1 else f'{coins // 3848} cows')
elif coins >= 1296:
    print(f'{coins // 1296} pig' if coins // 1296 == 1 else f'{coins // 1296} pigs')
elif coins >= 678:
    print(f'{coins // 678} goat' if coins // 678 == 1 else f'{coins // 678} goats')
elif coins >= 23:
    print(f'{coins // 23} chicken' if coins // 23 == 1 else f'{coins // 23} chickens')
else:
    print('None')
