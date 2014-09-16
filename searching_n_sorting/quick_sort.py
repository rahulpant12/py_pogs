item=[x for x in raw_input("Enter your numbers for quick sort comma separated:").split(',')]
def quick (item,left,right):

    if left<right:
        pivot=left
        i=left
        j=right

        while (i<j):
            while (item[i]<=item[pivot] and i<j):
                i=i+1
            while (item[j]>item[pivot]):
                j=j-1
            if (i<j):
                temp=item[i]
                item[i]=item[j]
                item[j]=temp


        temp=item[pivot]
        item[pivot]=item[j]
        item[j]=temp

        quick (item,left,j-1)
        quick (item,j+1,right)

quick(item,0,len(item)-1)
print item,