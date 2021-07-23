class Solution {
    int[] dict = new int[26];
    public boolean isAlienSorted(String[] words, String order) {
        
        
        for (int i=0; i<order.length(); i++)
            dict[order.charAt(i) - 'a'] = i;
        for (int i=0; i<words.length-1; i++){
            if(isBigger(words[i], words[i+1]))
                return false;
        }
        return true;
    }
    
    public boolean isBigger(String s1, String s2){
        int m = s1.length(), n = s2.length();
        for(int i=0; i<n && i<m; i++){  //在重叠区域
            if(s1.charAt(i) != s2.charAt(i)){ // 找第一个不相同然后做出 return
                return (dict[s1.charAt(i) - 'a'] > dict[s2.charAt(i) - 'a']) ;
            }
        }
        return m > n; //如果重叠区域都相同，那么就看长短
    }
}
