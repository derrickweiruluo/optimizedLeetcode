class Solution {.  // 1793
    public int maximumScore(int[] nums, int k) {
        
        int left = k, right = k, n=nums.length;
        int score = nums[k], subArray = nums[k];
        
        while(left> 0 || right<n-1){
            if(left==0) right++;             //boundary
            else if (right == n-1) left--;   //boundary
            else if (nums[left-1] > nums[right+1]) left--;  //windowing expanding direction 
            else right++;                                   //windowing expanding direction
            
            subArray = Math.min(subArray, Math.min(nums[left], nums[right]));
            score = Math.max(score, subArray*(right - left + 1));
        }
        return score;
    }
}


