def median(arr, brr):
    l=[]
    n = len(arr)+ len(brr)

    for i in range(n):
        if len(arr)>0 and len(brr)>0:
            if brr[0]<arr[0]:
                l.append(brr[0])
                brr.pop(0)
            else:
                l.append(arr[0])
                arr.pop(0)

        else:
            if len(arr)>0:
                l.extend(arr)
                break
            elif len(brr)>0:
                l.extend(brr)
                break

    if n%2==0:
        return min(l[(n//2)-1],l[n//2])
    else:
        return l[n//2]


arr = [1, 2]
brr = [1, 4]

print(median(arr, brr))

