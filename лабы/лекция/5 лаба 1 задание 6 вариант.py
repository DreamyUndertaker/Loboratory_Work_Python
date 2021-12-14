arr = [x * x for x in range(11)] #generator array
arr1 = (x * x for x in range(11)) #link to generator

#for i in arr1:
#	print(i)

#for i in arr1:
#	print(i)
                    
print(max(arr1))