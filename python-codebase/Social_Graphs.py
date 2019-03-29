def socialGraphs(counts):
    # Write your code here
    i, cmap, sl = 0, {}, []
    sl = []
    while i < len(counts):
        count = counts[i]
        if count not in cmap:
            cmap[count] = []
        cmap[count].append(i)
        maplist = cmap[count]
        if len(maplist) == count:
            sl.append(maplist)
            cmap[count] = []
        #
        # if len(maplist) == 0 or len(maplist[-1]) == count:
        #     cmap[count].append([])
        #     if not len(maplist) == 0:
        #         sl.append(maplist[-1])
        i += 1

    for l in sl:
        for ele in l:
            print ele,
        print ''


counts = [2,2,3,3,1,2,2,2,2,3]
socialGraphs(counts)
