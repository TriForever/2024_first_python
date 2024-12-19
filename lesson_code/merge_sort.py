import math


def merge(left, right):

    print(f"merge ,left ={left},right={right}")
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            x = left.pop(0)
            result.append(x)
        else:
            x = right.pop(0)
            result.append(x)

    if len(left) > 0:
        result = result + left
    else:
        result = result + right
    return result


def merge_sort(numbers):
    print(f"Level: {int(math.log2(len(numbers)))}", numbers)
    if len(numbers) <= 1:
        return numbers
    else:
        mid_index = len(numbers)//2
        left_part = numbers[:mid_index]
        right_part = numbers[mid_index:]
        sorted_left_part = merge_sort(left_part)
        sorted_right_part = merge_sort(right_part)
        result = merge(sorted_left_part, sorted_right_part)
        # print(f"Level {int(math.log2(len(result)))} completed:", result)
        return result


if __name__ == "__main__":
    numbers = [30, 10, 40, 70, 50, 90, 60, 20]
    result = merge_sort(numbers)
    print(result)
