

import java.util.*;
import java.util.AbstractMap.SimpleImmutableEntry;

public class Network {

    public static class UpTreeSize<T> {

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
            return this.findPathHalving();
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

        public static <T> boolean inSameSet(UpTreeSize<T> a, UpTreeSize<T> b) {
            return a.getRoot() == b.getRoot();
        }
    }

    public static class DisjointSubsets<T> {

        public HashMap<T, UpTreeSize<T>> elements;

        public DisjointSubsets() {
            this.elements = new HashMap<>();
        }

        public void add(T index) {
            this.elements.put(index, new UpTreeSize<T>(index));
        }

    /*public void addWithCheck(T index, K data) {
        if (!this.elements.containsKey(index)) {
            this.elements.put(index, new SimpleImmutableEntry<>(new UpTreeSize<T>(index), data));
        }
    }*/

        public UpTreeSize<T> find(T index) {
            return this.elements.get(index);
        }

    /*public Optional<SimpleImmutableEntry<UpTreeSize<T>, K>> optionalFind(T index) {
        return Optional.ofNullable(this.elements.get(index));
    }

    public SimpleImmutableEntry<UpTreeSize<T>, K> findWithAdd(T index, K defaultData) {
        if (this.elements.containsKey(index)) {
            return this.elements.get(index);
        }
        this.elements.put(index, new SimpleImmutableEntry<>(new UpTreeSize<T>(index), defaultData));
        return this.elements.get(index);
    }*/

        public void join(T a, T b) {
            UpTreeSize.union(this.find(a), this.find(b));
        }

    /*public boolean joinWithCheck(T a, T b) {
        Optional<SimpleImmutableEntry<UpTreeSize<T>, K>> aElement = this.optionalFind(a);
        if (aElement.isEmpty()) {
            return false;
        }
        Optional<SimpleImmutableEntry<UpTreeSize<T>, K>> bElement = this.optionalFind(b);
        if (bElement.isEmpty()) {
            return false;
        }
        UpTreeSize.union(aElement.get().getKey(), bElement.get().getKey());
        return true;
    }

    public void joinWithAdd(T a, T b, K aDefaultData, K bDefaultData) {
        SimpleImmutableEntry<UpTreeSize<T>, K> aElement = this.findWithAdd(a, aDefaultData);
        SimpleImmutableEntry<UpTreeSize<T>, K> bElement = this.findWithAdd(b, bDefaultData);
        UpTreeSize.union(aElement.getKey(), bElement.getKey());
    }*/

        public boolean inSame(T a, T b) {
            return UpTreeSize.inSameSet(this.find(a), this.find(b));
        }

    /*public boolean inSameWithCheck(T a, T b) {
        Optional<SimpleImmutableEntry<UpTreeSize<T>, K>> aElement = this.optionalFind(a);
        if (aElement.isEmpty()) {
            return false;
        }
        Optional<SimpleImmutableEntry<UpTreeSize<T>, K>> bElement = this.optionalFind(b);
        if (bElement.isEmpty()) {
            return false;
        }
        return UpTreeSize.inSameSet(aElement.get().getKey(), bElement.get().getKey());
    }*/
    }

    public static class Edge {
        public String start;
        public String end;
        public int length;
        public Edge(String start, String end, int length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        HashMap<String, HashMap<String, SimpleImmutableEntry<Integer, Boolean>>> edges = new HashMap<>();
        HashSet<String> vertices = new HashSet<>();
        HashSet<String> redVertices = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] inp = sc.nextLine().split(" ");
            vertices.add(inp[0]);
            vertices.add(inp[1]);
            if (inp[3].equals("1")) {
                redVertices.add(inp[0]);
                redVertices.add(inp[1]);
            }
            if (!edges.containsKey(inp[0])) {
                edges.put(inp[0], new HashMap<>());
            }
            if (!edges.get(inp[0]).containsKey(inp[1])) {
                edges.get(inp[0]).put(inp[1], new SimpleImmutableEntry<>(Integer.parseInt(inp[2]), inp[3].equals("1")));
            }
        }

        HashMap<String, HashMap<String, Integer>> doubleEdges = new HashMap<>();
        for (String vertex: vertices) {
            doubleEdges.put(vertex, new HashMap<>());
        }
        for (String start: edges.keySet()) {
            for (String end: edges.get(start).keySet()) {
                //System.out.println("Adding");
                doubleEdges.get(start).put(end, edges.get(start).get(end).getKey());
                doubleEdges.get(end).put(start, edges.get(start).get(end).getKey());
            }
        }

        //System.out.println(redVertices.size());
        ArrayList<String> redVertexList = new ArrayList<>(redVertices);
        int bestCost = 2147483647;
        for (int i = 0; i < (1 << redVertices.size()); i++) {
            int thisCost = 0;
            int temp = i;
            HashSet<String> takenRedVertices = new HashSet<>();
            for (int j = 0; j < redVertices.size(); j++) {
                if (temp % 2 == 1) {
                    takenRedVertices.add(redVertexList.get(j));
                    thisCost += 10000;
                }
                temp = temp / 2;
            }
            //HashMap<String, HashMap<String, Integer>> thisEdges = new HashMap<>();
            PriorityQueue<Edge> queue = new PriorityQueue<>(11, new Comparator<Edge>() {
                @Override
                public int compare(Edge o1, Edge o2) {
                    return o1.length - o2.length;
                }
            });
            for (String start: edges.keySet()) {
                for (String end: edges.get(start).keySet()) {
                    if (edges.get(start).get(end).getValue() && !takenRedVertices.contains(start) && !takenRedVertices.contains(end)) {
                        continue;
                    }
                    //System.out.println(start + " " + end);
                    queue.add(new Edge(start, end, doubleEdges.get(start).get(end)));
                }
            }
            if (queue.size() < vertices.size() - 1) {
                continue;
            }
            //System.out.println("Case " + i);

            DisjointSubsets<String> subsets = new DisjointSubsets<String>();
            for (String vertex: vertices) {
                subsets.add(vertex);
            }

            HashSet<SimpleImmutableEntry<String, String>> subtreeEdges = new HashSet<>();
            while (!queue.isEmpty()) {
                Edge edge = queue.poll();
                //System.out.println(edge.start + " " + edge.end);
                if (!subsets.inSame(edge.start, edge.end)) {
                    subtreeEdges.add(new SimpleImmutableEntry<>(edge.start, edge.end));
                    subtreeEdges.add(new SimpleImmutableEntry<>(edge.end, edge.start));
                    subsets.join(edge.start, edge.end);
                    thisCost += edge.length;
                    if (thisCost > bestCost) {
                        break;
                    }
                }
            }
            if (subtreeEdges.size() < (vertices.size() - 1) * 2) {
                continue;
            }
            if (thisCost < bestCost) {
                bestCost = thisCost;
            }
            //System.out.println("Case " + i);
            //System.out.println(subtreeEdges.size());
            //System.out.println(" ");
        }
        System.out.println(bestCost);
    }
}
