# Problem
You are given a choclate bar (1d list) with varying sweetnes (ints). Find the solutoin which is evenly distributed and has the highest low number.


## Thoughts
Ye olde bin packing. The idea of 'even division' at a high level should always reek of an NP problem. 
So a first approximate approach is:
0. Check to see if the list is equal (in case you're done) or unable to be split (ie groups>array items) 
1. find the smallest number 
    * Runtime: n on the first try as the list is unordered. A dictionary could be used to make future looksups=1
2. Add that entry to it's smallest neighbor
    * If neighbors are equal, compare the stdev of both sides.
        * This is cute optimization made after the fact, but it also ensures that our function work consistent when passed intput forward and backwards. As the same candy should always have the same splits.
3. Remove the entry from the list
