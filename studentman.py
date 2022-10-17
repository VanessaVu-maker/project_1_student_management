# Nghiệp vụ quản lý Học viên
from utils import clearScreen, printMenu, printHeader, checkEmail, checkDate
from dbprovider import writeStudent, writeStudents, readStudents, getStudentByCode, checkExistsStudent


def studentMenuScreen():
    clearScreen()
    printHeader('QUẢN LÝ HỌC VIÊN')

    funcs = [
        '1. Thêm HỌC VIÊN',
        '2. Sửa HỌC VIÊN',
        '3. Xoá HỌC VIÊN',
        '4. Danh sách HỌC VIÊN',
        '0. Trở về màn hình CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI'
    ]
    printMenu(funcs)

    cmd = None  # mã lệnh người dùng chọn, ban đầu chưa phải lệnh nào cả
    while cmd not in ['1', '2', '3', '4', '0']:
        cmd = input('Chọn chức năng: ')

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
    printHeader('THÊM HỌC VIÊN')

    # Nhập dữ liệu từ bàn phím
    # Validate dữ liệu nhập từ bàn phím - ma hoc vien
    while True:
        # 6 ký tự
        code = input('Mã HV: ')
        if len(code) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        # 2 ký tự đầu phải là 'PY'
        if code.startswith('PY') == False:
            print('2 ký tự đầu phải là "PY".')
            continue
        # không tồn tại trong DB
        isExists = checkExistsStudent(code)
        if isExists == True:
            print(f'Mã HV "{code}" đã được sử dụng.')
            continue
        # phai viet hoa
        if code.isupper() == False:
            print('Mã học viên phải viết hoa')
            continue
        # Khong duoc bo trong
        if code == '':
            print('Không được để trống mã HV')
            continue
        break    
    
    # Validate dữ liệu nhập từ bàn phím - ten hoc vien
    while True:
        fullName = input('Họ tên:')    
        # Phai viet hoa
        if fullName.isupper() == False:
            print('Tên học viên phải viết hoa')
            continue
        # Khong duoc bo trong
        if fullName == '':
            print('Không được để trống tên học viên')
            continue
        break    

    # Validate dữ liệu nhập từ bàn phím - ngay sinh

    while True:
        birthday = input('Ngày sinh (dd/MM/yyyy): ') 
        # đúng định dang đd/MM/yyyy
        if checkDate(birthday) == None:
            print('Hãy nhập ngày sinh đúng với format dd/mm/yyyy')
            continue
        # không được để trống
        if birthday == '':
            print('Không được để trống ngày sinh')
            continue
        break   

    # Validate dữ liệu nhập từ bàn phím - gioi tinh

    while True:
        sex = input('Giới tính (0-nữ|1-nam): ') 
        # chỉ là '0' hoặc '1'
        if sex not in ['0','1']:
            print('Hãy nhập giới tính: 1 - Nam, 0 - nữ')
            continue
         # Không được bỏ trống
        if sex == '':
            print('Không được bỏ trống giới tính')
            continue
        break

    address = input('Địa chỉ: ')

    # Validate dữ liệu nhập từ bàn phím - SDT

    while True:
        phone = input('SĐT: ')          
        # Có thể không nhập
        if phone == '':
            break
        # Chỉ chứa số, độ dài 10 kí tự
        if phone.isdigit() == False:
            print('SĐT chỉ được chứa số')
            continue
        # độ dài 10 kí tự
        if len(phone) != 10:
            print(' Số điện thoại phải chứa đúng 10 kí tự')
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
            print('Yêu cầu nhập đúng format Email')
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
    print(f'Thêm học viên có mã "{code}" thành công !!!')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        addStudentScreen()


def editStudentScreen():
    clearScreen()
    printHeader('CHỈNH SỬA THÔNG TIN HỌC VIÊN')

    while True:
        code = input('Mã HV cần sửa: ')
        # ko bo trong
        if len(code) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print(f'HV có mã "{code}" không tồn tại.')
            continue
        break

    # Lấy thông tin theo mã học viên đã nhập
    st = getStudentByCode(code)

    print('Họ tên:', st['FullName'])  # Hiển thị họ tên cũ
    fullName = st['FullName']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        while True:
            fullName = input('Họ tên mới: ')       
            # Khong duoc bo trong
            if fullName == '':
                print('Không được để trống tên học viên')
                continue
            # Phai viet hoa
            if fullName.isupper() == False:
                print('Tên học viên phải viết hoa')
                continue
            break      

    print('Ngày sinh:', st['Birthday'])
    birthday = st['Birthday']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        while True:
            birthday = input('Ngày sinh mới (dd/MM/yyyy): ') 
            # không được để trống
            if birthday == '':
                print('Không được để trống ngày sinh')
                continue
            # đúng định dang đd/MM/yyyy
            if checkDate(birthday) == None:
                print('Hãy nhập ngày sinh đúng với format dd/mm/yyyy')
                continue
            break   

    print('Giới tính:', st['Sex'])
    sex = st['Sex']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        sex = input('Giới tính mới: ')
        while True:
            sex = input('Giới tính (0-nữ|1-nam): ') 
            # chỉ là '0' hoặc '1'
            if sex not in ['0','1']:
                print('Hãy nhập giới tính: 1 - Nam, 0 - nữ')
                continue
            # Không được bỏ trống
            if sex == '':
                print('Không được bỏ trống giới tính')
                continue
            break

    print('Địa chỉ:', st['Address'])
    address = st['Address']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        address = input('Địa chỉ mới: ')

    print('SĐT:', st['Phone'])
    phone = st['Phone']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        phone = input('SĐT mới: ')
        while True:
            phone = input('SĐT: ')          
            # Có thể không nhập
            if phone == '':
                break
            # Chỉ chứa số, độ dài 10 kí tự
            if phone.isdigit() == False:
                print('SĐT chỉ được chứa số')
                continue
            # độ dài 10 kí tự
            if len(phone) != 10:
                print(' Số điện thoại phải chứa đúng 10 kí tự')
                continue
            break  

    print('Email:', st['Email'])
    email = st['Email']
    ans = input('Nhập y/Y để sửa: ')
    if ans.lower() == 'y':
        email = input('Email mới: ')
        while True:
            email = input('Email: ')        
            # Có thể không nhập
            if email == '':
                break
            # Có thể không nhập, nhưng nếu nhập thì phải đúng format Email (sử dụng regex Email để check)  
            if checkEmail(email) == False:
                print('Yêu cầu nhập đúng format Email')
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
    print(f'Chỉnh sửa học viên có mã "{code}" thành công !!!')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        editStudentScreen()


def deleteStudentScreen():
    clearScreen()
    printHeader('XÓA HỌC VIÊN')

    while True:
        code = input('Mã HV cần xóa: ')
        if len(code) != 6:
            print('Mã HV phải bao gồm 6 ký tự.')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print(f'HV có mã "{code}" không tồn tại.')
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
    print(f'Xóa học viên có mã "{code}" thành công !!!')

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        deleteStudentScreen()


def searchStudentScreen():
    sts = readStudents()
    printStudents(sts)

    searchContent = input('Nội dung tìm kiếm: ')
    if searchContent != '':
        stsFiltered = []
        for st in sts:
            # == Code, like FullName, like Email
            if st['Code'] == searchContent \
                or searchContent.lower() in st['FullName'].lower() \
                    or searchContent.lower() in st['Email'].lower():
                stsFiltered.append(st)
        printStudents(stsFiltered)

    ans = input('Nhập y/Y để tiếp tục: ')
    if ans.lower() == 'y':
        # Quay lại nhập tiếp, call chính nó
        searchStudentScreen()


def printStudents(sts: list):
    clearScreen()
    printHeader('DANH SÁCH HỌC VIÊN')

    print('Mã HV\tHọ tên\t\tNgày sinh\tGiới\tĐịa chỉ\tSĐT\t\tEmail')
    for st in sts:
        print(f"{st['Code']}\t{st['FullName']}\t{st['Birthday']}\t{st['Sex']}\t{st['Address']}\t{st['Phone']}\t{st['Email']}")
