import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, width = max_width)
    ans = ""
    for r in result :
        ans += (r+"\n")
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)