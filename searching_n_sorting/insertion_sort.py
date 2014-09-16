"Taking input from users"
items= [x for x in raw_input("Enter your numbers for insertion sort comma separated: ").split(',')]

for i in range(1,len(items)):
      "performing sorting"
      temp=items[i]
      j=i-1

      while ((temp<items[j]) and (j>=0)):
        items[j+1]=items[j]
        j=j-1

      items[j+1]=temp

print items