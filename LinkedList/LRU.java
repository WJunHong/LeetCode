package LinkedList;

class LRUCache {
    


    public class Node {
        public int val;
        public int key;
        public Node next;
        public Node prev;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private int capacity;
    private int curr_count = 0;
    private Node dummy_head = new Node(-1, 0);
    private Node dummy_tail = new Node(-1, 0);
    private HashMap<Integer, Node> nodeTable = new HashMap<>();

    public void addNode(Node n) {
        n.next = this.dummy_head.next;
        n.prev = this.dummy_head;

        this.dummy_head.next.prev = n;
        this.dummy_head.next = n;

    }

    public void removeNode(Node n) {
        n.prev.next = n.next;
        n.next.prev = n.prev;
    }

    public Node removeLRUNode() {
        Node lru = this.dummy_tail.prev;
        this.removeNode(lru);
        return lru;
    }

    public void moveToTop(Node n) {
        this.removeNode(n);
        this.addNode(n);
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.dummy_head.next = this.dummy_tail;
        this.dummy_tail.prev = this.dummy_head;
    }
    
    public int get(int key) {
        Node n = this.nodeTable.get(key);
        if (n != null) {
            this.moveToTop(n);
            return n.val;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        Node n = this.nodeTable.get(key);
        if (n != null) {
            n.val = value;
            this.moveToTop(n);
        } else {
            if (this.curr_count < this.capacity) {
                this.curr_count++;

                Node m = new Node(key, value);
                this.nodeTable.put(key, m);
                this.addNode(m);
            } else {
                Node i = this.removeLRUNode();
                this.nodeTable.remove(i.key);

                Node j = new Node(key, value);
                this.nodeTable.put(key, j);
                this.addNode(j);
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
