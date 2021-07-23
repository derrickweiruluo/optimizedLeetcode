class MyCalendarThree {
    
    TreeMap <Integer, Integer> tree;


    public MyCalendarThree() {
        tree = new TreeMap();
    }
    
    public int book(int start, int end) {
        tree.put(start, tree.getOrDefault(start, 0) + 1);
        tree.put(end, tree.getOrDefault(end, 0) - 1);
        
        int count = 0, maxCount = 0;
        for(int value: tree.values()){
            count += value;
            maxCount = Math.max(maxCount, count);
        }
        return maxCount;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */
