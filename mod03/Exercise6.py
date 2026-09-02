import random

digit3_1, digit3_2, digit3_3, = random.randint(0,9), random.randint(0,9), random.randint(0,9)
digit4_1, digit4_2, digit4_3, digit4_4 = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)


print(f"3-digit code: {digit3_1}{digit3_2}{digit3_3}")
print(f"4-digit code: {digit4_1}{digit4_2}{digit4_3}{digit4_4}")