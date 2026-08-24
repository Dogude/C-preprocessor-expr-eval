# Program uses shunting yard algorithm to interpret C #if expressions
* It holds a Precedence Dictionary
# Examples
* ``` c_eval ``` function has a lexer, parser and eval loop 
* ``` defined ```  operator can not take a only number, it must take a identifier
* Below Expression will output syntax error
```
expr = "!defined(123)"
print(c_eval(expr))
```
<img width="176" height="41" alt="image" src="https://github.com/user-attachments/assets/8d20f22b-ab58-4d1a-852e-53642e6ac64e" />

* If still an identifier in this expression, it means it has not defined and treated as 0 in eval loop
* so in that example B will be treated as 0
```
expr = "!defined(B) && 123 > 1257"
print(c_eval(expr))
```
<img width="455" height="97" alt="image" src="https://github.com/user-attachments/assets/6c866087-1c7a-477a-a2c8-b69ed8186665" />

```
* Also FOO and F Treated as 0
expr = "!defined(FOO) && 123678 > 1257 || F + 12"
print(c_eval(expr))
```
<img width="452" height="114" alt="image" src="https://github.com/user-attachments/assets/e721b20b-4c58-4fe8-b8e6-9e1466dc1c39" />


