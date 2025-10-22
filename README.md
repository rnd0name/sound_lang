# sound_lang
A very simple interpreter to do beeps on windows

## syntax
There are four expressions in sound_lang : beep, sleep, jmp and for

### beep
`beep` takes two arguments : pitch and duration in milliseconds

### sleep
`sleep` takes one argument : the duration in seconds

### jmp
`jmp` takes one argument : the destination line 

### for
`for` takes eight arguments :
the number of iterations  
two <arg0> integers  
two <arg1> integers  
two <arg2> floats  
the number of lines in the loop  
<arg> variables work as folows :  
`<arg0> = argument 2 * current iteration + argument 3`  
`<arg1> = argument 4 * current iteration + argument 5`  
`<arg2> = argument 6 * current iteration + argument 7` 
you can use them while in the loop as arguments

### comments
comments must start by `#`
