import math
from itertools import permutations


def generate_screen():
    line1 = '-' * 39
    line2 = '|' + ' ' * 9 + 'Roberto' + ' ' * 19 + ' ' * 2 + '|'
    line3 = '|' + ' ' * 37 + '|'
    line4 = '|' + ' ' * 9 + '5786' + ' ' * 24 + '|'
    line5 = '|' + ' ' * 37 + '|'
    line6 = '|' + ' ' * 9 + 'UNIFEI' + ' ' * 22 + '|'
    line7 = '-' * 39
    result = '\n'.join([line1, line2, line3, line4, line5, line6, line7])
    print(result)


generate_screen()


def calculate_circumference(radius):
    if 0 < radius < 10:
        result: float = 2 * math.pi * radius
        print(result)
    else:
        print("Invalid radius")


r = float(input('Enter the radius of the circle: '))
calculate_circumference(r)


def calculate_total_gdp_fluctuation(f1, f2):
    if -100 <= f1 and f2 <= 100:
        GDP = (float(f1) - float(f2)) / float(f2) * 100
        print(GDP)
    else:
        print("Invalid")


first_year = float(input('Enter the percentage of the first year: '))
second_year = float(input('Enter the percentage of the second year: '))
calculate_total_gdp_fluctuation(first_year, second_year)


def hIndex(citations):
    n = len(citations)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if citations[mid] == n - mid:
            return n - mid
        elif citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1
    return n - left


citations = [0, 1, 3, 5, 6]
result = hIndex(citations)
print(result)


def getHint(secret, guess):
    bulls = 0
    cows = 0
    secret_count = {}
    guess_count = {}
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            secret_count[s] = secret_count.get(s, 0) + 1
            guess_count[g] = guess_count.get(g, 0) + 1
    for digit in secret_count:
        if digit in guess_count:
            cows += min(secret_count[digit], guess_count[digit])
    return f"{bulls}A{cows}B"


print(getHint("1807", "7810"))
print(getHint("1123", "0111"))


def num_squares(n):
    if n <= 3:
        return n

    result = n
    for i in range(1, n + 1):
        temp = i * i
        if temp > n:
            break
        else:
            result = min(result, 1 + num_squares(n - temp))

    return result


def permutation(input_string):
    return [''.join(p) for p in permutations(input_string)]


def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    perms = permutation(s1)
    for perm in perms:
        if perm in s2:
            return True
    return False


print(check_inclusion("ab", "eidboaoo"))
