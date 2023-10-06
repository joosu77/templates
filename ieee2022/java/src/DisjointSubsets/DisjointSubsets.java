package DisjointSubsets;

import java.util.AbstractMap.SimpleImmutableEntry;
import java.util.HashMap;
import java.util.Optional;

public class DisjointSubsets<T> {

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
