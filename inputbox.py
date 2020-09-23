import pygame

class Inputbox():

    def __init__(self, position, rect, width, color):
        # color 为RGB形式，如（255，255，255）
        self.color = color
        self.rect = rect
        self.position = position
        self.width = width

    def draw_box(self, screen):
        pygame.draw.rect(screen, self.color, [self.position, self.rect], self.width)


class Cursor():

    def __init__(self, color, width, position):
        # position 参数为列表，包含起点，终点
        self.color = color
        self.width = width
        self.start_pos = position[0]
        self.end_pos = position[1]



    def draw_cursor(self, screen, status, addpos):
        if status > 0:
            pygame.draw.line(screen, self.color, [self.start_pos[0]+addpos,self.start_pos[1]], [self.end_pos[0]+addpos,self.end_pos[1]], self.width)


class Printer():

    def __init__(self):
        self.fonts = pygame.font.Font('pygame输入框/Verdana.ttf',24)
        self.pos = (51,301)

    def printintext(self, content, screen):
        text = self.fonts.render(content, 8, (0,0,0))
        text_rect = text.get_rect()
        screen.blit(text, self.pos)
        return text_rect.width

content_list = []
key_dict = {pygame.K_a: 'a',pygame.K_b:'b',pygame.K_c:'c',pygame.K_d:'d',pygame.K_e:'e',pygame.K_f:'f',pygame.K_g:'g',pygame.K_h:'h',pygame.K_i:'i',pygame.K_j:'j',pygame.K_k: 'k',pygame.K_l:'l',pygame.K_m:'m',pygame.K_n:'n',
pygame.K_o:'o',pygame.K_p:'p',pygame.K_q:'q',pygame.K_r:'r',pygame.K_s:'s',pygame.K_t:'t',pygame.K_u:'u',pygame.K_v:'v',pygame.K_w:'w',pygame.K_x:'x',pygame.K_y:'y',pygame.K_z:'z',pygame.K_SPACE:' ',pygame.K_COMMA:',',pygame.K_PERIOD:'.',
pygame.K_0:'0',pygame.K_1:'1',pygame.K_2:'2',pygame.K_3:'3',pygame.K_4:'4',pygame.K_5:'5',pygame.K_6:'6',pygame.K_7:'7',pygame.K_8:'8',pygame.K_9:'9',
pygame.K_TAB:'    ',pygame.K_SLASH:'/',pygame.K_SEMICOLON:';',pygame.K_EQUALS:'=',pygame.K_MINUS:'-',pygame.K_QUOTE:'‘',pygame.K_LEFTBRACKET:'[',pygame.K_RIGHTBRACKET:']'}
key_dict_caps = {pygame.K_a: 'A',pygame.K_b:'B',pygame.K_c:'C',pygame.K_d:'D',pygame.K_e:'E',pygame.K_f:'F',pygame.K_g:'G',pygame.K_h:'H',pygame.K_i:'I',pygame.K_j:'J',pygame.K_k: 'K',pygame.K_l:'L',pygame.K_m:'M',pygame.K_n:'N',
pygame.K_o:'O',pygame.K_p:'P',pygame.K_q:'Q',pygame.K_r:'R',pygame.K_s:'S',pygame.K_t:'T',pygame.K_u:'U',pygame.K_v:'V',pygame.K_w:'W',pygame.K_x:'X',pygame.K_y:'Y',pygame.K_z:'Z',pygame.K_SPACE:' ',pygame.K_COMMA:',',pygame.K_PERIOD:'.',
pygame.K_0:'0',pygame.K_1:'1',pygame.K_2:'2',pygame.K_3:'3',pygame.K_4:'4',pygame.K_5:'5',pygame.K_6:'6',pygame.K_7:'7',pygame.K_8:'8',pygame.K_9:'9',
pygame.K_TAB:'    ',pygame.K_SLASH:'/',pygame.K_SEMICOLON:';',pygame.K_EQUALS:'=',pygame.K_MINUS:'-',pygame.K_QUOTE:'‘',pygame.K_LEFTBRACKET:'[',pygame.K_RIGHTBRACKET:']'}
key_special = {pygame.K_0:')',pygame.K_1:'!',pygame.K_2:'@',pygame.K_3:'#',pygame.K_4:'$',pygame.K_5:'%',pygame.K_6:'^',pygame.K_7:'&',pygame.K_8:'*',pygame.K_9:'(',pygame.K_TAB:'    ',pygame.K_SLASH:'?',pygame.K_SEMICOLON:':',pygame.K_EQUALS:'+',pygame.K_MINUS:'_'
,pygame.K_COMMA:'<',pygame.K_PERIOD:'>',pygame.K_QUOTE:'"',pygame.K_LEFTBRACKET:'{',pygame.K_RIGHTBRACKET:'}'}
def get_content(keystatus,key_status,event):
    if key_status == 1:
        for keyname in key_special:
            if event.key == keyname:
                content_list.append(key_special[keyname])
    else:
        if keystatus == 1:
            for keyname in key_dict_caps:
                if event.key == keyname:
                    content_list.append(key_dict_caps[keyname])
        else:
            for keyname in key_dict:
                if event.key == keyname:
                    content_list.append(key_dict[keyname])


    content = updatetext(content_list)

    return content



def updatetext(list):
    text = ''
    for i in list:
        text = text + i
    return text





