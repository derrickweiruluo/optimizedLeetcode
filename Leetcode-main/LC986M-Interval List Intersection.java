class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        
        ArrayList<int[]> ans = new ArrayList<>();
        int l1=firstList.length; 
        int l2=secondList.length;
        int i=0,  j=0;
        
        while(i<l1 && j<l2){
            int a = Math.max(firstList[i][0], secondList[j][0]); //找左边最大的boundary
            int b = Math.min(firstList[i][1], secondList[j][1]); //找右边最小的boundary
            
            if(a<=b) ans.add(new int[]{a, b});
            
            if(firstList[i][1] < secondList[j][1]) i++; //当前sublist 小的那个 index ++

            else j++;
        }
        
        return ans.toArray(new int[ans.size()][]);  // Arraylist toArray
    }
}
