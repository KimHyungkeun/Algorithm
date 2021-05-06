# 210119 정답코드

def solution(routes):
    routes.sort(key = lambda x:x[1])
    camera = -100000
    count = 0

    for i in routes :
        print(i)
        if camera < i[0] :
            count += 1
            camera = i[1]
    
    # print(routes)
    return count

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]	
solution(routes)