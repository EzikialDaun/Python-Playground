def print_triangle():
    max_width = int(input("홀수인 정수를 입력하세요. ==> "))
    max_height = int(max_width / 2) + 1

    #     *
    #    ***
    #   *****
    #  *******
    # *********

    # 삼각형
    for i in range(0, max_height):
        front = " " * (max_height - 1 - i)
        mid = "*" * (2 * i + 1)
        back = " " * (max_height - 1 - i)
        result = front + mid + back
        print(result)

    print("")

    # 역삼각형
    for i in range(0, max_height):
        front = " " * i
        mid = "*" * (max_width - (2 * i))
        back = " " * i
        result = front + mid + back
        print(result)

if __name__ == "__main__":
    print_triangle()
