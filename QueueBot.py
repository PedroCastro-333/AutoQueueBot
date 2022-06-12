import pyautogui
from time import sleep

from pyscreeze import center


# !VARIAVEIS / COLETA DE DADOS
print("*"*40)
print("Qual campeão quer banir?")
print("*"*40)
champ_ban = input(': ').lower()

print("*"*40)
print('Com qual campeão quer jogar?')
print("*"*40)
champ_pick = input(': ').lower()

print("*"*40)
print("Dê uma segunda opção de pick caso o primeiro esteja banido ou pickado.")
print("*"*40)
champ_pick_2 = input(': ').lower()

print("*"*40)
print("Dê uma terceira opção de pick caso os anteriores estejam banidos ou pickados.")
print("*"*40)
champ_pick_3 = input(': ').lower()



# !FUNÇÕES
def click(x, y):
    pyautogui.moveTo(x, y, duration=.2)
    pyautogui.click()


def banir():
    banir = pyautogui.locateOnScreen('./assets/banpick/bana.png')
    if banir != None:
        procuar = pyautogui.locateOnScreen('./assets/banpick/procurar1.png', confidence=.7)
        click(procuar.left+8, procuar.top+8)
        pyautogui.write(champ_ban)
        sleep(1)
        ban = pyautogui.locateOnScreen(f'./assets/banpick/topBan.png', confidence=.6)
        click(ban.left+20, ban.top+40)
        sleep(1)
        conf_ban = pyautogui.locateOnScreen('./assets/banpick/conf_ban.png')
        if conf_ban != None:
            click(conf_ban.left+8, conf_ban.top+8)
            print('Banindo ' + champ_ban)


def pickar():
    pickar = pyautogui.locateOnScreen('./assets/banpick/escolha.png')
    if pickar != None:
        procuar = pyautogui.locateOnScreen('./assets/banpick/procurar1.png', confidence=.7)
        click(procuar.left+8, procuar.top+8)
        pyautogui.write(champ_pick)
        sleep(1)
        pick = pyautogui.locateOnScreen(f'./assets/banpick/topPick.png', confidence=.6)
        click(pick.left+20, pick.top+40)
        sleep(1)
        conf_pick = pyautogui.locateOnScreen('./assets/banpick/pick_conf.png')
        if conf_pick != None:
            click(conf_pick.left+8, conf_pick.top+8)
            print('Selecionando ' + champ_pick)
            return
        else:
            click(procuar.left+8, procuar.top+8)
            pyautogui.press("del", 15)
            pyautogui.write(champ_pick_2)
            click(pick.left+20, pick.top+40)
            sleep(1)
            conf_pick = pyautogui.locateOnScreen('./assets/banpick/pick_conf.png')
            if conf_pick != None:
                click(conf_pick.left+8, conf_pick.top+8)
                print('Selecionando ' + champ_pick_2)
                return
            else:
                click(procuar.left+8, procuar.top+8)
                pyautogui.press("del", 15)
                pyautogui.write(champ_pick_3)
                click(pick.left+20, pick.top+40)
                sleep(1)
                conf_pick = pyautogui.locateOnScreen('./assets/banpick/pick_conf.png')
                if conf_pick != None:
                    click(conf_pick.left+8, conf_pick.top+8)
                    print('Selecionando ' + champ_pick_3)
                    return




def check_screen():
    button_pos = pyautogui.locateOnScreen('./assets/accept/tem_fila.png', confidence=.7)

    if button_pos != None:
        click(button_pos.left+8, button_pos.top+8)
        print('Partida encontrada!')
        return True
    return False


def main():
    print("Clique para procurar partida!")
    while True:
        if check_screen():
            print('Partida aceita!')
        sleep(2)
        banir()
        sleep(2)
        pickar()


try:
    while True:
        main()

except KeyboardInterrupt:
    print('O bot foi parado pelo usuário')
    print('\n')
c
