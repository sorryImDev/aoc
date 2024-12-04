class Solution:
    def isSafeReport(self, reportList: list[int]) -> bool:
        haveDecreases = haveIncreases = False

        for i in range(1, len(reportList)):
            diff = int(reportList[i]) - int(reportList[i - 1])
            absDiff = abs(diff)
            if absDiff not in [1,2,3]:
                return False
            else:
                if diff > 0:
                    haveIncreases = True
                elif diff < 0:
                    haveDecreases  = True
                else:
                    continue

        if haveDecreases is False and haveIncreases is False:
            return False
        else:
            return not (haveIncreases and haveDecreases)



        



solution = Solution()
with open("input.txt", "r") as file:
    safeReportCount = 0
    for line in file:
        report = line.split()
        # part 1
        # safeReportCount = safeReportCount + 1 if solution.isSafeReport(report) is True else safeReportCount

        # part 2
        if solution.isSafeReport(report):
            safeReportCount = safeReportCount + 1
        else:
            canStillBeSafe = False
            for i in range(len(report)):
                subReport = report[:i] + report[i+1:]
                canStillBeSafe = True if solution.isSafeReport(subReport) else canStillBeSafe
            safeReportCount = safeReportCount + 1 if canStillBeSafe else safeReportCount



    print(safeReportCount)
