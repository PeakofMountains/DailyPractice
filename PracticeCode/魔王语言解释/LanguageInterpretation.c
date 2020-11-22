/*
 * Author: PeakofMountains
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100    // 定义最大处理长度

typedef char DataforStack,DataforQueue;   // 为方便编程，给char两个别名DataforStack,DataforQueue
 
typedef struct node{    // 存储信息和指向下一位节点的指针
    DataforStack data;
    struct node *link;
}StackNode,QueueNode;// 栈、队列结点定义(一样的结构)
 
typedef struct{   // 单向链表实现栈
    StackNode* top; // 栈中只保存栈顶指针
}Stack;
 
typedef struct{ // 链表实现队列
    QueueNode *rear,*front; // 包含头尾指针
}Queue;
 
void InitStack(Stack *s)// 初始化栈
{
    s->top=NULL;    // 初始化时栈顶指针置空，说明此时栈为空
}
int Push(Stack *S,DataforStack x) // 入栈-----返回值为1表示成功为0表示失败
{
    StackNode *p=(StackNode*)malloc(sizeof(StackNode)); // 在使用的时候申请空间(保存信息的StackNode节点大小)
    if(!p) return 0;    // 为空函数返回0
    p->data=x;  // 将数据存储到节点的数据点
    p->link=S->top; // 节点指针指向前一位
    S->top=p;   // 头插法构建单向链表， 其中S->top也作为链表的头指针起作用    
    // S->top指针指向最左节点的地址
    return 1;   
}
int PoP(Stack *s,DataforStack *x) // 出栈-----返回值为1表示成功为0表示失败
{
    if(s==NULL||s->top==NULL)   // 空栈返回0
        return 0;
    StackNode *p=s->top;
    *x=p->data; // 获取栈顶数据
    s->top=p->link; // 移动栈顶指针位置，指向新的最左节点地址
    free(p);    // 释放出栈的位置的空间
    return 1;
}
void InitQueue(Queue *q) //初始化队列
{
    q->rear=q->front=NULL;  // 初始化时首尾指针置空
}
int EnQueue(Queue *Q,DataforQueue x)//进队列------成功返回1反之返回0
{
    QueueNode *p=(QueueNode*)malloc(sizeof(QueueNode)); // 申请空间
    if(!p) return 0;
    p->data=x;  
    p->link=NULL;   // 指向空
    if(Q->front==NULL)   // 说明队列为空，创建第一个节点
        Q->front=Q->rear=p; // 第一个节点是作为头，头尾均指向第一个节点地址，方便出队和入队
    else
        Q->rear->link=p;    // 尾的指针域指向申请来的空间的数据地址
    Q->rear=p;  // 尾指针移动到新的位置等待下一次数据的输入
    return 1;
}
int DeQueue(Queue *Q,DataforQueue *x)   // 出队列-----成功返回1
{
    if(Q->front==NULL) return 0;    // 队空
    QueueNode *p=Q->front;
    *x=p->data; // 从头指针开始出队
    Q->front=Q->front->link;    // 头指向下一个节点地址
    free(p);    // 释放出队节点的空间
    return 1;
}
int main() {
    char language[MAX_SIZE];    // 数组形式读入魔王语言
    char data,frontdata;
    Stack S;
    Queue Q;
    // 初始化队，栈
    InitQueue(&Q);  
    InitStack(&S);
    
    
    scanf("%s",language);
    int i=strlen(language); 
    for(i;i>=0;i--) // 数组自右向左逐一进栈
        Push(&S,language[i]);
    while(PoP(&S,&data))    //出栈操作，括号内部内容入队
    {
        if(data=='A')
            printf("sae");
        else if(data=='B')
            printf("tsaedsae");
        else if(data=='(')
        { 
            while(data!=')')
            {
                // 括号内内容出栈入队
                PoP(&S,&data);  
                EnQueue(&Q, data);
            }
            DeQueue(&Q,&data); // 出队首元素
            frontdata=data; // 存储首元素
            while(DeQueue(&Q, &data))
            {
                //按照要求规则进行出队入栈
                Push(&S,frontdata);
                Push(&S,data);
            }
            // 此处最后一次压栈是将括号内首元素和左括号一起压栈，但是输
            // 出的时候不输出左括号，实现了要求的格式。
        }
        else if(data==')')
        {}// 不输出括号
        else
            printf("%c",data);
    }
    return 0;
}
