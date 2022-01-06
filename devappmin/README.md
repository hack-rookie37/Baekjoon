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
