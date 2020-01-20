def bubbleSort(arr):
    for i in range(1,len(arr)):
        print("\ti= "+str(i)+" ")
        for j in range(0,len(arr)-i):
            print("j= "+str(j)+" ")
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[i]
    return arr
arr = [2,45,65,3,5,43,56]

print (bubbleSort(arr))
