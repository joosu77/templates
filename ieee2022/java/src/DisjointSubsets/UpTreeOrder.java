package DisjointSubsets;

import java.util.ArrayList;
import java.util.Random;

public class UpTreeOrder<T> {

    public T index;
    public UpTreeOrder<T> parent;
    public int order;

    public UpTreeOrder(T index) {
        this.index = index;
        this.parent = this;
        this.order = 0;
    }

    public UpTreeOrder<T> find() {
        UpTreeOrder<T> root = this;
        while (root.parent != root) {
            root = root.parent;
        }

        UpTreeOrder<T> active = this;
        UpTreeOrder<T> next;
        while (active != root) {
            next = active.parent;
            active.parent = root;
            active = next;
        }

        return root;
    }

    public UpTreeOrder<T> findPathSplit() {
        UpTreeOrder<T> active = this;
        UpTreeOrder<T> temp;
        while (active.parent != active) {
            temp = active.parent;
            active.parent = temp.parent;
            active = temp;
        }
        return active;
    }

    public UpTreeOrder<T> findPathHalving() {
        UpTreeOrder<T> active = this;
        UpTreeOrder<T> temp;
        while (active.parent != active) {
            active.parent = active.parent.parent;
            active = active.parent;
        }
        return active;
    }

    public UpTreeOrder<T> getRoot() {
        return this.find();
    }

    public static <T> void union(UpTreeOrder<T> a, UpTreeOrder<T> b) {
        UpTreeOrder<T> aRoot = a.getRoot();
        UpTreeOrder<T> bRoot = b.getRoot();
        if (aRoot.order < bRoot.order) {
            aRoot.parent = bRoot;
        } else if(bRoot.order < aRoot.order) {
            bRoot.parent = aRoot;
        } else {
            aRoot.parent = bRoot;
            bRoot.order++;
        }
    }

    public static <T> UpTreeOrder<T> unionWithReturn(UpTreeOrder<T> a, UpTreeOrder<T> b) {
        UpTreeOrder<T> aRoot = a.getRoot();
        UpTreeOrder<T> bRoot = b.getRoot();
        if (aRoot.order < bRoot.order) {
            aRoot.parent = bRoot;
            return bRoot;
        }
        if(bRoot.order < aRoot.order) {
            bRoot.parent = aRoot;
            return aRoot;
        }
        aRoot.parent = bRoot;
        bRoot.order++;
        return bRoot;
    }

    public static <T> boolean inSameSet(UpTreeOrder<T> a, UpTreeOrder<T> b) {
        return a.getRoot() == b.getRoot();
    }

    public static void main(String[] args) {
        Random random = new Random();
        ArrayList<UpTreeOrder<Integer>> trees = new ArrayList<>();
        long totalTime = - System.currentTimeMillis();
        for (int i = 0; i < 1000000; i++) {
            UpTreeOrder<Integer> tree = new UpTreeOrder<>(i);
            trees.add(tree);
            union(tree, trees.get(random.nextInt(trees.size())));
        }
        System.out.println((totalTime + System.currentTimeMillis()) / 1000.0);
    }
}
