class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int max = 0;
        for (int i=0; i<weights.length; i++){
            if(max < weights[i]) max = weights[i];
        }
        
        int left = max, right = (int) 1e9;
        while (left < right) {
            int mid = (left + right) / 2;
            if (canPass ( weights, D, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
    
    private boolean canPass (int[] weights, int D, int x) {

        int consecutive = 0;
        int count = 1;
        int weightLimit = x;
        
        for (int i=0; i<weights.length; i++) {
            consecutive += weights[i];
            if (consecutive > weightLimit){
                count ++;
                consecutive = weights[i];
            }
        }
        
        return count <= D;
    }
}
