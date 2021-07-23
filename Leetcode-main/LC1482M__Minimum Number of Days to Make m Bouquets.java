class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        if (m * k > n) return -1;
        int left = 1, right = (int)1e9;
        
        while (left < right) {   // binary search 基操
            int mid = (left + right) / 2;
            if(isOk (bloomDay, mid, m, k))
                right = mid;
            else
                left = mid + 1;
        }
        return left;  
    }
    
    public boolean isOk (int[] bloomDay, int mid, int m, int k){
        int consecutive = 0, numBouquet = 0;
        for (int i=0; i<bloomDay.length; i++) {
            if(bloomDay[i] > mid){
                consecutive = 0; //因为adjacent flower，每次碰壁都清零
            }else{
                consecutive ++;
                if(consecutive == k){
                    numBouquet++;     // 达到每束花的要求，花束++
                    consecutive = 0;  // 达到每束花的要求，就清零
                }
            }
        }
        return numBouquet >= m;  
    }
}
