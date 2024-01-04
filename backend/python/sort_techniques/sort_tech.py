class sort_tech:
    def __init__(self,l):
        self.l=l


    def bubble_sort(self):
        for i in range(len(self.l)-1):
            for j in range(len(self.l)-i-1):
                if self.l[j]>self.l[j+1]:
                    self.l[j],self.l[j+1]=self.l[j+1],self.l[j]

        return l
    
    def merge_sort(self):
        if len(self.l) > 1:
 
            m = len(self.l)//2
            l_half1 = self.l[:m]
            l_half2 = self.l[m:]
 
            print(l_half1)
            print(l_half2)
            print('11111111111111111111')
            s1=sort_tech(l_half1)
            s1.merge_sort()
            print(l_half1)
            print(l_half2)
            print('22222222222222222222222')
            s2=sort_tech(l_half1)
            s2.merge_sort()
            print(l_half1)
            print(l_half2)
            print('33333333333333333333333333333')



l=[20,32,4,23,2,12,1,56]
s=sort_tech(l)

print(s.bubble_sort())

