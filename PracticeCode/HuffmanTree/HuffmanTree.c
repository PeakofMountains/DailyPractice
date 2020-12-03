/*
 * Name: HuffmanTree.c
 * Author: PeakOfMountains
 * Date: 2020-12-3
 * 
*/
#include <stdio.h>
#include <string.h> // 用到strlen()
#include <stdlib.h> // 用到malloc
#define MaxCharNum 30   // 定义编码电文需要前缀码的种类
#define MaxHuffmanNodeNum 2*MaxCharNum-1    // 定义Huffman树中节点个数的最大值，初始化的时候用
#define MaxInt 10240    // 一个较大的数
typedef char *huffmanCode[MaxCharNum+1];    // 相当于定义一个长度为MaxCharNum+1长的一个指针数组，
                                            //用法例：`huffmanCode hc;`就是创建长度为MaxCharNum+1的指针数组

// 定义HuffmanTree的节点结构体
typedef struct 
{
    int weight; // 权值，放在叶子节点上
    int parent; // 双亲节点，保存父节点的下标
    int lchild; // 左孩子，保存左孩子的下标
    int rchild; // 右孩子
}HuffmanNode,HuffmanTree[MaxHuffmanNodeNum+1];  // 不对HuffmanTree的首位置进行了利用，用法和上面的huffmanCode

// HuffmanTree创建之前的初始化
int InitHuffmanTree(HuffmanTree HT,int weights[],int weightNum)
{
    int i =1,m=weightNum*2-1;
    for(i=1;i<=weightNum;i++)   // 给叶子赋权值
    {
        HT[i].weight = weights[i];
        HT[i].parent = 0;
        HT[i].lchild = 0;
        HT[i].rchild = 0;
    }
    for(i=weightNum+1;i<=m;i++) // 其余节点初始化
    {
        HT[i].weight = 0;
        HT[i].parent = 0;
        HT[i].lchild = 0;
        HT[i].rchild = 0;
    }

    return 0;
}

// 选择出权值最小和此小的两个树的叶子所在下标
int Select(HuffmanTree HT,int position,int *s1,int *s2)
{
    int j,m1=MaxInt,m2=MaxInt;
    for(j=1;j<=position;j++)
    {
        if(HT[j].weight<m1&&HT[j].parent==0)
        {
            m2 = m1;
            *s2 = *s1;
            *s1 = j;
            m1 = HT[j].weight;
        }
        else if(HT[j].weight<m2&&HT[j].parent==0)
        {
            *s2 = j;
            m2 = HT[j].weight;
        }
    }
    return 0;
}

// 利用Select中选出最小和次小权值下标将森林进行逐步合并形成HuffmanTree
int CreatHuffmanTree(HuffmanTree HT,int weights[],int weightNum)
{
    int i=0,s1,s2,m=2*weightNum-1;
    for(i=weightNum+1;i<=m;i++) // 对除树叶的其他节点进行判断和合并
    {
        Select(HT,(i-1),&s1,&s2); // 选出来要合并的两个的下标之后进行接下来的合并
        HT[i].weight=HT[s1].weight+HT[s2].weight;   // 合并后的权值是之前之和
        HT[s1].parent=i;    
        HT[s2].parent=i;    // 改变合并项的指向
        HT[i].lchild=s1;   
        HT[i].rchild=s2;
    }
    return 0;
}



// 对树进行0-1编码，并将编码结果保存
int CreatHuffmanCode(HuffmanTree HT,huffmanCode hc,int weightNum)
{
    int c=0,i=0,start=0,p=0,WPL=0;
    char *Code; // 暂时存储的动态数组
    Code = (char *)malloc(weightNum*sizeof(char));
    Code[weightNum-1] = '\0';   // 数组的最后位置设为`\0`，为后边的strcpy()使用
    
    for(i=1;i<=weightNum;i++)
    {
        start = weightNum-1;
        c = i;
        p=HT[i].parent;
        while(p!=0) // 若双亲节点不为空，则继续
        {
            start--;
            if(HT[i].lchild==c) // 左边编码0，右边编码1
            {
                Code[start]='0';
            }
            else{
                Code[start]='1';
            }
            c = p;
            p=HT[p].parent;
        }
        hc[i]=(char *)malloc((weightNum-start)*sizeof(char));
        strcpy(hc[i],&Code[start]); // 将编码保存
    }
    // 计算WPL
    for(i=1;i<=weightNum;i++)
    {
        WPL+= HT[i].weight*strlen(hc[i]);
    }
    free(Code); // 释放空间
    return WPL;
}

int main()
{
       
    int i=0,charNum=0,WPL=0;
    scanf("%d",&charNum);
    int weights[MaxCharNum];
    huffmanCode hc; // 创建保存编码信息的指针数组
    for(i=1;i<=charNum;i++)
    {
        scanf("%d",&weights[i]);
    }
    // char *huffmanCode[charNum+1];   
    HuffmanTree hT; // Huffman树的创建
    InitHuffmanTree(hT,weights,charNum);
    CreatHuffmanTree(hT,weights,charNum);
    printf("%d",CreatHuffmanCode(hT,hc,charNum));   // 给HuffmanTree编码，计算WPL并输出
    return 0;
}
