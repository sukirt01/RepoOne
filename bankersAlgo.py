class Process:
    def __init__(self, pid, allocated, maxNeed):
        self.pid = pid
        self.allocated = allocated
        self.maxNeed = maxNeed
        self.currentNeed = [0, 0, 0]
        for i in range(len(allocated)):
            self.currentNeed[i] = self.maxNeed[i] - self.allocated[i]
        print("Current Need of ", self.pid, " is ", self.currentNeed)

    def matrixAdditionOfAllocation(self, vector):
        sum = [0, 0, 0]
        for i in range(len(sum)):
            sum[i] = self.allocated[i] + vector[i]
        return sum

    def matrixSubtractionOfAllocation(self, vector):
        sum = [0, 0, 0]
        for i in range(len(sum)):
            sum[i] = vector[i] - self.allocated[i]
        return sum

    def isCurrentNeedSatisfied(self, vector):
        for i in range(len(vector)):
            if (self.currentNeed[i] > vector[i]):
                return False
        return True


if __name__ == "__main__":
    processQ = []
    processQ.append(Process(pid=1, allocated=[0, 1, 0], maxNeed=[7, 5, 3]))
    processQ.append(Process(pid=2, allocated=[2, 0, 0], maxNeed=[3, 2, 2]))
    processQ.append(Process(pid=3, allocated=[3, 0, 2], maxNeed=[9, 0, 2]))
    processQ.append(Process(pid=4, allocated=[2, 1, 1], maxNeed=[4, 2, 2]))
    processQ.append(Process(pid=5, allocated=[0, 0, 2], maxNeed=[5, 3, 3]))

    # intial Declaration
    totalResources = [10, 5, 7]

    totalAllocation = [0, 0, 0]

    for p in processQ:
        totalResources = p.matrixSubtractionOfAllocation(vector=totalResources)

    iterations = 0
    while (processQ):
        processToBeRemoved = []
        if (iterations > len(processQ)):
            print("DeadLock Encountered !!")
            pass
        for proc in processQ:
            if (proc.isCurrentNeedSatisfied(totalResources)):
                print("Process", proc.pid, " -> ", end="")
                totalResources = proc.matrixAdditionOfAllocation(
                    totalResources)
                processToBeRemoved.append(proc)
                iterations = 0
            else:
                iterations += 1
        for p in processToBeRemoved:
            processQ.remove(p)
    if (iterations == 0):
        print("Safe Sequence Generated")
