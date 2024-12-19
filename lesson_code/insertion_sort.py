def insertion_sort(array):
    if len(array) <= 1:
        return array
    else:

        answer = list()
        for new_insert in array:
            print("new insert = ", new_insert)
            is_insert = False
            if answer == list():
                print("ooo", answer)
                answer = [new_insert]
            else:

                for index, value in enumerate(answer):
                    print(index, value)
                    # print("in")
                    print(answer)
                    if new_insert < value:
                        print("insert")
                        answer = answer[:index] + [new_insert] + answer[index:]
                        # print(answer)
                        is_insert = True
                        break

                if is_insert == False:
                    print("back insert")
                    answer = answer + [new_insert]
                    # print(answer)

        return answer


ass = [40, 30, 60, 50, 20]

test = insertion_sort(ass)

print(test)
