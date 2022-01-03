/*1920

초안 -> 시간초과

#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int n,m;
    bool Yeah = false;
    //cout<<"n입력";
    cin>>n;
    int *a1 = new int[n];
    
    for (int i =0 ; i<n;i++){
        cin>>a1[i];
    }
    
    //cout<<"m입력";
    cin>>m;
    int *a2 = new int[m]; 
    for (int i =0 ; i<m;i++){
        cin>>a2[i];
    }

    for(int i=0; i<m;i++){
        for(int k=0;k<n;k++){
            if(a2[i]==a1[k]){
                cout<<1<<"\n";
                Yeah=true;
                break;
            }
            Yeah=false;
        }
        
        if(!Yeah){
            cout<<0<<"\n";
        }
    }
    
    

    return 0;
}

제출본(라이브러리 씀)
*/
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main()
{
    int n,m;
    int *find;
    scanf("%d",&n);
    int *a1 = new int[n];
  
    for (int i =0 ; i<n;i++){
        scanf("%d",&a1[i]);
    }
    
    sort(a1,a1+n);

    scanf("%d",&m);
    int *a2 = new int[m]; 
    for (int i =0 ; i<m;i++){
        scanf("%d",&a2[i]);
        if(binary_search(a1, a1 + n, a2[i])){
            printf("1\n");
        }else{
            printf("0\n");
        }
    }

   
    return 0;
}

