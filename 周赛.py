# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# 656101987
# 1

def minMoves(target: int, maxDoubles: int) -> int:
    res = 0
    while target > 1:
        if target % 2 == 1:
            target -= 1
            res += 1
        elif maxDoubles and target % 2 == 0:
            target = target //2
            maxDoubles -= 1
            res += 1
        else:
            target -=1
            res += 1
    return res 
a = minMoves(656101987, 1)
print(a)



def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        
        n = len(nums)
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        print(pos)
        print(neg)
        idx1, idx2 = 0, 0
        
        res = [0] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = pos[idx1]
                idx1 += 1
            else:
                res[i] = neg[idx2]
                idx2 += 1
        
        return nums




s = "kfedcbdngvlykqyrbvwbnaassgjifjxtawlafhcpjtpzfnbsqfasohevbbhkwmtnmixolfepkjmcbadqcljmsbonrngsgfqwzqiisbiwiqgtqtqddukgtjymbxzmtxrobuhkdxmdmqccrauzkrjisstznnkhupiandekzcchsrzwintkkzhvqomqmnbasynmvtxwydcvwoukqmgrpmgzqancuzapgncasxnbyznlrdvcbomdptjftgxdzeqzyavfdpseoxpvohpxtikyjfvskxyqbubgnseraxtrcrwjxloxymhqgaxwbbvzhjsbncqrlpdbiuakdjzjrbclhxgnjjyfrqyjchlsdrcwtdoktviqwjctlmzqemumgmjufcbixkfhzkugsvnkrrakccguybwhmuexiemqusltaaqrswsezccqzaputgaabrjdeihmkpzbojnusmhkwjdxvgiexwdkkazhhmlalgzvxgqgncfytrxuhkwhwcxhmlbvkhjcnyztepwnlpthozdqexvhxpvheopjrsjzkqrstczffkhkikelwydcbnghfiibeyabgegdgaqvasujmggltkvokmnsmontjzsmzoeeqenafvurbnbwqbizvaqxfgnoxasctfrwvqmoufvpajdkethlvbhbehxahcpcizocbchwfznhuqtblwepeqdhycrovqosmxxeeqaffjvvclmpcqdugndexexcykyusetuamymszlteobxkestwbzubpstbwrstuovlybycevedzgurqvlgkouvavcukccgixixsrndurvrkfegegnchbhockujlafxexlxhgysraviztkjymiqxrlldcixvfnzrpserrqycbfmesqbltywmandcqtluccbisfqzosbvedqhsxepdjevaasylvjmfpvyxqvclaalgxytiukyarojmzyovmiunkvqhkouhxxhbemavagrhteofpowvlpdunjjpwgcjibagfswrzwkgrwklppchvtukzncvoqorlsskyghkhrazwvyqqjfygmduhsfkrseddgmtdvlqeruxogmyttdqmdpmscspatkoifauivwjtbwisiiqztrllfqnjvbagrfylrpjudjmvwhdkhahyxlsfbkuuyofryfgblllzeacfiqqawridcbtqnroxwuqhyspqmwhxmjztqokofnkfvupcykszthicdgjbrgafpztktrcwtayoulnjaazigkinnpttghhyboiczvtswenshlmqyelnwhzqlswblqssiiynypfcxerlykpiyimkoodimdfdlzbwmlwflylcqwaflivqeonjswvowxgeoafmppodmfbvooodtnzgmhfnchenaaywqevklrpgajbmbxgiopofghlouhjfarjxlclcullsgyzhohowtragbkaebrvbkmxfxughlirtikheojbrrgxtqldfdnqxndzvfgajiltnqnuwavxbrvuiycsizunlglwnivpseyfwmgydmmpzhxkdtpuzpddacjmjhvncdoicedkimdgaqobdfagpggvjemstqbsshynyvhdyslgldvkapqgusmnuroqxcivjifkhrotomxodficktxmcytkbqitrlalpbtphowfgtzgfacabjodvivgykorvmxhzpqvskolkbfpbdgowlighossrlwiomgohfhgklmlnekniqfjmvvqvmimkeddfxnxwzzroospxvndynetghkgrakuslukqsrdtmjkblwrmwhzzojcwwogrjvnftdwwpoqcjqimvjbwgqgpeffjnwlzdyhkhwmvpwpcmjmdqneexqwcrvdxsfsnidwyflwxwngczklprhoazeeqwclrqvnicfvrtbqailbwrqxadxslouwdjycidupemdwhpkqekaxxprtdtmjficrhlvqidvgwkllaowyyajkxugqiztbpzvjqtpuyugkvdfcaczzruskvucsxtvroljnjojuzncatgnypbzwvilbajqqnjovqxcfunwwbxgshrjlajwveaswqegidfnedpxqdreddvawrpbllkcshlafnxyocbmwacytvgtoonlkukqhxwbfxcfnbgmrfcnkvtxmygiyjoyoljd"
power = 71717
modulo = 94536
k = 1149
hashValue = 39999

def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    # hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 312) mod 100 = 23132 mod 100 = 32
    
    def _hash(s, i, j):
        res = 0
        x = 0
        for char in s[i: j + 1]:
            v = ord(char) - ord('a') + 1
            res += (v * (power ** x) % modulo)
            x += 1
        return res % modulo
        
    
    
    
    for i in range(k - 1, len(s)):
        val = _hash(s, i - k + 1, i)
        if val == hashValue:
            return s[i - k + 1 : i + 1]



s = "kfedcbdngvlykqyrbvwbnaassgjifjxtawlafhcpjtpzfnbsqfasohevbbhkwmtnmixolfepkjmcbadqcljmsbonrngsgfqwzqiisbiwiqgtqtqddukgtjymbxzmtxrobuhkdxmdmqccrauzkrjisstznnkhupiandekzcchsrzwintkkzhvqomqmnbasynmvtxwydcvwoukqmgrpmgzqancuzapgncasxnbyznlrdvcbomdptjftgxdzeqzyavfdpseoxpvohpxtikyjfvskxyqbubgnseraxtrcrwjxloxymhqgaxwbbvzhjsbncqrlpdbiuakdjzjrbclhxgnjjyfrqyjchlsdrcwtdoktviqwjctlmzqemumgmjufcbixkfhzkugsvnkrrakccguybwhmuexiemqusltaaqrswsezccqzaputgaabrjdeihmkpzbojnusmhkwjdxvgiexwdkkazhhmlalgzvxgqgncfytrxuhkwhwcxhmlbvkhjcnyztepwnlpthozdqexvhxpvheopjrsjzkqrstczffkhkikelwydcbnghfiibeyabgegdgaqvasujmggltkvokmnsmontjzsmzoeeqenafvurbnbwqbizvaqxfgnoxasctfrwvqmoufvpajdkethlvbhbehxahcpcizocbchwfznhuqtblwepeqdhycrovqosmxxeeqaffjvvclmpcqdugndexexcykyusetuamymszlteobxkestwbzubpstbwrstuovlybycevedzgurqvlgkouvavcukccgixixsrndurvrkfegegnchbhockujlafxexlxhgysraviztkjymiqxrlldcixvfnzrpserrqycbfmesqbltywmandcqtluccbisfqzosbvedqhsxepdjevaasylvjmfpvyxqvclaalgxytiukyarojmzyovmiunkvqhkouhxxhbemavagrhteofpowvlpdunjjpwgcjibagfswrzwkgrwklppchvtukzncvoqorlsskyghkhrazwvyqqjfygmduhsfkrseddgmtdvlqeruxogmyttdqmdpmscspatkoifauivwjtbwisiiqztrllfqnjvbagrfylrpjudjmvwhdkhahyxlsfbkuuyofryfgblllzeacfiqqawridcbtqnroxwuqhyspqmwhxmjztqokofnkfvupcykszthicdgjbrgafpztktrcwtayoulnjaazigkinnpttghhyboiczvtswenshlmqyelnwhzqlswblqssiiynypfcxerlykpiyimkoodimdfdlzbwmlwflylcqwaflivqeonjswvowxgeoafmppodmfbvooodtnzgmhfnchenaaywqevklrpgajbmbxgiopofghlouhjfarjxlclcullsgyzhohowtragbkaebrvbkmxfxughlirtikheojbrrgxtqldfdnqxndzvfgajiltnqnuwavxbrvuiycsizunlglwnivpseyfwmgydmmpzhxkdtpuzpddacjmjhvncdoicedkimdgaqobdfagpggvjemstqbsshynyvhdyslgldvkapqgusmnuroqxcivjifkhrotomxodficktxmcytkbqitrlalpbtphowfgtzgfacabjodvivgykorvmxhzpqvskolkbfpbdgowlighossrlwiomgohfhgklmlnekniqfjmvvqvmimkeddfxnxwzzroospxvndynetghkgrakuslukqsrdtmjkblwrmwhzzojcwwogrjvnftdwwpoqcjqimvjbwgqgpeffjnwlzdyhkhwmvpwpcmjmdqneexqwcrvdxsfsnidwyflwxwngczklprhoazeeqwclrqvnicfvrtbqailbwrqxadxslouwdjycidupemdwhpkqekaxxprtdtmjficrhlvqidvgwkllaowyyajkxugqiztbpzvjqtpuyugkvdfcaczzruskvucsxtvroljnjojuzncatgnypbzwvilbajqqnjovqxcfunwwbxgshrjlajwveaswqegidfnedpxqdreddvawrpbllkcshlafnxyocbmwacytvgtoonlkukqhxwbfxcfnbgmrfcnkvtxmygiyjoyoljd"
power = 71717
modulo = 94536
k = 1149
hashValue = 39999
# s = "leetcode"
# power = 7
# modulo = 20
# k = 2
# hashValue = 0
def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    # hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 312) mod 100 = 23132 mod 100 = 32
    
    def _hash(s, i, j):
        res = 0
        x = 0
        while i <= j:
        # for char in s[i: j + 1]:
            char = s[i]  
            v = lookup[char]
            res += (v * (power ** x)) % modulo
            x += 1
            i += 1
        return res % modulo
        
    lookup = {}
    lower = 'abcdefghijklmnopqrstuvwxyz'
    for char in lower:
        v = ord(char) - ord('a') + 1
        lookup[char] = v
    
    
    for i in range(k - 1, len(s)):
        val = _hash(s, i - k + 1, i)
        if val == hashValue:
            return s[i - k + 1 : i + 1]
    
    return []

print(subStrHash(s, power, modulo, k, hashValue))