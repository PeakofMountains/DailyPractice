.386
.MODEL flat, stdcall
.STACK 4096
ExitProcess PROTO,dwExitCode:DWORD
.data
Rval SDWORD ?
Xval SDWORD 26
Yval SDWORD 30
Zval SDWORD 40
.code
main PROC
	mov ax,1000h    ; INC and DEC
	inc ax          ; 1001h
	dec ax          ; 1000h
	; Expression: Rval = -Xval + (Yval - Zval)
	mov  eax,Xval
	neg  eax        ; -26
	mov  ebx,Yval
	sub  ebx,Zval   ; -10
	add  eax,ebx
	mov  Rval,eax   ; -36
; Zero flag example:
	mov cx,1
	sub cx,1		; ZF = 1
	mov ax,0FFFFh
	inc ax		; ZF = 1
	; Sign flag example:
	mov cx,0
	sub cx,1		; SF = 1
	mov ax,7FFFh
	add ax,2		; SF = 1
	; Carry flag example:
	mov al,0FFh
	add al,1		; CF = 1, AL = 00
	; Overflow flag example:
	mov  al,+127
	add  al,1		; OF = 1
	mov  al,-128
	sub  al,1		; OF = 1
	INVOKE ExitProcess,0
main ENDP
END main
