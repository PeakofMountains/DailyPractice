.model small,stdcall
.stack 4096

speaker = 61h
timer = 42h
delay1 = 500
delay2 = 500
startPitch = 7600

.code
main PROC
    in al,speaker
    push ax
    or al,00000011b
    out speaker,al

    mov bx,startPitch
L2: mov al,bl
out timer,al
mov al,bh
out timer,al

mov cx,delay1
L3a: push cx
mov cx,delay2
L3b: loop L3b
pop cx
loop L3a

sub bx,200
jnz L2

pop ax
and al,11111100b
out speaker, al

mov ax,4c00h
int 21h
main ENDP
end main