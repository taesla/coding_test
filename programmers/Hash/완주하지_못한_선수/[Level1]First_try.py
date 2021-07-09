def solution(participant, completion):
    
    ans1 = {}
    for i in participant:
        if i not in ans1:
            ans1[i] = 1
        else :
            ans1[i] = ans1[i]+1
    ans2 = dict.fromkeys(completion,1)

    #ans = set(ans1).intersection(set(ans2))
    ans_key = [x for x in list(ans1.keys())if x not in list(ans2.keys()) ]
    ans_value = [x for x in list(ans1.values()) if x not in list(ans2.values())]
    if ans_value==[] :
        return ans_key[0]
    else :
        for key, value in ans1.items():
            if [value] == ans_value:
                return key
                
            #return key , value
    return ans_key, key
    

    #return ans

a=["leo", "kiki", "eden"]
b=["eden", "kiki"]
print(solution(a,b))