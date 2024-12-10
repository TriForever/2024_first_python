def my_buble_sort(num_list:list , is_log = False):
  n = len(num_list)
  for round in range(n - 1):
    for index in range(len(num_list) - 1 - round):
      if num_list[index] > num_list[index + 1]:
          num_list[index],num_list[index + 1] = num_list[index + 1],num_list[index]
    print(round,num_list) if is_log else None
  print(num_list) if is_log else None
  return num_list


def my_selection_sort(num_list:list , is_log = False):
  n = len(num_list)
  for round in range(n - 1):
    min_index = round
    for index in range(round + 1,len(num_list)):
      if num_list[index] < num_list[min_index]:
          min_index = index
    if min_index != round:
      num_list[round],num_list[min_index] = num_list[min_index],num_list[round]

    print(round,num_list) if is_log else None
  print(num_list) if is_log else None
  return num_list


if __name__ == "__main__":
  print("main = sort_algorithm")
  num_list = [7,9,10,4,2,6]
  print(f" bubble sort :",my_buble_sort(num_list))
  print(f" selection sort :",my_selection_sort(num_list))
else:
  print(__name__)