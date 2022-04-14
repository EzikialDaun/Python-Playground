# 자릿수(digit)를 입력받아서
# 정수로 이루어진 리스트의 리스트로 리턴하는 함수
# 1. 숫자는 서로 달라야하며
# ex) 122 => skip
# 2. 이미 생성된 숫자의 조합은 자릿수 무관하게 불가능하다.
# ex) 789가 있을 경우 987은 skip
# ex) 123이 있을 경우 231은 skip
# 각 결과의 범위는 0 ~ (10 ^ digit)
def create_unique_number(digit):
    max_num = pow(10, digit)
    result = []
    for i in range(0, max_num):
        # 자릿수를 쪼개서 리스트로 만드는 함수
        # ex) 345 => [3, 4, 5]
        temp = [int(j) for j in str(i)]
        # 현재 수의 자릿수가 제시된 자릿수보다 작으면 맨 앞에 0 삽입
        # ex) 12 => 012
        while len(temp) < digit:
            temp.insert(0, 0)
        # set으로 전환한 리스트의 길이와 원래 리스트의 길이가 다르면 skip
        # 숫자에 중복이 있는지 체크
        # ex) 122 => skip
        if len(temp) != len(set(temp)):
            continue
        # 지금까지 나온 결과를 순회하여
        is_duplicated = False
        for j in result:
            # 같은 숫자들의 조합으로 이루어진 리스트가 있는지 체크
            # 두 리스트를 정렬하여 같은지 체크
            # ex) 789, 987 => skip
            if sorted(j) == sorted(temp):
                is_duplicated = True
                continue
        # 중복이 없으면 결과에 삽입
        if is_duplicated == False:
            result.append(temp)
    return result

# 본 파일에서 실행되었을 때 동작
# 다른 파일에서 import하여 실행했을 때에는 동작하지 않음.
if __name__ == "__main__":
    # 자릿수로 지정
    result = create_comb(3)
    # 출력
    for i in result:
        print(i)
