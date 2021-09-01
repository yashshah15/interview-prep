def mergeSort(start,end):
    if start<end:
        mid=int((start+end)/2)
        mergeSort(start,mid)
        mergeSort(mid+1,end)
        merge(start,end,mid)

def merge(start,end,mid):
    b=[0]*(end-start+1)
    i=start
    j=mid+1
    k=0
    while i<=mid and j<=end:
        if a[i]<a[j]:
            b[k]=a[i]
            k=k+1
            i=i+1
        else:
            b[k]=a[j]
            j=j+1
            k=k+1
    while i<=mid:
        b[k]=a[i]
        i=i+1
        k=k+1
    while j<=end:
        b[k]=a[j]
        j=j+1
        k=k+1
    for i in range(start,end+1):
        a[i]=b[i-start]

a=[int (i) for i in input("Enter numbers").split()]

mergeSort(0,len(a)-1)
for i in a:
    print(i,end=" ")