package DisjointSubsets;

import java.util.ArrayList;
import java.util.Random;

public class UpTreeSize<T> {

    public T index;
    public UpTreeSize<T> parent;
    public int size;

    public UpTreeSize(T index) {
        this.index = index;
        this.parent = this;
        this.size = 1;
    }

    public UpTreeSize<T> find() {
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
    }

    public UpTreeSize<T> findPathSplit() {
        UpTreeSize<T> active = this;
        UpTreeSize<T> temp;
        while (active.parent != active) {
            temp = active.parent;
            active.parent = temp.parent;
            active = temp;
        }
        return active;
    }

    public UpTreeSize<T> findPathHalving() {
        UpTreeSize<T> active = this;
        UpTreeSize<T> temp;
        while (active.parent != active) {
            active.parent = active.parent.parent;
            active = active.parent;
        }
        return active;
    }

    public UpTreeSize<T> getRoot() {
        return this.find();
    }

    public static <T> void union(UpTreeSize<T> a, UpTreeSize<T> b) {
        UpTreeSize<T> aRoot = a.getRoot();
        UpTreeSize<T> bRoot = b.getRoot();
        if (aRoot.size < bRoot.size) {
            aRoot.parent = bRoot;
            bRoot.size += aRoot.size;
        } else if(bRoot.size < aRoot.size) {
            bRoot.parent = aRoot;
            aRoot.size += bRoot.size;
        } else {
            aRoot.parent = bRoot;
            bRoot.size += aRoot.size;
        }
    }

    public static <T> UpTreeSize<T> unionWithReturn(UpTreeSize<T> a, UpTreeSize<T> b) {
        UpTreeSize<T> aRoot = a.getRoot();
        UpTreeSize<T> bRoot = b.getRoot();
        if (aRoot.size < bRoot.size) {
            aRoot.parent = bRoot;
            bRoot.size += aRoot.size;
            return bRoot;
        }
        if(bRoot.size < aRoot.size) {
            bRoot.parent = aRoot;
            aRoot.size += bRoot.size;
            return aRoot;
        }
        aRoot.parent = bRoot;
        bRoot.size += aRoot.size;
        return bRoot;
    }

    public static <T> boolean inSameSet(UpTreeSize<T> a, UpTreeSize<T> b) {
        return a.getRoot() == b.getRoot();
    }

    public static void main(String[] args) {
        Random random = new Random();
        ArrayList<UpTreeSize<Integer>> trees = new ArrayList<>();
        long totalTime = - System.currentTimeMillis();
        for (int i = 0; i < 1000000; i++) {
            UpTreeSize<Integer> tree = new UpTreeSize<>(i);
            trees.add(tree);
            union(tree, trees.get(random.nextInt(trees.size())));
        }
        System.out.println((totalTime + System.currentTimeMillis()) / 1000.0);
    }
}
