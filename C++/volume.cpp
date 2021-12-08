#include <iostream>
using namespace std;

class Volume
{
public:
    void setValue(float l, float w, float h);
    void getVolume();
    Volume();

private:
    float length;
    float width;
    float height;
};
// 构造函数进行成员变量初始化
Volume::Volume()
{
    length = 0;
    width = 0;
    height = 0;
}
// 设置成员变量
void Volume::setValue(float l, float w, float h)
{
    length = l;
    width = w;
    height = h;
}
// 计算和输出体积
void Volume::getVolume()
{
    cout << length * width * height << endl;
}
int main()
{
    Volume object1, object2, object3;
    float length = 0, width = 0, height = 0;
    cin >> length >> width >> height;
    object1.setValue(length, width, height);
    cin >> length >> width >> height;
    object2.setValue(length, width, height);
    cin >> length >> width >> height;
    object3.setValue(length, width, height);
    cout << "这几个长方柱的体积分别是:" << endl;
    object1.getVolume();
    object2.getVolume();
    object3.getVolume();
    return 0;
}