# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

inputData = input('introdu data sub forma : dd,mm,yyyy')
print('new date : ', str.replace(inputData, ',', '/'))
