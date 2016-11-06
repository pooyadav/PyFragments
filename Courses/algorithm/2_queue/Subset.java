import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.NoSuchElementException;

public class Subset {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        RandomizedQueue<String> rq = new RandomizedQueue<String>();
        while (true) { // Ugly Code to read in
            try {
                String str = StdIn.readString();
                rq.enqueue(str);
            } catch (NoSuchElementException e) {
                // e.printStackTrace();
                break;
            }
        }
        // int foo = rq.size();
        // Suppose 0<= n <= foo
        for (int i = 0; i < n; i++) 
            StdOut.printf("%s\n", rq.dequeue());
    }
}