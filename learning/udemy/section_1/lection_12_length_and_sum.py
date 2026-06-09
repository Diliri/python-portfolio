''' Length and sum of a list '''

grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

avarage = total / length
print(avarage)      # 86.25

# the SET is worst for collection of grades, because
# it can't have duplicates of grades !!! Set is { 80, 77, 100 } .
# so we should use sets only if we want to compare them two !