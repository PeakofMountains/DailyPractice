/*
 * Author: PeakofMountains
 * Date: 2020-10-28
 * Describe: 用数组解决约瑟夫环
*/
#include<stdio.h>
#include<stdlib.h>
#define MaxSize 30  //定义处理的最大长度
int main()
{
    struct Seats
    {
        int nextm;  //保存每个人的密码
        int order;  //保存每个人的编号
    }Seat;
    int n = 0,m = 0,i = 0;    
    scanf("%d %d",&n,&m);
    int length = n; // 将原始长度记录
    struct Seats seats[MaxSize];  // 创建数组
    int temp1=0;
    for(i=0;i<n;i++)
    {
        scanf("%d",&seats[i].nextm);
        seats[i].order=i+1; 
    }
    int num = 0;  // 记录当前出局人数
    do
    {  
        if(m%n!=0)  // 不能整除的情况
        {
            temp1 = seats[m%n-1].nextm; // 将要出局的人的密码保存
            seats[length]=seats[m%n-1]; // 将要出局的人的序号和密码信息记录
            for(int i=m%n-1;i<n-1;i++)  // 将出局人之后的所有人位置前移
            {
                seats[i]=seats[i+1];
                
                //seats[i].nextm=seat[i];
            }
            num++;  // 记录出局人数
            seats[length-num]=seats[length];  // 将出局人的信息保存
            m=temp1+m%n-1;  // 确定下一次出局的人是谁
        }
        else  //整除的情况，单独处理最后一个元素
        {
            temp1 = seats[n-1].nextm;// 将要出局的人的密码保存
            m=temp1;  // 决定下一个出局的人
            num++;
        }
        n--;  // 每次一个人出局，剩余的人数减一
    }while(n!=0);
    for(i=length-1;i>=0;i--)
    {
        printf("%d ",seats[i].order);// 将出局顺序信息打印
    }
    return 0;
}
