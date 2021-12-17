'''  SD Questions
Design Venmo
Design AB testing
OOD/Coding: Decision Tree实现
Design 付款系统
'''




'''Q1  + 6
https://www.1point3acres.com/bbs/thread-821210-1-1.html
https://www.1point3acres.com/bbs/thread-810853-1-1.html
https://www.1point3acres.com/bbs/thread-795276-1-1.html

2. 地里高频题 {{'a','b','c'},{'b','c','d'},{'c','d','e'}} 找到与每个字符（原题为String）出现最频繁的其他字符
a -> b,c
b -> c
c -> c,d
e -> c,d

e.g. [['Casper', 'Purple', 'Wayfair'],['Purple',‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌ 'Wayfair', 'Tradesy'],['Wayfair', 'Tradesy', 'Peloton']]

 [['Casper', 'Purple', 'Wayfair'],['Purple', 'Wayfair', 'Tradesy'],['Wayfair', 'Tradesy', 'Peloton']] =>
  {
    'Casper': ['Purple', 'Wayfair'],
    'Purple': ['Wayfair'],
    'Wayfair': ['Purple', 'Tradesy'],
    'Tradesy': ['Wayfair'],
    'Peloton': ['Wayfa‍‍‌‌‌‍‌‌‌‍‌‌‍‍‌‌ir', 'Tradesy']
'''
import collections
arr = [['a', 'b', 'c'],['b', 'c', 'd'], ['c', 'd', 'e']]

graph = collections.defaultdict(collections.Counter)
# counter = collections.Counter()
for lst in arr:
    counter = collections.Counter(list(set(lst)))
    for elem in counter:
        counter[elem] -= 1
        graph[elem] += counter
        counter[elem] += 1
    print(counter)


print(graph)

for elem in graph:
    max_value = max(graph[elem].values())
    res = [k for k,v in graph[elem].items() if v == max_value]
    # print(max_value)
    print(elem, "-->", res)



# Undirected graph 解法




''' Q3 +3  OOD Questions
https://www.1point3acres.com/bbs/thread-807416-1-1.html

wo player card game "war", 给52张（value: [1,52]）卡牌分别随机分给两个人，两个人看不到自己的牌，每轮比大小，胜者得一分；比分判断输赢
edge case：如果得分一样，手上拥有最大卡牌的胜利。
further：player不止两个人‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌的时候怎么改代码？
'''
def getRoundResult(winning_suit, suit1, number1, suit2, number2):
    win1, win2, draw = "Player 1 wins", "Player 2 wins", "Draw"
    
    if suit1 == suit2:
        if suit1 == winning_suit:
            if number1 > number2:
                return win1
            elif number2 > number1:
                return win2
            else:
                return draw
        elif suit1 != winning_suit:
            if number1 > number2:
                return win1
            elif number2 > number1:
                return win2
            else:
                return draw
            
    elif suit1 != suit2:
        if suit1 == winning_suit:
            return win1
        elif suit2 == winning_suit:
            return win2
        elif number1 > number2:
            return win1
        elif number2 > number1:
            return win2
        else:
            return draw


'''Q4
https://www.1point3acres.com/bbs/thread-777237-1-1.html

1轮coding：找出字符串的唯一缩写， 假设无冲突
Example:

Input: ["cheapair", "cheapoair", "peloton", "pelican"]
Output:
"cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
"cheapoair": "po" // "oa" would also be acceptable
"pelican": "ca"   // "li", "ic", or "an" would also be acceptable
"peloton": "t"    // this single letter doesn't occur in any other string
扩展： open question， 自定义解决冲突的方法

'''
arr = ["cheapair", "cheapoair", "peloton", "pelican"]

dic = {}
for s in arr:  # O(N)
    dic[s] = s 
    for i in range(len(s)): # O(N * K)
        for j in range(i + 1, len(s)): # O(N * K * K)
            subStr = str(s[i:j])
            flag = True
            for s2 in arr:  # O(N^2 K^2)
                if s2 == s:
                    continue
                if subStr in s2:
                    flag = False
                    break

            if flag and len(subStr) < len(dic[s]) and subStr not in dic.values():
                dic[s] = subStr

print(dic.values())
# dict_values(['pa', 'po', 't', 'li'])




''' Q5
https://www.1point3acres.com/bbs/thread-772905-1-1.html

Round 1 coding (新題)
面試官人很nice, 全程專心
寫一個找零的function, 輸入是ex. (76, [1, 5, 10, 25]) 表示76 cents 回傳要用幾個1, 5, 10, 25cents 的硬幣找零，有多解，回傳其一
接著問了幾個follow up 都是建立在以上寫的function, 都不難, 例如輸入多了一個n, 限定一定要用至少幾個硬幣，或是至少幾種硬幣

'''





''' Q6
https://www.1point3acres.com/bbs/thread-726848-1-1.html

给的是一个file path, 让你读这个文件，然后parse, 最后filter 结果，得到他们想要的东西
color    date    number
green  2001/02/23  8
purple 2006/05/11   1
white 2019/02/17   200

sheet = SpreadSheet("a.txt");
sheet.filter(['color', '=', 'green'])

=>
[
  ['g‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌reen' , 2001/02/03, 8]
]

注意， 颜色可能有duplicate.

'''




'''  Q7

Decision Tree
//   signal_value                  constant
//                        X1 < 3
//                       ------------
//           |                                 |
//       X2 < 1                        X1 < 6
//    -----------                        ---------
//  |              |                 |                  |
//  N             Y                N             X3 < 2
//                                                  ----------
//                                                  |          |
//                                                 Y          N

Test cases:
// {X1 <- 2, X2 <- 1, X3 <- 11} -> Y
// {X1 <- 8, X2 <- 4, X3 <- 12} -> N


让写个class，实现以下三个方法：
  建树要用 add_split方法建

class DecisionTree:

   method add_split(leaf, signal_name, constant):
     Add a split condition to the given leaf.
     Return the newly created leaves for future calls.
     Feel free to pass a sentinel value (like null) as the leaf for the first call to this method.‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌
     Subsequent calls should pass leaves returned by previous calls.

   method set_leaf_value(leaf, value):
     Set the return value for a leaf.

   method evaluate(signals):
     Evaluate the tree on a mapping of signal_name -> signal_value.
     Return the value of the leaf reached by traversing the tree.

'''