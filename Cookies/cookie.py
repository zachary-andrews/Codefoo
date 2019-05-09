children = [1,2,1]
cookies = [1,2,3]

cookies.sort(reverse = True)
children.sort(reverse = True)
count = 0
while cookies and children:
    if cookies[-1] >= children[-1]:
        count +=1
        cookies.pop()
        children.pop()
    else:
        children.pop()
print count