#coding=utf-8

import os,time
import requests                          #用于发送http请求到蒲公英，第三方模块，需要pip install requests来下载
import webbrowser

def app_created_lastly(dir):         #传入的dir就是文件夹A的路径，如果你的脚本就在当前路径，直接传入“.”即可
    dirdic = {}                            #key＝文件夹名称（包含IPA的文件夹路径），value＝创建的时间
    for i in os.listdir(dir):          #查找文件夹A中所有的文件
        if os.path.isdir(i):
            print i
            creattime = os.path.getctime(dir+os.sep+i) #算出每个文件夹的创建时间，这里的时间是指距离1970年一月一日的秒数，所以数值越大越说明是最新创建的
            dirdic[i] = creattime
    dirdic = sorted(dirdic.items(), key=lambda item: item[1], reverse=True)            #按value值（创建的时间）从大到小对字典排序
    dir_created_lastly = dirdic[0][0]                                                    #字典排列的第一的key值，即最新创建的文件夹
    print '要上传的文件目录是：'+dir_created_lastly
    ipa_path = ""
    for i in os.listdir(dir+os.sep+dir_created_lastly):                         #找到该文件路径下面的IPA文件
        if i.find('.ipa') != (-1):
            ipa_path = dir+os.sep+dir_created_lastly+os.sep+i      #得到最新打包的IPA的夹路径
            return ipa_path
    return ipa_path



def upload_app(path):
    if path == '':
        print '未找到对应上传的app!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        return
    else:
        url = 'http://www.pgyer.com/apiv1/app/upload'         #上传的url地址
        data = {
            'uKey': 'a9de0768c2aa1fddf7365c6996d44885',
            '_api_key': '0c874f6d6e895be5147aa1460fd1af8f',
            'installType': '1',
            'password': '123456',
            'updateDescription': 'poc'
            }                                #发送的参数数据
        files = {'file': open(path, 'rb')}       #上传的文件
        r = requests.post(url, data=data, files=files)   # 发送post请求。完事。。。。
        if r.status_code == 200:
            print "上传成功"
        else:
            print "上传失败"



if __name__ == '__main__':
    dir_ipa = '.'
    IpaPath = app_created_lastly(dir_ipa)
    upload_app(IpaPath)