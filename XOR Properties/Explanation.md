# Approach
First, solve for KEY2 using the equation KEY2 ^ KEY1 ( We have KEY1 already).
Then use KEY2 to solve for KEY3 using the equation KEY2 ^ KEY3.
Finally, use KEY1, KEY2, and KEY3 to solve for the flag.

# KEY2 Calculation:
KEY2 = KEY2 ⊕ KEY1 ⊕ KEY1 = KEY2 (because XOR with itself gives 0 and 0 XOR with any number gives that number)

# KEY3 Calculation:
KEY3 = KEY2 ⊕ KEY3 ⊕ KEY2 = KEY3

# FLAG Calculation:
FLAG = (FLAG ⊕ KEY1 ⊕ KEY2 ⊕ KEY3) ⊕ KEY1 ⊕ KEY2 ⊕ KEY3 = FLAG
This will yield the original flag as the output.