package Graphs.NormalGraphs;

import java.util.*;
import java.util.AbstractMap.SimpleImmutableEntry;

public class Graph<T, D> {

    public HashMap<T, Node<T, D>> nodes;

    public Graph() {
        this.nodes = new HashMap<>();
    }

    public void addNode(T key, D data) {
        this.nodes.put(key, new Node<>(key, data));
    }

    public void addNode(T key) {
        this.nodes.put(key, new Node<>(key, null));
    }

    public void addConnection(T source, T target, int distance) {
        this.nodes.get(source).addNeighbour(this.nodes.get(target), distance);
    }

    public void addConnection(T source, T target) {
        this.nodes.get(source).addNeighbour(this.nodes.get(target), 1);
    }

    public void addBidirectionalConnection(T a, T b, int distance) {
        this.nodes.get(a).addNeighbour(this.nodes.get(b), distance);
        this.nodes.get(b).addNeighbour(this.nodes.get(a), distance);
    }

    public void addBidirectionalConnection(T a, T b) {
        this.nodes.get(a).addNeighbour(this.nodes.get(b), 1);
        this.nodes.get(b).addNeighbour(this.nodes.get(a), 1);
    }

    public void addConnectionWithObject(Node<T, D> source, Node<T, D> target, int distance) {
        source.addNeighbour(target, distance);
    }

    public void addConnectionWithObject(Node<T, D> source, Node<T, D> target) {
        source.addNeighbour(target, 1);
    }

    public void addBidirectionalConnectionWithObject(Node<T, D> a, Node<T, D> b, int distance) {
        a.addNeighbour(b, distance);
        b.addNeighbour(a, distance);
    }

    public void addBidirectionalConnectionWithObject(Node<T, D> a, Node<T, D> b) {
        a.addNeighbour(b, 1);
        b.addNeighbour(a, 1);
    }

    public SimpleImmutableEntry<HashMap<T, Integer>, HashMap<T, T>> dijkstra(T start) {
        Node<T, D> startNode = this.nodes.get(start);
        HashMap<T, Integer> distances = new HashMap<>();
        HashMap<T, T> previous = new HashMap<>();
        PriorityQueue<SimpleImmutableEntry<T, Integer>> queue = new PriorityQueue<>(11, new Comparator<SimpleImmutableEntry<T, Integer>>() {
            @Override
            public int compare(SimpleImmutableEntry<T, Integer> o1, SimpleImmutableEntry<T, Integer> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }
        });
        HashSet<T> explored = new HashSet<>();
        for (T key: this.nodes.keySet()) {
            distances.put(key, Integer.MAX_VALUE);
            previous.put(key, null);
        }
        distances.put(start, 0);
        queue.add(new SimpleImmutableEntry<>(start, 0));
        while (!queue.isEmpty()) {
            SimpleImmutableEntry<T, Integer> entry = queue.poll();
            if (explored.contains(entry.getKey())) {
                continue;
            }
            explored.add(entry.getKey());
            for (SimpleImmutableEntry<Integer, Node<T, D>> neighbour: this.nodes.get(entry.getKey()).neighbours) {
                int altDistance = entry.getValue() + neighbour.getKey();
                if (altDistance < distances.get(neighbour.getValue().key)) {
                    distances.put(neighbour.getValue().key, altDistance);
                    previous.put(neighbour.getValue().key, entry.getKey());
                    queue.add(new SimpleImmutableEntry<>(neighbour.getValue().key, altDistance));
                }
            }
        }
        return new SimpleImmutableEntry<>(distances, previous);
    }

    public static void main(String[] args) {
        long timeTaken = 0;
        int nodeAmount = 1000;
        int connectionAmount = 3000;
        Random random = new Random();
        for (int i = 0; i < 10000; i++) {
            Graph<String, Integer> graph = new Graph<>();
            for (int j = 0; j < nodeAmount; j++) {
                graph.addNode("A" + j, j);
            }
            ArrayList<Node<String, Integer>> nodes = new ArrayList<>(graph.nodes.values());
            for (int j = 0; j < connectionAmount; j++) {
                Node<String, Integer> a = nodes.get(random.nextInt(nodes.size() - 1));
            }
            timeTaken -= System.currentTimeMillis();


            timeTaken += System.currentTimeMillis();
        }
        System.out.println(timeTaken);
    }
}
