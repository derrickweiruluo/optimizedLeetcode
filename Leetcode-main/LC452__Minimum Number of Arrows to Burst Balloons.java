class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points.length == 0) return 0;
        if(points.length == 1) return 1;
        
        // Always sort the end
        
        //Arrays.sort(points, (a,b) -> (a[0]==b[0]) ? Integer.compare(a[1],b[1]) : Integer.compare(a[0],b[0]));  // worked
        //Arrays.sort(points, (a,b) -> (a[0]==b[0]) ? (a[1]-b[1]) : (a[0]-b[0]));  // subtraction cause overflow
        
        Arrays.sort(points, (a, b) -> Integer.compare(a[1],b[1]));  //worked
        //Arrays.sort(points, (a,b) -> a[1] < b[1] ? -1 : 1);   // worked, comparator 
        
        int start = points[0][0], end = points[0][1];
        int counter = 1;
        
        for(int i=1; i<points.length; i++){
            if(points[i][0] <= end){  
                start = points[i][0];
                end = Math.min(end, points[i][1]);
            }
            else{
                start = points[i][0];
                end   = points[i][1];
                counter ++;
            }
        } 
        //System.out.println(Arrays.deepToString(points));
        //System.out.println(2<3);
        return counter;
    }
}
