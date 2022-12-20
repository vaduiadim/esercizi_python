def merge_lists(l1, l2):
    merged_list = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1
    return merged_list