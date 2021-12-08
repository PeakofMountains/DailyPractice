#include <iostream>
#define PI 3.14
using namespace std;

class Circle
{
public:
    float Radius;
    void GetArea();
};
void Circle::GetArea()
{
    cout << PI * Radius * Radius << endl;
}
int main()
{
    Circle circle;
    cin >> circle.Radius;
    circle.GetArea();
    return 0;
}