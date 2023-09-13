# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


# solution 1
def solution(arr):
    answer = [arr[0]]  # 첫 번째 원소는 무조건 남기므로 미리 추가
    
    for num in arr[1:]:  # 두 번째 원소부터 시작
        if num != answer[-1]:  # 이전에 추가한 원소와 다르면 추가
            answer.append(num)
    
    return answer

# solution 2 
def solution(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a




def solution2(arr):
    answer = [arr[0]]

    for num in arr[1:]:
       if num != arr[-1]:
           answer.append(num)
    return answer

if __name__=='__main__':
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution2(arr))


