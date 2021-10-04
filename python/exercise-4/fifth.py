inputData = [1, 6, -3, 45, 11, -67, 332, 885, 11, 4, 77, -5]

negativeList = [x for x in inputData if x < 0]
positiveList = [x for x in inputData if x > 0]

print("Negative List: ", negativeList, "Positive List: ", positiveList)
