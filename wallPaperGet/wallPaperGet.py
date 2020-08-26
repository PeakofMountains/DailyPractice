'''从知乎上爬取图片(壁纸),目前只处理了图片重复的问题，未能解决剔除其他回答中的无关图片的问题'''
import requests
import re
import os
import traceback
import time


def getUrlList(list, html):
    try:
        findJpg = re.findall(r'https://pic[A-Za-z0-9]{1}.zhimg.com/v2-[A-Za-z0-9]+_r.jpg\?source=1940ef5c', html)
        for i in range(len(findJpg)):
            if i > 0:
                if findJpg[i] != findJpg[i-1]:
                    list.append(findJpg[i])

            else:
                list.append(findJpg[0])
    except:
        traceback.print_exc()
        print("")


def storagePictures(list, path):
    count1 = 1
    for i in list:
        try:
            # print(i)
            filename = (path+"//{}.png".format(count1))

            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(filename):
                r = requests.get("{}".format(i))
                time.sleep(6)
                with open(filename, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    count1 = count1 + 1
                    print("\rDownload Success: {} 张".format(count1), end="")

        except:
            traceback.print_exc()
            continue


def main():
    url = "https://www.zhihu.com/api/v4/questions/378523181/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=&limit=3&sort_by=default&platform=desktop"
    payload = {}
    headers = {
        'authority': 'www.zhihu.com',
        'x-ab-param': 'li_topics_search=0;se_searchwiki=0;tp_topic_tab_new=0-0-0;zr_training_boost=false;li_yxzl_new_style_a=1;top_root=0;li_edu_page=old;li_pl_xj=0;tp_dingyue_video=1;tp_clubhyb=0;se_auth_src2=1;top_quality=0;pf_profile2_tab=0;ug_newtag=1;pf_foltopic_usernum=50;se_recommend=0;se_return_1=0;se_auth_src=0;tp_fenqu_wei=1;ls_video_commercial=0;zr_topic_rpc=0;se_college=default;se_guess=0;tp_sft=a;tp_topic_tab=0;pf_creator_card=1;li_ebook_gen_search=2;zr_km_answer=open_cvr;zr_expslotpaid=1;pf_newguide_vertical=0;li_car_meta=0;li_svip_cardshow=1;li_svip_tab_search=1;zr_intervene=2;se_topicfeed=0;pf_adjust=1;qap_question_author=0;zr_slot_training=2;se_adsrank=4;se_usercard=0;tp_contents=1;top_universalebook=1;se_hi_trunc=0;qap_question_visitor= 0;zr_training_first=false;tp_discover=1;pf_fuceng=1;zw_sameq_sorce=999;zr_rec_answer_cp=open;tp_zrec=1;top_v_album=1;top_test_4_liguangyi=1;qap_labeltype=1;zr_sim3=0;se_colorfultab=1;ug_follow_topic_1=2;ls_recommend_test=4;tp_header_style=1;tsp_hotlist_ui=3;li_sp_mqbk=0;se_col_boost=1;se_merge=0;li_vip_verti_search=0;li_video_section=0;tp_meta_card=0;se_entity22=1;tp_m_intro_re_topic=1;li_paid_answer_exp=0;zr_slotpaidexp=8;tp_topic_style=0;soc_notification=1;se_whitelist=1;se_club_ui=0;top_ebook=0;pf_noti_entry_num=2;se_sug_term=0;li_catalog_card=1;li_panswer_topic=0;zr_search_paid=1;se_ffzx_jushen1=0;li_viptab_name=0;li_answer_card=0',
        'x-zse-86': '1.0_aL28bTUBkLxpQMYBBTN0Nge8UqSfghNBMXSqbQXBnGYf',
        'x-ab-pb': 'CiQPC+cKJQrjCicK1woMC5wKAQveChILmwrtCuQK6wq0CuwKEAsSEgACBQAGAAABAAABAAAAAQAAAA==',
        'x-requested-with': 'fetch',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-zse-83': '3_2.0',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.zhihu.com/question/378523181/answer/1154462214',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_zap=d08b2a16-736d-4244-9ced-2d14e046d949; d_c0="AJDTDLfHChGPTmh-041dJiuzJgVygZUoKOA=|1585561218"; _ga=GA1.2.1382362438.1585561219; z_c0="2|1:0|10:1586858813|4:z_c0|92:Mi4xLWhOWUVRQUFBQUFBa05NTXQ4Y0tFU1lBQUFCZ0FsVk5QZG1DWHdDdWlBSUo4c3hZYVY5UXFhZlM1dzA3WXVIdjhn|7941ac5c5176ae75a8656856ab8243623ecb7360e68a765706cfbc135535a53e"; tshl=; __utma=51854390.1382362438.1585561219.1591414883.1591414883.1; __utmz=51854390.1591414883.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20190801=1^3=entry_date=20190801=1; _xsrf=5G0WiVv6mJIMtxyoCPK0Wuh6ekDYv111; q_c1=0854d121d0b84c3f8c2aee8ad6a91393|1597656252000|1586860301000; tst=h; _gid=GA1.2.773828514.1598317561; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1598350251,1598354447,1598360025,1598435544; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598447291; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1598447576|1598446542; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1598448026|1598446542'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jpglist = []
    folderName = 'D://wallPaperGet'
    try:
        getUrlList(jpglist, response.text)
        storagePictures(jpglist, folderName)
        # print("==================               Mission accomplished!           ===========================")
        print("按任意键退出\n")
        a = input()
    except:
        print("====================                Mission failed!               =======================")


main()



