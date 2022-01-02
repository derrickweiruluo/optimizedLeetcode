'''
Remove len=k duplicates


Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

'''

# 'abba',  k = 2,  ""
# 'abbba', k = 2, 'aba'

# Notice that here we consider groups of elements with the same value which are adjacent. If we delete them, another symbols will become adjacent. Stack is just ideal for this purposes.

# So, we keep stack with pairs of elements: element itself and its frequency. Also I put in the beginning dummy variable, so I do not need to check if stack is empty. For each element we:

# Check if it is equal to the last element in stack, if it is, increase it frequency, if not - create new instance in stack with frequency 1.

# Check if we can delete groups of k equal elements: check if last frequency in stack is >=k and if it is, decrease it. Also if we get frequency equal to 0, delete element at all.

# Complexity
# It is just O(n) for time and space: we proceed every element at most twice: to put it to stack and to remove it from stack.


class Solution: # Both O(N)
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []                  # stack of [char, freq]
        
        for i, char in enumerate(s):
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            # check stack[-1][1]'s frequency before go to next index
            if stack[-1][1] == k:   # only buidling the char from freq 0 to k - 1
                stack.pop()         # so the stack[-1][1]'s frequency will never >= k
        
        return "".join(char * freq for char, freq in stack)



# FOllow-up:
'''Iteratively. 
Complexity Analysis
Time: O(n * n / k). We scan the entire string for each duplicte we find and remove.
Space: O(1) for the iterative approach.

string removeDuplicates(string s, int k, bool replaced = true) {
  while (replaced) {
    replaced = false;
    for (auto i = 1, cnt = 1; i < s.size() && !replaced; ++i) {
      if (s[i] != s[i - 1]) cnt = 1;
      else if (++cnt == k) {
        s = s.substr(0, i - k + 1) + s.substr(i + 1);
        replaced = true;
      }
    }
  }
  return s;
}'''
