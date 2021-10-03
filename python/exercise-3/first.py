idata = ["Developia", 4, "Lesson", 3.4, 'Yes', False]

indexLesson = idata.index("Lesson")
indexNum = idata.index(3.4)

idata[indexLesson] = 3.4
idata[indexNum] = "Lesson"

print(idata)
