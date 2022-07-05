dic = {'Janet': 87, 'Logan': 62, 'Whitaker': 46, 'Alyssa': 100, 'Stef': 80, 'Jeff': 88, 'Kim': 52, 
'Sylvia': 95}
dic2 = {'Logan': 62, 'Kim': 52, 'Whitaker': 52, 'Jeff': 88, 'Stef': 80, 'Brian': 60, 'Lisa': 83,
 'Sylvia': 87}


def intersect(dic,dic2):
    newDic = {}
    for i in dic:
        for j in dic2:
            if i == j:
                if dic2[j] == dic[i]:
                    newDic[j] = dic2[j]
                
    return newDic


        
        
    
        
            
            

print(intersect(dic,dic2))
    
