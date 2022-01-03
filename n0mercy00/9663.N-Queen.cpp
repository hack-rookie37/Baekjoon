//참조 : https://chanhuiseok.github.io/posts/baek-1/
#include <iostream>
#include <stdlib.h>
using namespace std;

int answer = 0;
int n;
int board[15];                  //퀸의 위치를 표시하는 배열 
                                //배열의 인덱스는 행을 value는 열을 의미

//현재위치에 체크 가능한지
bool passable(int position){
    for(int i = 0 ; i< position;i++){
        //열이 같거나 대각선에 위치한다면 짤
        //행은 볼필요 없음 인덱스 자체가 행이니깐
        if(board[position]==board[i]||position-i==abs(board[position]-board[i])){
            return false;
        }
    }
    
    return true;
}

void Queen(int position){
    
    //n번째 퀸이 들어온다면
    if(position==n){
        answer++;
        return;
    }
    
    for(int i = 0 ; i<n ; i++){
        board[position]=i;         //[position][i] 에 퀸을 위위치를
        if(passable(position)){
            //만약 현재위치에 퀸을 놓는게 가능하다면 퀸을 두고
            //그 다음행에 퀸을 두러 간다.
            Queen(position+1);
        }
    }
}

int main()
{
    cin>>n;
    Queen(0);
    cout<<answer;
    return 0;
}
