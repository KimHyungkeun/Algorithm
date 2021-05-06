# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    word_key = {}
    start = 97 # a~z 까지의 아스키코드 
    for n in h :
        # a ~ z 까지 각각 알파벳에 h리스트에 담긴 값들을 서로 매핑 시킨다
        word_key[chr(start)] = n
        start += 1 
    
    stack = []
    # word의 철자가 가진 값들을 스택에 넣는다.
    for w in word :
        stack.append(word_key[w])
    
    # 스택에 쌓인 값들중 가장 최대값을 스택 전체 갯수와 곱한다
    return max(stack) * len(stack)