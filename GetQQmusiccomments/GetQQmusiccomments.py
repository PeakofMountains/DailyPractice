''' ##########################################################
# @Author: PeakofMountains
# @Version: 1.1
# Date: 2020/05/15
# Description: To get comments of songs in QQmusic
# SolvedProblems:
    1. 网页版QQ音乐采用JavaScript框架
    2. 对爬取数据进行文件储存
    3. 对储存文本进行编号
    4. 对储存文本中的指定字符进行删除
    5. 对文件的相应操作
    6. 使用Postman自动生成应对json的访问代码
# Future goals:
    1. 添加爬取的数据去重功能
    2. 添加根据用户的输入爬取指定歌曲的评论
    3. 添加对评论点赞数的过滤
    4. 添加GUI界面方面用户使用
    5. 添加对数据中字符表情的处理

##########################################################'''

import requests     # 获取html
import re           # 正则表达式使用
import os           # 文件的操作


def getcomments(html, list):
    try:
        # 将匹配的message存储在messages数组中
        # 正则表达式进行指定数据获取
        messages=re.findall(r'"rootcommentcontent" : (\"\S*\")', html)
        for message in messages:    # 逐个处理messages中的message
            list.append(message)    # 将每个内容追加到原来的数组后端
    except:
        print("")


def write_comments(list, root):
    count = 0                                                   # 对数据进行编号保存
    path = root + "LastReunion的热评.txt"                        # 指定文件名
    for comment in list:
        try:
            # 对数据中指定字符进行删除
            compile = re.compile(r'\[em\]\S*\[/em\]', re.S)     # 删除表情
            comment = re.sub(compile, '', comment)
            compile = re.compile(r'\\n')                        # 删除'\n'符
            comment = re.sub(compile, '', comment)
            compile = re.compile(r'\\')                         # 删除'\'符
            comment = re.sub(compile, '', comment)

            count=count+1
            if not os.path.exists(root):    # 如果没有相应文件夹，创建文件夹
                os.mkdir(root)
            # 向文件中进行写入
            with open(path, 'a') as f:      # 这里的'a'意思是指定追加写操作
                    f.write(f'{count}'+': '+comment+'\n')   # 对写入文本进行编号和换行处理
                    print('正在写入文件'+comment+'\n')    # 向用户反馈当前写入状态

        except:
                print("写入文件出现异常\n")
    f.close()


def main():
    # 这段代码是通过Postman生成的,用来访问json类型数据
    url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=1343863661&g_tk=2043415418&loginUin=2793213702&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=224897331&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010"

    payload = {}
    headers = {
        'authority': 'c.y.qq.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'origin': 'https://y.qq.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://y.qq.com/n/yqq/song/001WnNHk3ujgrz.html',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'pgv_pvi=393520128; ptui_loginuin=2793213702; RK=GWwN4Gu33K; ptcz=ed948f93478a4609b02f0b2658558b3f033129d5be73af12c0eef8deba92aaf7; pgv_pvid=4503517525; lskey=00010000b7cbd00151c12e42f42b2ac0943f897418a31946362ca88f714916e16425f470299c8ec04a954a96; o_cookie=2793213702; pac_uid=1_2793213702; ts_refer=www.baidu.com/link; ts_uid=1123423425; psrf_qqopenid=A7E87EB5210EBBD365E4878F06856A4F; psrf_qqaccess_token=5E2F291275CA9E65D67B83B39A63EEBC; psrf_qqrefresh_token=6C6AB7F84B66A8A0B4173F2F237D47CC; psrf_qqunionid=A5BFB107A42821289F9997B76D07B3CA; yq_index=0; tvfe_boss_uuid=9c6184ed5d68eb6c; _qpsvr_localtk=1589525017270; yqq_stat=0; pgv_si=s5139066880; pgv_info=ssid=s4801050000; qqmusic_key=Q_H_L_2ekI_w50eSEGk3fR7BDvyY-HkPqrayx4R748-uGrvLdR-SHz1KYIEij0W7NF-q8; psrf_access_token_expiresAt=1597305322; qm_keyst=Q_H_L_2ekI_w50eSEGk3fR7BDvyY-HkPqrayx4R748-uGrvLdR-SHz1KYIEij0W7NF-q8; psrf_musickey_createtime=1589529322; player_exist=1; qqmusic_fromtag=66; userAction=1; yplayer_open=0; uin=o2793213702; skey=@fAWJLCRZ2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    html = response.text            # 这里直接用response.text得到从request得来的html数据，不用encode('utf8')
    List = []                       # 存储数据的数组
    root = "D://QQmusiccomments//"  # 创建文件夹的目录
    getcomments(html, List)         # 从url得到html
    write_comments(List, root)      # 写入文件
    print("完成文件写入过程，在指定文件夹内查看文件")



main()
