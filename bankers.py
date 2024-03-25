def isSafe(processes, available, maxm, allot):
    need = [[0]*len(maxm[0]) for _ in range(len(processes))]

    for i in range(len(processes)):
        for j in range(len(available)):
            need[i][j] = maxm[i][j] - allot[i][j]

    finish = [0]*len(processes)
    safeSeq = [0]*len(processes)

    work = available.copy()
    count = 0
    while(count < len(processes)):
        found = False
        for p in range(len(processes)):
            if finish[p] == 0:
                for j in range(len(available)):
                    if need[p][j] > work[j]:
                        break
                else:
                    for k in range(len(available)):
                        work[k] += allot[p][k]
                    safeSeq[count] = p
                    count += 1
                    finish[p] = 1
                    found = True
        if not found:
            print("System is not in safe state \n")
            return False, []

    print("System is in safe state.\nSafe sequence is: ", end="")
    print(*[processes[i] for i in safeSeq])
    return True, safeSeq

processes = [0, 1, 2, 3, 4]
available = [3, 3, 2]
maxm = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

isSafe(processes, available, maxm, allot)