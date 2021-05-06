dial = input()

dial_dict = { # 다이얼 목록을 딕셔너리로 정리
    3 : ['A','B','C'], 
    4 : ['D','E','F'],
    5 : ['G','H','I'],
    6 : ['J','K','L'],
    7 : ['M','N','O'],
    8 : ['P','Q','R','S'],
    9 : ['T','U','V'],
    10 : ['W','X','Y','Z']
}

times = 0 # 총 걸린 시간

for word in dial :
    for key,item in dial_dict.items() :
        if word in item : # 만약 다이얼 딕셔너리에, 해당하는 알파벳이 있으면  
            times += key # 그 다이얼까지 걸리는 시간을 더한다

print(times)
