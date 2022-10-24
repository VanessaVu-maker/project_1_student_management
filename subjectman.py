# Nghiệp vụ quản lý môn học
from dbprovider import writeSubject, writeSubjects, readSubjects, checkExistsSubject, checkExistsName, getSubjectByCode
from utils import printMenu,clearScreen,printHeader

def subjectMenuScreen():
    clearScreen()
    printHeader('Student Management')
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
    printHeader('Add subjects')
    
    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - ma mon hoc

    while True:
        Code = input('Enter subject code: ') 
        # Không được để trống
        if Code == '':
            print('Cannot leave empty')
            continue
        # Không được trùng
        if checkExistsSubject(Code) == True:
            print('Subject existed')
            continue
        # Phai viet in hoa
        if Code.isupper() == False:
            print('Has to be in capital letters')
            continue
        # 5 ki tu
        if len(Code) != 5:
            print('Can only have 5 characters')
            continue
        break

    # Validate dữ liệu nhập từ bàn phím - tên môn học

    while True:
        Name = input('Enter subject name: ')  # KHông được để trống
        if Name == '':
            print('Cannot leave empty')
            continue
        if checkExistsName(Name) == True: # không được trùng
            print('Already existed')
            continue
        break
    
    # Đổ dữ liệu vào cái túi 'dict' để gửi xuống hàm writeSubject trong DBProvider
    sub = {
        'Code': Code,
        'Name': Name
    }
    writeSubject(sub)
    print(f"Succesfully added!!!")

    ans = input('Enter y/Y to proceed')
    if ans.lower() == 'y':
        addSubjectScreen()

def editSubjectScreen():
    clearScreen()
    printHeader('Edit Subject Screen')

    while True:
        code = input('Subject Code: ')
        if len(code) != 5:
            print('Has to have 5 characters.')
            continue
        isExists = checkExistsSubject(code)
        if isExists == False:
            print(f'Doesnt exist')
            continue
        break

    # Lấy thông tin theo mã môn học đã nhập
    sub = getSubjectByCode(code)

    print('Subject:', sub['Name'])  # Hiển thị tên cũ
    name = sub['Name']
    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        name = input('New subject: ')  

    # Sửa thông tin bằng cách sửa trên list, sau đó ghi đè mode 'w' vào trong file .txt
    # Validate du lieu 

    subs = readSubjects()
    for sub in subs:
        if sub['Code'] == code:
            sub['Name'] = name
            break #thoát vòng lặp, sửa xong thì ko duyệt những phần tử sau nữa. Nếu thụt ra ngoài (ngang hàng với 
        # if, thì nó có nghĩa là chỉ lặp một vòng for rồi sau đó sẽ break luôn, vì  vậy phải thụt vào trong)
    writeSubjects(subs)
    print(f'Successfully edited !!!')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editSubjectScreen()

def deleteSubjectScreen():
    clearScreen()
    printHeader('Delete subjects')

    while True:
        code = input('Subject Code: ')
        if len(code) != 5:
            print('Only 5 characters.')
            continue
        isExists = checkExistsSubject(code)
        if isExists == False:
            print(f'Doesnt exist.')
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
    print(f'Successfully deleted')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteSubjectScreen()

def searchSubjectScreen():
    subs = readSubjects()
    printSubjects(subs)

    searchContent = input('Search info: ')
    if searchContent != '':
        subsFiltered = []
        for sub in subs:
            if sub['Code'] == searchContent \
                or searchContent.lower() in sub['Name'].lower():
                subsFiltered.append(sub)
        
        printSubjects(subsFiltered)
        
    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchSubjectScreen()
    
def printSubjects(subs: list):
    clearScreen()
    printHeader('SUBJECT LIST')

    print('Code\tName')
    for sub in subs:
        print(f"{sub['Code']}\t{sub['Name']}")