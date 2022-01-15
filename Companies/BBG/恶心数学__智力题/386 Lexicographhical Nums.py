'''
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
    
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:           # 如果不超出，先一直 *= 10
                cur = cur * 10
            else:
                if cur + 1 > n:         #  降一位数
                    cur = cur // 10
                cur += 1                # 升一位 to next greater
                while cur % 10 == 0:    # start from 个位数 next greater
                    cur = cur // 10
            
        return res




class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = [None] * n
        cur = 1
        for i in range(n):
            res[i] = cur
            
            # 先测进十位数，因为这样lexico最小
            if cur * 10 <= n:
                cur = cur * 10
            # 不行的话，先测室 + 1
            else:
                # 如果 + 1 都超出，那么取 //=10
                if cur + 1 > n:
                    cur = cur // 10
                
                # regardless，这一步都是要走的
                cur += 1
                # 如果新数字是10的倍数，那么我们要取他的个位数数值
                # 例如 19 -> 2 -> 20
                while cur % 10 == 0:  
                    cur = cur // 10
        return res
    
    
#         研究序列[1,10,11,12,13,2,3,4,5,6,7,8,9]，找出字典序的规律。

#         规律1：不考虑上限，元素1后面跟什么元素？10, 100 … 也就是不断乘以10。

#         规律2：如果99是上限，那么10后面的元素不能是100了，该怎么办？答案是11，也就是加1，这样个位上的数变大了。如果加1导致进位的话，虽然个位数变0，但十位上的数会变大，总之肯定字典序往后移。但此时得到的并不是下一个的目标，因为把其末尾的0去掉会得到字典序相对更前的数。砍掉0之后就可以重复规律1的操作了。

#         规律3：如果上限是19，那么19后面的元素就不能是20了，该怎么办？答案是将19除以10，然后再重复规律2（也就是加1），也就是得到2，之后又可以重复规律1了。