def main():
    x=int(input())
    ans = []
    for a in range(1,10):
        for b in range(1,10):
            c = a*b
            if c != x:
                ans.append(c)
    s = sum(ans)
    print(s)

if __name__ == "__main__":
    main()