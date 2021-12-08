#include <stdio.h>
int if_add_o(int a, int b);
int main()
{
    int a, b;
    a = 1;
    b = 2;
    printf("%11d + (%2d) = %d, \t\t %s \n", a, b, a + b, if_add_o(a, b) ? "Overflow" : "OK");

    return 0;
}
int if_add_o(int a, int b)
{
    __asm {
        mov EAX, a;
        add EAX, b;
        jo overflowed;
        xor EAX, EAX;
        jmp no_overflowed;

    overflowed:
        mov EAX, 1;
    no_overflowed:
    }
    ;
}