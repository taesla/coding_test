
def solution(participant, completion):
    
    p_dict = dict()
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
            
        else : 
            p_dict[p] = 1
    
    for c in completion:
        if c in p_dict:
            p_dict[c] -= 1

    

    answer = [key for key,value in p_dict.items() if value >0]        
    if answer !=[]:
        return answer[0]
    return ""

    

a=["leo", "kiki", "eden"]
b=["eden", "kiki"]
print(solution(a,a))
print('=============================')
print(solution(a,b))