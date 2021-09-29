# pip install pyautogui
# upbit에서 특정 코인을 매수/매도 할 수 있는 상태에서 필요한 버튼 좌표 값으로 자동 주문하는 파이썬 프로그램
#
#   https://pyautogui.readthedocs.io/en/latest/

import pyautogui
import time

pyautogui.doubleClick() 
 
price   = [993, 584]  # 가격 입력 창
qty     = [1085, 640]  # 수량 입력 창
order   = [939, 906]  # 주문 버튼
confirm = [719, 634]  # 주문 확인 버튼
done    = [715, 473]  # 닫기 버튼

order_price = 48000000
order_qty = 0.001

print('start order')

# input price
pyautogui.moveTo(price[0], price[1])
pyautogui.doubleClick() # 현재가가 있으므로 double click하여 모두 선택
pyautogui.typewrite(str(order_price), interval=0.1)

# input qty
pyautogui.moveTo(qty[0], qty[1])
pyautogui.doubleClick() # 현재가가 있으므로 double click하여 모두 선택
pyautogui.typewrite(str(order_qty), interval=0.1)

# press order
pyautogui.click(order[0], order[1])
time.sleep(2)

# confirm
pyautogui.click(confirm[0], confirm[1])
time.sleep(2)

# done
pyautogui.click(done[0], done[1])
time.sleep(2)

print('done')
