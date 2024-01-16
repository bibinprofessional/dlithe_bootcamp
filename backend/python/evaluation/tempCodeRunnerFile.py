def math_exp(e):

    e=e.replace('{','(').replace('}',')').replace('[','(').replace(']',')')
    try:
        a=eval(e)
        return 1
    except:
        return 0

example1 = '{(1+2)*3}+4'
example2 = '((1+2)*3*)'


print(math_exp(example1))  
print(math_exp(example2))  
