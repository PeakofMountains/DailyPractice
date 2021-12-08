#include <iostream>
using namespace std;
int add(int a, int b)
{
    return a + b;
}
double add(double a, double b)
{
    return a + b;
}
int main()
{
    int a = 1, b = 1;
    double c = 1.5, d = 1.5;
    cout << "a + b = " << add(a, b) << ",c + d = " << add(c, d);

    return 0;
}
