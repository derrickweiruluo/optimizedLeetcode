class Solution {
    public int maximizeSweetness(int[] sweetness, int K) {
        int n = sweetness.length;
        int left = 0, right = (int) 1e9;
        
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (canPass(sweetness, K, mid))
                left = mid;
            else 
                right = mid - 1;
        }
        return right;
    }
    
    private boolean canPass (int[] sweetness, int K, int X) {
        int consecutive = 0, count = 0;
        for (int i=0; i<sweetness.length; i++) {
            consecutive += sweetness[i];
            if (consecutive >= X){
                consecutive = 0;
                count ++;
                if(count > K) break;
            }
        }
        return count > K;
    }
}
