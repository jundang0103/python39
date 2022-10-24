
import sungjukv7lib as sjv7

# 프로그램 주 실행부
while True:
    # 메뉴 표시 및 값 입력
    menu = sjv7.displayMenu()

    if menu == '1': sjv7.addSungJuk()
    elif menu == '2': sjv7.readSungJuk()
    elif menu == '3': sjv7.readOneSungJuk()
    elif menu == '4': sjv7.modifySungJuk()
    elif menu == '5': sjv7.removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다!')