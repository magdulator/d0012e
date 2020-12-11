def test():
    i = 1
    while i <= 5001:
        random = generateList(30, i)
        starttime = time.time()
        (DivideAndConquerQ(random))
        timetaken = time.time()
        f = open("myfile.txt", "a")
        f.write(str(i)+" " +str(timetaken-starttime) + "\n")
        f.close()
        i += 200
        