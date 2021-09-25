.model small
; .stack 4096
.data
array  dw 0000H,8000H,0FFFH,0001H,0FFEH
.code
main PROC
	     mov ax,@data
	     mov ds,ax
	     mov ax,[array]
	     sub ax,1
	     mov ax,[array+1]
	     neg ax
	     mov ax,[array+4]
	     add ax,1
main ENDP
end main