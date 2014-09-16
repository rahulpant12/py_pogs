"Slection sorting"
items=[x for x in raw_input("Enter your numbers for selection sort comma separated:").split(',')]

for i in range(len(items)):

    for j in range(i+1,len(items)):

        if (items[i]>items[j]):

            temp=items[i]
            items[i]=items[j]
            items[j]=temp

print items