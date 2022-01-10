'''
For each person i, preferences[i] contains a list of friends 
sorted in the order of preference. 
In other words, 
a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.


All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.


'''




# Clarifications:
# Each person is contained in exactly one pair.
# Even Paris
# preferences[i] does not include i 


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        '''
        Create dictionary using each friend as keys and a list of people they are closer to than the person they are paired with as values. 
        This can be done using [:index(y)].
        Then convert to set for O(1) lookup

        Then use nested for loop to find when people are on each other's list.
        '''
        
        # 存储 每一个pair， x: y, for x, who are preferred over y
        # memo 是双向的， y: x 同理
        memo = {}  # "more-prefer" list
        
        for x, y in pairs:
            memo[x] = set(preferences[x][:preferences[x].index(y)])
            memo[y] = set(preferences[y][:preferences[y].index(x)])
        
        res = 0
        
        for x in memo:
            for y in memo[x]:
                if x in memo[y]:
                    res += 1   # y is unhappy
                    break
        
        return res