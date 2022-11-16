def flatten (p):

    for x in p:
        if isinstance(x,list):
            flatten(x)
        else:
            newlist.append(x)


p =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

newlist=[]

flatten(p)

print(newlist)



def reverse (q):
    for i in range(len(q)):
        (q[i])=(q[i])[::-1]

q=[[1, 2], [3, 4], [5, 6, 7]]

print(ters(q))
