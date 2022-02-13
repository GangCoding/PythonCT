button = int(input())

button_types = [300, 60, 10]  # 5분은 300초, 1분은 60초
counts = []
for mon in button_types :
    counts.append(button // mon)
    button%= mon

if button == 0:
    print(f"{counts[0]} {counts[1]} {counts[2]}")
else:
    print(-1)