#include <iostream>
using namespace std;

// 通过使用函数模板简化程序
template <typename T1>

void sort(T1 &a, T1 &b, T1 &c)
{
    T1 temp = a;
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