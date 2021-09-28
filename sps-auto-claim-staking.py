# pip install pip install pyautogui
# steemmonster.com에서 sps를 자동으로 claim하고 staking하는 프로그램
# This is automatic claim and staking prgrom for sps in Splinterland or steemmonsters
# 
#   

import pyautogui
import time


# parameters  본인의 환경에 맞는 값으로 
num_sps_staked = 10000 # SPS 스테이킹 수
apr             = 80 # 현재 APR 여유있게 현재보다는 낮은 값
harvest_interval= 10 # 자동 claim 주기, based on min

claim           = [480, 523]   # claim 버튼 위치
stake           = [492, 649]   # stake 버튼 위치
input_num_stake = [511, 535]  # stake할 수량을 넣는 곳의 위치
inside_stake    = [617, 598]  # 수량을 넣은 후 누를 stake 버튼 위치
# end of parameters

sps_per_day = int(num_sps_staked * apr / 100 / 365)
num_stake = ("%4.3f")%(sps_per_day / 1440 * harvest_interval)
print('스테이킹 수량    %8d\n일 SPS 채굴량 %8d\nStake할 수량 %12s'%(num_sps_staked, sps_per_day, num_stake))

print('start')

while(1) :
    print('press claim')
    pyautogui.click(claim[0], claim[1])
    time.sleep(10)

    print('press stake')
    pyautogui.click(stake[0], stake[1])
    time.sleep(2)

    # input #sps to staking
    pyautogui.moveTo(input_num_stake[0], input_num_stake[1])
    pyautogui.click()
    pyautogui.typewrite(num_stake, interval=0.1)

    #press STAKE
    pyautogui.click(617, 598)
    time.sleep(2)
    #press 확인
    pyautogui.typewrite('\n', interval=0.1)

    time.sleep(harvest_interval*60)
