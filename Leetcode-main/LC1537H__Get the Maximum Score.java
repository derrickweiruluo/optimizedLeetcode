class Solution { //1537
    public int maxSum(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;
        int i = 0, j = 0;
        long mod = (long)1e9+7, routeA = 0, routeB = 0;
        
        while(i<n1 && j<n2){
            if(nums1[i] < nums2[j]){
                routeA = (routeA + nums1[i]); 
                i++;
            }else if(nums2[j] < nums1[i]){ 
                routeB = (routeB + nums2[j]);
                j++;
            }else{
                routeA = routeB = Math.max(routeA, routeB) + nums1[i];
                i++; j++;
            }
        }
        // for the leftover parts
        while(i<n1) routeA += nums1[i++];
        while(j<n2) routeB += nums2[j++];
        
        return (int) (Math.max(routeA, routeB) % mod);
    }
}
