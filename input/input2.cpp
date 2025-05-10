#include <iostream>
using namespace std;

int max(int arr[],int size){
        int max=arr[0];
        for(int i=0;i<size;i++){
                max=(arr[i]>max?arr[i]:max);
        }
        return max;
}

int main(){
        int array[]={1,2,3,99,6};
        int size=sizeof(array)/sizeof(int);
        cout<<max(array,size);
}