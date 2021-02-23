# 爬取指定网站、网页的表情包

import requests
import re #正则匹配
import time # 延时
import os # 文件和文件夹创建

# 爬取的实际地址
url = "https://www.zhihu.com/api/v4/questions/383126743/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&sort_by=default&platform=desktop"

payload={}
headers = {
  'authority': 'www.zhihu.com',
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
  'x-ab-param': 'pf_noti_entry_num=2;tp_dingyue_video=0;li_panswer_topic=0;tp_zrec=1;top_test_4_liguangyi=1;li_vip_verti_search=0;li_video_section=0;tp_topic_style=0;li_sp_mqbk=0;zr_slotpaidexp=1;pf_adjust=1;zr_expslotpaid=1;tp_contents=1;li_paid_answer_exp=0;li_edu_page=old;qap_question_author=0;qap_question_visitor= 0;se_ffzx_jushen1=0',
  'x-ab-pb': 'ClC0AFYMBwzgC1gBiAFqAQ8LtwDcCwEL7AoIAM8L1wsbALULRwBpAWsBiQyWC1ILQAGFAY0BmwtgC+QKxQD0CzQMdQy0Cj8AZwBDAE8BNwxMCxIoAAEBAAEAAAEAAAABAgsAAAMAAgIAAAEBAAAAAAAAAAABAAAAFQABAA==',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
  'x-requested-with': 'fetch',
  'x-zse-86': '2.0_aRFBHrHBSMtp20YyzwSqo6r02Txp28O8M8OBFrUqH9Sf',
  'x-zse-83': '3_2.0',
  'accept': '*/*',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.zhihu.com/question/383126743/answer/1110409545',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '_zap=d08b2a16-736d-4244-9ced-2d14e046d949; d_c0="AJDTDLfHChGPTmh-041dJiuzJgVygZUoKOA=|1585561218"; _ga=GA1.2.1382362438.1585561219; __utma=51854390.1382362438.1585561219.1591414883.1591414883.1; __utmv=51854390.100--|2=registration_date=20190801=1^3=entry_date=20190801=1; _xsrf=5G0WiVv6mJIMtxyoCPK0Wuh6ekDYv111; z_c0="2|1:0|10:1602680547|4:z_c0|92:Mi4xLWhOWUVRQUFBQUFBa05NTXQ4Y0tFU1lBQUFCZ0FsVk40a1IwWUFBTGNlWDZ1RElXWkRGU2NPUTZ1ekZzSS1oa3J3|c11edf5410071cc7041d9db4b5f5deda0b1b3c6c47fc01e2cfd50a5adc8f9e80"; tst=h; tshl=; q_c1=0854d121d0b84c3f8c2aee8ad6a91393|1613880582000|1586860301000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1613633528,1613639617,1613880540,1613919045; SESSIONID=uUnaikEghpsU9bavF8KFQCEuH3E10D4ydqGIJpqLqpz; JOID=Vl4UA0t8NE0TDUtuU3hC1Nu9PvlHC2YicmAiLDUQRjlHNC0NIj9BfncLTmhSiqqhB5q7Nf5TqQY6y_rxRw9d7cU=; osd=WlwUC0NwNk0bBUdsU3BK2Nm9NvFLCWYqemwgLD0YSjtHPCUBID9JdnsJTmBahqihD5K3N_5boQo4y_L5Sw1d5c0=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1613920710; KLBRSID=81978cf28cf03c58e07f705c156aa833|1613920879|1613919044; KLBRSID=81978cf28cf03c58e07f705c156aa833|1613921118|1613919044'
}
# 得到请求结果
response = requests.request("GET", url, headers=headers, data=payload)
# 设计匹配的正则表达式
pat = re.compile(r' src=\\"(.{84})\\" data-rawwidth')
# 通过正则进行匹配所有图片链接
urls = pat.findall(response.text)

# 保存图片
count=0
dir_name = 'F:\\Emoticon' # 设置文件夹路径
if not os.path.exists(dir_name):
  os.mkdir(dir_name)  # 创建文件夹
for url in urls:
  count=count+1
  file_name = str(count)  # 图片名字
  response = requests.request("GET", url, headers=headers, data=payload)  # 访问每个图片的网页，获取图片信息
  with open(dir_name+'\\'+file_name+'.jpg','wb') as f:
    f.write(response.content) # 将图片内容写入
  time.sleep(5) # 延时函数