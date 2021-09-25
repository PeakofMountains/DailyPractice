; 汇编简写
.model small
.stack 4096
.data
	theSum dw (?)	; 定义变量
.code
main PROC
	      mov  dx, @data
	      mov  ds, dx
	      mov  ax,1000h 	; argument
	      mov  bx,2000h 	; argument
	      mov  cx,3000h 	; argument
	      call SumOf    	; 子程序的调用，实现累加的功能
	      mov  theSum,ax	;	将最终的计算结果存储在变量中
	      mov  ah,4ch
	      int  21h
main ENDP
	; 子程序部分
SumOf PROC
	      add  ax,bx
	      add  ax,cx
	      ret
SumOf ENDP
end main
