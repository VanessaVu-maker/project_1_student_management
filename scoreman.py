# # Nghiệp vụ quản lý điểm
from dbprovider import readScores, readStudents, readSubjects, writeScore, writeScores, getScoreByCode, checkExistsScore
from dbprovider import checkExistsStudent, checkExistsSubject, getStudentByCode, getSubjectByCode


from utils import printMenu, clearScreen, printHeader
def scoreMenuScreen():
    clearScreen()
    printHeader('QUẢN LÍ ĐIỂM THI')
    funcs = [
        '1. Thêm ĐIỂM THI',
        '2. Sửa ĐIỂM THI',
        '3. Xóa ĐIỂM THI',
        '4. Tìm kiếm ĐIỂM THI',
        '5. Thống kê theo Điểm Tổng Kết',
        '6. Xuất ra file CSV',
        '0. Trở về màn hình chính'
    ]
    printMenu(funcs)

    # Điều hướng màn hình

    cmd = None 
    while cmd not in ['1','2','3','4', '5', '6','0']: 
        cmd = input('Chọn chức năng: ')

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
    printHeader('THÊM ĐIỂM THI')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - student_Code
    while True:
        # 6 ký tự
        studentCode = input('Nhập mã học viên:')
        # Khong duoc bo trong
        if studentCode == '':
            print('Không được để trống mã HV')
            continue
        if len(studentCode) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        # 2 ký tự đầu phải là 'PY'
        if studentCode.startswith('PY') == False:
            print('2 ký tự đầu phải là "PY".')
            continue
        # phai tồn tại trong DB
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'Mã HV "{studentCode}" không tồn tại.')
            continue
        # phai viet hoa
        if studentCode.isupper() == False:
            print('Mã học viên phải viết hoa')
            continue
        break 

    # Validate dữ liệu nhập từ bàn phím - ma mon hoc

    while True:
        subjectCode = input('Nhập vào mã môn học: ') 
        # Không được để trống
        if subjectCode == '':
            print('Không được để trống Mã môn học ')
            continue
        # phai tồn tại trong DB
        if checkExistsSubject(subjectCode) == False:
            print('Mã môn học không tồn tại')
            continue
        # Phai viet in hoa
        if subjectCode.isupper() == False:
            print('Mã môn học phải viết in hoa')
            continue
        # 5 ki tu
        if len(subjectCode) != 5:
            print('Mã môn học phải có 5 kí tự')
            continue
        break

    # Kiểm tra xem đã có điểm thi nào tồn tại hay chưa (check dùng bộ studentCode và subjectCode, hàm checkExistsScore

    isExists = checkExistsScore(studentCode, subjectCode)
    if isExists == True:
        print('Điểm này đã nhập rồi!')
    else:
        while True:
            processScore = float(input('Nhập điểm quá trình: '))         
            # 1-100
            if processScore > 100 or processScore < 0:
                print('Vui lòng nhập lại điểm từ 1-100')
                continue
            # Không được để trống
            if processScore == '':
                print('Không được để trống điểm quá trình ')
                continue
            break  
        
        while True:
            finalTestScore = float(input('Nhập điểm kết thúc: '))          
            # 1-100
            if finalTestScore > 100 or finalTestScore < 0:
                print('Vui lòng nhập lại điểm từ 1-100')
                continue
        # Không được để trống
            if finalTestScore == '':
                print('Không được để trống điểm kết thúc')
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
        print("Thêm điểm thành công!!")

    ans = input("Nhập y/Y để tiếp tục thêm: ")
    if ans.lower() == 'y':
        # quay lại để nhập tiếp
        addScoreScreen()

def editScoreScreen():
    clearScreen()
    printHeader('CHỈNH SỬA THÔNG TIN ĐIỂM THI')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - studentCode
    while True:
        # 6 ký tự
        studentCode = input('Mã HV cần sửa: ')
        # Khong duoc bo trong
        if studentCode == '':
            print('Không được để trống mã HV')
            continue
        if len(studentCode) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        # 2 ký tự đầu phải là 'PY'
        if studentCode.startswith('PY') == False:
            print('2 ký tự đầu phải là "PY".')
            continue
        # phai tồn tại trong DB
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'Mã HV "{studentCode}" không tồn tại.')
            continue
        # phai viet hoa
        if studentCode.isupper() == False:
            print('Mã học viên phải viết hoa')
            continue
        break 

    # Validate dữ liệu nhập từ bàn phím - subjectCode
    while True:
        subjectCode = input('Nhập vào mã môn học: ') 
        # Không được để trống
        if subjectCode == '':
            print('Không được để trống Mã môn học ')
            continue
        # phai tồn tại trong DB
        if checkExistsSubject(subjectCode) == False:
            print('Mã môn học không tồn tại')
            continue
        # Phai viet in hoa
        if subjectCode.isupper() == False:
            print('Mã môn học phải viết in hoa')
            continue
        # 5 ki tu
        if len(subjectCode) != 5:
            print('Mã môn học phải có 5 kí tự')
            continue
        break

# Validate để ensure là cặp studentCode, subjectCode được nhập vào đã tồn tại để có thể chỉnh sửa

    # Lấy thông tin theo mã học viên và mã môn học đã nhập
    sc = getScoreByCode(studentCode, subjectCode)

    print('Điểm quá trình:', sc['Process_Score'])
    processScore_new = sc['Process_Score']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        # Validate process score mới
        processScore_new = float(input('Điểm quá trình mới: '))
        while True:       
        # 1-100
            if processScore_new > 100 or processScore_new < 0:
                print('Vui lòng nhập lại điểm từ 1-100')
                continue
            # Check số thực dùng hàm checkPoint
            # Không được để trống
            if processScore_new == '':
                print('Không được để trống điểm quá trình ')
                continue
            break  

    print('Điểm kết thúc:', sc['Final_Test_Score'])
    finalTestScore_new = sc['Final_Test_Score']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        finalTestScore_new  = float(input('Điểm kết thúc mới: '))   
        while True:
            finalTestScore_new = float(input('Nhập điểm kết thúc: '))          
            # 1-100
            if finalTestScore_new > 100 or finalTestScore_new < 0:
                print('Vui lòng nhập lại điểm từ 1-100')
                continue
        # Check số thực dùng hàm checkPoint
        # Không được để trống
            if finalTestScore_new == '':
                print('Không được để trống điểm kết thúc')
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

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editScoreScreen()
    
def deleteScoreScreen():
    clearScreen()
    printHeader('XÓA ĐIỂM THI')
    
    while True:
        studentCode = input('Mã học viên cần xóa: ')
        if len(studentCode) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        isExists = checkExistsStudent(studentCode)
        if isExists == False:
            print(f'HV có mã "{studentCode}" không tồn tại.')
            continue
        break

    while True:
        subjectCode = input('Mã môn học cần xóa: ')
        if len(subjectCode) != 5:
            print('Mã HV phải bao gồm 5 ký tự.')
            continue
        isExists = checkExistsSubject(subjectCode)
        if isExists == False:
            print(f'Môn học có mã "{subjectCode}" không tồn tại.')
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

    print(f'Xóa điểm môn học có mã "{subjectCode}" thành công')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteScoreScreen()

def searchScoreScreen():
    scs = readScores()
    printScores(scs)
    searchContent = input('Nội dung tìm kiếm: ')
    if searchContent != '':
        scsFiltered = []
        for sc in scs:
            if searchContent == sc['Student_Code'] \
                    or searchContent == sc['Subject_Code']:
                scsFiltered.append(sc)
        
        printScores(scsFiltered)

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchScoreScreen()

def printScores(scs: list):
    clearScreen()
    printHeader('DANH SÁCH ĐIỂM THI')

    print('Mã HV\tMã môn học\tĐiểm quá trình\tĐiểm cuối cùng')
    for sc in scs:
        print(f"{sc['Student_Code']}\t{sc['Student_Code']}\t{sc['Process_Score']}\t{sc['Final_Test_Score']}")

def printRankScore():
    clearScreen()
    printHeader('THỐNG KÊ ĐIỂM THI')

    scs = readScores()
    print('Mã học viên\tHọ Tên\tMã môn học\tTên môn học\tĐiểm quá trình\tĐiểm kết thúc\tĐiểm tổng kết\tXếp loại')
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

    ans = input("Nhập y/Y để thoát: ")
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

