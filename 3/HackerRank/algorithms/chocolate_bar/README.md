#Problem
You are given a choclate bar (1d list) with varying sweetnes (ints). Find the most amenable solution.


## Thoughts
Ye olde bin packing. The idea of 'even division' at a high level should always reek of an NP problem. 
So a first approximate approach is:
 0. Check to see if the list is equal (in case you're done) or unable to be split (ie groups>array items) 
 1. find the smallest number
 2. Add that entry to it's smallest neighbor
 3. Remove the entry from the list