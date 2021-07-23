//03-14-2021 DerrickL 
//思路： 当完全没重叠，直接加 int[]interval， 但有重叠，加改良过的interval，完全被删掉就啥都不干


class Solution {
    public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
        
        List<List<Integer>> list = new ArrayList<>();  // 用法
        
        int i=0,  length = intervals.length;
        int cutStart = toBeRemoved[0];
        int cutEnd   = toBeRemoved[1];
              
        for(int[] interval: intervals){
            if(interval[1] < cutStart || interval[0] > cutEnd)
                list.add(Arrays.asList(interval[0], interval[1]));  //用法
            else{
                if(interval[0] < cutStart)
                    list.add(Arrays.asList(interval[0], cutStart));
                if(interval[1] > cutEnd)
                    list.add(Arrays.asList(cutEnd, interval[1]));
            }
        }        
        return list;
    }
}

// class Solution {
//     public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
        
//         List<List<Integer>> list = new ArrayList<>();
        
//         int i=0,  length = intervals.length;
//         int cutStart = toBeRemoved[0];
//         int cutEnd   = toBeRemoved[1];
              
//         for(int[] interval: intervals){
//             if(interval[1] < cutStart || interval[0] > cutEnd)
//                 list.add(Arrays.asList(interval[0], interval[1]));
//             else{
//                 if(interval[0] < cutStart)
//                     list.add(Arrays.asList(interval[0], cutStart));
//                 if(interval[1] > cutEnd)
//                     list.add(Arrays.asList(cutEnd, interval[1]));
//             }
//         }
        
//         return list;

//     }
// }

