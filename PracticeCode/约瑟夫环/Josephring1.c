/* 
 * Author: zyw02
 * Date: 2020-10-28
 * Describe: 用循环链表解决约瑟夫环
*/
#include<stdio.h>
#include<stdlib.h>
typedef struct person{
    int num;
    int key;
    struct person* next;
}ppl;
int main(){
    int n = 0, m = 0, seq = 0;
    scanf("%d %d",&n, &m);
    ppl *h;
    ppl* p = (ppl*)malloc(sizeof(ppl));
    h = p;
    for(int i = 1; i < n; i++){
        ppl *q = (ppl*)malloc(sizeof(ppl));
        p -> next = q;
        scanf("%d", &p -> key);
        p -> num = ++seq;
        p = q;
    }
    scanf("%d", &p -> key);
    p -> num = ++seq;
    p -> next = h;
    int cnt = 1;
    ppl *q = p;
    while(n){
        while(cnt != m){
            cnt++;
            q = q -> next;
        }
        if(q == p)  h = q -> next ->next;
        ppl* k = q -> next;
        m = k -> key;
        printf("%d ",k -> num);
        q -> next = q -> next -> next;
        free(k);
        n--;
        cnt = 1;
    }
}
