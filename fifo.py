def fifo(pages, frames):
    s = set()
    indexes = []
    page_faults = 0

    for i in range(len(pages)):
        if len(s) < frames:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                indexes.append(pages[i])
        else:
            if pages[i] not in s:
                s.remove(indexes[0])
                s.add(pages[i])
                indexes.pop(0)
                indexes.append(pages[i])
                page_faults += 1

    return page_faults
print("No of page faults with FIFO:")
pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
frames= 3
print(fifo(pages, frames))  # Output: 7