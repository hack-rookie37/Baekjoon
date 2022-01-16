//제출본

#include <iostream>
#include<stdio.h>
#include <algorithm>

using namespace std;
int forest[1000000];
int n=0; // 나무갯수
int m=0; // 필요 미터
int h=0; //컷팅라인

int cut(int h, int n){
    int temp = 0 ;
    
    for(int i=0;i<n;i++){
        if(forest[i]-h>0){
            temp+=forest[i]-h;
        }
    }
    return temp;
}

int bcut(int left,int right){
    int mid=(left+right)/2;
    int temp = cut(mid,n);
    if(m>temp){
        return bcut(mid+1,right);
    }else if(m<temp){
        return bcut(left,mid-1);
    }else{
        return mid;
    }
}

int main()
{
    int temp=0;
    scanf("%d",&n);
    scanf("%d",&m);
    for(int i=0;i<n;i++){
        scanf("%d",&forest[i]);
    }
    temp= *max_element(&forest[0],&forest[n]);
    int mid = temp/2;
    int answer = bcut(temp,0);
    printf("%d",answer);
    return 0;
}