//1260

//제출본 
/*
@출처 : https://jun-itworld.tistory.com/18

*/

#include <iostream>
#include <queue> 
using namespace std;

#define MAX 1001        //0노드가 0부터 시작이 아니니깐 1001
int N,M,V;              //각 노드,간선,시작지점
int matrix[MAX][MAX];   //각 노드별 이동 경로 저장을 위한 행렬
int visit[MAX];         //방문 지점 체크

void DFS(int v){
    
    //시작 지점 출력
    cout<<v<<" ";
    visit[v]=1;         //방문지점 체크
    
    //노드 수만큼 반복
    for(int i=1;i<=N;i++){
        
        //이미 방문했거나 길이 없는 노드는 패스
        if(visit[i]==1||matrix[v][i]==0){
            continue;
        }
        
        //방문한적이 없고 길이 이어져 있는 노드는 재귀 실행 
        
        DFS(i);
    }
}

void BFS(int v){
    queue<int> q;
    q.push(v);
    
    visit[v]=2;         //방문지 초기화 안해서 1말고 다른거
    while(!q.empty()){
        v=q.front();    //여기 이해안감 q에 v하나있는거아님?
        cout<<q.front()<<" "; 
        q.pop();
        
        for(int i=1; i<=N; i++) {
            if(visit[i] == 2 || matrix[v][i] == 0)
                continue;
            q.push(i);
            visit[i] = 2;
        }
    }
}

int main()
{
    int start,desiny;   //노드 경로 시작점과 도착지점
    cin>>N>>M>>V;       //문제에서 정의 노드수,간선수,시작지점
    
    //간선들 저장
    for(int i = 0 ; i< M;i++){
        cin>>start>>desiny;
        
        //경로가 있음을 표시
        matrix[start][desiny]=1;
        //양방향 경로니 반대도 표시
        matrix[desiny][start]=1;
    }
    
    //깊이우선 실행
    DFS(V);
    cout<<"\n";
    //너비우선 실행
    BFS(V);
    
    return 0;
}
