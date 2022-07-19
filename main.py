# My case
def solution(number):
    results = 0

    if number > -1:
        for x in range(1, number):
            if x % 3 == 0 or x % 5 == 0:
                results = x + results

    return results


# Best case
def solution_bc(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution(10))
