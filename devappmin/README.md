# Tips

## LCS

문자열 크기의 2D Array를 선언한 후, 첫 행은 0으로 삽입.

```
만약, 비교하는 위치의 문자가 서로 같으면
    현재 위치의 값 = 왼쪽 대각선 값 + 1  (배열 범위를 벗어났으면 0이라고 가정)
다르다면
    현재 위치의 값 = MAX{왼쪽 값, 위쪽 값}
```

## LIS

LIS는 가장 긴 증가하는 부분 수열 길이를 구하는 방법이다.

주어진 값은 대부분 숫자로 이루어진 배열이고 해당 배열 내에서 증가하는 수열 중 가장 큰 수열의 길이를 구하는 문제이다.

### Case 1

```python
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[j] = max(dp[i], dp[j] + 1)

print(max(dp))
```

### Case 2

```python
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
```

> 중가하는 가장 큰 수열의 길이를 구하는 것이지, 모든 수열의 경우를 출력하는 것이 아님을 유의하자.

## 트리의 지름 구하기

트리의 지름을 구하기 위해서는 무작위 정점을 하나 고르고 그 정점에서 가장 먼 정점을 구한 뒤에 그 정점과 그 정점에서 가장 먼 정점의 거리를 구하면 된다.

```
1. 임의의 정점으로 부터 가장 먼 정점을 구한다.
2. 1에서 나온 정점으로 부터 가장 먼 정점을 구한다.
3. 1과 2에서 나온 정점간의 거리가 트리의 지름!

이 말은 즉슨,

1. 트리에서 임의의 정점 x를 잡는다.
2. 정점 x에서 가장 먼 정점 y를 찾는다.
3. 정점 y에서 가장 먼 정점 z를 찾는다.
```

## Priority Queue Dijkstra

```python
def dijkstra(graph, start, fin):

    # 시작점을 제외한 모든 거리를 무한대로 저장
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    q = []

    # heapq로 (거리, 노드)로 입력
    heappush(q, [dist[start], start])

    while q:
        c_dist, c_dest = heappop(q)

        if dist[c_dest] < c_dist:
            continue

        for n_dest, n_dist in graph[c_dest]:
            d = c_dist + n_dist
            if d < dist[n_dest]:
                dist[n_dest] = d
                heappush(q, [d, n_dest])

    return dist[fin]
```

`dist`에는 start 노드에서 각 노드까지 최단경로가 저장이 되는 곳이다.

여기에는 자기 자신은 0으로 나머지는 전부 무한대로 생각을 하고 값을 저장한다.

그 이후에는 `priority_queue`를 생성하고 (출발 지점까지 거리(0), 출발 지점 노드)를 넣는다.

이후 큐에서 반복하여 값을 빼오면서 `dist[큐에서 뺀 노드]`의 값이 `큐에서 뺀 거리`의 값보다 클 경우에,

해당 지점까지의 최단경로를 찾고 존재하면 dist에 넣어준 뒤 큐에다가 삽입한다.

## Bellman-Ford

```python
def bellman_ford(world, dist, start, n):
    dist[start] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for next_node, weight in world[j]:
                if dist[next_node] > dist[j] + weight:
                    dist[next_node] = dist[j] + weight
                    if i == n:
                        return True
    return False
```

`graph`와 `dist`을 구하는 방식은 다익스트라와 동일.

하지만 전체를 돌면서 체크를 하는 부분이 다르다.

# C++

## prev_permutation, next_permutation

순열을 구하기 위해 사용할 수 있는 간단한 알고리즘

알고리즘 라이브러리를 추가해야 한다.

```c++
#include <algorithm>
```

해당 값은 `do-while`문에다가 넣어줘야한다.

```c++
bool next_permutation (BidirectionalIterator first, BidirectionalIterator last);
bool prev_permutation (BidirectionalIterator first, BidirectionalIterator last);
```

### 예제

```c++
int arr[100];
bool check[100];

do {
    for(int i = 0; i < 100; i++) {
        if(check[i])
            cout << arr[i];
    }
    cout << endl;
} while(prev_permutation(check, check + 100))
// vector의 경우 vector.begin(), vector.end()
```

## priority_queue

`priority_queue`는 `queue`와 동일하게 생성하고 사용하면 된다.

```c++
priority_queue<int> pq;
```

하지만 이러면 값이 내림차순으로 정렬이 되기 떄문에 이를 정렬하는 방식을 `priority_queue`의 세번째 인자 값으로 넣어줘야한다.

```c++
priority_queue<int, vector<int>, greater<int> > inversed_pq;
```

추가적으로 만약에 값을 원하는 방식으로 정렬하고 싶을 경우 아래처럼 `operator`를 직접 정의해준 후에 풀면 된다.

```c++
// User defined class, Point
class Point
{
   int x;
   int y;
public:
   Point(int _x, int _y)
   {
      x = _x;
      y = _y;
   }
   int getX() const { return x; }
   int getY() const { return y; }
};

// To compare two points
class myComparator
{
public:
    int operator() (const Point& p1, const Point& p2)
    {
        return p1.getX() > p2.getX();
    }
};

int main() {
    priority_queue<Point, vector<Point>, myComparator > custom_pq;
}
```

## multiset

`multiset`은 `set`과 동일하나 동일한 키 값을 가질 수 있다는 차이를 가지고 있음.

`7662.이중 우선순위 큐.cpp`를 해결하기 위해서 사용했으며 `iterators`인 multiset의 `end()`와 `begin()`을 통해서 첫 값과 마지막 값을 가져올 수 있음.

이 때 주의할 점은 `ms.end()`가 아닌 `--ms.end()`를 통해서 마지막 전 값을 가져와야 하고, 포인터를 통해서 값을 가져와야 함.

또한 중복되는 키가 있을 때 `erase`를 하면 전부 삭제 됨. 이 떄 `ms.lower_bound()`를 사용해서 삭제하면 하나만 삭제 됨.

```c++
multiset<int> ms;

ms.insert(1);
ms.insert(1);
ms.insert(2);

ms.erase(1); // ms는 { 2 }
ms.erase(ms.lower_bound(1)); // ms는 { 1, 2 }
```

# Python

## Set

### Discard / Remove

```python
s = set()
s.remove(1) # 1이 없으면 에러가 남.
s.discard(1) # 1이 없어도 에러가 안 남.
```

## Recursion

재귀 함수를 하다가 `RecursionError`를 만났을 경우 아래 라인을 추가해서 해결할 수 있다.

```python
sys.setrecursionlimit(10**6) # 혹은 그 이상의 값.
```
