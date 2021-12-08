; count the times of A appeared in main store from 40000h to 40000h+16k. 
.model small
.stack 4096
.code
	; init part
init PROC
	; 不明白为什么只传位 high 16 bit of sagment start address
          mov  dx, 4000h
	      mov  ds, dx
	      mov  cx, 16*1024	; init cx with the time of loops
	      mov  si, 0      	; init si with 0
	      mov  dx, 0      	;
init ENDP
	; count part
count PROC
	      mov  al, [si]
	      cmp  al, 'A'    	; check
	      jnz  next
	      inc  dx         	; dx save the number of A
count ENDP
	; next check
next PROC
	      inc  si         	; update si
	      loop count
next ENDP
	; show the result
show PROC
	; 不明白如何显示寄存器中的值
	      int  21h
	      mov  ah, 4ch
	      int  21h
show ENDP
end init