class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        int length = intervals.length;
        if(length ==0 || length ==1) return length;
        
        Arrays.sort(intervals, (a, b)->(a[0] == b[0] ? b[1] - a[1] : a[0] - b[0])); //lambda好用法
        int updatedLength = length;
        int start = intervals[0][0], end = intervals[0][1];
        
        for(int i=1; i<length; i++){
            if(intervals[i][0]>= start && intervals[i][1] <= end) // 被cover的条件
                updatedLength--;
            else {
                start = intervals[i][0];
                end   = intervals[i][1];
            }
        }
        return updatedLength;
    }
}
