
num_arrests = int(input("Prior arrests: "))
local_ord = input("Prior arrests for local ordinance (Y/N): ")
age_at_r = int(input("Age at realease: "))

score = 0

if num_arrests >= 2 and num_arrests < 5:
    score += 1
if num_arrests >= 5:
    score += 1
if local_ord == 'Y':
    score += 1
if age_at_r >= 18 and age_at_r <= 24:
    score += 1
if age_at_r >= 40:
    score += -1

print(f"The recidivism risk score is {score}")
    
