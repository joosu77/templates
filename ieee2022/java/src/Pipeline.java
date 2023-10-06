// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Pipeline {

    static class Area {
        int index;
        int amount;
        public Area(int index) {
            this.index = index;
            this.amount = 0;
        }
    }

    public static void main (String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);

        // Read the number of testcases
        int t = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < t; i++) {
            String[] size = sc.nextLine().split(" ");
            int n = Integer.parseInt(size[0]);
            int m = Integer.parseInt(size[1]);
            int d = Integer.parseInt(size[2]);

            int[][][] amounts = new int[d][m][n];
            boolean[][][] visited = new boolean[d][m][n];
            int[][][] area = new int[d][m][n];
            int innerSpace = 0;

            for (int a = 0; a < d; a++) {
                for (int b = 0; b < n; b++) {
                    String current = sc.nextLine();
                    int c = 0;
                    for (char ch: current.toCharArray()) {
                        visited[a][c][b] = false;
                        area[a][c][b] = -1;
                        if (ch == '*') {
                            amounts[a][c][b] = 3;
                            innerSpace += 3;
                        } else if (ch == 'o') {
                            amounts[a][c][b] = 2;
                            innerSpace += 2;
                        } else {
                            amounts[a][c][b] = 0;
                        }
                        c++;
                    }
                }
                sc.nextLine();
            }

            List<Integer> areas = new ArrayList<>();
            int[][] stack = new int[1000][3];
            int stackSize = 0;
            int a = 0;
            int b = 0;
            int c = 0;
            while (a < d || b < m || c < n) {
                stack[stackSize] = new int[]{a, b, c};
                stackSize++;
                while (stackSize > 0) {
                    stackSize--;
                    int[] current = stack[stackSize];

                }
            }

            if (innerSpace % 2 == 1) {
                System.out.println("NO");
                continue;
            }
            // TODO: check better
            System.out.println("YES");
        }
    }
}
