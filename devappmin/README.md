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