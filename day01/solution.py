

class Solution:
    def partOne(self, listOne: list[int], listTwo:list[int]):
        listOne_sorted = sorted(listOne)
        listTwo_sorted = sorted(listTwo)
        sum = 0
        if (len(listOne_sorted) >= len(listTwo_sorted)):
            shorterList = listTwo_sorted
            longerList = listOne_sorted
        else:
            shorterList = listOne_sorted
            longerList = listTwo_sorted
        
        for index, element in enumerate(shorterList):
            sum += abs(int(element) - int(longerList[index]))

        return sum
    
    def partTwo_similarity(self, listOne: list[str], listTwo:list[str]):
        listOne_Hash = dict.fromkeys(set(listOne), 0)
        listTwo_Hash = dict.fromkeys(set(listTwo), 0)
        similarity= 0
        
        for i in listTwo:
            try:
                listOne_Hash[i] += 1
            except KeyError:
                continue

        for key in listOne_Hash.keys():
            similarity += int(key) * listOne_Hash[key]


        return similarity



solution = Solution()
listOne = []
listTwo = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = line.split()
        listOne.append(left)
        listTwo.append(right)

solution = Solution()
print(solution.partTwo_similarity(listOne, listTwo))
# print(solution.partOne(listOne, listTwo))
        


