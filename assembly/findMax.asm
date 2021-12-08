; find max
.model small
.stack 4096
.data
	MYDATA db 11h, 12h, 13h, 14h, 16h
KVFF db ?
.code
	; init part
	init: 
	      mov  bx, SEG MYDATA
	      mov  ds, bx
	      mov  si, 0
	      mov  al, [si]
	      INC  si
	      mov  cx, 4
	      mov  KVFF,al

	; check part
	check:
	      mov  al, [si]
	      cmp  KVFF, al
	      ja   next
	      mov  KVFF, al

	; next part
	next: 
	      inc  si
	      loop check
    
end init
