"Find all the employees who directly or indirectly reports to manager"
result_count=[]
def get_me_the_children(root):
    if reverse_d.get(root,0) == 0:
        return
    for _ in reverse_d.get(root,0):
        if _== root:
            continue
        else:
            get_me_the_children(_)
            print(_,end=" ")
            result_count.append(_)

if __name__ == "__main__":
    input_d = {"A":"A","B":"A","C":"B","D":"B","E":"D","F":"E"}
    reverse_d={}
    result_count_dict = {}
    
    for key,values in input_d.items():
        reverse_d.setdefault(values,[])
        reverse_d[values].append(key)
    
    #reverse_d = {'A': ['A', 'B'], 'B': ['C', 'D'], 'D': ['E'], 'E': ['F']}
    
    for key,value in input_d.items():
        result_count=[]
        print(key,end=": ")
        get_me_the_children(key)
        result_count_dict[key] = len(result_count)
        print("")

    print(result_count_dict) #{'A': 5, 'B': 4, 'C': 0, 'D': 2, 'E': 1, 'F': 0}
    
    """output:
        A: C F E D B 
        B: C F E D 
        C: 
        D: F E 
        E: F 
        F:  
    """
