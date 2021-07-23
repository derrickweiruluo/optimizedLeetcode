class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        PriorityQueue <int[]> minHeap = new PriorityQueue<int[]>((a,b)->a[1]-b[1]);
        
        for(int[] interval : intervals){
            if(minHeap.isEmpty() || interval[0]<minHeap.peek()[1]) {
                minHeap.add(interval);
            }
            else{
                int[] top = minHeap.poll();
                top[1] = interval[1];
                minHeap.add(top);
            }
        }
        return minHeap.size();
    }
}
