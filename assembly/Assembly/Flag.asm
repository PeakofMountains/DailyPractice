
.386
.MODEL flat, stdcall
.STACK 4096
ExitProcess PROTO,dwExitCode:DWORD
.data
arrayB word 0000h,8000h,0FFFFh,0001h,0FFFEh
.code
main PROC
	mov ax,@data
	mov ds,ax
	mov ax,[arrayB]
	sub ax,1
	mov ax,[arrayB+2]
	neg ax
	mov ax,[arrayB+4]
	add ax,1
	INVOKE ExitProcess,0
main ENDP
END main
