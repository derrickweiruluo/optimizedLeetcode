class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1,(a,b)->a[0]-b[0]);
        Arrays.sort(slots2,(a,b)->a[0]-b[0]);
        
        int length1 = slots1.length, p1=0;
        int length2 = slots2.length, p2=0;
        
        while(p1<length1 && p2<length2){
            int start = Math.max(slots1[p1][0], slots2[p2][0]);
            int end   = Math.min(slots1[p1][1], slots2[p2][1]);
            
            if(end-start>=duration){
                return new ArrayList<Integer>(Arrays.asList(start, start+duration));
            }
            
            if(slots1[p1][1]<slots2[p2][1]){
                p1++;
            }else{
                p2++;
            }
        }
        return new ArrayList<Integer>();
    }
}
