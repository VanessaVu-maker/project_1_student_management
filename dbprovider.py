# Giao tiếp (vào/ra) dữ liệu từ database

studentsPath = 'database/students.txt'
subjectsPath = 'database/subjects.txt'
scoresPath = 'database/scores.txt'


def writeStudent(st: dict):
    with open(studentsPath, 'a', encoding='utf-8') as f:
        line = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
        f.write(line)

def writeStudents(sts: list):
    with open(studentsPath, 'w', encoding='utf-8') as f:
        for st in sts:
            line = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
            f.write(line)

def readStudents():
    sts = []
    try:
        with open(studentsPath, 'r', encoding='utf-8') as f:
                for line in f:
                    value = line.strip().split('|')
                    st = {
                        'Code': value[0],
                        'FullName': value[1],
                        'Birthday': value[2],
                        'Sex': value[3],
                        'Address': value[4],
                        'Phone': value[5],
                        'Email': value[6]
                    }
                    sts.append(st)
    except FileNotFoundError as err:
        # Tạo file nếu chưa tồn tại
        with open(studentsPath, 'w', encoding='utf-8') as f:
            f.write('')
    return sts

def getStudentByCode(code: str):
    result = None

    # Lấy ra toàn bộ danh sách Học viên trong DB
    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            result = st
            break

    return result

def checkExistsStudent(code: str):
    isExists = False

    # Lấy ra toàn bộ danh sách Học viên trong DB
    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            isExists = True
            break

    return isExists

def writeSubject(sub: dict):
    with open(subjectsPath,'a',encoding = 'utf-8') as f:
        line = f"{sub['Code']}|{sub['Name']}\n"
        f.write(line)

def writeSubjects(subs: list):
    with open(subjectsPath,'w',encoding='utf-8') as f:
        for sub in subs:
            line = f"{sub['Code']}|{sub['Name']}\n"
            f.write(line)

def readSubjects():
    subs = []
    try:
        with open(subjectsPath, 'r', encoding='utf-8') as f:
            for line in f:
                value = line.strip().split("|")
                sub = {
                    'Code': value[0],
                    'Name': value[1]
                }
                subs.append(sub)
    except:
        with open(subjectsPath, 'w', encoding='utf-8') as f:
            f.write('')
    return subs

def checkExistsSubject(code: str):
    isExists = False
    subs = readSubjects()
    for sub in subs:
        if sub['Code'] == code:
            isExists = True
            break
    return isExists

def getSubjectByCode(code: str):
    result = None

    # Lấy ra toàn bộ danh sách Môn học trong DB
    subs = readSubjects()
    for sub in subs:
        if sub['Code'] == code:
            result = sub
            break

    return result

def checkExistsName(name: str):
    isExists = False
    subs = readSubjects()
    for sub in subs:
        if sub['Name'] == name:
            isExists = True
            break
    return isExists

def writeScore(sc: dict):
   with open(scoresPath,'a',encoding='utf-8') as f:
        line = f"{sc['Student_Code']}|{sc['Subject_Code']}|{sc['Process_Score']}|{sc['Final_Test_Score']}\n"
        f.write(line)

def writeScores(scs: list):
    with open(scoresPath,'w',encoding='utf-8') as f:
        for sc in scs:
            line = f"{sc['Student_Code']}|{sc['Subject_Code']}|{sc['Process_Score']}|{sc['Final_Test_Score']}\n"
            f.write(line)

def readScores():

    scs = []
    try:
        with open(scoresPath, 'r', encoding='utf-8') as f:
            for line in f:
                value = line.strip().split('|')
                sc = {
                    'Student_Code':value[0],
                    'Subject_Code':value[1],
                    'Process_Score':value[2],
                    'Final_Test_Score':value[3]
                }
                scs.append(sc)               
    except FileNotFoundError as err:
        # Tạo file nếu chưa tồn tại
        with open(scoresPath, 'w', encoding='utf-8') as f:
            f.write('')
    return (scs)

def checkExistsScore(studentCode: str, subjectCode: str):
    isExists = False
    scs = readScores()
    for sc in scs:
        if sc['Subject_Code'] == subjectCode and sc['Student_Code'] == studentCode:
            isExists = True
            break
    return isExists

def getScoreByCode(studentCode: str, subjectCode: str):
    result = None
    # Lấy ra toàn bộ danh sách Điểm thi trong DB
    scs = readScores()
    for sc in scs:
        if sc['Subject_Code'] == subjectCode and sc['Student_Code'] == studentCode:
            result = sc
            break
    return result
    
