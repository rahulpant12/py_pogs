item=[x for x in raw_input("Enter your numbers for bubble sort comma separated:").split(',')]

for i in range(len(item)-1):
    for j in range(len(item)-i-1):
        if (item[j]>item[j+1]):
            temp=item[j]
            item[j]=item[j+1]
            item[j+1]=temp

print item