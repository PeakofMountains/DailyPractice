; 汇编完整写法
mystack segment stack
	        db 100h dup(0)
mystack ends
data segment
	theSum dw (?)	; 定义变量
data ends
code segment
	      assume cs:code,ds:data, ss:mystack,
main PROC
	      mov    dx, data
	      mov    ds, dx
	      mov    ax,1000h                    	; argument
	      mov    bx,2000h                    	; argument
	      mov    cx,3000h                    	; argument
	      call   SumOf                       	; 子程序的调用，实现累加的功能
	      mov    theSum,ax                   	; 将最终的计算结果存储在变量中
	      mov    ah,4ch
	      int    21h
main ENDP
	; 子程序部分
SumOf PROC
	      add    ax,bx
	      add    ax,cx
	      ret
SumOf ENDP
code ends
    end main

