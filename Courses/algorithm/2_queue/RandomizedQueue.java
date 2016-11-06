import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Node first, last;
    private int len = 0;
    private class Node {
        Item item;
        Node next;
    }
    public RandomizedQueue() {               
    // construct an empty randomized queue
        first = null;
        last = null;
        len = 0;
    }
    public boolean isEmpty() {
    // is the queue empty?
        return len == 0;
    }                
    public int size() {
    // return the number of items on the queue
        return len;
    }

    public void enqueue(Item item) {
    // add the item
        if (item == null) 
            throw new NullPointerException();
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        if (isEmpty()) first = last;
        else oldlast.next = last;
        ++len;
    }

    public Item dequeue() {
    // remove and return a random item
        if (len == 0) { // isEmpty()
            throw new NoSuchElementException();
        }

        // create a helper that one step ahead of location pointer
        Node helper = new Node();
        helper.next = first;
        Node loc = helper; // copy or refrence?

        int randmove = StdRandom.uniform(len); //[0, len)
        
        for (int i = 0; i < randmove; ++i) {
            loc = loc.next;
            helper = helper.next; 
        }
        loc = loc.next; 
        Item item = loc.item;

        if (loc == first) {
            first = loc.next;
        } else if (loc == last) {
            last = helper;
            last.next = null;
        } else {
            helper.next = loc.next;
        }
        --len;
        return item;
    }

    public Item sample() {
    // return (but do not remove) a random item
        if (len == 0) { // isEmpty()
            throw new NoSuchElementException();
        }
        int randmove = StdRandom.uniform(len); // [0, len)
        Node loc = first;
        for (int i = 0; i < randmove; ++i) {
            loc = loc.next;
        }
        return loc.item;
    }

    public Iterator<Item> iterator() {
    // return an iterator over items in order from front to end
        return new ListIterator();  
    }

    private class ListIterator implements Iterator<Item> { 
    // return an independent iterator over items in random order
    // Repeated Code Alert

    // This output should be RANDOM!!! 
        public boolean hasNext() { return isEmpty(); }
        public void remove() {
            throw new UnsupportedOperationException();
        }
        public Item next() {
            if (!hasNext()) { // hasNext()
                throw new NoSuchElementException();
            }
            return dequeue();
        }
    }

    public static void main(String[] args) {   
        // unit testing
        RandomizedQueue<Integer> dq = new RandomizedQueue<Integer>();
        /*while (true) { // Ugly Code to read in
            try {
                String str = StdIn.readString();
                rq.enqueue(str);
            } catch (NoSuchElementException e) {
                // e.printStackTrace();
                break;
            }
        }*/
        
        dq.enqueue(1);
        dq.enqueue(2);
        dq.dequeue();
        dq.enqueue(4);
        dq.enqueue(5);
        dq.enqueue(6);
        dq.enqueue(7);
        dq.enqueue(8);
        dq.enqueue(9);
        dq.dequeue();
        dq.dequeue();
        dq.dequeue();
        
        Iterator<Integer> iter = dq.iterator();
        while (iter.hasNext()) {
            StdOut.printf("%d\n", iter.next());
        }
    }
}