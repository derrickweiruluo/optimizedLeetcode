class MyCalendar {
    
    TreeMap <Integer, Integer> calendar;

    public MyCalendar() {
        calendar = new TreeMap();
    }
    
    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);   //最靠近start time && 小于
        Integer next = calendar.ceilingKey(start);   //最靠近start time && 大于
        
        //满足两头的boundary conditions
        if((prev==null || calendar.get(prev) <= start) && (next == null || end <= next)){ 
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
