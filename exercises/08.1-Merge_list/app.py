chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    newlist = []
    #Your code go here:
    for x in chunk_one:
        newlist.append(x)
    for x in chunk_two:
        newlist.append(x)
    return newlist

    
print(merge_list(chunk_one, chunk_two))
