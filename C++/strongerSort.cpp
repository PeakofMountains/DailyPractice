#include <iostream>
using namespace std;
// 通过引用直接修改原变量的值
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
// 整数类型和浮点数类型分别定义，重构，采用同一函数名， 不同参数类型，
void sort(float &a, float &b, float &c)
{
    float temp = a;
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
    int int1 = 0, int2 = 0, int3 = 0;
    float float1 = 0.0, float2 = 0.0, float3 = 0.0;
    cin >> int1 >> int2 >> int3;
    sort(int1, int2, int3);
    cout << int1 << " " << int2 << " " << int3 << endl;
    cin >> float1 >> float2 >> float3;
    sort(float1, float2, float3);
    cout << float1 << " " << float2 << " " << float3;
    return 0;
}