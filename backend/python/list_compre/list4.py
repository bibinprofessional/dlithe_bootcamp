l=[[1,23,4],[32,3,45],[43,5,5]]
r=len(l)
c=len(l[0])

t_l=[[l[i][j] for i in range(r)] for j in range(c)]

print(t_l)