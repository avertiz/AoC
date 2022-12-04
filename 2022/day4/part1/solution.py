class Solution:

    def __init__(self) -> None:
        self.overlapCount = 0

    @staticmethod
    def getIdRangeList(sectionIds:str) -> list:
        sectionIds = sectionIds.split('-')
        return(sectionIds)

    @staticmethod
    def createIdRange(sectionIdTuple:list) -> list:
        sectionIdList = [i for i in range(int(sectionIdTuple[0]), int(sectionIdTuple[1])+1)]
        return(sectionIdList)

    def lineParse(self, line:str) -> list:
        line = line.strip().split(',')
        sectionIds1, sectionIds2 = self.getIdRangeList(line[0]), self.getIdRangeList(line[1])
        sectionIds1, sectionIds2 = self.createIdRange(sectionIds1), self.createIdRange(sectionIds2)
        return(sectionIds1, sectionIds2)

def main():
    solution = Solution()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        for line in lines:
            sectionIds1, sectionIds2 = solution.lineParse(line=line)
            overlap = all(elem in sectionIds1 for elem in sectionIds2) or all(elem in sectionIds2 for elem in sectionIds1)
            if overlap:
                solution.overlapCount += 1

    print(solution.overlapCount)

if __name__ == '__main__':
    main()
        
