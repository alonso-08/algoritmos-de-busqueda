def search_binary(target,sorted_list):
    min_index=0
    max_index=len(sorted_list)-1

    while min_index<=max_index:
        middle_index=(min_index+max_index)//2

        if sorted_list[middle_index]==target:
            return middle_index
        
        if sorted_list[middle_index]<target:
            min_index=middle_index+1
        else:
            max_index=middle_index-1

    return -1


#nota
print(search_binary(3,[2,3,4,5,7,8]))
            
        


    