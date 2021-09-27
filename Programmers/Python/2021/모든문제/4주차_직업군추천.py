def solution(table, languages, preference):
    answer = ''
    # print(table)
    
    # 업계별 언어 선호도 점수 딕셔너리
    company = {}
    for t in table :
        t_list = t.split()
        company[t_list[0]] = 0
    
    # print(company)

    # 업계별 언어 선호도를 테이블로 나타냄
    for t in table :
        t_list = t.split()
        key = t_list[0] # 업계 종류와 사용 언어들은 문자열로 되어있으므로, 리스트로 변환 하고 나면 가장 맨 앞이 업계명임
        
        t_list = t_list[1:]
        for i in range(len(languages)) :
            for j in range (len(t_list)) :
                # 해당 업계에서 쓰는 언어를 찾은 경우, preference와 해당 업계의 언어 선호도 점수를 곱한값을 더함
                if languages[i] == t_list[j] :
                    company[key] += preference[i] * (len(t_list) - j)
    
    # 모든 결과값을 알아낸 후, 선호도 점수별로 내림차순 정렬
    result = []       
    for key,val in company.items() :
        result.append((key, val))
    result.sort(key = lambda x : x[1], reverse=True)
    
    # 같은 점수결과가 나온 경우가 있을 수 있으므로, 이때는 사전순으로 정렬한다
    maximum = result[0][1]
    final_result = []
    for r in result :
        if r[1] == maximum :
            final_result.append(r)
        else :
            break
    
    # 결과 출력
    final_result.sort(key = lambda x : x[0])
    answer = final_result[0][0]
    return answer