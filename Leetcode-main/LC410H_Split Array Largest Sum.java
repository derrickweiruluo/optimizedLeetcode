class Solution {  //410
    public int splitArray(int[] nums, int m) {
        int maxNum = 0, totalSum = 0;
        for(int i = 0; i<nums.length; i++){
            totalSum += nums[i];
            if(maxNum < nums[i])
                maxNum = nums[i];
        }
        while (maxNum < totalSum) {
            int mid = (totalSum - maxNum) / 2 + maxNum;
            if(checkIfValid(nums, mid, m)) 
                totalSum = mid;
            else 
                maxNum = mid + 1;
        }
        return maxNum;
    }
    
    private boolean checkIfValid(int[] nums, int x, int m){
        int sum = 0;
        int count = 1;
        for(int i = 0; i<nums.length; i++){
            if(sum + nums[i] > x){
                count++;
                sum = nums[i];
            }else{
                sum += nums[i];
            }
        }
        return count <= m;
    }
}
