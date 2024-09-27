# The function should print numbers from 1 to 5, but it doesn't. Find the bug.
#for i in range(1, 5):  from my understanding if it goes from 1,5 it caps out at 5 for whatever reason I think its because the actual range from 1-5 is 4, so it only prints to 4. An easy fix is to just change to 1,6 so it has a range of 5
for i in range(1, 6):
    print(i)
