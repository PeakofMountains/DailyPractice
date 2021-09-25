; calculate the sum of arrray data

.model small
.stack 4096
.data
	array  dw 0100h, 0200h, 0300h, 0100h, 0200h, 0300h
	array_len = ($-array)/2
    theSum dw ?

.code
	; main：give initial array data and the size of array
main PROC
            ;  mov ax, @data
            ;  mov ds,ax
	         mov  si, OFFSET array  	; give first address of array to si
	         mov  cx, array_len	    ; give the length of array to cx
	         call ArraySum         	; call sun part to calculate sum value and save it in ax
	         mov  theSum, ax        	; give ax value to theSum variety
	         mov  ax, 4ch
	         int  21h
main ENDP
	; calculate the sum, return the sum to ax
ArraySum PROC
	         push si               	; push si and cx, to avoid data in si being changed
	         push cx
	         mov  ax, 0            	; ax initial
	L1:      
	         add  ax, [si]         	; add si array data to ax
	         add  si, 2            	; the size of a element in array
	         loop L1               	; LOOP ADDING

	         pop  cx               	; pop cx and si in order. The order between push and pop should be reverse
	         pop  si
	         ret                   	; the end of ArraySum
ArraySum ENDP
    end main