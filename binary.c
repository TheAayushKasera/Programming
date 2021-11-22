#include<stdio.h>
#include<conio.h>
int search(int arr[],int size,int srch){
    int first=0,last=size-1,mid=(first+last)/2,pos=-1;
    while(first<=last){
        printf("mid=%d\n",mid);
        if(srch==arr[mid]){
            pos=mid;
            break;
        }
        else if(srch>arr[mid]){
            first=mid+1;
            mid=(first+last)/2;
            
        }
        else{
            last=mid-1;
            mid=(first+last)/2;
        }   
        mid=(first+last)/2;    
        printf("pos=%d %d\n",pos,last);
    }
    printf("pos=%d\n",pos);
    return pos;
}
int main(){
    int arr[10],srch,i,result;
    printf("Input Sorted array of 10 elements");
    for(i=0;i<10;i++){
        scanf("%d",&arr[i]);
    }
    printf("Input number to find its position in the array");
    scanf("%d",&srch);
    result=search(arr,10,srch);
    if(result==-1) printf("Error searching");
    else printf("Psition is %d",result+1);
    return 0;
}