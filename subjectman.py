# Nghiệp vụ quản lý môn học
from dbprovider import writeSubject, writeSubjects, readSubjects, checkExistsSubject, checkExistsName, getSubjectByCode
from utils import printMenu,clearScreen,printHeader

def subjectMenuScreen():
    clearScreen()
    printHeader('QUẢN LÍ MÔN HỌC')
    funcs = [
        '1. Thêm',
        '2. Sửa',
        '3. Xóa',
        '4. Tìm kiếm',
        '0. Trở về màn hình CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI'
    ]
    printMenu(funcs)

    # Điều hướng màn hình

    cmd = None 
    while cmd not in ['1','2','3','4','0']: 
        cmd = input('Chọn chức năng: ')

    if cmd == '1':
        # Chuyển sang màn hình Thêm MÔN HỌC 
        addSubjectScreen()
        subjectMenuScreen()
    elif cmd == '2':
        # Chuyển sang màn hình Sửa MÔN HỌC
        editSubjectScreen()
        subjectMenuScreen()
    elif cmd == '3':
        # Chuyển sang màn hình Xóa MÔN HỌC
        deleteSubjectScreen()
        subjectMenuScreen()
    elif cmd == '4':
        # Chuyển sang màn hình Tìm kiếm MÔN HỌC
        searchSubjectScreen()
        subjectMenuScreen()
    elif cmd =='0':
        # Chuyển về màn hình 
       pass

def addSubjectScreen():
    clearScreen()
    printHeader('THÊM MÔN HỌC')
    
    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - ma mon hoc

    while True:
        Code = input('Nhập vào mã môn học: ') 
        # Không được để trống
        if Code == '':
            print('Không được để trống Mã môn học ')
            continue
        # Không được trùng
        if checkExistsSubject(Code) == True:
            print('Môn học đã tồn tại')
            continue
        # Phai viet in hoa
        if Code.isupper() == False:
            print('Mã môn học phải viết in hoa')
            continue
        # 5 ki tu
        if len(Code) != 5:
            print('Mã môn học có 5 kí tự')
            continue
        break

    # Validate dữ liệu nhập từ bàn phím - tên môn học

    while True:
        Name = input('Nhập vào tên môn học: ')  # KHông được để trống
        if Name == '':
            print('Không được để trống Tên môn học')
            continue
        if checkExistsName(Name) == True: # không được trùng
            print('Tên môn học đã tồn tại')
            continue
        break
    
    # Đổ dữ liệu vào cái túi 'dict' để gửi xuống hàm writeSubject trong DBProvider
    sub = {
        'Code': Code,
        'Name': Name
    }
    writeSubject(sub)
    print(f"Thêm môn học {Code} thành công !!!")

    ans = input('Nhập y/Y để tiếp tục')
    if ans.lower() == 'y':
        addSubjectScreen()

def editSubjectScreen():
    clearScreen()
    printHeader('CHỈNH SỬA THÔNG TIN MÔN HỌC')

    while True:
        code = input('Mã môn cần sửa: ')
        if len(code) != 5:
            print('Mã HV phải bao gồm 5 ký tự.')
            continue
        isExists = checkExistsSubject(code)
        if isExists == False:
            print(f'HV có mã "{code}" không tồn tại.')
            continue
        break

    # Lấy thông tin theo mã môn học đã nhập
    sub = getSubjectByCode(code)

    print('Môn học:', sub['Name'])  # Hiển thị tên cũ
    name = sub['Name']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        name = input('Tên môn mới: ')  

    # Sửa thông tin bằng cách sửa trên list, sau đó ghi đè mode 'w' vào trong file .txt
    # Validate du lieu 

    subs = readSubjects()
    for sub in subs:
        if sub['Code'] == code:
            sub['Name'] = name
            break #thoát vòng lặp, sửa xong thì ko duyệt những phần tử sau nữa. Nếu thụt ra ngoài (ngang hàng với 
        # if, thì nó có nghĩa là chỉ lặp một vòng for rồi sau đó sẽ break luôn, vì  vậy phải thụt vào trong)
    writeSubjects(subs)
    print(f'Chỉnh sửa môn học có mã "{code}" thành công !!!')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editSubjectScreen()

def deleteSubjectScreen():
    clearScreen()
    printHeader('XÓA MÔN HỌC')

    while True:
        code = input('Mã môn học cần xóa: ')
        if len(code) != 5:
            print('Mã mon hoc phải bao gồm 5 ký tự.')
            continue
        isExists = checkExistsSubject(code)
        if isExists == False:
            print(f'Môn học có mã "{code}" không tồn tại.')
            continue
        break

    # Xóa
    subs = readSubjects()
    idx = None
    for i, sub in enumerate(subs):
        if sub['Code'] == code:
            idx = i
            break #thoát vòng lặp, kp duyệt những phần tử sau nữa
    subs.pop(idx)
    writeSubjects(subs)
    print(f'Xóa môn học có mã "{code}" thành công')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteSubjectScreen()

def searchSubjectScreen():
    subs = readSubjects()
    printSubjects(subs)

    searchContent = input('Nội dung tìm kiếm: ')
    if searchContent != '':
        subsFiltered = []
        for sub in subs:
            if sub['Code'] == searchContent \
                or searchContent.lower() in sub['Name'].lower():
                subsFiltered.append(sub)
        
        printSubjects(subsFiltered)
        
    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchSubjectScreen()
    
def printSubjects(subs: list):
    clearScreen()
    printHeader('DANH SÁCH MÔN HỌC')

    print('Code\tName')
    for sub in subs:
        print(f"{sub['Code']}\t{sub['Name']}")