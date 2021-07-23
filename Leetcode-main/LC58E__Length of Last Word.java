class Solution1 {
    public int lengthOfLastWord(String s) {
        s = s.trim(); // trim the spaces in the front and back of a string
        return s.length() - (s.lastIndexOf(' ') + 1); // math
    }
}






// 下面这个第二节法， while loop 从后面开始数直到碰到第一个空格
class Solution2 {
    public int lengthOfLastWord(String s) {
        int p = s.length(), length = 0;
        while(p > 0){
            
            p--;
            // we're in the middle of the last word
            if (s.charAt(p) != ' ') {
                length++;
                
            }
            // here is the end of last word
            else if (length > 0) { 
                return length;
            }
        }
        return length;
    }
}
