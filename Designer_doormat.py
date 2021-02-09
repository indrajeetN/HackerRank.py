# Enter your code here. Read input from STDIN. Print output to STDOUT
N, W = map(int, input().split())
#Top part
for i in range(0, (N-1)//2):
    print((".|."*i).rjust((W-3)//2,'-')+".|."+(".|."*i).ljust((W-3)//2,'-'))
#Middle Part
print("WELCOME".center(W,'-'))
#Bottom part
for i in range(((N-1)//2)-1, -1, -1):
    print((".|."*i).rjust((W-3)//2,'-')+".|."+(".|."*i).ljust((W-3)//2,'-'))
