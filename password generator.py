
import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="1234567890"
symbols = "@#%&*?"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 20

password = "".join(random.sample(Use_for,length_for_pass))

print("Generated password is :",password)