import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class Deque<Item> implements Iterable<Item> {

    private Node first;
    private Node last;
    private int num;
    private class Node {
        Item item;
        Node next;
        Node prev;
    }

    public Deque() {                           // construct an empty deque
        first = null;
        last = null;
        num = 0;
    }
    public boolean isEmpty() {
    // is the deque empty?
        return num == 0;
    }     
    public int size() {
    // return the number of items on the deque
        return num;
    }                     
    public void addFirst(Item item) {        
    // add the item to the front
        if (item == null) 
            throw new NullPointerException();

        // if the queue is empty
        if (num == 0) {
            Node n = new Node();
            n.item = item;
            n.prev = null;
            n.next = null;
            first = n;
            last = n; 
        } else {
            Node oldfirst = first;
            first = new Node();
            first.item = item;
            first.next = oldfirst;
            first.prev = oldfirst.prev;
            oldfirst.prev = first;
        }
        ++num;
    }

    public void addLast(Item item) {         
    // add the item to the end
        if (item == null) 
            throw new NullPointerException();

        if (num == 0) {
            Node n = new Node();
            n.item = item;
            n.prev = null;
            n.next = null;
            first = n;
            last = n;
        } else {
            Node oldlast = last;
            last = new Node();
            last.item = item;
            last.prev = oldlast;
            last.next = oldlast.next;
            oldlast.next = last;
        }
        ++num;
    }

    public Item removeFirst() {               
    // remove and return the item from the front
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = first.item;
        // only one element
        if (num == 1) { 
            first = null;
            last = null;
        } else {
            first = first.next;
            first.prev = null;
        }
        --num;
        return item;
    }
    public Item removeLast() {
    // remove and return the item from the end
        if (num == 0) { // isEmpty()
            throw new NoSuchElementException();
        }

        Item item = last.item;
        // only one element
        if (num == 1) { 
            first = null;
            last = null;
        } else {
            last = last.prev;
            last.next = null;
        }
        --num;
        return item;
    }

    public Iterator<Item> iterator() {
    // return an iterator over items in order from front to end
        return new ListIterator();  
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;
        public boolean hasNext() { return current != null; }
        public void remove() {
            throw new UnsupportedOperationException();
        }
        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) {   
    // unit testing
        /* Deque<Integer> dq = new Deque<Integer>();
        dq.addFirst(1);
        dq.addFirst(2);
        dq.removeFirst();
        dq.addLast(4);
        dq.addLast(5);
        dq.addFirst(6);
        dq.addLast(7);
        dq.addLast(8);
        dq.addLast(9);
        dq.removeFirst();
        dq.removeFirst();
        dq.removeLast();
        Iterator<Integer> iter = dq.iterator();
        while (iter.hasNext()) {
            StdOut.printf("%d\n", iter.next());
        }
        //StdOut.printf("%d\n", dq.removeFirst());
        //StdOut.printf("%d\n", dq.removeFirst()); */
    }
}
