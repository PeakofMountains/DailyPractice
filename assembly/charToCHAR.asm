.model small
.stack 4096
.data
	     smallChar db (01100001b)
         
.code
main PROC
	     mov  ax, @data
	     mov  ds, ax
	     and  smallChar, 11011111b	; 用byte ptr 来说明inc操作的是byte
         mov al, smallChar
         mov ah, 01h
         int 21
         mov  ax, 4ch
	     int  21
main ENDP
end main