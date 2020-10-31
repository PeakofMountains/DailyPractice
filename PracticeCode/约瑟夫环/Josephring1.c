/*
 * Author: zyw02、PeakofMountains
 * Date: 2020-10-28
 * Describe: 用循环链表解决约瑟夫环问题
*/
#include<stdio.h>
#include<stdlib.h>
typedef struct Seats{
    int order;
    int key;
    struct Seats* next;
}seat;
int main(){
    int n = 0, m = 0, pos = 1;
    scanf("%d %d",&n, &m);
    seat *h;    // 用来存储首节点的地址的指针
    seat* p = (seat*)malloc(sizeof(seat));  // 申请指针p的空间,也是作为链表首节点
    h = p;  
    for(int i = 1; i < n; i++){
        seat *q = (seat*)malloc(sizeof(seat));  // 在每次接受数据前申请空间
        p -> next = q;  // p指针在链表上移动，确定下一个位置 
        scanf("%d", &p -> key);
        p -> order = pos++;
        p = q;
    }
    scanf("%d", &p->key);
    p->order= pos++;
    p->next = h;    // 指回首节点，构成循环链表
    seat *q = p;    //从倒数第一个开始，因为最终更新链表的时候要把删除的那个节点前面的指针域指向后面的节点
    while(n){
        
        while(1 < m){   // 出循环的时候，q到了要删除的节点的前驱节点
            q=q->next;
            m--;
        }
        seat* k = q->next;  // k保存的是要删除的节点的信息
        m = k->key;
        printf("%d ",k->order);
        q->next = q->next->next;    // 前置节点连接到后继节点
        free(k);    // 释放删去节点的空间
        n--;
    }
}
