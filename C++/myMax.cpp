#include <iostream>
using namespace std;
// 默认参数的函数，实现两个参数或是三个参数的调用
void myMax(int a, int b, int c = 0)
{
    int temp = 0;
    if (a > temp)
    {
        temp = a;
    }
    if (b > temp)
    {
        temp = b;
    }
    if (c > temp)
    {
        temp = c;
    }
    cout << temp << endl;
}
int main()
{
    myMax(1, 2);
    myMax(1, 3, 2);
    return 0;
}