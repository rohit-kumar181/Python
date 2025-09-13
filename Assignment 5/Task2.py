orgList = [i for i in range(1, 11)]
print("Original List:",orgList)

extList = [orgList[i] for i in range(0, 5)]
print("Extracted first five elements:",extList)

extList.reverse()
print("Reversed extracted elements:",extList)
