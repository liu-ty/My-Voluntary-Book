import time
import pygame
import sys
from inputbox import*
from sprites import*
from functions import*

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('My Vocabulary Book')
status = True
clock = pygame.time.Clock()
mousestatus = 'up'
bg_list = ['My Vocabulary Book/imgs/bg1.png',
           'My Vocabulary  Book/imgs/bg2.png',
           'My Vocabulary  Book/imgs/bg1.png',
           'My Vocabulary  Book/imgs/bg3.png',
           'My Vocabulary  Book/imgs/默写背景.png',
           'My Vocabulary  Book/imgs/默写背景.png']
sb_list = [] #选择按钮列表
cb_list = []
for i in range(3):
    new_sb = Selectbutton(i,(50,400+i*60),(329,44))
    sb_list.append(new_sb)
for i in range(2):
    new_sb = Selectbutton(i+3,(600,300+i*100),(165,82))
    sb_list.append(new_sb)
for i in range(3):
    new_sb = Selectbutton(i+5,(80,400+i*60),(204,42))
    sb_list.append(new_sb)
new_sb = Selectbutton(8,(600,500),(72,37))
sb_list.append(new_sb)
new_sb = Selectbutton(9,(640,480),(85,85))
sb_list.append(new_sb)
main_status = 0
timer = Timer()
jr = Judgeresult()
sp = Showprinter()
#导入输入框
inputbox = Inputbox((50,300),(300,30),0,(220,220,220))
cursor = Cursor((0,0,0),2,[[51,301],[51,328]])
printer = Printer()
cursor_status = 0
inputcontent = ''
add_pos = 0
keystatus = 0
key_status = 0
addtext = Addtexts()
print_status = 0
translator = ''
word_list = []
content = ''
test_status = 0
testlist = []
testprinter = Testprinter()
test_index = 0
cntestlist = []
now_tick = 0
start_tick = 0
correcter = 0
ts = Test_score()
print_index = 0
printlist = []
translist = []

while status:
    mouse_pos = pygame.mouse.get_pos()#获取鼠标坐标
    background_img = pygame.transform.scale(pygame.image.load(bg_list[main_status]),(800,600))
    screen.blit(background_img,(0,0))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousestatus = 'down'
        if event.type == pygame.MOUSEBUTTONUP:
            mousestatus = 'up'

        #_______________________________________
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if main_status == 5:
                    if test_status == 1:
                        test_type = '小默写'
                    elif test_status == 2:
                        test_type = '大默写'
                    elif test_status == 3:
                        test_type = '百词默写'
                    create_result('默写成绩单',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),test_type,correcter,len(testlist)-correcter,t)
            if event.key == pygame.K_UP:
                if main_status == 3:
                    print_index -= 1
                    printlist,translist = change_wordlist(printlist,word_list,translist,print_index,'up')
                    print(printlist,translist)
            if event.key == pygame.K_DOWN:
                if main_status == 3:
                    print_index += 1
                    printlist,translist = change_wordlist(printlist,word_list,translist,print_index,'down')
                    print(printlist,translist)
            if event.key == pygame.K_BACKSPACE:
                if len(content_list) > 0:
                    content_list.pop()
                    inputcontent = updatetext(content_list)
            elif event.key == pygame.K_RETURN:
                inputtion = inputcontent
                content = ''.join(content_list)
                translator = translate(content)
                content_list.clear()
                inputcontent = updatetext(content_list)
                print_status = 1
            elif event.key == pygame.K_CAPSLOCK:
                keystatus = 1
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                key_status = 1
            else:
                inputcontent = get_content(keystatus,key_status,event)
            #add_pos = printer.printintext(inputcontent,screen)
            #print(content_list)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_CAPSLOCK:
                keystatus = 0
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                key_status = 0
        #___________________________________



    for sb in sb_list:
        if sb.id <= 2:
            if main_status == 0:
                sb.draw_img(screen)
                if mousestatus == 'down':
                    if sb.touching(mouse_pos,main_status) == True:
                        main_status = sb.id+1
                        mousestatus = 'up'
                        if sb.id == 0:
                            with open('wordlist.txt','r') as file:
                                word_list = divide_words()
                        if sb.id == 2:
                            print_index = 0
                            word_list = divide_words()
                            for x in range(8):
                                printlist.append('')
                                translist.append('')
                            printlist,translist = initlist(printlist,translist)
        elif 3 <= sb.id <= 4:
            if main_status == 1:
                sb.draw_img(screen)
                if mousestatus == 'down':
                    if sb.touching(mouse_pos,0) == True:
                        if sb.id == 3:
                            print_status = 0
                            if not content in word_list:
                                word_list.append(content)
                        if sb.id == 4:
                            main_status = 0
                            write_in(word_list)
        elif main_status == 2:
            word_list = divide_words()
            if len(word_list)<= 10:
                if sb.id == 5:
                    sb.draw_img(screen)
            elif 10 < len(word_list) <= 100:
                if 5<=sb.id<=6:
                    sb.draw_img(screen)
            elif len(word_list) > 100:
                if 5<=sb.id<=7:
                    sb.draw_img(screen)
            if mousestatus == 'down':
                if sb.touching(mouse_pos,0) == True:
                    if sb.id == 5:
                        test_status = 1
                    if sb.id == 6:
                        test_status = 2
                    if sb.id == 7:
                        test_status = 3
                    testlist = []
                    cntestlist = []
                    testlist = create_test(test_status,word_list)
                    test_index = 1
                    mousestatus = 'up'
                    for tl in testlist:
                        cntestlist.append(translate(tl))
                    start_tick = now_tick
                    correcter = 0
                    finish = 0
                    main_status = 4
        elif main_status == 4:
            if sb.id == 8:
                sb.draw_img(screen)
                if mousestatus == 'down':
                    if sb.touching(mouse_pos,0) == True:
                        main_status = 0
            testprinter.handling(cntestlist,test_index-1)
            testprinter.draw(screen)
            if print_status == 1:
                finish += 1
                print_status = 0
                jr.drawstatus = 60
                result = judge(content,testlist[test_index-1])
                if result == '正确':
                    correcter+=1


            if jr.drawstatus > 0:
                jr.draw(screen,content,testlist[test_index-1],result,0)
            elif jr.drawstatus == 0:
                jr.draw(screen,content,testlist[test_index-1],result,1)
                test_index += 1
                if test_index-1 == len(testlist):
                    test_index-=1
                    ts.calculate(correcter/finish,now_tick-start_tick,len(testlist))
                    main_status = 5
                    t = str(round((now_tick-start_tick)/16,1))+'s'
            else:
                pass
            testprinter.handling_ui(test_index,len(testlist),correcter,start_tick,now_tick,finish)
            testprinter.draw_ui(screen)
        elif main_status == 5:
            if sb.id == 8:
                sb.draw_img(screen)
                if mousestatus == 'down':
                    if sb.touching(mouse_pos,0) == True:
                        main_status = 0
            testprinter.draw_ui(screen)
            ts.draw(screen)

        elif main_status == 3:
            if sb.id == 9:
                sb.draw_img(screen)
                if mousestatus == 'down':
                    if sb.touching(mouse_pos,0) == True:
                        main_status = 0
                        mousestatus = 'up'
            sp.draw(screen,printlist,translist)

    if main_status == 1:
        if print_status == 1:
            addtext.print_text(screen,content,translator)
        else:
            pass

    if (main_status == 1) or (main_status == 4):
        inputbox.draw_box(screen)
        cursor.draw_cursor(screen,cursor_status,add_pos)
        add_pos = printer.printintext(inputcontent,screen)



    cursor_status+=1
    if cursor_status >= 12:
        cursor_status = -12
    timer.print_time(screen)
    clock.tick(16)
    now_tick += 1
    pygame.display.update()
