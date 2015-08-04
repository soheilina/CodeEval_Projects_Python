__author__ = 'Soheil'

with open("DeltaTime.txt", "r") as my_text:
    for line in my_text:
        T1, T2 = line.strip('\n').split(" ")
        h1, m1, s1 = map(int, T1.split(":"))
        h2, m2, s2 = map(int,T2.split(":"))
        if T1 >= T2:
            delta = (h1*3600 + m1*60+s1) - (h2*3600 + m2*60+s2)
        else:
            delta = (h2*3600 + m2*60+s2) - (h1*3600 + m1*60+s1)
        deltaH = delta / 3600
        deltaM = (delta % 3600) / 60
        deltaS = (delta % 3600) % 60
        print "%02d:%02d:%02d" % (deltaH, deltaM, deltaS)