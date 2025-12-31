def ex1(numbers: list[int]) -> int:
    return sum(numbers)

def ex2(numbers: list[int]) -> None:
    average = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return average, maximum, minimum

def ex3(numbers: list[int], exists: int) -> str:
    if exists in numbers:
        return "Yes"
    else:
        return "No"

def ex4(numbers: list[int], exists: int) -> int:
    if exists in numbers:
        return numbers.index(exists) + 1
    else:
        return -1

def ex5(numbers: list[int], exists: int) -> int:
    if exists in numbers:
        return len(numbers) - 1 - numbers[::-1].index(exists) + 1
    else:
        return -1

def ex6(numbers: list[int], exists: int) -> int:
    return numbers.count(exists)

def ex7(numbers: list[int], exists: int) -> list[int]:
    if exists in numbers:
        numbers.remove(exists)
        return numbers
    else:
        return numbers

def ex8(numbers: list[int], exists: int) -> list[int]:
    for i in range(len(numbers)):
        if numbers[i] == exists:
            numbers.pop(i)
    return numbers

def ex9(numbers: list[int]) -> set[int]:
    return set(numbers)

def ex10(numbers: list[int]) -> list[int]:
    return list(reversed(numbers))    

def ex11(numbers: list[int]) -> list[int]:
    return sorted(numbers)

def ex12(numbers: list[int]) -> int:
    return sorted(numbers, reverse=True)

def ex13(numbers_a: list[int], numbers_b: list[int]) -> list[int]:
    return list(set(numbers_a) & set(numbers_b))
    
def ex14(numbers_a: list[int], numbers_b: list[int]) -> int:
    return list(set(numbers_a) | set(numbers_b))
    
def ex15(numbers: list[int]) -> dict[int, int]:
    return {number: numbers.count(number) for number in numbers}
    

if __name__ == '__main__':
    #numbers_a = list(map(int, input("Enter numbers (list A): ").split()))
    numbers_a = [1, 2, 3, 4, 5, 6, 3]
    print("List A:", numbers_a)
    
    # print(f"Ex 1: {ex1(numbers_a)}")
    # print(f"Ex 2: {ex2(numbers_a)}")

    #exists = int(input("Enter the number: "))
    exists = 3
    # print(f"Ex 3: {ex3(numbers_a, exists)}")
    # print(f"Ex 4: {ex4(numbers_a, exists)}")
    # print(f"Ex 5: {ex5(numbers_a, exists)}")
    # print(f"Ex 6: {ex6(numbers_a, exists)}")
    # print(f"Ex 7: {ex7(numbers_a, exists)}")
    # print(f"Ex 8: {ex8(numbers_a, exists)}")
    # print(f"Ex 9: {ex9(numbers_a)}")
    # print(f"Ex 10: {ex10(numbers_a)}")
    # print(f"Ex 11: {ex11(numbers_a)}")
    # print(f"Ex 12: {ex12(numbers_a)}")

    #numbers_b = list(map(int, input("Enter numbers (list B): ").split()))
    numbers_b = [5, 3, 7, 1, 7, 2, 1]
    print("List B:", numbers_b)

    # print(f"Ex 13: {ex13(numbers_a, numbers_b)}")
    # print(f"Ex 14: {ex14(numbers_a, numbers_b)}")
    # print(f"Ex 15: {ex15(numbers_a)}")
