import sys

sys.stdin = open("2_input.txt", "r")

for i in range(int(input())):
    num = float(input())
    count = 1
    text = ""
    while True:
        text += f"{int(num // (1/(2**count)))}"
        num %= (1/(2**count))
        if num != 0:
            count += 1
            if count >= 13:
                text = "overflow"
                break
            continue
        break
    print(f"#{i+1} {text}")
