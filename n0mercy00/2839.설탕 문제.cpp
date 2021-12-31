/*2839

초안

#include <iostream>

using namespace std;

int main()
{
    cout<<"2839설탕배달\n ";
    
    int N,A,B,temp;
    cin>>N;
    
    A=N/5;
    temp=N%5;
    B=temp/3;
    temp=temp%3;
    if(temp!=0){
        cout<<"-1";
        return -1;
    }else{
        cout<<A+B;
        return A+B;
    }

    return 0;
}

수정본

#include <iostream>

using namespace std;

int
main ()
{
  cout << "2839설탕배달\n";
  
  int a=0; //5로 나눈 경우 1포대
  int b=0; //3kg 에담은 11포대
  int answer=0; //return 값
  int temp =0;//임시 계산값
  int n = 0; //입력값
  
  cin>>n;
  //5kg 포대에 최대한 담는다
  a = n/5;
  
  while(a>=0){
    temp = (n-(5*a));
    
      //담은걸 3포대에 최대한 담아
      b= temp /3;
      
      if(temp%3==0){
          answer = a + b;
          cout<<answer;
          return answer; 
      }else{
          a--;
          //5랑 3조합으로 안되면 5한번 빼기
      }
  }
  
  //모든 경우에 안나눠지면 -1리턴
  cout<<a,n;
  return -1;

}

제출본

*/
#include <iostream>

using namespace std;

int
main ()
{
    
  int a=0; //5로 나눈 경우 1포대
  int b=0; //3kg 에담은 11포대
  int answer=0; //return 값
  int temp =0;//임시 계산값
  int n = 0; //입력값
  
  cin>>n;
  //5kg 포대에 최대한 담는다
  a = n/5;
  
  while(a>=0){
    temp = (n-(5*a));
    
      //담은걸 3포대에 최대한 담아
      b= temp /3;
      
      if(temp%3==0){
          answer = a + b;
          cout<<answer;
          return 0;
          
      }else{
          a--;
          //5랑 3조합으로 안되면 5한번 빼기
      }
  }
  
  //모든 경우에 안나눠지면 -1리턴
  cout<<-1;
  return 0;

}
