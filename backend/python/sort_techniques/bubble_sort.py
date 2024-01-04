from time import time 
  
  
def calc_time(fun): 
    def wrap_fun(*args, **kwargs): 
        t1 = time() 
        res = fun(*args, **kwargs) 
        t2 = time() 
        print(f"sec {t2-t1:.10f}") 
        return res
    return wrap_fun

@calc_time
def sort_fun(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# l_str=input('Enter the list :')
l_str='23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23,23,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,2323,234,234,435,5436,54645,43543,43,2343,543,543,546,56,67,67,68,45,3,4343432,423,4324,234,34,456456,54,6546,54,65,765,767,65,756,7,67,6,756,45634,534,34,32,342,3432,432,23,4,23234,34,324,32,4,3,43,4,32,4,324,32,4,32,432,4,32,4,32,43,24,3,4,32432,4,324,32,4,324,32,4,324,32,432,5,43,5,4,64,6,5,46,5,6,6,5,4,35,34,55,3424,324,32,4,32,432,43243,4352,324,432,23,4,32,4,325,43,5,345,34,6,54,654,7,5,6,54,34,532,432,324,324,32432,423432432432,54,35,35,34,5,34,53,456,4,6,54,6,4,5654,6,345435,34,5,34,53454,5,346,55,6,5464,32432432,4324,324,23,4,3243,4,32,4,324,3,5,435,3,5,43,5,345,34,5345,324,32,432432,4,32,4324,324,53,5,43,324,32,432,534,34,234,324,324,32,43,24,3,243,2,132,42,324,423,5,325,43,5,43,5,4,35345,345,34,5,345,34,5,4,34,45,4,543,345,456,345234,123,3243,24,3,53,45,4,5,45,4,6,4,6,54,6,54,65,76,345345,7,65,7,34543,43634,543,5,234,423,423,23,435,436,346,546,56,5,53,2432,4,234,23,4,2,32,4,32,4435,345,34,5,345,43,534,5,45,435,234,324,23'
l_str=l_str.replace(",,",",")
l=list(map(int, l_str.split(",")))
sorted_l=sort_fun(l)
print(sorted_l)
