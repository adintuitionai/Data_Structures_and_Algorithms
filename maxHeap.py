#Code for the max heap
#TC- Time Complexity
#SC - Space Complexity

import heapq

# create an array
maxHeap = []

#Heapify the array to form Heap , TC - O(n) , SC - O(1)- because empty

heapq.heapify(maxHeap)

# Adding the elements into the array, TC - O(logn), SC-O(n)
#There is no maxHeap in python so in order to use minHeap as the maxHeap we multiply each entered number by -1 and that ways the Heap gives us the smallest negative number which in reality is our largest number

heapq.heappush(maxHeap,-1*5)
heapq.heappush(maxHeap,-1*3)
heapq.heappush(maxHeap,-1*4)
heapq.heappush(maxHeap,-1*2)
heapq.heappush(maxHeap,-1*1)

#Printing the elements of the minheap - Output --->[-5, -3, -4, -2, -1]

print("The minheap is",maxHeap)

#Fetching the top element of the minheap, TC -O(1) Output --->5
#we multiply the peek number with -1 to get the actual number that we want

peekNum = maxHeap[0]
print("The peek Number:", -1*peekNum)

#Deleting the top element from the Heap, TC - O(1), SC-O(1) Output --->-5
#we multiply the peek number with -1 to get the actual number that we want

popNum = heapq.heappop(maxHeap)
print("The popped out number is", -1*popNum)

#The top element after the deletion, TC - O(1), SC-O(1) Output --->-4
#we multiply the peek number with -1 to get the actual number that we want

print("The peek Number is", -1*maxHeap[0])

#All the elements of the minHeap Output --->[-4, -3, -1, -2]

print("The minheap now is",maxHeap)

#Size of the minHeap, TC - O(1), SC - O(1)  Output ---> 4

size = len(maxHeap)
print("minHeap size is", size)

# Code Inspired from Heap Explorer card leetcode
#https://leetcode.com/explore/learn/card/heap/644/common-applications-of-heap/4028/


