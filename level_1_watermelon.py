


# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.



def solution(n):
    answer = "수박" * (n // 2)  # "수박"을 (n // 2)번 반복
    if n % 2 == 1:  # n이 홀수인 경우 "수"를 추가
        answer += "수"
    return answer



if __name__=='__main__':
    n = 1
    print(solution(n))