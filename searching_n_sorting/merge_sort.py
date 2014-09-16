item=[x for x in raw_input("Enter your numbers for merge sort comma separated:").split(',')]
def Merge_Sort(item):
    n=len(item)

    if (n<2):
        return

    mid=n/2
    left=[x for x in range(mid)]
    right=[x for x in range(n-mid)]

    for i in range(mid-1):
        left[i]=item[i]
    for i in range(mid,n):
        right[i-mid]=item[i]

    Merge_Sort(left)
    Merge_Sort(right)
    Merge(left,right,item)

def Merge(left,right,item):
    nl=len(left)
    nr=len(right)
    i=j=k=0
    while(i<nl and j<nr):
        if(left[i]<=right[j]):
            item[k]=left[i]
            i=i+1
            k=k+1
        else:
            item[k]=right[j]
            j=j+1
        k=k+1
    while(i<nl):
        item[k]=left[i]
        i=i+1
        k=k+1
    while(j<nr):
        item[k]=right[j]
        j=j+1
        k=k+1
Merge_Sort(item)
print item

