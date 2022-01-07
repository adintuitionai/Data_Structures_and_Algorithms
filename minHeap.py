#Code for the min heap
#TC- Time Complexity
#SC - Space Complexity

import heapq

# create an array
minHeap = []

#Heapify the array to form Heap , TC - O(n) , SC - O(1)- because empty

heapq.heapify(minHeap)

# Adding the elements into the array, TC - O(logn), SC-O(n)

heapq.heappush(minHeap,5)
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,4)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,1)

#Printing the elements of the minheap - Output --->[1, 2, 4, 5, 3]

print("The minheap is",minHeap)

#Fetching the top element of the minheap, TC -O(1) Output --->1

peekNum = minHeap[0]
print("The peek Number:", peekNum)

#Deleting the top element from the Heap, TC - O(1), SC-O(1) Output --->1

popNum = heapq.heappop(minHeap)
print("The popped out number is", popNum)

#The top element after the deletion, TC - O(1), SC-O(1) Output --->2

print("The peek Number is", minHeap[0])

#All the elements of the minHeap Output --->[2, 3, 4, 5]

print("The minheap now is",minHeap)

#Size of the minHeap, TC - O(1), SC - O(1)  Output ---> 4

size = len(minHeap)
print("minHeap size is", size)

# Code Inspired from Heap Explorer card leetcode
#https://leetcode.com/explore/learn/card/heap/644/common-applications-of-heap/4028/


