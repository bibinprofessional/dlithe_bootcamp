def reduce(num):
    while True:
        if len(str(num))>2:
            rem=num%10
            num//=10
            num+=rem

        else:
            break
    
    return num

# l=[12345,456723,23213,76543,652321]
# l=[111,100,215]
# l=[400,120,3286]
# l=[123,777,890]
# l=[124,526,43347,9914,661,41,378]
l=[1234,1234,1234]

val=0
for i in l:
    val=reduce(val+i)
print(val)
