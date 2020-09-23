import http.client
import hashlib
import urllib
import random
import json
import matplotlib.pyplot as plt

def get_new_words():
    pass
    #return [english,chinese]

def write_in(words):
    text = ''
    for word in words:
        text = text + word + ','
    with open('wordlist.txt','w') as file:
        file.write(text)

def divide_words():
    with open('wordlist.txt','r') as file:
        words = file.read()
        r_list = []
        content = ''
        for r in words:
            if r == ',':
                r_list.append(content)
                content = ''
            else:
                content = content + r
        return r_list

def translate(word):
    appid = '20200918000568741'  # 填写你的appid
    secretKey = 'qerlhrooD83U_V6t9I3x'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q= word
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print('request once')
        return result['trans_result'][0]['dst']

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()


def create_test(status,randlist):
    rtlist = []
    random.shuffle(randlist)
    if status == 1:
        if len(randlist) < 10:
            rtlist = randlist
        else:
            rtlist = randlist[:10]
    elif status == 2:
        if len(randlist) < 50:
            rtlist = randlist
        else:
            rtlist = randlist[:50]
    else:
        rtlist = randlist[:100]
    return rtlist

def judge(inword,answer):
    if inword == answer:
        return '正确'
    else:
        return '错误'

def create_result(name,time,types,a,b,timer):
    ab = [a,b]
    title = str(name)+'\n'+str(time)+'\n'+str(types)+'\n'+'用时:'+str(timer)
    plt.rcParams['font.sans-serif']='SimHei'
    plt.figure(figsize=(6,6))
    explode=[0.04,0.01]
    label=['正确','错误']
    plt.pie(ab,explode=explode,labels=label,autopct='%1.1f%%')
    plt.title(title)
    plt.show()

def change_wordlist(relist,wordlist,translist,index,status):
    if len(wordlist) <= 8:
        return(relist,translist)
    else:
        flist = relist
        slist = translist
        if status == 'up':
            flist.insert(0,wordlist[index%len(wordlist)])
            flist.pop()
            slist.insert(0,translate(wordlist[index%len(wordlist)]))
            slist.pop()
        elif status == 'down':
            flist.append(wordlist[(index+8)%len(wordlist)])
            flist.pop(0)
            slist.append(translate(wordlist[(index+8)%len(wordlist)]))
            slist.pop(0)
        else:
            pass
        return flist,slist

def initlist(relist,translist):
    words = divide_words()
    flist = relist
    slist = translist
    if len(words) <= 8:
        for i in range(len(words)):
            flist[i] = words[i]
            slist[i] = translate(words[i])
    elif len(words) > 8:
        for i in range(8):
            flist[i] = words[i]
            slist[i] = translate(words[i])
    else:
        pass
    return flist,slist
