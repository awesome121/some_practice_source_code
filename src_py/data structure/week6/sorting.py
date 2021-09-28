def load_file(file_name):
    """ Reads integers from a file.
    The file should have one integer per line """
    data_list = []
    with open(file_name) as infile:
        lines = infile.readlines()
    for line in lines:
        number = int(line.strip())
        data_list.append(number)
    # a simpler way would be:
    # data_list = [int(line) for line in lines]
    return data_list



def selection_sort(file_name):
    """ Loads numbers from the given file and returns them as a sorted list.
    The numbers are sorted using selection sort - surprise, surprise!
    """
    alist = load_file(file_name)
    n_comps = 0
    for fillslot in range(len(alist)-1, 0, -1):
        index_of_max  = 0
        for location in range(1, fillslot+1):
            n_comps += 1
            if alist[location] > alist[index_of_max]:
                index_of_max = location
        alist[fillslot], alist[index_of_max]  = alist[index_of_max], alist[fillslot]
    
    # Note: you will need to count the comparisons
    print(alist)
    print('Selection sort on {}, {} items'.format(file_name, len(alist)))
    print('  Used {} comparisons.\n'.format(n_comps))
    return alist

#selection_sort('file0.txt')



def insertion_sort(file_name):
    """ Loads numbers from the given file and returns them as a sorted list.
    The numbers are sorted using insertion sort - surprise, surprise!
    """
    n_comps = 0
    alist = load_file(file_name)
    for index in range(1, len(alist)):
        stop = False
        currentvalue = alist[index]
        position = index
        while position > 0 and not(stop):
            n_comps += 1
            if alist[position-1] > currentvalue:
                alist[position] = alist[position-1]
                position = position - 1
            else:
                stop = True
        alist[position] = currentvalue
    # Note: you will need to count the comparisons
    print('Insertion sort on {}, {} items'.format(file_name, len(alist)))
    print('  Used {} comparisons.\n'.format(n_comps))
    return alist




def gap_insertion_sort(alist, start, gap, n_comps):
    """In-place insertion sort on alist with given start and gap."""
    for i in range (start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        stop = False
        while position >= gap and not(stop):
            n_comps += 1
            if alist[position-gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            else:
                stop = True
        alist[position] = currentvalue
    return n_comps



def shell_sort(file_name):
    """ Runs shell sort with gap starting at n//2 and then gap = gap //2 etc """
    alist = load_file(file_name)
    gap = len(alist) // 2
    n_comps = 0
    gaplist = []
    while gap > 0:
        for startposition in range(gap):
            n_comps = gap_insertion_sort(alist, startposition, gap, n_comps)
        # build a list of gaps used as we go
        gaplist.append(gap)
        gap = gap // 2
    # Note: you will need to count the comparisons
    print('Shell sort on {}, {} items, '.format(file_name,len(alist)))
    print('  Used {} comparisons.'.format(n_comps))
    print('    Gaps were {}\n'.format(gaplist))
    return alist

def shell_sort2(file_name, gaplist):
    """ Receives a list of gaps and runs shell sort with those gaps
    If a gap is greater than the number of items then ignore and move to the next.
    """
    alist = load_file(file_name)
    n_comps = 0
    # ---start student section---
    for gap in gaplist:
        if gap <= len(alist):
            for startposition in range(gap):
                n_comps = gap_insertion_sort(alist, startposition, gap, n_comps)
    # ===end student section===
    print('Shellsort2 with gap list on {}, {} items'.format(file_name, len(alist)))
    print('  Used {}  comparisons.'.format(n_comps))
    print('    Gaps were {}: \n'.format(gaplist))
    return alist

print(shell_sort2('', [50, 25, 10, 1]))

