class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if(intervals.length == 0 || intervals.length == 1) return 0;
        
        Arrays.sort(intervals, (a,b) -> a[1]-b[1]);  //must sort by the end index of ea interval since it will later be used in finding overlapping
        
        int start = intervals[0][0], end = intervals[0][1];
        int counter = 0, length = intervals.length;
        
        for(int i=1; i<length; i++){
            if(intervals[i][0] < end) counter ++;
            else end = intervals[i][1];
        }
        return counter;
    }
}
