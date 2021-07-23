class Solution1 {
    public int numTriplets(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int count = 0;
        
        HashMap <Long, Integer> map1 = new HashMap<>();
        HashMap <Long, Integer> map2 = new HashMap<>();
        
        for(int i=0; i<nums1.length; i++){
        //for (int i: nums1)    
            
            long key = (long) nums1[i] * nums1[i];
            if(!map1.containsKey(key)) map1.put(key, 1);
            else map1.put(key, map1.get(key)+1);
        }
        for(int i=0; i<nums2.length; i++){
            long key = (long) nums2[i] * nums2[i];
            if(!map2.containsKey(key)) map2.put(key, 1);
            else map2.put(key, map2.get(key)+1);
        }
        
        for(int i=0; i<nums1.length-1; i++){
            for(int j=i+1; j<nums1.length; j++){
                long product = (long) nums1[i] * nums1[j];
                if(map2.containsKey(product)) count += map2.get(product);
            }
        }
        
        for(int i=0; i<nums2.length-1; i++){
            for(int j=i+1; j<nums2.length; j++){
                long product = (long) nums2[i] * nums2[j];
                if(map1.containsKey(product)) count += map1.get(product);
            }
        }
        return count;
    }
}


-----------------------

class Solution2 {
    public int numTriplets(int[] a, int[] b) {
        return cnt(a, b) + cnt(b, a);
    }
    
    private int cnt(int[] a, int[] b) {
        int res = 0, m = a.length;
        for (int i = 0; i < m; i++) {
            Map<Long, Integer> map = new HashMap<>();
            long t = ((long) a[i]) * ((long) a[i]);
            for (long n : b) {  //must transferred to long
                if (t % n == 0) res += map.getOrDefault(t / n, 0); //new pair formed btw n and previous found t / n
                map.put(n, map.getOrDefault(n, 0) + 1); // cached the count found;
            }
        }
        return res;
    }
}
