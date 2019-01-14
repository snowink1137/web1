import random
import requests

## pick my lotto number
def pick_lotto():
    numbers = list(range(1,46))
    my_numbers = random.sample(numbers, 6)
    my_numbers.sort()
    return my_numbers



## get my lotto number
def get_lotto(round):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(round)
    response = requests.get(url)
    lotto_data = response.json()

    real_numbers = []
    for key in lotto_data:
        if 'drwt' in key:
            real_numbers.append(lotto_data[key])

    real_numbers.sort()
    bonus_number = lotto_data['bnusNo']
    return {'real_numbers' : real_numbers, 'bonus_number' : bonus_number}



def am_i_lucky(my_numbers, win_numbers):
    my_numbers = set(my_numbers)
    real_numbers = set(win_numbers['real_numbers'])
    bonus_number = win_numbers['bonus_number']

    if len(my_numbers.intersection(real_numbers)) == 6:
        result = '축하합니다. 1등 입니다!'
    elif len(my_numbers.intersection(real_numbers)) == 5:
        if bonus_number in my_numbers:
            result = '축하합니다. 2등 입니다!'
        else:
            result = '축하합니다. 3등 입니다!'  
    elif len(my_numbers.intersection(real_numbers)) == 4:
        result = '축하합니다. 4등 입니다!'
    elif len(my_numbers.intersection(real_numbers)) == 3:
        result = '축하합니다. 5등 입니다!'
    elif len(my_numbers.intersection(real_numbers)) == 2:
        result = '축하합니다. 6등 입니다!'
    elif len(my_numbers.intersection(real_numbers)) == 1:
        result = '축하합니다. 7등 입니다!'
    else:
        result = '당첨되지 않았습니다. 다음에 도전해주세요!'

    return result



# my_numbers = pick_lotto()
# win_numbers = get_lotto(837)


# print('내가 선택한 번호 :', my_numbers)
# print('실제 당첨 번호, 보너스 번호 :', win_numbers['real_numbers'], ',', win_numbers['bonus_number'])

# result = am_i_lucky(my_numbers, win_numbers)

# print('결과는...', result)