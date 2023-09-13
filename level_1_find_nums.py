

def solution(numbers):
    answer = []
    for i in range(10):  # 0부터 9까지의 숫자를 순회합니다.
        if i not in numbers:  # 숫자 i가 numbers 리스트에 없는 경우
            answer.append(i)   # i를 answer 리스트에 추가합니다.

    return sum(answer)

if __name__ == "__main__":
    num = [1, 2, 4, 5, 7, 9]
    print(solution(num))