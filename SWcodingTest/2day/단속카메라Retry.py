# 210119 정답코드

def solution(routes):
    routes.sort(key = lambda x:x[1])
    # print(routes)
    camera = -100000
    count = 0

    for i in routes :
        print(i)
        if camera <= i[0] :
            count += 1
            camera = i[1]
    
    # print(routes)
    print(count)
    return count

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]	
# routes = [[1,2], [2,3], [3,4], [4,5]]
solution(routes)


# times = [[0,86399]] * 100000
# time_range = {i:0 for i in range(86400)}

# for t in times :
#     for i in range(t[0], t[1]+1) :
#         time_range[i] += 1