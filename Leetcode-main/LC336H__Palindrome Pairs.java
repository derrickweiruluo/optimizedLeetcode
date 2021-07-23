//DerrickLLL
//02-27-2021
//68 ms, beat 60%
//67 MB, beat 19%

class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> ans = new ArrayList<>(); 
        // build a dictionary of the reverse of every words[]
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            String rev = new StringBuilder(words[i]).reverse().toString();
            map.put(rev, i);
        }
        
        for (int i = 0; i < words.length; i++) {
            String curr = words[i];
            if (map.containsKey(curr) && map.get(curr) != i) 
                ans.add(Arrays.asList(i, map.get(curr)));
            //left piviot "i" - searching for a prefix
            for (int j = curr.length() - 1; j >= 0; j--) {
                if (isPalindrome(curr, 0, j)) {
                    String sub = curr.substring(j + 1);
                    if (map.containsKey(sub))
                        ans.add(Arrays.asList(map.get(sub), i));
                }   
            }
            // right pivot "j" - searching for a suffix
            for (int j = 0; j < curr.length(); j++) {
                if (isPalindrome(curr, j, curr.length() - 1)) {
                    String sub = curr.substring(0, j);
                    if (map.containsKey(sub))
                        ans.add(Arrays.asList(i, map.get(sub)));
                }
            }
        }
        return ans;
    }
    
    private boolean isPalindrome(String s, int i, int j){

        while(i<j){
            if(s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}



