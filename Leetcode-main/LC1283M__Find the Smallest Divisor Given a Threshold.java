class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int left = 1, right = (int) 1e6+1;
        while(left < right) {
            int mid = (left + right) / 2;
            if (canPass (nums, threshold, mid)) {
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
    
    private boolean canPass (int[] nums, int threshold, int x){
        int sum = 0;
        for (int i=0; i<nums.length; i++) {
            if (nums[i] % x == 0)
                sum += nums[i] / x;
            else
                sum += nums[i] / x + 1;
        }
        return sum <= threshold;
    }
}
