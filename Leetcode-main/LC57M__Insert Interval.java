// 03/13/2021 DerrickL


class Solution {   
    List<int[]> list = new ArrayList<>();
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
        int i=0;
        int length=intervals.length;
        int start = newInterval[0], end = newInterval[1];
        
        while(i< length && intervals[i][1] < start) { 
            list.add(intervals[i++]);   // when当前interval的尾部没 碰到 新interval的时候，直接加进Arraylist
        }
        
        while(i< length && intervals[i][0] <= end){     //when当前interval的头部没 <= 新interval尾部的时候 
            start = Math.min(start, intervals[i][0]);   // 重新设置 start 和 end， i++
            end   = Math.max(end, intervals[i][1]);
            i++;
        }
        
        list.add(new int[]{start, end}); // 加进 arrayList
        while(i< length) list.add(intervals[i++]);  // 加剩下的arrayList
        
        return list.toArray(new int[list.size()][]);
       
    }
}
