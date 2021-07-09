
def solution(array, commands):
    
    answer=[]
    for x in range(0,len(commands)):
        i=list(commands[x])[0]
        j=list(commands[x])[1]
        k=list(commands[x])[2]
        arr=sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer
    


a = [1, 5, 2, 6, 3, 7, 4]
b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,b))