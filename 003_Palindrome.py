# Write a code to check if a given string is a palindrome or not

name="nitin"
n=len(name)

for i in range((n//2)+1):
    if name[i]!=name[n-1-i]:
        print(f"{name} Is Not Palindrome")
        break
    elif i==n//2:
        print(f"{name} Is Palindrome")