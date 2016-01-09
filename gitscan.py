#!/usr/bin/python
# -*- coding: utf-8 -*-
#author:ago
import re
import urllib
import string
import argparse
import os
import sys
import threading, time
import MySQLdb
import time

reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.Connection(host="127.0.0.1", port=3306, user="gitscan", passwd="gitscan", charset="UTF8")
conn.select_db('gitscan')

cursor = conn.cursor(MySQLdb.cursors.DictCursor)



def getHtmlSummary(url):
    page = urllib.urlopen(url)
    content = page.read()
    return content

def getHtmlurl(html):
    reg = r'href="(.*?)" title'
    urlre = re.compile(reg)
    urllist = re.findall(urlre,html)
    return urllist


#q = raw_input ("pelase input the keyword(eg:username+password+mail):")


def emails():    
        mails=[]
        htmls=[]
        x = range (1,6)
        for i in x:
            page = str(i)
            try :
				htmlSummary = getHtmlSummary("https://github.com/search?o=desc&p="+str(i)+"&q=mail+password&s=indexed&type=Code&utf8=✓")        
				urllist = getHtmlurl(htmlSummary)
            except:
				pass
            #test = urllist[2:12]
            #if len(urllist) > 2:
            print "searching on the page "+page+",please wait..."
            for url in urllist[2:12]:
                try:
                    htmlDetail = getHtmlSummary("https://github.com"+url)
                    reg_emails1 = re.compile('[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*'+'@(?:[\w](?:[\w-]*[\w])?\.)'+'[\w](?:[\w-]*[\w])?')
                    reg_emails2 = re.compile('[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*'+'@(?:[\w](?:[\w-]*[\w])?\.)'+'(?:[\w](?:[\w-]*[\w])?\.)'+'[\w](?:[\w-]*[\w])?')
                    mail1 = reg_emails1.findall(htmlDetail)
                    mail2 = reg_emails2.findall(htmlDetail)
                    mail = mail1+mail2					
                    mails.extend(mail)
                except:
				    pass
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            #with open('recent_mails.txt', 'wb+') as domain_file:
        for item in mails:
            domain = item.split('@',1)[1]
                #domain_file.write(item + '\n')
            domains=["tencent.com","baidu.com","sohu.com","discuz.net","rising.com.cn","alibaba.com","alibaba-inc.com","360.cn","maxthon.cn","renren.com","ifeng.com","snda.com","sdo.com","sogou-inc.com","9you.com","duba.net","xunlei.com","ctrip.com","19lou.com","shooter.cn","verycd.com","mop.com","ourgame.com","douban.com","youku.com","wanmei.com","39.net","uc.cn","pps.tv","taobao.com","blogbus.com","shopex.cn","gtja.com","alipay.com","phpwind.net","ftchinese.com","lenovo.com","net.cn","17173.com","qiyi.com","focus.cn","chinaren.com","tudou.com","ztgame.com","mtime.com","tompda.com","51.com","shandagames.com","4399.com","jiepang.com","it168.com","huawei.com","ku6.com","dxy.cn","xiami.com","xywy.com","qunar.com","7daysinn.cn","phpcms.cn","pipi.cn","58.com","ganji.com","chinaunix.net","songtaste.com","gaopeng.com","duowan.com","dnspod.cn","tuchong.com","yeepay.com","the9.com","ylmf.com","cnzz.com","pindao.com","jd.com","dzcom","91wan.com","guokr.com","newegg.com.cn","lashou.com","55tuan.com","zhihu.com","cnbeta.com","pptv.com","9158.com","ubox.cn","hudong.com","sangfor.com.cn","vancl.com","unnoo.com","sucop.com","bianfeng.com","6.cn","elong.com","10jqka.com.cn","anquanbao.com","taomee.com","yxlink.com","coremail.cn","crucco.com","zhenai.com","dangdang.com","aipai.com","xiaomi.com","joy.cn","letao.com","jingwei.com","51job.com","changyou.com","hada.me","sf-express.com","kingsoft.com","leyou.com","jiayuan.com","soufun.com","youtx.com","lefeng.com","yoybuy.com","eset.com.cn","7k7k.com","aqgj.cn","guosen.com.cn","ly.com","tom.com","cntv.cn","veryeast.cn","12306.cn","goodbaby.com","cenwor.com","tttuangou.net","jiangmin.com","yonyou.com","ccw.com.cn","vip.com","ftsafe.com.cn","csdn.net","topsec.com.cn","west263.com","wanda.cn","letv.com","dns.com.cn","diandian.com","kugou.com","us.syyx.com","xiu.com","baihe.com","kingdee.com","iboxpay.com","nokia.com","playcool.com","duote.com","wdlinux.cn","yupoo.com","263.net","coo8.com","wooyun.org","36kr.com","dahe.cn","cmseasy.cn","tianya.cn","suning.com","zol.com.cn","easybuy.com.cn","gome.com.cn","jiajia.me","5173.com","baobeihuijia.com","thinksky.hk","neusoft.com","gamemayi.com","51web.com","dajie.com","qianpin.com","2345.com","51cto.com","guang.com","lvmama.com","happigo.com","m18.com","gooann.com","lakala.com","knownsec.com","99.com","xd.com","jiapin.com","docin.com","ip66.com","tnyoo.com","cwan.com","dianping.com","sclub.com.tw","iciba.com","xoyo.com","ijinshan.com","xueqiu.com","chinacache.com","hx168.com.cn","17sup.com","mangocity.com","shop.edu.cn","tiexue.net","cpic.com.cn","venustech.com.cn","huatu.com","178.com","yihaodian.com","house365.com","51greenorange.com","360shop.com.cn","weibo.com","touzhu.cn","qiaogu.com","zblogcn.com","firefox.com.cn","xcar.com.cn","goldmail.cn","trip8080.com","baijob.com","zhubajie.com","acfun.tv","qfpay.com","xianguo.com","tp-link.com.cn","zhenpin.com","hiall.com.cn","800app.com","yuantiku.com","redbaby.com.cn","baixing.com","2cto.com","linktrust.com.cn","womai.com","tuciabbay.com","1ting.com","akcms.com","kingosoft.com","meitu.com","meizu.com","taocms.org","53kf.com","oschina.net","thinksns.com","hxage.com","moliyo.com","3158.cn","oppo.com","tuniu.com","3158.com","meituan.com","eversec.com.cn","kuaibo.com","cins.cn","papa.me","591wed.com","cheshi.com","shopxx.net","m1905.com","argos.cn","tgbus.com","mafengwo.cn","cnblogs.comcmt","fun.tv","hupu.com","sudu.cn","feng.com","nandu.com","changba.com","jinwankansha.com","51bi.com","chinaz.com","umeng.com","mogujie.com","xinghua.org.cn","coolping.com","chinanetcenter.com","iyiyun.com","yunyun.com","eguan.cn","winenice.com","opera.com","zhimei.com","tongbu.com","haodf.com","3322.org","dodonew.com","lesuke.com","iiyi.com","sudytech.com","8684.cn","bjsako.com","newsmyshop.com","tiancity.com","looyu.com","jollymm.com","dopool.com","fantong.com","zhuna.cn","secoo.com","gamtee.com","huanqiu.com","kanglu.com","wssys.net","xinnet.com","ebrun.com","duoshuo.com","bilibili.tv","gfan.com","pconline.com.cn","50cms.com","trs.com.cn","xdf.cn","htinns.com","wacai.com","mplife.com","donews.com","qyer.com","9978.cn","admin5.com","etuan.com","liepin.com","998.com","eastmoney.com","hc360.com","welove520.com","autonavi.com","lusen.com","ecisp.cn","lightinthebox.com","desdev.cn","sgcc.com.cn","mydrivers.com","zte.com.cn","56.com","mbaobao.com","airchina.com.cn","spacebuilder.cn","eyou.net","didatuan.com","jstv.com","v2ex.com","yesky.com","nsfocus.com","qiushibaike.com","anjuke.com","hexun.com","creditcard.cmbc.com.cn","founderbn.com","youmi.cn","ceair.com","sdcms.cn","gddddo.cn","now.cn","safedog.cn","hiwifi.com","jeecms.com","gewara.com","rong360.com","renrendai.com","zzidc.com","jiuxian.com","yinyuetai.com","tcl.com","sootoo.com","ppdai.com","locojoy.com","5sing.com","candou.com","appchina.com","300.cn","phpstat.net","52pk.com","shendu.com","ccidnet.com","diditaxi.com.cn","jiankongbao.com","fc.tcl.com","aicai.com","smartisan.cn","sto.cn","duokan.com","cndns.com","haier.net","haier.com","ehaier.com","jushanghui.com","hairongyi.com","ooopic.com","autohome.com.cn","che168.com","pp.cc","super8.com.cn","17k.com","59.cn","zhaopin.com","amazon.cn","yundaex.com","51zhangdan.com","leiphone.com","ikuai8.com","aoshitang.com","codoon.com","moko.cc","nuomi.com","liba.com","tuan800.com","bizcn.com","destoon.com","22.cn","baofeng.com","kyfw.12306.cn","zgsj.com","chuangxin.com","diyou.cn","zbird.com","e-chinalife.com","kuaiyong.com","v5shop.com.cn","zuzuche.com","chinapost.com.cn","pook.com","4.cn","crsky.com","wandoujia.com","oupeng.com","h3c.com","pcauto.com.cn","pclady.com.cn","pcbaby.com.cn","pcgames.com.cn","pchouse.com.cn","baomihua.com","dolphin.com","pcpop.com","itpub.net","zhe800.com","caijing.com.cn","hikvision.com","bitauto.com","fengyunzhibo.com","app111.com","hanweb.com","id5.cn","jumei.com","onefoundation.cn","weipai.cn","zuche.com","sfbest.com","dbappsecurity.com.cn","jobui.com","imobile.com.cn","shenzhenair.com","douguo.com","v1.cn","diyicai.com","kuwo.cn","csair.com","mama.cn","115.com","foxitsoftware.cn","zto.cn","cofco.com","mycolorway.com","breadtrip.com","qiniu.com","mingdao.com","zoomla.cn","ename.cn","feixin.10086.cn","icafe8.com","anymacro.com","zhujiwu.com","ele.me","phpyun.com","thinkphp.cn","500wan.com","paidai.com","fumu.com","homeinns.com","chinabank.com.cn","meishichina.com","hinews.cn","jj.cn","immomo.com","cnaaa.com","duobei.com","gw.com.cn","tieyou.com","qibosoft.com","zqgame.com","meilishuo.com","sitestar.cn","qmango.com","sohu-inc.com","onlylady.com","edong.com","99bill.com","12321.cn","kongzhong.com","ucloud.cn","kuaidadi.com","cyzone.cn","ujipin.com","damai.cn","jinjianginns.com","stockstar.com","zdnet.com.cn","netentsec.com","spb.gov.cn","cnzxsoft.com","chinaamc.com","china.com","jb51.net","cmstop.com","lecai.com","yongche.com","pingan.com","51credit.com","cnfol.com","china-sss.com","btcchina.com","okcoin.com","kaspersky.com.cn","yinxiang.com","nipic.com","antiy.com","juhe.cn","wumii.org","uzai.com","anzhi.com","yto.net.cn","58pic.com","t3.com.cn","aibang.com","yaolan.com","zhongchou.com","ubuntu.org.cn","smartisan.com","hb-n-tax.gov.cn","chanjet.com","bytedance.com","1hai.cn","tebon.com.cn","tdxinfo.com","tujia.com","cmbchina.com","dbw.cn","pingan.com","legendsec.com","woniu.com","mcafee.com","vasee.com","juesheng.com","wasu.cn","wowsai.com","chinadaily.com.cn","51talk.com","mbachina.com","ifanr.com","boc.cn","jiathis.com","gongchang.com","nbcb.com.cn","91160.com","imooc.com","gf.com.cn","bangcle.com","zhuqu.com","cnmo.com","17ugo.com","zcool.com.cn","jiemian.com","creditease.cn","ebay.com","12308.com","7po.com","itenable.com.cn","tesla.cn","szse.cn","enorth.com.cn","newone.com.cn","haodai.com","cdb.com.cn","sino-life.com","coocaa.com","cgbchina.com.cn","17500.cn","chsi.com.cn","yz.chsi.com.cn","cnpc.com.cn","petrochina.com.cn","welomo.com","zank.mobi","kf5.com","ehaier.com","piccnet.com.cn","88.com.cn","shenhuagroup.com.cn","unionpayintl.com","haigou.unionpay.com","youzu.com","yxdown.com","56.com","gopay.com.cn","wiwide.com","fesco.com.cn","samsung.com","sfn.cn","chinaums.com","htsc.com.cn","ciwong.com","hp.com","itouzi.com","cs.ecitic.com","to8to.com","camera360.com","cfsc.com.cn","ebscn.com","24cp.com","chinahr.com","sinopec.com","mcdonalds.com.cn","chexun.com","jinri.cn","psbc.com","swsresearch.com","picchealth.com","cnooc.com.cn","yohobuy.com","h3c.com","icbccs.com.cn","aol.com","umetrip.com","sunits.com","youyuan.com","cdrcb.com","comba.com.cn","adtsec.com","nffund.com","zhaoshang.net","cytobacco.com","weizhonggou.com","addnewer.com","scti.cn","feiniu.com","chinapnr.com","heetian.com","yungouos.com","zjedu.org","ccic-net.com.cn","shengpay.com","yirendai.com","essence.com.cn","1218.com.cn","228.com.cn","anbanggroup.com","m6go.com","xiangshe.com","vvipone.com","51jingying.com","cmbc.com.cn","51idc.com","autono1.com","jsbchina.cn","dfzq.com.cn","ssscc.com.cn","chaoxing.com","yingjiesheng.com","thfund.com.cn","duxiu.com","myfund.com","x.com.cn","cits.cn","lufax.com","hongkongairlines.com","touna.cn","hhedai.com","jinlianchu.com","tsinghua.edu.cn","qufenqi.com","tv.tcl.com","pinganfang.com","boqii.com","plu.cn","flnet.com","beibei.com","mizhe.com","vivo.com.cn","ahtv.cn","daling.com","cankaoxiaoxi.com","s.cn","lingying.com","voc.com.cn","bankofshanghai.com","wukonglicai.com","zszq.com","fanhuan.com","zhiwang.yixin.com","91jinrong.com","cec.com.cn","jxlife.com.cn","csrc.gov.cn","dianrong.com","leyou.com.cn","benlai.com","cdce.cn","fxiaoke.com","metao.com","minmetals.com.cn","jzjt.com","sinosig.com","umpay.com","sgcc.com.cn","leju.com","fuzegame.tv","fuzegame.com","lonlife.cn","zbj.com","didichuxing.com","emao.com","cang.com","qianxs.com","meican.com","westsecu.com","feidee.com","easou.com","easou-inc.com","csvw.com","cjn.cn","pku.edu.cn","longzhu.com","jdpay.com","tuhu.cn","yahui.cc"]
            if domain in domains:
			    cursor.executemany("insert into persons (mail) values (%s)", [item])
                #print item

c = range (1,100000)
for a in c:    
    emails()
    time.sleep(1000)


print "I need you,boss~~"
cursor.close()
conn.close()
