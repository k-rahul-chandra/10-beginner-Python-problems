st=input("Enter a string: ")
st=st.lower()
print("Palindrome") if st == st[::-1] else print("not a palindrome")