import time

text = "The quick brown fox jumps over the lazy dog"
print(f"Type this:\n\n{text}\n")
input("Press Enter when ready...")

start = time.time()
typed = input("\nStart typing:\n")
end = time.time()

if typed.strip() == text:
    print(f"✅ Correct! Time taken: {round(end - start, 2)}s")
else:
    print("❌ Mismatch. Try again.")
