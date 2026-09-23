# 5. 🧩 Array Searching

Searching means:

> **Given an array and a target, determine where the target is—or whether it exists.**

There are two fundamental approaches:

* **Linear search** → inspect elements one by one.
* **Binary search** → repeatedly eliminate half of a **sorted** search space.

---

# 5.1 🔎 Linear Search

Linear search is the natural approach when you **don't have an ordering that lets you eliminate elements**.

```python id="c8i0fm"
arr = [7, 3, 9, 2, 5]
target = 9

for i, x in enumerate(arr):
    if x == target:
        print(i)
        break
```

Here we check:

```text
7 → 3 → 9 ✓
```

### Find the first occurrence

Stop at the first match:

```python id="1j8q9k"
def first_occurrence(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
```

```python
first_occurrence([2, 5, 3, 5, 7], 5)
# 1
```

### Find the last occurrence

Don't stop after finding a match. Keep updating the answer:

```python id="y1ap5v"
def last_occurrence(arr, target):
    ans = -1

    for i, x in enumerate(arr):
        if x == target:
            ans = i

    return ans
```

```python
last_occurrence([2, 5, 3, 5, 7], 5)
# 3
```

### Find all occurrences

Collect every matching index:

```python id="7c3c1k"
def all_occurrences(arr, target):
    ans = []

    for i, x in enumerate(arr):
        if x == target:
            ans.append(i)

    return ans
```

```python
all_occurrences([5, 2, 5, 3, 5], 5)
# [0, 2, 4]
```

### Count occurrences

You don't need to store the indices:

```python id="7w7n9j"
count = 0

for x in arr:
    if x == target:
        count += 1
```

Or simply:

```python
count = arr.count(target)
```

For learning DSA, the loop is important because it exposes the underlying pattern.

### Complexity

For `n` elements:

* **Time:** `O(n)`
* **Extra space:** `O(1)` for first/last/count
* **All occurrences:** `O(k)` output space, where `k` is the number of matches.

Worst case, linear search may inspect **every element**.

---

# 5.2 ⚡ Binary Search

Binary search uses a completely different idea:

> **If the search space is sorted, one comparison can eliminate half of it.**

Prerequisite for ordinary binary search:

> **The array must be sorted according to the ordering you're searching.**

Example:

```text
[2, 5, 8, 12, 16, 23, 38]
```

Suppose target = `16`.

Instead of checking every element:

```text
2 → 5 → 8 → 12 → 16
```

we repeatedly inspect the middle and discard half.


### The search space

Maintain a range of possible answers:

```text
left                 right
  ↓                     ↓
[ 2, 5, 8, 12, 16, 23, 38 ]
```

Initially:

```python id="h6n3yp"
left = 0
right = len(arr) - 1
```

### Middle

```python id="y3m0ba"
mid = (left + right) // 2
```

Then compare:

```text
arr[mid] vs target
```

Three possibilities:

### 1. Found

```text
arr[mid] == target
```

Return `mid`.

### 2. Target is smaller

```text
arr[mid] > target
```

Everything from `mid` onward is too large.

Search the left half:

```python id="w7jzci"
right = mid - 1
```

### 3. Target is larger

```text
arr[mid] < target
```

Everything through `mid` is too small.

Search the right half:

```python id="w8v6i6"
left = mid + 1
```

### Standard implementation

```python id="h5g5mc"
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

The important invariant is:

> **If the target exists, it must still be inside `[left, right]`.**

The loop continues while there is a valid candidate:

```python
while left <= right:
```

When:

```text
left > right
```

the search space is empty, so the target doesn't exist.

### Complexity

Each iteration roughly halves the search space:

```text
n → n/2 → n/4 → n/8 → ...
```

So:

* **Time:** `O(log n)`
* **Extra space:** `O(1)` iterative

---

# 5.3 🔍 Binary Search Variations

This is where binary search becomes a **problem-solving pattern**, not just a "find target" algorithm.

The central idea is:

> **Don't always ask "Is `target` present?" Ask what boundary or condition you're trying to locate.**

Consider:

```text
arr = [1, 2, 2, 2, 4, 7, 9]
             ↑
           target = 2
```

There are multiple useful answers.

---

## First occurrence

Find the **leftmost** `target`.

Instead of stopping when you find `2`, record it and continue left.

```python id="7kz1cj"
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

The key modification is:

```python
ans = mid
right = mid - 1
```

**Found it, but maybe there is another occurrence further left.**

---

## Last occurrence

Symmetrically:

```python id="vq6a4x"
def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

When found:

```python
ans = mid
left = mid + 1
```

**Found it, but maybe there is another occurrence further right.**

---

# Lower Bound

**Lower bound** = first position where:

```text
arr[i] >= target
```

Example:

```text
arr = [1, 2, 4, 4, 7, 9]
target = 4

answer = 2
```

Because index `2` is the first position containing a value `≥ 4`.

A useful implementation:

```python id="0l9z5r"
def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

Notice the search interval is:

```python
[0, len(arr))
```

rather than `[0, len(arr)-1]`.

The answer can legitimately be `len(arr)` when every element is smaller than the target.

---

# Upper Bound

**Upper bound** = first position where:

```text
arr[i] > target
```

Example:

```text
arr = [1, 2, 4, 4, 7, 9]
target = 4

answer = 4
```

Index `4` contains `7`, the first value greater than `4`.

```python id="2l2e8c"
def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

### The key distinction

```text
lower_bound → first element >= target
upper_bound → first element >  target
```

This is one of the most important binary-search definitions to remember.

---

## First element ≥ target

That's exactly:

```text
lower_bound(target)
```

## First element > target

That's exactly:

```text
upper_bound(target)
```

---

## Last element ≤ target

If `upper_bound(target)` gives the first index with value `> target`, then the previous index is the last index with value `≤ target`.

```python id="2n9w2f"
i = upper_bound(arr, target)
answer = i - 1
```

You still need to check whether `answer >= 0`.

---

## Last element < target

If `lower_bound(target)` gives the first index with value `≥ target`, then:

```python id="m0w1xp"
i = lower_bound(arr, target)
answer = i - 1
```

Again, `answer` may be `-1` if no such element exists.

---

# Count occurrences

For a **sorted array**, if:

```text
first = first occurrence of target
last  = last occurrence of target
```

then:

```text
count = last - first + 1
```

Or using bounds:

```text
count = upper_bound(target) - lower_bound(target)
```

Example:

```text
[1, 2, 2, 2, 4, 7]
    ↑     ↑
   first last

count = 3
```

Using bounds:

```text
lower_bound(2) = 1
upper_bound(2) = 4

4 - 1 = 3
```

---

# Search Insertion Position

Suppose:

```text
arr = [1, 3, 5, 6]
target = 4
```

Where should `4` be inserted while keeping the array sorted?

```text
[1, 3, 4, 5, 6]
      ↑
    index 2
```

The answer is the **first position where `arr[i] >= target`**.

Therefore:

> **Insertion position = lower bound**

```python
lower_bound(arr, target)
```

For:

```text
target = 5
```

the answer is `2`, because `5` already occupies index `2`.

For:

```text
target = 7
```

the answer is `4`, meaning it would be inserted at the end.

---

# 🧠 The Binary Search Pattern

Instead of memorizing ten separate algorithms, recognize the underlying pattern:

```text
              Binary Search
                    │
          ┌─────────┴─────────┐
          │                   │
    Exact target          Boundary
          │                   │
     find target       ┌───────┴───────┐
                       │               │
                first valid       last valid
```

The most useful boundary definitions are:

| Question          | Boundary                    |
| ----------------- | --------------------------- |
| First `>= target` | **Lower bound**             |
| First `> target`  | **Upper bound**             |
| Last `<= target`  | `upper_bound - 1`           |
| Last `< target`   | `lower_bound - 1`           |
| First occurrence  | first `== target`           |
| Last occurrence   | last `== target`            |
| Count target      | `upper_bound - lower_bound` |
| Insert target     | `lower_bound`               |

### One mental shift

Basic binary search asks:

> **"Is the target here?"**

Boundary binary search asks:

> **"Where does a condition change from false to true?"**

That second way of thinking is the foundation for many harder binary-search problems later.

chat reference: https://chatgpt.com/share/6ab34d8a-474c-83ee-94ee-c580118d1118