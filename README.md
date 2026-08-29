# Program uses shunting yard algorithm to interpret C Preprocessor #if boolean expressions
* It holds a Precedence Dictionary
# Examples
* ``` c_eval ``` function has a lexer, parser and eval loop 
* ``` defined ```  operator cannot take only a number, it must take an identifier
* Below Expression will output a syntax error
```
expr = "!defined(456)"
c_eval(expr)
```
<img width="291" height="83" alt="image" src="https://github.com/user-attachments/assets/b83c3296-3d14-4aa5-95fb-6308f0a42b5d" />

```
expr = "!defined(AAA) && F > H +"
c_eval(expr)
```
<img width="341" height="69" alt="image" src="https://github.com/user-attachments/assets/340f2e8c-e0a1-4122-badd-b4b6d988bdf8" />


* If there is an identifier in this expression, it means it has not defined and treated as 0 in eval loop
* For Example below, B will be treated as 0
```
expr = "!defined(B) && 123 > 1257"
c_eval(expr)
Outputs : False
```
* Also FOO and F Treated as 0
```
expr = "!defined(FOO) && 123678 > 1257 || F + 12"
print(c_eval(expr))
Outputs : True
```


