import edu.princeton.cs.algs4.WeightedQuickUnionUF;
// import java.io.FileNotFoundException;
// import java.util.Scanner;
// import java.io.File;

public class Percolation {
    private WeightedQuickUnionUF grid;
    private int[] op;
    private int side, vecLen;

    // Encircle the map with "sentinel" sites. 
    // So: side --> side + 2; i --> i + 1; j --> j + 1;
    // And also a virtual "top" site at id = 0

    public Percolation(int n) {  // create n-by-n grid, with all sites blocked
        if (n <= 0) {
            throw new java.lang.IllegalArgumentException();
        }
        
        side = n + 2;
        vecLen = side * side + 2;
        grid = new WeightedQuickUnionUF(vecLen);
        op = new int[vecLen];
        for (int i = 1; i < vecLen; ++i) { op[i] = 0; }
        op[0] = 1; 
        op[vecLen-1] = 1;
    }

    public void open(int i, int j) {          
        // open site (row i, column j) if it is not open already
        if (i < 1 || i > side - 2 || j < 1 || j > side - 2) {
            throw new java.lang.IndexOutOfBoundsException();
        } 
        int id = i * side + j + 1; //(i + 1 - 1) * side + j + 1
        if (!isOpen(i, j)) {
            op[id] = 1; // Bad code. Should use "isOpen"
            int[] neighbor = getLegalNeighbor(i, j);
            for (int a = 0; a < neighbor.length; ++a) {
                if (op[neighbor[a]] == 1) 
                    grid.union(id, neighbor[a]);
            }
        }
    }

    public boolean isOpen(int i, int j) {    // is site (row i, column j) open?
        if (i < 1 || i > side - 2 || j < 1 || j > side - 2) {
            throw new java.lang.IndexOutOfBoundsException();
        }
        if (op[i* side + j + 1] == 1) return true;
        return false;
    }

    public boolean isFull(int i, int j) {     // is site (row i, column j) full?
        if (i < 1 || i > side - 2 || j < 1 || j > side - 2) {
            throw new java.lang.IndexOutOfBoundsException();
        }
        int id = i * side + j + 1;
        return grid.connected(id, 0);
    }

    public boolean percolates() {            // does the system percolate?
        if (grid.connected(0, vecLen-1)) { return true; }
        return false;
    }

    private int[] getLegalNeighbor(int i, int j) {
        i += 1; 
        j += 1;
        int id = (i - 1) * side + j;
        int[] neigh = new int[]{ id - side, id + side, id - 1, id + 1 };
        if (i == 2) { neigh = new int[]{0, id - side, id + side, id - 1, id + 1}; }
        if (i == side - 1) { neigh = new int[]{vecLen-1, id - side, id + side, id - 1, id + 1}; }
        return neigh; 
    }

    public static void main(String[] args) { // test client (optional)

        /* try {
            Scanner scanner = new Scanner(new File("./test/input8-no.txt"));
            int n = scanner.nextInt();
            Percolation perc = new Percolation(n);
            int i, j;
            while(scanner.hasNextInt()){
                i = scanner.nextInt(); j = scanner.nextInt();
                perc.open(i, j);
            }
            
            int[] foo = perc.op;
            int side = 10;
            for (int a = 0; a < side; ++a){
                for (int b = 0; b < side; ++b)
                    System.out.printf("%4d", foo[a*side + b + 1]);
                System.out.println();
            }
            
            System.out.println(perc.isFull(5,2));
            System.out.println(perc.percolates());

            scanner.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        } */  
    }  
    
}