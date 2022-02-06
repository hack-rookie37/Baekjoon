# Tips

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

## LCS
문자열 크기의 2D Array를 선언한 후, 첫 행은 0으로 삽입.
```
만약, 비교하는 위치의 문자가 서로 같으면 
    현재 위치의 값 = 왼쪽 대각선 값 + 1  (배열 범위를 벗어났으면 0이라고 가정)
다르다면  
    현재 위치의 값 = MAX{왼쪽 값, 위쪽 값}    
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
