# # Nghiệp vụ quản lý điểm
from dbprovider import readScores, readStudents, readSubjects, writeScore, writeScores, getScoreByCode, checkExistsScore
from dbprovider import checkExistsStudent, checkExistsSubject, getStudentByCode, getSubjectByCode


from utils import printMenu, clearScreen, printHeader
def scoreMenuScreen():
    clearScreen()
    printHeader('SCORE MANAGEMENT')
    funcs = [
        '1. Add score',
        '2. Edit score',
        '3. Delete score',
        '4. Search score',
        '5. List score',
        '6. Export score as CSV',
        '0. Return'
    ]
    printMenu(funcs)

    # Điều hướng màn hình

    cmd = None 
    while cmd not in ['1','2','3','4', '5', '6','0']: 
        cmd = input('Choose number: ')

    if cmd == '1':
        addScoreScreen()
        scoreMenuScreen()
    elif cmd == '2':
        editScoreScreen()
        scoreMenuScreen()
    elif cmd == '3':
        deleteScoreScreen()
        scoreMenuScreen()
    elif cmd == '4':
        searchScoreScreen()
        scoreMenuScreen()
    elif cmd == "5":
        printRankScore()
        scoreMenuScreen()
    elif cmd == '6':
        exportScoreScreen()
        scoreMenuScreen()
    elif cmd == '0':
        # Trở về màn hình Menu chính
            pass

def addScoreScreen():
    clearScreen()
    printHeader('Add score')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - student_Code
    while True:
        # 6 ký tự
        studentCode = input('Enter student code:')
        # Khong duoc bo trong
        if studentCode == '':
            print('Student Code cannot be empty')
            continue
        if len(studentCode) != 6:
            print('Student code has to have 6 characters')
            continue
        # 2 ký tự đầu phải là 'PY'
        if studentCode.startswith('PY') == False:
            print('Student code has to begin with PY')
            continue
        # phai tồn tại trong DB
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'Student Code "{studentCode}" does not exist')
            continue
        # phai viet hoa
        if studentCode.isupper() == False:
            print('Student Code has to be in capital letters')
            continue
        break 

    # Validate dữ liệu nhập từ bàn phím - ma mon hoc

    while True:
        subjectCode = input('Enter subject code: ') 
        # Không được để trống
        if subjectCode == '':
            print('Subject Code cannot be empty ')
            continue
        # phai tồn tại trong DB
        if checkExistsSubject(subjectCode) == False:
            print('Student code has to exist in database')
            continue
        # Phai viet in hoa
        if subjectCode.isupper() == False:
            print('Student code has to be in capital letters')
            continue
        # 5 ki tu
        if len(subjectCode) != 5:
            print('Subject code has to have 5 characters')
            continue
        break

    # Kiểm tra xem đã có điểm thi nào tồn tại hay chưa (check dùng bộ studentCode và subjectCode, hàm checkExistsScore

    isExists = checkExistsScore(studentCode, subjectCode)
    if isExists == True:
        print('This score has been entered!')
    else:
        while True:
            processScore = float(input('Enter process score: '))         
            # 1-100
            if processScore > 100 or processScore < 0:
                print('Process score has to be from 1 to 100')
                continue
            # Không được để trống
            if processScore == '':
                print('Cannot leave empty ')
                continue
            break  
        
        while True:
            finalTestScore = float(input('Enter final test score: '))          
            # 1-100
            if finalTestScore > 100 or finalTestScore < 0:
                print('Final Test score has to be from 1 to 100')
                continue
        # Không được để trống
            if finalTestScore == '':
                print('Cannot leave empty')
                continue
            break  
        # (loi 'processScore' referenced before assignment)
        
        # Đổ dữ liệu vào cái túi 'dict' để gửi xuống hàm writeScore trong DBProvider
        sc = {
                'Student_Code': studentCode,
                'Subject_Code': subjectCode,
                'Process_Score': processScore,
                'Final_Test_Score': finalTestScore
            }
        writeScore(sc)
        print("Add score successfully!!")

    ans = input("Enter y/Y to proceed: ")
    if ans.lower() == 'y':
        # quay lại để nhập tiếp
        addScoreScreen()

def editScoreScreen():
    clearScreen()
    printHeader('Edit Score Information')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - studentCode
    while True:
        # 6 ký tự
        studentCode = input('Student Code: ')
        # Khong duoc bo trong
        if studentCode == '':
            print('Cannot leave empty')
            continue
        if len(studentCode) != 6:
            print('Studen code has to have 6 characters.')
            continue
        # 2 ký tự đầu phải là 'PY'
        if studentCode.startswith('PY') == False:
            print('First two characters have to start with "PY".')
            continue
        # phai tồn tại trong DB
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'Student Code"{studentCode}" does not exist.')
            continue
        # phai viet hoa
        if studentCode.isupper() == False:
            print('Student Code has to be in capital letters')
            continue
        break 

    # Validate dữ liệu nhập từ bàn phím - subjectCode
    while True:
        subjectCode = input('Enter subject code: ') 
        # Không được để trống
        if subjectCode == '':
            print('Cannot leave subject code empty ')
            continue
        # phai tồn tại trong DB
        if checkExistsSubject(subjectCode) == False:
            print('Subject code does not exist')
            continue
        # Phai viet in hoa
        if subjectCode.isupper() == False:
            print('Subject code has to be in capital letters')
            continue
        # 5 ki tu
        if len(subjectCode) != 5:
            print('Subject code has to have 5 letters')
            continue
        break

# Validate để ensure là cặp studentCode, subjectCode được nhập vào đã tồn tại để có thể chỉnh sửa

    # Lấy thông tin theo mã học viên và mã môn học đã nhập
    sc = getScoreByCode(studentCode, subjectCode)

    print('Process Score:', sc['Process_Score'])
    processScore_new = sc['Process_Score']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        # Validate process score mới
        processScore_new = float(input('New process score: '))
        while True:       
        # 1-100
            if processScore_new > 100 or processScore_new < 0:
                print('Please add score from 1 to 100')
                continue
            # Check số thực dùng hàm checkPoint
            # Không được để trống
            if processScore_new == '':
                print('Cannot leave empty ')
                continue
            break  

    print('Final Test Score:', sc['Final_Test_Score'])
    finalTestScore_new = sc['Final_Test_Score']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        finalTestScore_new  = float(input('New Final Test Score: '))   
        while True:
            finalTestScore_new = float(input('New final Test Score: '))          
            # 1-100
            if finalTestScore_new > 100 or finalTestScore_new < 0:
                print('Please enter score from 1 to 100')
                continue
        # Check số thực dùng hàm checkPoint
        # Không được để trống
            if finalTestScore_new == '':
                print('Cannot leave empty')
                continue
            break  

    # Sửa thông tin bằng cách sửa trên list, sau đó ghi đè mode 'w' vào trong file .txt

    scs = readScores()
    for sc in scs:
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            sc['Process_Score'] =  processScore_new
            sc['Final_Test_Score'] =  finalTestScore_new
            break
    writeScores(scs)
    print(f'Chỉnh sửa điểm của học viên có mã "{studentCode}", môn "{subjectCode}" thành công !!!')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editScoreScreen()
    
def deleteScoreScreen():
    clearScreen()
    printHeader('Delete score')
    
    while True:
        studentCode = input('Student Code: ')
        if len(studentCode) != 6:
            print('student code has to have 6 characters.')
            continue
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'student with student code "{studentCode}" doesnt exist.')
            continue
        break

    while True:
        subjectCode = input('Subject Code: ')
        if len(subjectCode) != 5:
            print('Subject code has to have 5 characters.')
            continue
        isExists = checkExistsSubject(subjectCode)
        if isExists == False:
            print(f'Subject code "{subjectCode}" doesnt exist')
            continue
        break

    # while True:
    #     isExists = checkExistsScore(studentCode, subjectCode)
    #     if isExists == False:
    #         print('Điểm của học viên có mã') 
    #         # # "{studentCode}", môn "{subjectCode}" không tồn tại')
    #         continue
    #     break

    # Xóa
    scs = readScores()
    idx = None
    for i, sc in enumerate(scs):
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            idx = i
            break
    scs.pop(idx)
    writeScores(scs)

    print(f'Delete subject "{subjectCode}" successfully')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteScoreScreen()

def searchScoreScreen():
    scs = readScores()
    printScores(scs)
    searchContent = input('Search info: ')
    if searchContent != '':
        scsFiltered = []
        for sc in scs:
            if searchContent == sc['Student_Code'] \
                    or searchContent == sc['Subject_Code']:
                scsFiltered.append(sc)
        
        printScores(scsFiltered)

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchScoreScreen()

def printScores(scs: list):
    clearScreen()
    printHeader('Score List')

    print('Student Code\tSubject Code\tProcess Score\tFinal Test Score')
    for sc in scs:
        print(f"{sc['Student_Code']}\t{sc['Student_Code']}\t{sc['Process_Score']}\t{sc['Final_Test_Score']}")

def printRankScore():
    clearScreen()
    printHeader('Score List')

    scs = readScores()
    print('Student Code\tStudent Name\tSubject Code\tSubject\tProcess Score\tFinal Test Score\tTotal Score\tRanking')
    for sc in scs:
        studentCode = sc['Student_Code']
        
        st = getStudentByCode(studentCode)
        fullName    = st['FullName']

        subjectCode = sc['Subject_Code']
        
        sub = getSubjectByCode(subjectCode)
        name = sub['Name']

        processScore = float(sc['Process_Score'])
        finalTestScore = float(sc['Final_Test_Score'])                   
        totalScore = round((processScore + finalTestScore*2)/3)
        rank = ranking(totalScore)
        print(f'{studentCode}\t\t{fullName}\t{subjectCode}\t\t{name}\t\t{processScore}\t\t{finalTestScore}\t\t{totalScore}\t\t{rank}')

    ans = input("Enter y/Y to exit: ")
    if ans.lower() == 't':
        scoreMenuScreen()
    
    # Xuất file csv
    import csv
    scs = readScores()
    with open('filecsv.csv','w',encoding = 'utf-8',newline='') as csvf:
        fieldnames = ['Mã học viên','Họ tên','Ngày sinh',\
            'Giới tính', 'Địa chỉ','Số điện thoại','Email',\
                'Tên môn học', 'Điểm quá trình','Điểm kết thúc','Điểm tổng kết']
        thewriter = csv.DictWriter(csvf, fieldnames=fieldnames)
        thewriter.writeheader()  
        for i,sc in enumerate(scs):
            studentlist = getStudentByCode(sc['Student_Code'])
            subjectlist = getSubjectByCode(sc['Subject_Code'])
            thewriter.writerow({'Mã học viên':studentlist['Code'], \
                                'Họ tên':studentlist['FullName'], \
                                'Ngày sinh': studentlist['Birthday'], \
                                'Giới tính': studentlist['Sex'], \
                                'Địa chỉ': studentlist['Address'], \
                                'Số điện thoại': studentlist['Phone'],\
                                'Email': studentlist['Email'],\
                                    'Tên môn học': subjectlist,\
                                        'Điểm quá trình': sc['Process_Score'],\
                                        'Điểm kết thúc': sc['Final_Test_Score']}) 
                                       #  'Điểm tổng kết': rank[i]})   
def ranking(result):
    if result >= 90:
        return 'A'
    elif result >=70:
        return 'B'
    elif result >=50:
        return 'C'
    elif result <50:
        return 'D'


# import csv
# def exportScoreScreen():
#     # open the file in writer mode
#     f = open('result.csv','w',encoding='utf-8' )
#     #create the csv writer 
#     writer = csv.writer(f,delimiter=',')
#     sts = readStudents()
#     subs = readSubjects()
#     scs = readScores()
#     writer.writerow(['Mã học viên','Họ tên','Mã môn học','Tên môn học','Điểm quá trình','Điểm kết thúc','Điểm tổng kết','Xếp loại'])
#     # for st in sts:
#     #     student = st['Code']
#     #     for sub in subs:
#     #         subject = sub['Code']
#     #         for sc in scs:
#     #             if sc['Student_Code'] == student and sc['Subject_Code'] == subject:
#     #                 score = sc
#     #                 processScore = float(score['Process_Score'])
#     #                 finalTestScore = float(score['Final_Test_Score'])
#     #                 finalFinal = (processScore+finalTestScore*2)/3
#     #                 rank = ranking(finalFinal)
#     #                 writer.writerow([st['Code'],st['FullName'],sub['Code'],sub['Name'],score['Process_Score'],score['Final_Test_Score'],finalFinal,rank])
#     for sc in scs:
#         # TODO Thong tin student -> dua vao StudentCode
#         st = None #lay ra student tu list sts dua vao StudentCode

#         # TODO Thong tin subject -> SubjectCode
#         sub = None #lay ra subject tu list sbs dua vao SubjectCode

#         processScore = float(sc['Process_Score'])
#         finalTestScore = float(sc['Final_Test_Score'])
#         finalFinal = (processScore+finalTestScore*2)/3
#         rank = ranking(finalFinal)
#         writer.writerow([st['Code'],st['FullName'],sub['Code'],sub['Name'],sc['Process_Score'],sc['Final_Test_Score'],finalFinal,rank])

#     f.close()
#     print("Xuất file thành công!")

#     ans = input("Nhập y/Y để về màn hình chính: ")
#     if ans.lower() == 'y':
#         scoreMenuScreen()

