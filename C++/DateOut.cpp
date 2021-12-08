// 成员函数定义在类体外
#include <iostream>

using namespace std;

class Date
{
public:
    int year;
    int month;
    int day;
    // 先做成员函数的声明
    void getDate();
    // 构造函数
    Date();
};
Date::Date()
{
    year = 2021;
    month = 1;
    day = 1;
}
void Date::getDate()
{
    cout << year << "年" << month << "月" << day << "日" << endl;
}
int main()
{
    Date date;
    cin >> date.year >> date.month >> date.day;
    date.getDate();
    return 0;
}