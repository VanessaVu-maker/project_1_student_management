# Nghiệp vụ quản lý Học viên
from utils import clearScreen, printMenu, printHeader, checkEmail, checkDate
from dbprovider import writeStudent, writeStudents, readStudents, getStudentByCode, checkExistsStudent


def studentMenuScreen():
    clearScreen()
    printHeader('Student Management')

    funcs = [
        '1. Add Student',
        '2. Edit Student',
        '3. Delete Student',
        '4. Student List',
        '0. Return'
    ]
    printMenu(funcs)

    cmd = None  # mã lệnh người dùng chọn, ban đầu chưa phải lệnh nào cả
    while cmd not in ['1', '2', '3', '4', '0']:
        cmd = input('Enter number: ')

    if cmd == '1':
        # Chuyển sang màn hình Thêm Học viên
        addStudentScreen()
        # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
        studentMenuScreen()
    elif cmd == '2':
        # Chuyển sang màn hình Sửa Học viên
        editStudentScreen()
        # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
        studentMenuScreen()
    elif cmd == '3':
        # Chuyển sang màn hình Xoá Học viên
        deleteStudentScreen()
        # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
        studentMenuScreen()
    elif cmd == '4':
        # Chuyển sang màn hình Danh sách Học viên
        searchStudentScreen()
        # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
        studentMenuScreen()
    elif cmd == '0':
        # Trở về màn hình Menu chính
        pass


def addStudentScreen():
    clearScreen()
    printHeader('Add studnent')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - ma hoc vien
    while True:
        # 6 ký tự
        code = input('Student Code: ')
        if len(code) != 6:
            print('Student Code has to have 6 letters.')
            continue
        # 2 ký tự đầu phải là 'PY'
        if code.startswith('PY') == False:
            print('2 first characters has to be "PY".')
            continue
        # không tồn tại trong DB
        isExists = checkExistsStudent(code)
        if isExists == True:
            print(f'Student Code "{code}" has been used.')
            continue
        # phai viet hoa
        if code.isupper() == False:
            print('Student Code has to be in capital letters')
            continue
        # Khong duoc bo trong
        if code == '':
            print('Cannot leave empty')
            continue
        break    
    
    # Validate dữ liệu nhập từ bàn phím - ten hoc vien
    while True:
        fullName = input('Student Name:')    
        # Phai viet hoa
        if fullName.isupper() == False:
            print('Student Name has to be in capital letters')
            continue
        # Khong duoc bo trong
        if fullName == '':
            print('Cannot leave empty')
            continue
        break    

    # Validate dữ liệu nhập từ bàn phím - ngay sinh

    while True:
        birthday = input('Birthday (dd/MM/yyyy): ') 
        # đúng định dang đd/MM/yyyy
        if checkDate(birthday) == None:
            print('Enter format dd/mm/yyyy')
            continue
        # không được để trống
        if birthday == '':
            print('Cannot leave empty')
            continue
        break   

    # Validate dữ liệu nhập từ bàn phím - gioi tinh

    while True:
        sex = input('Gender (0-nữ|1-nam): ') 
        # chỉ là '0' hoặc '1'
        if sex not in ['0','1']:
            print('Enter gender: 1 - Nam, 0 - nữ')
            continue
         # Không được bỏ trống
        if sex == '':
            print('Cannot leave empty')
            continue
        break

    address = input('Address: ')

    # Validate dữ liệu nhập từ bàn phím - SDT

    while True:
        phone = input('Phone number: ')          
        # Có thể không nhập
        if phone == '':
            break
        # Chỉ chứa số, độ dài 10 kí tự
        if phone.isdigit() == False:
            print('Only contain numbers')
            continue
        # độ dài 10 kí tự
        if len(phone) != 10:
            print(' Phone number can only have 10 characters')
            continue
        break  
    
    # Validate dữ liệu nhập từ bàn phím - email

    while True:
        email = input('Email: ')        
        # Có thể không nhập
        if email == '':
            break
        # Có thể không nhập, nhưng nếu nhập thì phải đúng format Email (sử dụng regex Email để check)  
        if checkEmail(email) == False:
            print('Enter correct email format')
            continue
        break


    # Đổ dữ liệu vào cái túi 'dict' để gửi xuống hàm writeStudent trong DBProvider
    st = {
        'Code': code,
        'FullName': fullName,
        'Birthday': birthday,
        'Sex': int(sex),
        'Address': address,
        'Phone': phone,
        'Email': email
    }
    writeStudent(st)
    print(f'Added student "{code}" !!!')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        addStudentScreen()


def editStudentScreen():
    clearScreen()
    printHeader('Edit Student Score')

    while True:
        code = input('Student Code: ')
        # ko bo trong
        if len(code) != 6:
            print('Student Code has to have 6 characters.')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print(f'Student with code "{code}" doesnt exist.')
            continue
        break

    # Lấy thông tin theo mã học viên đã nhập
    st = getStudentByCode(code)

    print('Full Name:', st['FullName'])  # Hiển thị họ tên cũ
    fullName = st['FullName']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        while True:
            fullName = input('New Name: ')       
            # Khong duoc bo trong
            if fullName == '':
                print('Cannot leave empty')
                continue
            # Phai viet hoa
            if fullName.isupper() == False:
                print('Student Name has to be in capital letters')
                continue
            break      

    print('Birthday:', st['Birthday'])
    birthday = st['Birthday']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        while True:
            birthday = input('New birthday (dd/MM/yyyy): ') 
            # không được để trống
            if birthday == '':
                print('Cannot leave empty')
                continue
            # đúng định dang đd/MM/yyyy
            if checkDate(birthday) == None:
                print('Enter birhtday in format dd/mm/yyyy')
                continue
            break   

    print('Gender:', st['Sex'])
    sex = st['Sex']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        sex = input('New gender: ')
        while True:
            sex = input('Gender (0-female|1-male): ') 
            # chỉ là '0' hoặc '1'
            if sex not in ['0','1']:
                print('Enter gender: 1 - male, 0 - female')
                continue
            # Không được bỏ trống
            if sex == '':
                print('Cannot leave empty')
                continue
            break

    print('Address:', st['Address'])
    address = st['Address']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        address = input('New address: ')

    print('Phone number:', st['Phone'])
    phone = st['Phone']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        phone = input('New phone number: ')
        while True:
            phone = input('New phone number: ')          
            # Có thể không nhập
            if phone == '':
                break
            # Chỉ chứa số, độ dài 10 kí tự
            if phone.isdigit() == False:
                print('Phone number can only has numbers')
                continue
            # độ dài 10 kí tự
            if len(phone) != 10:
                print('Only 10 characters')
                continue
            break  

    print('Email:', st['Email'])
    email = st['Email']
    ans = input('Enter y/Y to edit: ')
    if ans.lower() == 'y':
        email = input('New email: ')
        while True:
            email = input('Email: ')        
            # Có thể không nhập
            if email == '':
                break
            # Có thể không nhập, nhưng nếu nhập thì phải đúng format Email (sử dụng regex Email để check)  
            if checkEmail(email) == False:
                print('Please enter correct format Email')
                continue
            break

    # Sửa thông tin bằng cách sửa trên list, sau đó ghi đè mode 'w' vào trong file .txt
    # Validate du lieu (da lam o tren)

    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            st['FullName'] = fullName
            st['Birthday'] = birthday
            st['Sex'] = int(sex)
            st['Address'] = address
            st['Phone'] = phone
            st['Email'] = email
            break
    writeStudents(sts)
    print(f'Edit student "{code}" succesfully !!!')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editStudentScreen()


def deleteStudentScreen():
    clearScreen()
    printHeader('Delete student')

    while True:
        code = input('Old student Code: ')
        if len(code) != 6:
            print('Student code has to have 6 characters.')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print(f'Does not exist.')
            continue
        break

    # Xóa
    sts = readStudents()
    idx = None
    for i, st in enumerate(sts):
        if st['Code'] == code:
            idx = i
            break
    sts.pop(idx)
    writeStudents(sts)
    print(f'Deleted !!!')

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteStudentScreen()


def searchStudentScreen():
    sts = readStudents()
    printStudents(sts)

    searchContent = input('Search info: ')
    if searchContent != '':
        stsFiltered = []
        for st in sts:
            # == Code, like FullName, like Email
            if st['Code'] == searchContent \
                or searchContent.lower() in st['FullName'].lower() \
                    or searchContent.lower() in st['Email'].lower():
                stsFiltered.append(st)
        printStudents(stsFiltered)

    ans = input('Enter y/Y to proceed: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchStudentScreen()


def printStudents(sts: list):
    clearScreen()
    printHeader('Student List')

    print('Student Code\tName\t\tBirthday\tGender\tAddress\tPhone number\t\tEmail')
    for st in sts:
        print(f"{st['Code']}\t{st['FullName']}\t{st['Birthday']}\t{st['Sex']}\t{st['Address']}\t{st['Phone']}\t{st['Email']}")
