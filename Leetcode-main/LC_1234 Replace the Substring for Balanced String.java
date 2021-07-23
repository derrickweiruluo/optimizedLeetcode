class Solution {
        public int balancedString(String s) {
        int[] count = new int[122];
        int n = s.length(), res = n, i = 0, k = n / 4;
        for (int j = 0; j < n; j++) {
            count[s.charAt(j)] ++;  //这个写法是按照ASCII 有 122个value
        }                           //这一步是根据不同char的ASCII code在计算出现次数
                
        // https://tinyurl.com/earbyude    (Stackover flow)
        // System.out.println(count['Q']);
        // System.out.println(count['W']);
        // System.out.println(count['E']);
        // System.out.println(count['R']);    
            
        for (int j = 0; j < n; j++) {
            count[s.charAt(j)] --;
            while (i < n && count['Q'] <= k && count['W'] <= k && count['E'] <= k && count['R'] <= k) {
                res = Math.min(res, j - i + 1);
                count[s.charAt(i++)]++;  
                i++;
            }
        }       
        return res;
    }
}
