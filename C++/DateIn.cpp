// 成员函数定义在类体内
#include <iostream>

using namespace std;

class Date
{
public:
    int year;
    int month;
    int day;
    void getDate()
    {
        cout << year << "年" << month << "月" << day << "日" << endl;
    }
    // 构造函数
    Date();
};
Date::Date()
{
    year = 2021;
    month = 1;
    day = 1;
}
int main()
{
    Date date;
    cin >> date.year >> date.month >> date.day;
    date.getDate();
    return 0;
}