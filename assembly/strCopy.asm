; 字符串拷贝
.model small
.stack 4096
.data
	string1 db 'I am string1',0dh,0ah,'$'
string2 db 'String2 is me',0dh,0ah,'$'
.code
	main:
	     mov ax, @data
	     mov ds, ax
	     mov es, ax
	     cld
	     mov si, OFFSET string1
	     mov di, OFFSET string2
	     mov cx, 12 ; 定义下面一条语句重复次数
	     rep movsb  ; 每次一个字母

    end main