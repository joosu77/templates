package Graphs.NormalGraphs;

import java.util.AbstractMap.SimpleImmutableEntry;
import java.util.ArrayList;
import java.util.List;

public class Node<T, D> {

    public T key;
    public D data;
    public List<SimpleImmutableEntry<Integer, Node<T, D>>> neighbours;

    public Node(T key, D data) {
        this.key = key;
        this.data = data;
        this.neighbours = new ArrayList<>();
    }

    public void addNeighbour(Node<T, D> neighbour, int distance) {
        this.neighbours.add(new SimpleImmutableEntry<>(distance, neighbour));
    }

    public void addNeighbour(Node<T, D> neighbour) {
        this.neighbours.add(new SimpleImmutableEntry<>(1, neighbour));
    }
}
