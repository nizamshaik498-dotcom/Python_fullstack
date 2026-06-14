#LIST

empty=[]
marks=[85,92,78,95,88]
mixed=[1,"hello",3.14,True]
print(marks[0])
print(marks[-1])
print(marks[1:4])
print(marks[::-1])
print(len(marks))
print(92 in marks)



marks[2]=82
marks.append(75)
marks.insert(8,100)
marks.extend([70,65])
marks.sort()
marks.sort(reverse=True)
marks.reverse
marks.remove(75)
popped=marks.pop()
popped2=marks.pop(0)
del marks[1]
marks.clear()
scores=[90,85,92,85]
print(scores.count(85))
print(scores.index(92))
copy=scores.copy()
print(sorted(scores))

