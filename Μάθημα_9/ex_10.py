#Καρχαρίας για το μέλλον. Κωδικοποιήσεις και τζιτζιμπλίκια.

for i in range(130000):
    if i % 50 == 0:
        print(f"\n{i}-{i + 49}: ", end="")
    print(chr(i), end="")
