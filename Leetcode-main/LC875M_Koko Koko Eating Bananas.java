class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1, right = 1000000001;
        
        while (left < right) {
            int mid = (left + right) / 2;
            if (CheckInTime(piles, h, mid)) right = mid ;
            else left = mid + 1;
        }
        return left;
    }
    
    private boolean CheckInTime (int[] piles, int h, int mid) {
        int time = 0;
        for (int i=0; i<piles.length; i++) {
            time += (piles[i] - 1) / mid + 1; // time for each pile
        }
        
        return time <= h;
    }
}
