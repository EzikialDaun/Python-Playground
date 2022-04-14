import random

# 로또 번호를 리스트로 생성하여 리턴
def create_lotto():
    min_value = 0
    max_value = 45
    max_digit = 6
    # 순서무관 랜덤 정수로 이루어진 리스트 리턴
    def create_random_list(digit, min_value, max_value):
        result = [i for i in range(min_value, max_value)]
        random.shuffle(result)
        result = result[0:digit]
        return result
    result = create_random_list(max_digit, min_value + 1, max_value + 1)
    return result

if __name__ == "__main__":
    print(create_lotto())
