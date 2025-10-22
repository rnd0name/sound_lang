# sound_lang

A very simple interpreter designed to produce beeps on Windows.

## Syntax

There are four expressions in **sound_lang**: `beep`, `sleep`, `jmp`, and `for`.

---

### `beep`

The `beep` command takes **two arguments**:  
- **pitch**  
- **duration** in milliseconds  

---

### `sleep`

The `sleep` command takes **one argument**:  
- **duration** in seconds  

---

### `jmp`

The `jmp` command takes **one argument**:  
- **destination line**  

---

### `for`

The `for` command takes **eight arguments**:  
1. The number of iterations  
2. Two `<arg0>` integers  
3. Two `<arg1>` integers  
4. Two `<arg2>` floats  
5. The number of lines in the loop  

`<arg>` variables work as follows:  

`<arg0> = argument 2 * current iteration + argument 3`  
`<arg1> = argument 4 * current iteration + argument 5`  
`<arg2> = argument 6 * current iteration + argument 7` 

You can use them within the loop as arguments.

---

### Comments

Comments must start with `#`.

---

## Writing `.beep` Files

Files do not need to use the `.beep` extension — a regular text file (`.txt`) or any extension you prefer  
(for example: `.hi_this_is_a_really_long_and_impractical_file_extension`)  
will also work, as long as it contains plain text.

---

### Creating a `.beep` File

You can launch **Notepad** or another simple text editor, write your code, and — after or while saving — change the `.txt` extension to `.beep`.  

If it is your first time using a `.beep` file, you may be asked how to open it.  
In that case, choose **sound_reader.bat** (you may need to locate it manually).

---
