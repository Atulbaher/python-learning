# user_input = input("Enter the input string\n")


# Palindrome
# Reverse the string and match with the old string if should bw same.

# 1. by using a Treditional method
# 2. Builtin functions.

def reverse_string(input_string):
    reverse_str = ""
    for c in input_string:
        reverse_str = c + reverse_str
    return reverse_str


original_str = "NAMAN"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not")
