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
