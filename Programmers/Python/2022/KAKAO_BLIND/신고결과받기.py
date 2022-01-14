def solution(id_list, report, k):
    ans = [0] * len(id_list)
    
    # 신고자와 신고할 id를 모아놓은 딕셔너리
    id_dict = {id:[] for id in id_list}
    # 각 id별 신고받은 횟수
    id_report_cnt = {id:0 for id in id_list}
    
    # 신고자와 신고할 id를 전부 입력한다
    for r in report :
        reporter, reported = r.split()[0], r.split()[1]
        if reported not in id_dict[reporter] :
            id_dict[reporter].append(reported)
            id_report_cnt[reported] += 1
    
    # k번 이상 신고받은 id만 따로 추려낸다
    final_reported = []
    for key in id_report_cnt.keys() :
        if id_report_cnt[key] >= k :
            final_reported.append(key)
    
    # 각 신고자들이 신고한 id들 중에서 k번 이상 신고받은 id가 포함되는 경우 당, 그 신고자들에게 메일이 1통씩 날아오게 된다 
    for i in range(len(id_list)) :
        for j in final_reported :
            if j in id_dict[id_list[i]] :
                ans[i] += 1
    return ans