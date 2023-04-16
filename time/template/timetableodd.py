import random
import mysql.connector as c
#from collections import defaultdict
def generateTimeTable():
    try:
        templist = []
        fact = []
        sem1 = ["ENG1", "AP", "C", "BEE1", "M1", ["ENG1", "AP", "C"]]
        sem2 = ["BEE2", "EC", "DS", "PYTHON", "M2", ["EC", "PYTHON", "DS"]]
        sem3 = ["JAVA", "DM", "PS", "SE", "DLD", ["JAVA", "DV", "CMHW", "ARTS"]]
        sem4 = ["ENG2", "WT", "OR", "DBMS", "COA", ["WT", "DBMS", "OOAD", 'JP']]
        sem5 = ["OS", "DAA", "DMDW", "SS", "TOC", ["GD", 'IOT', 'LP', 'CD']]
        sem6 = ["CN" , "FSD" , "MP" , "DAS" , "CS"]
        totalSem = [["ENG", "AP", "C", "BEE1", "M1"], ["BEE2", "EC", "DS", "PYTHON", "M2"], ["JAVA", "DM", "PS", "SE", "DLD"], ["ENG2", "WT", "OR", "DBMS", "COA"], ["OS", "DAA", "DMDW", "SS", "TOC"], ["CN" , "FSD" , "MP" , "DAS" , "CS"]]
        faculty = [["sudha mam", 8, ["WT", "JAVA", "CN", "PYTHON"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["ramarao sir", 7, ["WT", "DLD", "DM", 'LP'], 4, [0] * 6, [0] * 6, [0] * 6],
        ["kesava sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["darmaiah sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["ravikiran sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["vasubabu sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["kameswari mam", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["murthy sir", 9, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6], 
        ["G.ramesh babu sir", 1, ["COA", "DAA", "DLD", "GD"], 4, [0] * 6, [0] * 6, [0] * 6], 
        ["srikanth sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["prasad sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["purushothamaraju sir", 15, ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
        ["ramachandraroa sir", 12,  ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
        ["srihariraju sir", 12,  ["ENG1", "SS", "SS2", "ENG2"], 4, [0] * 6, [0] * 6, [0] * 6], 
        ["devi mam", 7,  ["ENG1", "SS", "SS2", "ENG2"],4,[0] * 6, [0] * 6,[0] * 6],
        ["M.ramesh babu sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["P.Raju sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Dharmaih sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Kalpana mam",7,["SE","OS", "CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Durga mam",0,["SE","OS","CD","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Archana mam",7,["SE","OS","CD","CS", "CD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Soni mam",7,["SE","OS","CD","CS", "CD", "GD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["V.V.R.Maheshwara Rao sir",10,["SE","OS","CD","DM"], 4 ,[0] * 6, [0] * 6,[0] * 6],
        ["Shalem Raju sir",9,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Tharaka satyanaran sir",2,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Sunil sir",8 ,["DS","PYTHON","DAA","TOC"], 4 ,[0] * 6, [0] * 6, [0] * 6, []],
        ["Gayathri mam",7,["COA","PYTHON","C","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Silpa mam",9,["C","SE","OS","CS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Swathi mam",8,["C","PYTHON","DS","FSD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Seenu sir", 9, ["C", "PYTHON", "JAVA", "MC"], 4, [0] * 6, [0] * 6, [0] * 6],
        ["Phaneendhra varma sir",2,["FSD","CS","JAVA","DAS", 'GD'], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Srinivas sir",9,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Bhramhanandam sir",8,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Jagadeesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Ganesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Arun sir",7,["ENG1","ENG2","SS","SS2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Swaroop sir",6,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Narayana kiran sir",5,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Kalyan sagar sir",4,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
        ["Ramu sir",9,["DMDW","DBMS","DAS","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6 , []],
        ["Ratna kumari mam",9,["DMDW","DBMS","DAS","CS", "JP", "ARTS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []]]
        faculty = sorted(faculty, key = lambda x : x[1], reverse = True)
        week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
        count = 0
        def mainFunction(subjects, labs, sem):
            
            factDict = {}
    #labs = [0, 1, 2]
            sec1 = []
            weeks = [0,1,2,3,4,5]
            w = 0
            while weeks:
                w += 1
                sec2 = []
                ranWeek = random.choice(weeks)
                subjectIndex = [0,1,2,3,4]
                days = [1, 2, 3, 4, 5, 6, 7, 8]
                labDays = [2, 6]
                if labs:
                    ranLab = random.choice(labs)
                    lab = subjects[5][ranLab]
                    labs.remove(ranLab)
                    for i in faculty:
                        if lab in i[2]:
                            if i[4].count(0) != 0 and i[3] > 3:
                                
                                if lab in factDict.values():
            
                                    try:
                                        if factDict[i[0]] == lab:
                                            randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                            i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            
                                            i[3] -= 1
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            break
                                    except:
                                        continue
                                else:
                                    factDict[i[0]] = lab
                                    randomDay = random.choice(labDays)
                                    labDays.remove(randomDay)
                                    days.remove(randomDay)
                                    days.remove(randomDay + 1)
                                    days.remove(randomDay + 2)
                                    
                                    i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                    
                                    i[3] -= 1
                                    sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                    break
                           

                            elif i[5].count(0) != 0 and i[3] >= 3:
                                if lab in factDict.values():
                                    try:
                                        if factDict[i[0]] == lab:
                                            f = 0
                                            try:
                                                if i[4][ranWeek][0] in labDays:
                                                    x.append(i[4][ranWeek][0])
                                                    labDays.remove(i[4][ranWeek][0])
                                                    f = 1
                                                if i[4][ranWeek][4] in labDays:
                                                    x.append(i[4][ranWeek][4])
                                                    labDays.remove(i[4][ranWeek][4])
                            
                                            except:
                                                if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                    x = 2
                                                    labDays.remove(2)
                                                    f = 1 
                                                elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                    x = 6
                                                    labDays.remove(6)
                                                    f = 1
                                            randomDay = random.choice(labDays)
                                        labDays.remove(randomDay)
                                        days.remove(randomDay)
                                        days.remove(randomDay + 1)
                                        days.remove(randomDay + 2)
                                       
                                        i[3] -= 1
                                        i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                        sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                        if f == 1:
                                            try:
                                                labDays.extend(x)
                                            except:
                                                labDays.append(x)
                                        break
                                    except:
                                        continue
                                else:
                                            factDict[i[0]] = lab
                                            f = 0
                                            try:
                                                if i[4][ranWeek][0] in labDays:
                                                    x.append(i[4][ranWeek][0])
                                                    labDays.remove(i[4][ranWeek][0])
                                                    f = 1
                                                if i[4][ranWeek][4] in labDays:
                                                    x.append(i[4][ranWeek][4])
                                                    labDays.remove(i[4][ranWeek][4])
                            
                                            except:
                                                if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                    x = 2
                                                    labDays.remove(2)
                                                    f = 1 
                                                elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                    x = 6
                                                    labDays.remove(6)
                                                    f = 1
                                            randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                            
                                            i[3] -= 1
                                            i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            if f == 1:
                                                try:
                                                    labDays.extend(x)
                                                except:
                                                    labDays.append(x)
                            
                                            break
                            elif lab not in subjects[:6] and i[3] >= 2 and i[4].count(0) != 0 and i[5].count(0) != 0:
                                
                                factDict[i[0]] = lab
                                if i[4][ranWeek] == 0:
                                    pass
                                elif i[4][ranWeek][0] in labDays:
                                    x = i[4][ranWeek][0]
                                    labDays.remove(i[4][ranWeek][0])
                                if i[5][ranWeek] == 0:
                                    pass 
                                elif i[5][ranWeek][0] in labDays:
                                    y = i[5][ranWeek][0]
                                    labDays.remove(i[5][ranWeek][0])
                                randomDay = random.choice(labDays)
                                labDays.remove(randomDay)
                                days.remove(randomDay)
                                days.remove(randomDay + 1)
                                days.remove(randomDay + 2)
                                i[3] -= 1
                                i[6][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                try:
                                    labDays.append(x)
                                except:
                                    continue
                                try:
                                    labDays.append(y)
                                except:
                                    continue
                            else:
                                continue       
                                
                day = 0
       #print(days, randomDay)
                while subjectIndex:
                   # print(days)
                    day += 1
                   # randomPeriod = random.choice(days)
                    ran = random.choice(subjectIndex)
                    subject = subjects[ran]
                    subjectIndex.remove(ran)
                    for i in faculty:
                        if subject in i[2] and i[3] >= 2:
                            if subject in factDict.values():
                                try:
                                    if factDict[i[0]] == subject:
                                        if i[4].count(0) != 0:
                                            
                                            randomPeriod = random.choice(days)
                                        #print("Hello")
                                            if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[4][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[4][ranWeek] = randomPeriod
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1
                                            break
                                        else:
                                           # print(i[4], i[0])
                                            a = 0
                                            y = []
                                            try:
                                                x = len(i[4][ranWeek])
                                                a = 1 
                                            except:
                                                x = 0
                                                pass 
                                            if a == 1:
                                                if (i[4][ranWeek][0] in days):
                                                    days.remove(i[4][ranWeek][0])
                                                    y.append(i[4][ranWeek][0])
                                                if (i[4][ranWeek][1] in days):
                                                    days.remove(i[4][ranWeek][1])
                                                    y.append(i[4][ranWeek][1])
                                                if (i[4][ranWeek][2] in days):
                                                    days.remove(i[4][ranWeek][2])
                                                    y.append(i[4][ranWeek][2])
                                                if len(i[4][ranWeek]) >= 4 and i[4][ranWeek][3] in days:
                                                    days.remove(i[4][ranWeek][3])
                                                    y.append(i[4][ranWeek][3])
                                            else:
                                                if i[4][ranWeek] in days:
                                                    days.remove(i[4][ranWeek])
                                                    y.append(i[4][ranWeek])
                                            randomPeriod = random.choice(days)
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1

                                            if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[5][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[5][ranWeek] = randomPeriod
                                        
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            try:
                                                days.extend(y)
                                            except:
                                                days.append(y)
                                            break 

                                        
                                except:
                                    continue
                            elif i[5].count(0) != 0:
                                if i[0] not in factDict:
                                    factDict[i[0]] = subject
                                    if i[4].count(0) != 0:
                                    #print("Hello")
                                            randomPeriod = random.choice(days)
                                           # i[4].append([randomPeriod, classes])
                                            if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[4][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[4][ranWeek] = randomPeriod
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            break
                                    else:
                                       
                                            a = 0
                                            y = []
                                            try:
                                                x = len(i[4][ranWeek])
                                                a = 1 
                                            except:
                                                x = 0
                                                pass 
                                            if a == 1:
                                                if (i[4][ranWeek][0] in days):
                                                    days.remove(i[4][ranWeek][0])
                                                    y.append(i[4][ranWeek][0])
                                                if (i[4][ranWeek][1] in days):
                                                    days.remove(i[4][ranWeek][1])
                                                    y.append(i[4][ranWeek][1])
                                                if (i[4][ranWeek][2] in days):
                                                    days.remove(i[4][ranWeek][2])
                                                    y.append(i[4][ranWeek][2])
                                                if len(i[4][ranWeek]) >= 4 and (i[4][ranWeek][3] in days):
                                                    days.remove(i[4][ranWeek][3])
                                                    y.append(i[4][ranWeek][3])
                                            else:
                                                if i[4][ranWeek] in days:
                                                    days.remove(i[4][ranWeek])
                                                    y.append(i[4][ranWeek])
                                            randomPeriod = random.choice(days)
                                            
                                            if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[5][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[5][ranWeek] = randomPeriod
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            try:
                                                days.extend(y)
                                            except:
                                                days.append(y)
                                            days = list(set(days))
                                            break 

                                else:
                                        continue
                            else:
                                continue
                        else:
                            continue
                   # print(days, randomPeriod)
                    days.remove(randomPeriod)
                    
                sec1.append((sec2))
        #print(sec2)
                weeks.remove(ranWeek)
            sec1 = sorted(sec1, key = lambda x : x[0][0])
            for k, v in factDict.items():
                for i in faculty:
                    if k == i[0]:
                        if i[6].count(0) != 6:
                            i[6].append(sem)
                        elif i[5].count(0) != 6:
                            i[5].append(sem)
                        elif i[4].count(0) != 6:
                            i[4].append(sem)
                    else:
                        continue
            #print(factDict)
           
            return sec1, factDict
        x = mainFunction(sem1, [0, 1, 2], "ICSEA")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem1, [0, 1, 2], "ICSEB")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem1, [0, 1, 2], "ICSEC")
        templist.append(x[0])
        fact.append(x[1])
        #templist.append(mainFunction(sem2, [0, 1, 2]))
        x = mainFunction(sem3, [0, 1, 2, 3], "IICSEA")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem3, [0, 1, 2, 3], "IICSEB")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem3, [0, 1, 2, 3], "IICSEC")
        templist.append(x[0])
        fact.append(x[1])
        #templist.append(mainFunction(sem4, [0, 1, 2, 3]))
        x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEA")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEB")
        templist.append(x[0])
        fact.append(x[1])
        x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEC")
        templist.append(x[0])
        fact.append(x[1])
        return templist, fact, faculty, False
    except Exception as e:
        #print(e)
        return templist, fact, faculty, True
con = c.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    
flag = True 
goal = "sudha mam"
while flag:
    templist,fact, faculty, flag = generateTimeTable()
for i in fact:
    print(i)
    print("...................................")
table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
#print(templist)
c = 0
for sec1 in templist:
        week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    #print("          1        2         3       4        5           6          7          8")
        data_items = []
        #print(c, len(fact), len(templist))
        fact1 = fact[templist.index(sec1)]
        #print(fact1)
        for p in fact1.keys():
            for w in range(6):
                x = []
                x.append(p)
                x.append(week[w])
                for j in range(8):
                    for k in sec1[w]:
                        k = k[1:]
                        try:
                            if j + 1 in k[1]:
                                if len(k[1]) == 3:
                                    x.append(k[2] + "lab")
                            #print(k[2], end = "lab     ")
                                    break
                        except:
                            if j + 1 == k[1]:
                                x.append(k[2])
                                break
                            else:
                                continue
                    else:
                        x.append("----")
                data_items.append(x)
               # print(x)
                mySql_insert_query = "INSERT INTO time1 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                cursor = con.cursor()
                cursor.execute(mySql_insert_query)
                con.commit()
                print(x)
table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
for i in faculty:
    if i[4].count(0) == 6:
        continue
    print("         " + i[0] + "           ")
    data_items = []
    c = 0
    for w in range(6):
        x = []
        x.append(i[0])
        x.append(week[w])
        for j in range(8):
            try:
                if j + 1 in i[4][w]:
                    if len(i[4]) == 6:
                        x.append(i[5][-2])
                    else:
                        x.append(i[4][-1])
                    continue
            except:
                if j + 1 == i[4][w]:
                    x.append(i[4][-1])
                    continue
            try:
                if j + 1 in i[5][w]:
                    x.append(i[5][-1])
                    continue
            except:
                if j + 1 == i[5][w]:
                    x.append(i[5][-1])
                    continue
            try:
                if j + 1 in i[6][w]:
                    x.append(i[6][-1])
                    continue
            except:
                if j + 1 == i[6][w]:
                    x.append(i[6][-1])
                    continue
            x.append("----")
        data_items.append(x)
        print(x)
        mySql_insert_query = "INSERT INTO time2 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
            #cursor = con.cursor()
        cursor.execute(mySql_insert_query)
        con.commit()
        print(x)
    format_row = "{:>9}" * (len(table) + 1)
    print(format_row.format("", *table))
    for team, row in zip(table, data_items):
        print(format_row.format(team, *row))
    print("...........................................................")
query = "select * from time3"
cursor = con.cursor()
cursor.execute(query)
records = cursor.fetchall()
print(faculty)
print(len(records))