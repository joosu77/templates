import java.util.Scanner;

public class Maze {

    public static class UpTreeSize {

        public int index;
        public UpTreeSize parent;
        public int size;
        public int data;
        public boolean cycle;

        public UpTreeSize(int index) {
            this.index = index;
            this.parent = this;
            this.size = 1;
            this.data = 0;
            this.cycle = false;
        }

        /*public UpTreeSize<T> find() {
            UpTreeSize<T> root = this;
            while (root.parent != root) {
                root = root.parent;
            }

            UpTreeSize<T> active = this;
            UpTreeSize<T> next;
            while (active != root) {
                next = active.parent;
                active.parent = root;
                active = next;
            }

            return root;
        }*/

        public UpTreeSize findPathSplit() {
            UpTreeSize active = this;
            UpTreeSize temp;
            while (active.parent != active) {
                temp = active.parent;
                active.parent = temp.parent;
                active = temp;
            }
            return active;
        }

        /*public UpTreeSize<T> findPathHalving() {
            UpTreeSize<T> active = this;
            UpTreeSize<T> temp;
            while (active.parent != active) {
                active.parent = active.parent.parent;
                active = active.parent;
            }
            return active;
        }*/

        public UpTreeSize getRoot() {
            return this.findPathSplit();
        }

        public static void union(UpTreeSize a, UpTreeSize b) {
            //UpTreeSize aRoot = a.getRoot();
            //UpTreeSize bRoot = b.getRoot();
            if (a.size < b.size) {
                a.parent = b;
                b.size += a.size;
                b.cycle = b.cycle || a.cycle;
            } else if(b.size < a.size) {
                b.parent = a;
                a.size += b.size;
                a.cycle = a.cycle || b.cycle;
            } else {
                a.parent = b;
                b.size += a.size;
                b.cycle = b.cycle || a.cycle;
            }
        }

        public static void unionOrder(UpTreeSize a, UpTreeSize b) {
            //UpTreeSize aRoot = a.getRoot();
            //UpTreeSize bRoot = b.getRoot();
            b.parent = a;
            a.size += b.size;
            a.cycle = a.cycle || b.cycle;
        }

        public static boolean inSameSet(UpTreeSize a, UpTreeSize b) {
            return a.getRoot() == b.getRoot();
        }
    }

    public static class DisjointSubsets {

        public UpTreeSize[] elements;

        public DisjointSubsets(int n) {
            this.elements = new UpTreeSize[n * n];
            for (int i = 0; i < n * n; i++) {
                this.elements[i] = new UpTreeSize(i);
            }
        }

        public void add(int index) {
            this.elements[index] = new UpTreeSize(index);
        }

    /*public void addWithCheck(T index, K data) {
        if (!this.elements.containsKey(index)) {
            this.elements.put(index, new SimpleImmutableEntry<>(new UpTreeSize<T>(index), data));
        }
    }*/

        public UpTreeSize find(int index) {
            return this.elements[index];
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt();
        int N = n;
        DisjointSubsets subsets = new DisjointSubsets(n);
        subsets.elements[0].data = 3;
        subsets.elements[n - 1].data = 2;
        subsets.elements[N * (n - 1) + n - 1].data = 1;
        boolean hasToy = false;
        boolean hasPrinted = false;
        int x0, y0, x1, y1;
        char ch;
        for (int i = 0; i < w; i++) {
            //String[] query = sc.nextLine().split(" ");
            x0 = sc.nextInt();
            y0 = sc.nextInt();
            ch = sc.nextLine().charAt(1);
            x1 = x0;
            y1 = y0;
            //System.out.println(ch);
            switch (ch) {
                case 'S':  // S
                    x1++;
                    break;
                case 'N':  // N
                    x1--;
                    break;
                case 'E':  // E
                    y1++;
                    break;
                default:  // W
                    y1--;
                    break;
            }
            UpTreeSize a = subsets.find(x0 * N + y0).getRoot();
            UpTreeSize b = subsets.find(x1 * n + y1).getRoot();
            UpTreeSize temp;
            if (b.data > a.data) {
                temp = a;
                a = b;
                b = temp;
            }
            if (a.data == 3) {
                if (b.data == 3) {
                    System.out.println("L");
                    hasPrinted = true;
                } else if (b.data == 2) {
                    System.out.println("M");
                    hasPrinted = true;
                } else if (b.data == 1) {
                    if (b.cycle) {
                        System.out.println("L");
                        hasPrinted = true;
                    } else {
                        UpTreeSize.unionOrder(a, b);
                        hasToy = true;
                    }
                } else if (b.data == 0) {
                    if (b.cycle) {
                        System.out.println("L");
                        hasPrinted = true;
                    } else {
                        UpTreeSize.unionOrder(a, b);
                    }
                }
            } else if (a.data == 2) {
                if (b.data == 2) {
                    b.cycle = true;
                } else {
                    UpTreeSize.unionOrder(a, b);
                }
            } else if (a.data == 1) {
                if (b.data == 1) {
                    a.cycle = true;
                } else {
                    UpTreeSize.unionOrder(a, b);
                }
            } else {
                if (a == b) {
                    a.cycle = true;
                } else {
                    UpTreeSize.union(a, b);
                }
            }
            if (hasPrinted) {
                hasPrinted = false;
            } else {
                if (hasToy) {
                    System.out.println("T");
                } else {
                    System.out.println("K");
                }
            }
        }
    }
}
