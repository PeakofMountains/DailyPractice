#include <iostream>
using namespace std;
// 通过引用直接修改变量的值
void sort(int &a, int &b, int &c)
{
    int temp = a;
    if (b < a)
    {
        a = b;
        b = temp;
        temp = a;
    }
    if (c < a)
    {
        a = c;
        c = temp;
    }
    temp = b;
    if (c < b)
    {
        b = c;
        c = temp;
    }
}
int main()
{
    int a = 0, b = 0, c = 0;
    cin >> a >> b >> c;
    sort(a, b, c);
    cout << a << " " << b << " " << c;
    return 0;
}