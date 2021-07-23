class Solution {  //1574
    public int findLengthOfShortestSubarray(int[] arr) {
        int length = arr.length;
        int left = 0, right = length -1;
        
        while(left < length-1 && arr[left+1] >= arr[left])
            left++;
        if (left == length-1) return 0;
        
        while(right >= left && arr[right] >= arr[right-1])
            right--;
        
        int result = Math.min(right, length-1-left);
        
        int i = 0, j = right;
        while(i<=left && j<length){
            if(arr[j] >= arr[i]){
                result = Math.min(result, j-i-1);
                i++;
            }else{
                j++;
            }
        }
        return result;
    }
}
