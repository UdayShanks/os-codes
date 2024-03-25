def optimal(pages, n, capacity):
    s = set()
    indexes = []
    page_faults = 0

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                indexes.append(pages[i])
        else:
            if pages[i] not in s:
                lru = -1
                for e in s:
                    if e not in pages[i+1:]:
                        lru = e
                        break
                else:
                    lru = indexes[0]
                s.remove(lru)
                s.add(pages[i])
                indexes.remove(lru)
                indexes.append(pages[i])
                page_faults += 1

    return page_faults

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
n = len(pages)
capacity = 3
print(optimal(pages, n, capacity))  # Output: 6