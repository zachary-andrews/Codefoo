def add_list():
    f2 = open("./list.txt", 'r')
    total = 0
    listouts = []
    for line in f2.readlines():
        total = total + int(line)
        if check_output(total,listouts):
            exit()

def check_output(output,listouts):
    if output in listouts:
        print output
        return True
    else:
        listouts.append(output)
        return False
        
add_list()