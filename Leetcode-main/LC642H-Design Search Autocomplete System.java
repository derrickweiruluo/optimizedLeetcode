//定义 Node 和 Trie
class Node {
  String sentence;
  int times;

  Node(String st, int t) {
    sentence = st;
    times = t;
  }
}

class Trie {
  int times=0;                       // 当前node的储存时间
  Trie[] branches = new Trie[27];  // trie tree, 一个tree 有 26+1的 子node
}

class AutocompleteSystem {
  private Trie root;
  private String cur_sent = "";

  public AutocompleteSystem(String[] sentences, int[] times) { //Comstructor of class AutocompleteSystem 
    root = new Trie();                                         // 在root node以trie tree的形式insert sentenses
    for (int i = 0; i < sentences.length; i++) {
      insert(root, sentences[i], times[i]);
    }
  }
    
  private void insert(Trie t, String s, int times) {  //helper method1 of constructor, 组建trie tree，完事后update t.times
    for (int i = 0; i < s.length(); i++) {
      if (t.branches[toInt(s.charAt(i))] == null) {
        t.branches[toInt(s.charAt(i))] = new Trie();
      }
      t = t.branches[toInt(s.charAt(i))];   // 从root node一直往下走，假如 s 走到底，最后一个node的  times=t.times + 参数的times
    }
    t.times = t.times + times;
  }
  private int toInt(char c) {  // helper method2 of constructor, leafnode indexing
    return c == ' ' ? 26 : c - 'a';
  }

  public List<String> input(char c) {
    List<String> res = new ArrayList<>();
    if (c == '#') { //如果遇到’#‘， 直接freq ++ 且 insert一次make sure之前的词存在于trie tree里
      insert(root, cur_sent, 1);
      cur_sent = "";
    } 
    else {
      cur_sent =  cur_sent + c;
      List<Node> list = lookup(root, cur_sent);
      Collections.sort(
         list
        ,(a, b) -> a.times == b.times ? a.sentence.compareTo(b.sentence) : b.times - a.times //如果 相同freq，则 ACSII code比较两个string，否则freq从大到小排列
      );
      for (int i = 0; i < Math.min(3, list.size()); i++) res.add(list.get(i).sentence); // 答案，freq从大到小
    }
    return res;
  }
    
  private List<Node> lookup(Trie t, String s) {
    List<Node> list = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
      if (t.branches[toInt(s.charAt(i))] == null) {
        return new ArrayList<>();
      }
      t = t.branches[toInt(s.charAt(i))];  
    }
    dfs(s, t, list);  // node走到尽头之后开始dfs --> update lookup结果的 List<Node> list
    return list;
  }

  private void dfs(String s, Trie t, List<Node> list) {
    if (t.times > 0){   // 每遇见一种可能，就记录到 lookup list里面
      list.add(new Node(s, t.times));  
    } 
    for (char i = 'a'; i <= 'z'; i++) {    // dfs from a to z
      if (t.branches[i - 'a'] != null) {
        dfs(s + i, t.branches[i - 'a'], list);
      }
    }
    if (t.branches[26] != null) { // dfs 空格 （和上面一样处理只是不能loop）
      dfs(s + ' ', t.branches[26], list);
    }
  }
}   

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */

