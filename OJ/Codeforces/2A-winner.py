from collections import defaultdict

def main():
    n = int(input())
    play = defaultdict(int)

    boss = ""; maxs = 0
    exboss = ""; exmax = 0

    for _ in range(n):
        x = input()
        n, s = x.split()
        s = int(s)
        if n != boss: # new player or existing non-boss player
            if s > maxs: 
                exboss = boss; exmax = maxs;
                boss = n; maxs = s
            # else everyting keeps the same
        else:
            # Get 2nd largest value: exmax
            if maxs + s <= exmax:
                swap(boss, exboss) 
                exmax = maxs + s
        play[n] = play[n] + int(s)
        update() #!!!!
        print(boss, maxs, exboss, exmax)
    print(play)

main()
