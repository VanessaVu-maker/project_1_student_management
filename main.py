# Main module của chương trình

# Nháp để call các function cho việc testing
import cmd
from unittest import result
from dbprovider import writeStudent, writeStudents , readStudents
from dbprovider import writeSubject,writeSubjects, readSubjects
from dbprovider import writeScore,writeScores,readScores
from utils import printMenu, clearScreen, printHeader
from studentman import studentMenuScreen, addStudentScreen
from subjectman import subjectMenuScreen, addSubjectScreen
from scoreman import scoreMenuScreen, addScoreScreen


# Màn hình Menu chính của chương trình
def mainMenuScreen():
    clearScreen()
    printHeader('CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI')

    funcs = [
        '1. Quản lý Học viên',
        '2. Quản lý Môn Học',
        '3. Quản lý Điểm thi',
        '0. Thoát'
    ]
    printMenu(funcs)

    cmd = None # mã lệnh người dùng chọn, ban đầu chưa phải lệnh nào cả
    while cmd not in ['1', '2', '3', '0']:
        cmd = input('Chọn chức năng: ')

    if cmd == '1':
        # Chuyển sang màn hình QL Học viên
        studentMenuScreen()
        # Quay lại màn hình Menu chính (Gọi chính nó)
        mainMenuScreen()
    elif cmd == '2':
        # Chuyển sang màn hình QL Môn học
        subjectMenuScreen()
        mainMenuScreen()
        pass
    elif cmd == '3':
        # Chuyển sang màn hình QL Điểm thi
        scoreMenuScreen()
        mainMenuScreen()
        pass
    elif cmd == '0':
        # Thoát chương trình
        print('Kết thúc chương trình. Hẹn gặp lại !!!')
        exit()

if __name__ == '__main__':
    mainMenuScreen()




