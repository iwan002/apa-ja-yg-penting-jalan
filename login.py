from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift import transport, protocol, server
from datetime import datetime, timedelta
import pytz, pafy, livejson, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, tweepy, codecs, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip
from zalgo_text import zalgo
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
From BEAPI import *
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()
from Naked.toolshed.shell import execute_js 

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
cl = LINE('fauziiwan858@gmail.com','sayang1')
cl.log("Auth Token : " + str(cl.authToken))

oepoll = OEPoll(cl)
call = cl
creator = ["u00e287effe898e54347d2ee6502d2ec2"]
owner = ["u00e287effe898e54347d2ee6502d2ec2"]
admin = ["u00e287effe898e54347d2ee6502d2ec2"]
staff = ["u00e287effe898e54347d2ee6502d2ec2"]
Tumbal = ["u8e603fce8dd01a68eeb8837342618f6d","u00e287effe898e54347d2ee6502d2ec2"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
KAC = [cl]
Bots = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
Setbot4 = codecs.open("user.json","r","utf-8")
settings = livejson.File('settings.json', True, False, 4)
premium = json.load(Setbot4)
protectantijs = []
protectcancel = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
offbot = []

settings = {
    "welcome": False,
    "leave": False,
    "mid": False,
    "size": "micro",
    "keyCommand": "dent",
    "commentPost": "hadir like ʙʏ me: 💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
    "Aip": True,
    "replySticker": False,
    "jumbosticker": False,
    "sticker": False,
    "media": False,
    "nCall": False,
    "checkContact": False,
    "postEndUrl": {},
    "postingan":{},
    "checkPost": False,
    "autoRead": True,
    "autoJoinTicket": True,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changevp": False,
    "changeCover":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "checkmid": False,
    "getMid": False,
    "invite":False,
    "Invi":False,
    "staff":{},
    "Timeline": True,
    "likePost": False,
    "likeOn": False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "readPoint":{},
    "readMember":{},
    "lang":False,
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist": False,
    "dblacklist": False,
    "wwhitelist": False,
    "dwhitelist": False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "tumbal":True,
    "key":True,
    "smule":True,
    "jumbosticker":False,
    "media": True,
    "smule":True,
    "notifsmule":True,
    "smule":True,
    "notif":True,
    "nCall":False,
    "backup":True,
    "contact":False,
    "autoRead": True,
    "autoBlock": True,
    "autoJoin":True,
    "autoAdd":False,
    'autoCancel':{"on":True, "members":1},
    "autoReject":False,
    "autoLeave":False,
    "detectMention":False,
    "detectMention2":False,
    "detectMention3": False,
    "detectMention4": False,
    "detectMention5": False,
    "Mentionkick":False,
    "welcomeOn":False,
    "Unsend":False,
    "sticker":False,
    "smule":True,
    "selfbot":True,
    "dell":"cok",
    "flexghost":"  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
    "JANJUK":"kowe",
    "NGENTOT":"memek",
    "broad":"aku datang bawa pesan",
    "mention":" 👿anyink ga tuh",
    "Respontag":"  OPO BRO",
    "Respontag2":"ᴋᴀɴɢᴇɴ ʏᴀ ᴛᴀɢ ᴀɪᴍ ᴍᴜʟᴜ",
    "Respontag3":"hadir bro",
    "Respontag4":"naon anyink ngetag aing wae 😠",
    "welcome":" sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ɢᴀᴇᴢ",
    "autoLeave":" sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴛᴇᴍᴀɴ",
    "comment":"salam kenal guyss\n│http://line.me/ti/p/~waentur01",
    "message1":"ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\n│http://line.me/ti/p/~waentur01",
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
clProfile = cl.getProfile()
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
           
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          print ("✪[]► Like Success")
        except:
          pass
      else:
          print ("Already Liked")
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
#remot tagall
def RemotOlengKiller(to, BotsOleng):
    try:
        AbiOleng = ""
        MuhazirOlengKiller = "Total {} Janda \n1.".format(str(len(BotsOleng)))
        Desah = []
        TapokPipit = 1
        JilatMpek = 2
        for Sedot in BotsOleng:
            MuhazirOleng = "@x\n"
            Wikwik = str(len(MuhazirOlengKiller))
            Ngentot = str(len(MuhazirOlengKiller) + len(MuhazirOleng) - 1)
            AbiOleng = {'S':Wikwik, 'E':Ngentot, 'M':Sedot}
            Desah.append(AbiOleng)
            MuhazirOlengKiller += MuhazirOleng
            if TapokPipit < len(BotsOleng):
                TapokPipit += 1
                MuhazirOlengKiller += "%i. " % (JilatMpek)
                JilatMpek=(JilatMpek+1)
            else:
                try:
                    TapokPipit = "\n[ {} ]".format(str(AbiOlengKiller.getGroup(to).name))
                except:
                    TapokPipit = "\n[ Success ]"
        cl.sendMessage(to, MuhazirOlengKiller, {'MENTION': str('{"MENTIONEES":' + json.dumps(Desah) + '}')}, 0)
    except Exception as error:
        logError(error)

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')
                     
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ᴋᴀɴɢ ᴍᴀʟɪɴɢ sᴇᴍᴠᴋ ɴɢɪɴᴛɪᴘ\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = (str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
    #    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        sendTextTemplate12(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sendTextTemplate12(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        sendTextTemplate12(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        sendTextTemplate12(to, "[ INFO ] Error :\n" + str(error))

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost

def sendTextTemplate12(to, text):
    data = {
        "type": "text",
        "text":text,
        "sentBy": {
            "label":"♻️𝖉𝖚𝖉𝖚𝖑 𝖇𝖔𝖙𝖘♻️",
        "iconUrl": "https://i.ibb.co/h9nLycK/1617387582638.gif",
        "linkUrl": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2"
     }
    }
    cl.postTemplate(to, data)

#=====DEF HELP MENU =======
def sendTextTemplate23(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#2bff44"            
      },
      {
        "type": "separator",
        "color": "#2bff44"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#2bff44"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
"weight": "bold",
"color": "#2bff44",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#2bff44",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ⁴",
"weight": "bold",
"color": "#2bff44",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#2bff44"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#2bff44"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#2bff44"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~sawargibots",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#2bff44"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#2bff44",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#2bff44"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#2bff44",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#2bff44"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#2bff44"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#2bff44"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#2bff44",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#2bff44"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#2bff44"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#2bff44"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://www.youtube.com/channel/UCHjL4ZK41GPortOBOIE8zdA?view_as=subscriber"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~sawargibots",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/XDL_IWAN_021_GSV",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#2bff44"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#2bff44"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate906(to, text):
    data = {
            "type": "flex",
            "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
            "contents":{
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text":  text,
            "size": "xs",
            "color": "#ffffff",
            "wrap": True,
            "weight": "regular",
            "offsetStart": "3px"
          }
        ],
        "margin": "xs",
        "spacing": "md",
        "backgroundColor": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
            "align": "center",
            "color": "#ffffff",
            "size": "xs"
          }
        ],
        "paddingAll": "2px",
        "backgroundColor": "#000000",
        "margin": "xs"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#FF0000",
    "cornerRadius": "10px",
    "spacing": "xs"
  },
  "styles": {
    "body": {
      "backgroundColor": "#ff0000"
    }
  }
}
}
    cl.postTemplate(to, data)
#=========DEF

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═════════🚫\n"+\
                  "┣😱► " + key + "ʜᴇʟᴘ1\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ2\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ3\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ4\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ5\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ6\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ wl\n" + \
                  "┣😱► " + key + "ʜᴇʟᴘ bl\n" + \
                  "┣😱► " + key + "help js\n" + \
                  "┣😱► " + key + "menu \n" + \
                  "┣😱► " + key + "menu respon\n" + \
                  "┣😱► " + key + "menu sticker\n" + \
                  "┣😱► " + key + "menu sticker1\n" + \
                  "╚═════════🚫"
    return helpMessage
def helpcreator():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭「🤕ᴄᴏᴍᴀɴᴅ ʙᴏᴛ🤕」\n"+\
                  "│🤕" + key + "ᴍᴇ\n" + \
                  "│🤕" + key + "ᴄᴠᴘ\n" + \
                  "│🤕" + key + "sᴇᴛᴛɪɴɢ\n" + \
                  "│🤕" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "│🤕" + key + "sᴘᴇᴇᴅ-sᴘ\n" + \
                  "│🤕" + key + "tagal/halo/tag\n" + \
                  "│🤕" + key + "ʙʏᴇ\n" + \
                  "│🤕" + key + "ʀj\n" + \
                  "│🤕" + key + "ʟᴠᴀʟʟ\n" + \
                  "│🤕" + key + "ʟɪsᴛғʀɪᴇɴᴅ\n" + \
                  "│🤕" + key + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "│🤕" + key + "ɢʀᴜᴘʟɪsᴛ\n" + \
                  "│🤕" + key + "ᴏᴘᴇɴ ǫʀ\n" + \
                  "│🤕" + key + "ᴄʟᴏsᴇ ǫʀ\n" + \
                  "│🤕" + key + "Set tag: [texs]\n" + \
                  "│🤕" + key + "Set tag2: [texs]\n" + \
                  "│🤕" + key + "Rtag: [Nogc]\n" + \
                  "│🤕" + key + "Jepit @\n" + \
                  "│🤕" + key + "ʙʟᴏᴄᴋ「@」\n" + \
                  "│🤕" + key + "ᴀᴅᴅᴍᴇ「@」\n" + \
                  "│🤕" + key + "ᴍʏʙᴏᴛ\n" + \
                  "│🤕" + key + "ʟɪsᴛᴘᴇɴᴅɪɴɢ\n" + \
                  "│🤕" + key + "ʙʟᴏᴄᴋᴄᴏɴᴛᴀᴄᴛ\n" + \
                  "│🤕" + key + "ʟᴋsᴛʙʟᴏᴄᴋ\n" + \
                  "│🤕" + key + "ʟɪsᴛᴍɪᴅ\n" + \
                  "│🤕" + key + "ᴀᴅᴅᴀsɪs\n" + \
                  "│🤕" + key + "ʙʀᴏᴀᴅᴄᴀsᴛ:「ᴛᴇxᴛ」\n" + \
                  "╰「🤧sᴇʟғ ᴘʏᴛʜᴏɴ³🤧」"
    return helpMessage1

def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "╭「🤢ᴄᴏᴍᴀɴᴅ ʙᴏᴛ🤢」\n"+\
                  "│🤮"  + key + "ʙᴏᴛᴀᴅᴅ「@」\n" + \
                  "│🤮"  + key + "ʙᴏᴛᴅᴇʟʟ「@」\n" + \
                  "│🤮"  + key + "sᴛᴀғғ「@」\n" + \
                  "│🤮"  + key + "sᴛᴀғᴅᴇʟʟ「@」\n" + \
                  "│🤮"  + key + "ᴀᴅᴍɪɴ「@」\n" + \
                  "│🤮"  + key + "ᴀᴅᴍɪɴᴅᴇʟʟ「@」\n" + \
                  "│🤮"  + key + "#ʀᴇʙᴏᴏᴛ\n" + \
                  "│🤮"  + key + "ʙᴀɴ「@」\n" + \
                  "│🤮"  + key + "ʙʟᴄ\n" + \
                  "│🤮"  + key + "ʙᴀɴ:ᴏɴ\n" + \
                  "│🤮"  + key + "ᴜɴʙᴀɴ:oɴ\n" + \
                  "│🤮"  + key + "ᴜɴʙᴀɴ「@」\n" + \
                  "│🤮"  + key + "ʙᴀɴʟɪsᴛ\n" + \
                  "│🤮"  + key + "ᴄʙᴀɴ\n" + \
                  "│🤮"  + key + "ʀᴇғʀᴇsʜ\n" + \
                  "╰「🤢sᴇʟғ ᴘʏᴛʜᴏɴ³🤢」"
    return helpMessage5
  
def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭「👽sᴇʟғ ᴘʏᴛʜᴏɴ³👽」\n"+\
                  "│😠" + key + "ɢᴍɪᴅ @\n" + \
                  "│😠" + key + "ɢᴇᴛ ɪᴅ @\n" + \
                  "│😠" + key + "ɢᴇᴛᴍɪᴅ @\n" + \
                  "│😠" + key + "ɢᴇᴛʙɪᴏ @\n" + \
                  "│😠" + key + "ɢᴇᴛɪɴғᴏ @\n" + \
                  "│😠" + key + "ɢᴇᴛᴘʀᴏғɪʟᴇ @\n" + \
                  "│😠" + key + "ɢᴇᴛᴘɪᴄᴛᴜʀᴇ @\n" + \
                  "│😠" + key + "ɪɴғᴏ @\n" + \
                  "│😠" + key + "ᴋᴇᴘᴏ @\n" + \
                  "│😠" + key + "ᴘᴘᴠɪᴅᴇᴏ @\n" + \
                  "│😠" + key + "ᴋᴏɴᴛᴀᴋ @\n" + \
                  "│😠" + key + "ᴄᴏɴᴛᴀᴄᴛ:「ᴍɪᴅ」\n" + \
                  "│😠" + key + "ɢɴᴀᴍᴇ「ᴛᴇxᴛ」\n" + \
                  "│😠" + key + "ᴍʏᴍɪᴅ\n" + \
                  "│😠" + key + "ᴍʏʙɪᴏ\n" + \
                  "│😠" + key + "ᴍʏғᴏᴛᴏ\n" + \
                  "│😠" + key + "ᴍʏɴᴀᴍᴇ\n" + \
                  "│😠" + key + "ᴍʏᴘʀᴏғɪʟᴇ\n" + \
                  "│😠" + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ\n" + \
                  "│😠" + key + "ᴍʏᴄᴏᴠᴇʀ\n" + \
                  "│😠" + key + "ᴍʏᴠɪᴅᴇᴏ\n" + \
                  "│😠" + key + "ᴋᴀʟᴇɴᴅᴇʀ\n" + \
                  "│😠" + key + "ᴍᴇᴍᴘɪᴄᴛ\n" + \
                  "│😠" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "│😠" + key + "ɢʀᴜᴘᴘɪᴄᴛ\n" + \
                  "│😠" + key + "ɪɴғᴏɢʀᴏᴜᴘ「ɴᴏ」\n" + \
                  "│😠" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "╰「👽sᴇʟғ ᴘʏᴛʜᴏɴ³👽」"
    return helpMessage4
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭「👽💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍👽」\n"+\
                  "│😡" + key + "ᴄᴇᴋ sɪᴅᴇʀ\n" + \
                  "│😡" + key + "ᴄᴇᴋ ʟᴇᴀᴠᴇ \n" + \
                  "│😡" + key + "ᴄᴇᴋ ᴘᴇsᴀɴ \n" + \
                  "│😡" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ \n" + \
                  "│😡" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ² \n" + \
                  "│😡" + key + "sᴇᴛ sɪᴅᴇʀ:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "sᴇᴛ ᴘᴇsᴀɴ:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "sᴇᴛ ʀᴇsᴘᴏɴ:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "sᴇᴛ ʀᴇsᴘᴏɴ²:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "sᴇᴛ ʟᴇᴀᴠᴇ:「ᴛᴇxᴛ」\n" + \
                  "│😡" + key + "ʟɪᴋᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "│😡" + key + "sider「ᴏɴ/ᴏғғ」\n" + \
                  "│😡" + key + "stag:「jumlah」\n" + \
                  "│😡" + key + "stag「@kontak」\n" + \
                  "│😡" + key + "call:「jumlah」\n" + \
                  "│😡" + key + "scall \n" + \
                  "│😡" + key + "scallto/yank\n" + \
                  "│😡" + key + "ᴘᴏsᴛ「oɴ/oғғ」\n" + \
                  "│😡" + key + "sᴛɪᴄᴋᴇʀ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ɪɴᴠɪᴛᴇ「oɴ/ᴏғғ」\n" + \
                  "│😡" + key + "ᴜɴsᴇɴᴅ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ʀᴇsᴘᴏɴ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ʀᴇsᴘᴏɴ²「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴀᴜᴛᴏᴀᴅᴅ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴡᴇʟᴄᴏᴍᴇ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴄᴏɴᴛᴀᴄᴛ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴀᴜᴛᴏᴊᴏɪɴ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴀᴜᴛᴏʙʟᴏᴄᴋ「oɴ/oғғ」\n" + \
                  "│😡" + key + "ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「oɴ/oғғ」\n" + \
				  "╰「😡sᴇʟғ ᴘʏᴛʜᴏɴ³😡」"
    return helpMessage2
def media():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔═══════════\n" + \
"┣😈► " + key + "Addsticker\n" + \
"┣😈► " + key + "Addmp3\n" + \
"┣😈► " + key + "Addaudio\n" + \
"┣😈► " + key + "Addimg\n" + \
"┣😈► " + key + "Dellsticker\n" + \
"┣😈► " + key + "Dellaudio\n" + \
"┣😈► " + key + "Dellmp3\n" + \
"┣😈► " + key + "Dellvideo\n" + \
"┣😈► " + key + "Dellimg\n" + \
"┣😈► " + key + "Liststicker\n" + \
"┣😈► " + key + "Listimage\n" + \
"┣😈► " + key + "Listvideo\n" + \
"┣😈► " + key + "Listaudio\n" + \
"┣😈► " + key + "Listmp3\n" + \
"┣😈► " + key + "Lihat「No」\n" + \
"┣😈► " + key + "Cctv metro\n" + \
"┣😈► " + key + "Smule「id」\n" + \
"┣😈► " + key + "Joox「text」\n" + \
"┣😈► " + key + "mp4「text」\n" + \
"┣😈► " + key + "mp3「text」\n" + \
"┣😈► " + key + "Yutube「text」\n" + \
"┣😈► " + key + "Youtube「text」\n" + \
"╚═══════════"
    return helpMessage3

def helpghost():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "╭「🐆ᴄᴏᴍᴀɴᴅ ʙᴏᴛ🐆」\n"+\
                  "│🐃"  + key + "sᴛᴀʏ\n" + \
                  "│🐃"  + key + "ᴊs ɪɴ-ᴏᴜᴛ\n" + \
                  "│🐃"  + key + "ᴀᴊsғᴏᴛᴏ\n" + \
                  "│🐃"  + key + "aing ᴀʙsᴇɴ\n" + \
                  "│🐃"  + key + "ᴊs ᴄᴇʟ\n" + \
                  "│🐃"  + key + "ᴊs ᴋᴀʟʟ\n" + \
                  "│🐃"  + key + "ᴘᴀs\n" + \
                  "│🐃"  + key + "ᴊsɴᴀᴍᴇ [ᴛᴇxᴛ]\n" + \
                  "│🐃"  + key + "ᴄᴇᴋʙᴏᴛ\n" + \
                  "│🐃"  + key + "ᴋɪᴄᴋ「@」\n" + \
                  "│🐃"  + key + "ᴄʀᴏᴛ-ᴄʀɪᴛ\n" + \
                  "╰「🐆𝖉𝖚𝖉𝖚𝖑 𝖇𝖔𝖙𝖘 𝖙𝖊𝖆𝖒🐆」"
    return helpMessage6

def helpwl():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage7 = "╭「🐆ᴄᴏᴍᴀɴᴅ ʙᴏᴛ🐆」\n"+\
                  "│🐃"  + key + "{key}whitelist\n" + \
                  "│🐃"  + key + "ᴊ{key}clearwl\n" + \
                  "│🐃"  + key + "{key}detectwl\n" + \
                  "│🐃"  + key + "{key}addwl「 Mention 」\n" + \
                  "│🐃"  + key + "{key}dewl「 Mention 」\n" + \
                  "│🐃"  + key + "{key}wl:「 On/Off 」\n" + \
                  "│🐃"  + key + "{key}unwl「 Num 」\n" + \
                  "╰「🐆𝖉𝖚𝖉𝖚𝖑 𝖇𝖔𝖙𝖘 𝖙𝖊𝖆𝖒🐆」"
    return helpMessage7
    
def helpbl():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage8 = "╭「🐆ᴄᴏᴍᴀɴᴅ ʙᴏᴛ🐆」\n"+\
                  "│🐃"  + key + "{key}blacklist\n" + \
                  "│🐃"  + key + "{key}clearbl\n" + \
                  "│🐃"  + key + "{key}detectbl\n" + \
                  "│🐃"  + key + "{key}addbl「 Mention 」\n" + \
                  "│🐃"  + key + "{key}debl「 Mention 」\n" + \
                  "│🐃"  + key + "{key}bl:「 On/Off 」\n" + \
                  "│🐃"  + key + "{key}unbl「 Num 」\n" + \
                  "╰「🐆𝖉𝖚𝖉𝖚𝖑 𝖇𝖔𝖙𝖘 𝖙𝖊𝖆𝖒🐆」"
    return helpMessage8
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                sendTextTemplate12(op.param1,"maaf auto block on\n│http://line.me/ti/p/~behboaedan021")
                
        if op.type == 13 or op.type == 124:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate12(op.param1,"eмooн coĸ" +str(ginfo.name))
                        cl.leavegroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate12(op.param1,"ᴛʜᴀɴᴋs" + str(ginfo.name))
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
                if msg.contentType == 6:
                  if wait["notif"] == True:
                    if msg._from not in Bots:
                        try:
                            contact = cl.getContact(sender)
                            group = cl.getGroup(msg.to)
                            cover = cl.getProfileCoverURL(sender)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            if msg.toType == 2:
                                b = msg.contentMetadata['GC_EVT_TYPE']
                                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                                if c == 'AUDIO' and b == "S":
                                    arg = "• nah kan jones nangkring FCG🤣"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    sendTextTemplate12(msg.to,arg)
                                if c == 'VIDEO' and b == "S":
                                    arg = "• cie ngajakin VCG ikut dong🤣"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}.@!".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    sendTextTemplate12(msg.to,arg)
                                if c == 'LIVE' and b == "S":
                                    arg = "• waseekk ada atis LIVE 👍"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    sendTextTemplate12(msg.to,arg)
                                else:
                                    mills = int(msg.contentMetadata["DURATION"])
                                    seconds = (mills/1000)%60
                                    if c == "AUDIO" and b == "E":
                                        arg = "• nah ko udahan sih FCG nya"
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        sendTextTemplate12(msg.to,arg)
                                    if c == "VIDEO" and b == "E":
                                        arg = "• baru jga mau ikut VCG malah turun"
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        sendTextTemplate12(msg.to,arg)
                                    if c == "LIVE" and b == "E":
                                        arg = "• ko udahan sil LIVE nya "
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}.".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        sendTextTemplate12(msg.to,arg)
                        except Exception as error:
                            print (error)
            
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
                if msg.contentType == 6:
                  if wait["nCall"] == True:
                    if msg._from not in Bots:
                        try:
                            contact = cl.getContact(sender)
                            group = cl.getGroup(msg.to)
                            cover = cl.getProfileCoverURL(sender)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            if msg.toType == 2:                
                                b = msg.contentMetadata['GC_EVT_TYPE']
                                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                                if c == "VIDEO" and b == "S":
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    a1 = "{}".format(str(contact.displayName))
                                    a2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    a3 = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#ffff00"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "0px",
            #"borderColor": "#ff0000",
            "cornerRadius": "3px",
            "offsetTop": "3px",
            "offsetStart": "2px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢CALL VIDEO",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "1px",
            #"borderColor": "#00ff00",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "20px",
            "offsetTop": "265px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴋᴇᴛᴀᴜᴀɴ ᴊᴏɴᴇs ɴʏᴀ ᴅɪᴀ",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a2,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#00ff00"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a3,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "70px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "0px",
            #"borderColor": "#00ff00",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "0px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#00ff00",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                if c == 'AUDIO' and b == "S":
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    satu = "{}".format(str(contact.displayName))
                                    dua = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    tiga = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            #"borderColor": "#ff0000",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢CALL AUDIO",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "2px",
            #"borderColor": "#ff0000",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": satu,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "20px",
            "offsetTop": "266px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴋᴇᴛᴀᴜᴀɴ ᴊᴏɴᴇs ɴʏᴀ ᴅɪᴀ",
                "size": "xxs",
                "color": "#ffff00",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": dua,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": tiga,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "90px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#ff0000",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#ff0000",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                if c == 'LIVE' and b == 'S':
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    c1 = "{}".format(str(contact.displayName))
                                    c2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    c3 = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            #"borderColor": "#ffff00",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢LIVE VIDEO",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "2px",
            #"borderColor": "#ffff00",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "20px",
            "offsetTop": "265px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "sɪᴊᴏɴᴇs ʟᴀɢɪ ᴄᴀᴘᴇʀ ʟɪᴠᴇ",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c2,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#ffff00"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c3,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "90px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#ffff00",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#ffff00",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                else:
                                    mills = int(msg.contentMetadata["DURATION"])
                                    seconds = (mills/1000)%60
                                    if c == "VIDEO" and b == "E":
                                   # 	tz = pytz.timezone("Asia/Jakarta")
                                  #      timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        b1 = "{}".format(str(contact.displayName))
                                        b2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        b3 = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            #"borderColor": "#00ff00",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢END CALLVI",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "2px",
            #"borderColor": "#00ff00",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "20px",
            "offsetTop": "265px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴛᴜᴋᴀɴɢ ɴɪᴋᴜɴɢ ᴛᴜʀᴜɴ",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b2,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#00ff00"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b3,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#00ff00",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#00ff00",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                                    if c == "AUDIO" and b == "E":
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        empat = "{}".format(str(contact.displayName))
                                        lima = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        enam = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            #"borderColor": "#ff0000",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢END CALL",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "2px",
            #"borderColor": "#ff0000",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": empat,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "20px",
            "offsetTop": "265px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴛᴜᴋᴀɴɢ ɴɪᴋᴜɴɢ ᴛᴜʀᴜɴ",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ff0000",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": lima,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": enam,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "90px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#ff0000",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#ff0000",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                                    if c == "LIVE" and b == "E":
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        d1 = "{}".format(str(contact.displayName))
                                        d2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        d3 = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:4",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            #"borderColor": "#fi9fff00",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            #"backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:2",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "190px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📞⃢END LIVE",
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "15px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            #"backgroundColor": "#000000",
            "offsetTop": "0px",
            "offsetStart": "30px",
            "borderWidth": "2px",
            #"borderColor": "#ffff00",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#00ff00",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "23px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "202px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "76px",
            "height": "40px",
            #"backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#ffff00",
            "cornerRadius": "20px",
            "offsetTop": "265px",
            "offsetStart": "39px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴋᴀsɪᴀɴ sɪᴊᴏɴᴇs ʟɪᴠᴇ ɢᴅᴀ ʏɢ ʟɪᴀᴛ",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "154px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "cornerRadius": "2px",
            "offsetTop": "225px",
            "offsetStart": "1px",
            #"backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "40px",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "114px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d2,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            #"backgroundColor": "#F08080cc",
            "offsetTop": "263px",
            "offsetStart": "55px",
            #"borderColor": "#ffff00"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d3,
                "size": "xxs",
                "color": "#ffffff",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            #"backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "283px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#ffff00",
            "cornerRadius": "10px",
            "offsetTop": "900px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#ffff00",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#C0C0C0"
        }
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                        except Exception as error:
                            print (error)

        if op.type == 13 or op.type == 124:
            if wait["autoJoin"] and mid in op.param3:
                group = cl.getGroup(op.param1)
                group.notificationDisabled = False
                cl.acceptGroupInvitation(op.param1)
              #  chat.chats[0].extra.groupExtra.preventedJoinByTicket = False
                cl.updateGroup(group)
                ginfo = cl.getGroup(op.param1)                
                sendTextTemplate12(op.param1,"ᴛʜᴀɴᴋs" + str(ginfo.name))

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message1"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message1"])
                        
        if op.type == 13 or op.type == 124:
            if mid in op.param3:
               if wait["autoReject"] == True:
                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       cl.rejectGroupInvitation(op.param1)

        if op.type == 13 or op.type == 124:
            if op.param2 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitetion(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitetion(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitetion(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True

        if op.param3 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitetion(op.param1,[op.param3])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitetion(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitetion(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True 
        if op.type == 17 or op.type == 130:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 32 or op.type == 126:
            if wait["backup"] == True:
              if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 133 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in creator:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.acceptGroupInvitation(op.param1)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 133 or op.type == 32:
            if op.param3 in creator:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 19 or op.type == 133 or op.type == 32:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 32 or op.type == 126:
            if wait["tumbal"] == True:
              if op.param3 in Tumbal:
                if op.param2 not in Bots and op.param2 not in creator and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,Tumbal)
                    except:
                    	pass
                return

            if op.param3 in mid: #Kalo Admin ke Kick
              if op.param2 in Bots:
                pass
              if op.param2 in mid:
                pass
              else:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])                
            if op.param3 in Amid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(ABC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀʏᴀ ɪʟᴀɴɢ':
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs\nᴘᴇɴɢɪʀɪᴍ: "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\nᴊᴀᴍ sʜᴀʀᴇ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ik = str(ika.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ika.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                           else:
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                ika1 = "🚹{}".format(str(ika.displayName))
                                ika2 = "🏠:{}".format(str(ginfo.name))
                                ika3 = "🕙{}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                seber = "═══「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」═══\n{}".format(str(msg_dict[msg_id]["text"]))
                                data = {
                                        "type": "flex",
                                        "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000ff"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(str(ika.pictureStatus)),
            "type": "image",
            "size": "xxs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": ika1,
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": ika3, #"🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"🕙"),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": ika2, #"{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#ffff00",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": seber,
           "size": "xxs",
       #   "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~waentur01",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~bancat525",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/BomberBSSI",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(at, data)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯」\n"
                                ret_ += "┣[]►🚹: {}".format(str(ryan.displayName))
                                ret_ += "\n┣[]►🏠: {}".format(str(ginfo.name))
                                ret_ += "\n┣[]►🕘: {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sendTextTemplate12(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'ɢᴀᴍʙᴀʀʏᴀ ᴅɪʙᴀᴡᴀʜ',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯]"
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ: {}".format(pkg_id)
                   ret_ += "\n┣[]►ᴜʀʟ:{}".format(pkg_id)
                   ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
#____________________________________________________________________
        if op.type == 17 or op.type == 130:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                welcomeMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(op.param2)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:1",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["welcome"],
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "68px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "150px",
"height": "16px",
"width": "140px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(op.param2).displayName),
                "color": "#ffff00",
                "size": "xxs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            #"backgroundColor": "#ffff00",
            "offsetTop": "26px",
            "offsetStart": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#ff0000",
            "offsetBottom": "900px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "W E L C O M E",
                "size": "xs",
                "color": "#ff0000",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xs",
                "color": "#ff0000",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "185px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "61px",
            "height": "61px",
            "offsetTop": "1px",
            "offsetStart": "1px",
            "offsetBottom": "1px",
            "borderColor": "#0000ff",
            "cornerRadius": "10px",
            "borderWidth": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": "#0000ff"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                cl.postTemplate(op.param1, data)
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
              #  cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                leaveMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(op.param2)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:1",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["autoLeave"],
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "68px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "besok puskun amin",
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "140px",
"height": "16px",
"width": "140px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(op.param2).displayName),
                "color": "#ffff00",
                "size": "xxs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            #"backgroundColor": "#ffff00",
            "offsetTop": "26px",
            "offsetStart": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#ff0000",
            "offsetBottom": "900px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "A U T O L E F T",
                "size": "xs",
                "color": "#ff0000",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xs",
                "color": "#ff0000",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "185px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "61px",
            "height": "61px",
            "offsetTop": "1px",
            "offsetStart": "1px",
            "offsetBottom": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "10px",
            "borderWidth": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": "#ffff00"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                cl.postTemplate(op.param1, data)

        #===cctv
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        cover = cl.getProfileCoverURL(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8","#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#696969")
                        warnanya1 = random.choice(warna1)
                        data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["mention"],
"weight": "bold",
"color": warnanya1,
"size": "xs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "45px",
#"backgroundColor": "#00ff00",
"offsetStart": "33px",
"height": "16px",
"width": "84px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": warnanya1,
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            "offsetTop": "40px",
            "offsetStart": "33px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "0px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": warnanya1,
            "offsetBottom": "40px",
            "offsetStart": "900px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " S I D E R",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str(cl.getProfileCoverURL(op.param2)),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "offsetStart": "3px",
            "cornerRadius": "100px",
            "offsetBottom": "3px",
            "borderColor": warnanya1,
            "borderWidth": "1px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": warnanya1,
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                        cl.postTemplate(op.param1, data)
#========={{{{{MENTION}}}}}===========
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if settings ["Aip"] == True:
                if msg.text in ["@zona","!bubarkan","Bypass"]:
                    cl.kickoutFromGroup(receiver,[sender])
            if wait["selfbot"] == True:
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	cl.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:2",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag"],
"weight": "bold",
"color": "#2bff44",
"size": "xs",
"offsetStart": "30px",
"offsetTop": "70px"
}
],
"position": "absolute",
"borderColor": "#ffff00",
"borderWidth": "2px",
"cornerRadius": "8px",
"offsetTop": "110px",
"backgroundColor": "#000000",
"offsetStart": "1px",
"height": "20px",
"width": "151px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": "#2bff44",
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ffff00",
            "borderWidth": "2px",
            "cornerRadius": "8px",
            "margin": "none",
            "backgroundColor": "#000000",
            "height": "20px",
            "width": "151px",
            "offsetTop": "132px",
            "offsetStart": "1px"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag"],
"weight": "bold",
"color": "#2bff44",
"size": "xxs",
"offsetStart": "0px",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "111px",
#"backgroundColor": "#000000",
"offsetStart": "5px",
"width": "120px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": "#2bff44",
                "size": "xxs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            #"backgroundColor": "#000000",
            "width": "120px",
            "offsetTop": "115px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "120px",
            "height": "90px",
            "offsetTop": "18px",
            "cornerRadius": "5px",
            "position": "absolute",
            "borderWidth": "2px",
            "borderColor": "#ffff00",
            "offsetBottom": "1px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "R E S P O N",
                "size": "xxs",
                "color": "#2bff44",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxs",
                "color": "#2bff44",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "30px",
            "height": "30px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "offsetBottom": "1px",
            "offsetStart": "123px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "30px",
            "height": "30px",
            "offsetTop": "48px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "offsetBottom": "1px",
            "offsetStart": "123px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "30px",
            "height": "30px",
            "offsetTop": "78px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "offsetBottom": "1px",
            "offsetStart": "123px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str(cl.getProfileCoverURL(op.param2)),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "offsetStart": "900px",
            "cornerRadius": "100px",
            "offsetBottom": "3px",
            "borderColor": "#ffff00",
            "borderWidth": "1px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": "#ffff00"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                           cl.postTemplate(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate1(msg.to,"j̸͟͞a̸͟͞n̸͟͞g̸͟͞a̸͟͞n̸͟͞ t̸͟͞a̸͟͞g̸͟͞ g̸͟͞u̸͟͞a̸͟͞ n̸͟͞a̸͟͞n̸͟͞t̸͟͞i̸͟͞ k̸͟͞e̸͟͞j̸͟͞i̸͟͞t̸͟͞a̸͟͞k̸͟͞")
                           cl.kickoutFromGroup(to, [msg._from])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag2"],
"weight": "bold",
"color": "#ffff00",
"size": "xs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "45px",
#"backgroundColor": "#00ff00",
"offsetStart": "33px",
"height": "16px",
"width": "84px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": "#00ff00",
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            "offsetTop": "40px",
            "offsetStart": "33px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "0px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#0000ff",
            "offsetBottom": "40px",
            "offsetStart": "900px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "R E S P O N 2",
                "size": "xs",
                "color": "#00ff00",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str(cl.getProfileCoverURL(op.param2)),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "offsetStart": "3px",
            "cornerRadius": "100px",
            "offsetBottom": "3px",
            "borderColor": "#48D1CC",
            "borderWidth": "1px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": "#48D1CC"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                           cl.postTemplate(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data ={
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:1",
            "gravity": "top"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag3"],
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "68px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
"weight": "bold",
"color": "#000000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "20px",
"backgroundColor": "#ffff00",
"offsetStart": "150px",
"height": "16px",
"width": "140px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": "#ffff00",
                "size": "xxs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            #"backgroundColor": "#ffff00",
            "offsetTop": "26px",
            "offsetStart": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "61px",
            "height": "61px",
            "cornerRadius": "10px",
            "position": "absolute",
            "borderWidth": "2px",
            "borderColor": "#ff00ff",
            "offsetBottom": "1px",
            "offsetTop": "1px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "R E S P O N 3",
                "size": "xs",
                "color": "#00ff00",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xs",
                "color": "#00ff00",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "1px",
            "offsetStart": "185px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str(cl.getProfileCoverURL(op.param2)),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "61px",
            "height": "61px",
            "offsetTop": "900px",
            "offsetStart": "1px",
            "offsetBottom": "900px",
            "borderColor": "#ff00ff",
            "cornerRadius": "10px",
            "borderWidth": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": "#ff00ff"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                           cl.postTemplate(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention4"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data ={
                            "type": "text",
                            "text": wait["Respontag4"],
                            "sentBy": {
                            "label": "{} ".format(contact.displayName),
                            "iconUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                            "linkUrl": "https://www.linkpicture.com/q/line_35331838825946.jpg"}}
                           cl.postTemplate(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention5"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           timeNow = datetime.now(tz=tz)
                           warna1 = ("#00ff00","#C0C0C0","#ffff00","#0000ff","#ff00ff","#00FFFF","#800000","#FF7F00","#BF00FF")
                           warnanya1 = random.choice(warna1)
                           data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "aspectRatio": "2:2",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "152px",
            "height": "25px",
            "cornerRadius": "0px",
            "position": "absolute",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "offsetBottom": "40px",
            "offsetTop": "172px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "aspectRatio": "2:4",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "152px",
            "height": "160px",
            "cornerRadius": "10px",
            "position": "absolute",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "offsetBottom": "40px",
            "offsetTop": "222px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔘𝔡𝔞𝔥 𝔡𝔦𝔟𝔦𝔩𝔞𝔫𝔤 𝔧𝔞𝔫𝔤𝔞𝔫 𝔱𝔞𝔤 𝔱𝔢𝔯𝔲𝔰",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "222px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔨𝔞𝔩𝔞𝔲 𝔨𝔞𝔫𝔤𝔢𝔫 𝔭𝔪 𝔞𝔧𝔞",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "234px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔫𝔤𝔢𝔶𝔢𝔩𝔫𝔶𝔞 𝔪𝔦𝔫𝔱𝔞 𝔞𝔪𝔭𝔲𝔫",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "244px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔬𝔧𝔬 𝔫𝔤𝔢𝔱𝔞𝔤 𝔱𝔯𝔲𝔰 𝔩𝔥𝔬 𝔩𝔢𝔨",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "254px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔨𝔞𝔩𝔞𝔲 𝔫𝔞𝔨𝔰𝔦𝔯 𝔟𝔦𝔩𝔞𝔫𝔤 𝔞𝔧𝔞",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "264px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔩𝔞𝔫𝔤𝔰𝔲𝔫𝔤 𝔡𝔦𝔡𝔢𝔭𝔞𝔫",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "274px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝔭𝔢𝔫𝔤𝔥𝔲𝔩𝔲",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "284px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "color": warnanya1,
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "margin": "none",
            "width": "220px",
            "offsetTop": "155px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "aspectRatio": "2:3",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "152px",
            "height": "152px",
            "cornerRadius": "0px",
            "position": "absolute",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "offsetBottom": "40px",
            "offsetTop": "20px",
            "offsetStart": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "154px",
            "height": "150px",
            "cornerRadius": "0px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": warnanya1,
            "offsetBottom": "40px",
            "offsetStart": "900px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "R E S P O N 5",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "offsetStart": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "color": warnanya1,
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "200px",
            "offsetStart": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str(cl.getProfileCoverURL(op.param2)),
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "offsetStart": "300px",
            "cornerRadius": "100px",
            "offsetBottom": "300px",
            "borderColor": warnanya1,
            "borderWidth": "1px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": warnanya1,
      },
      "styles": {
        "body": {         
         "backgroundColor": "#ffffff"
        }
      }
    }
  ]
}
}
                           cl.postTemplate(to, data)
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n°❂° STKID : " + msg.contentMetadata["STKID"] + "\n°❂° STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n°❂° STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate12(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            elif msg.toType == 1:
                to = receiver
            elif msg.toType == 2:
                to = receiver
            if msg.contentType == 0:
                to = receiver
            if msg.contentType == 16:
              if settings["checkPost"] == True:
                url = msg.contentMetadata["postEndUrl"]
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                warna6 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                warnanya6 = random.choice(warna6)
                warna4 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                warnanya4 = random.choice(warna4)
                warna5 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                warnanya5 = random.choice(warna5)
                cl.likePost(url[25:58], url[66:], likeType=1004)
                cl.createComment(url[25:58], url[66:], wait["comment"])
                cover = cl.getProfileCoverURL(sender)
                data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "kilo",
"body": {
"backgroundColor": warnanya4,
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
"size": "sm",
"aspectMode": "cover",
"aspectRatio": "2:2",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u8e603fce8dd01a68eeb8837342618f6d",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "0px",
"offsetStart": "0px",
"height": "0px",
"width": "0px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg", #"https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "sm",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "-100px",
"offsetStart": "0px",
"height": "110px",
"width": "160px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xs",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "5px",
"offsetStart": "2px",
"height": "150px",
"width": "50px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xs",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2",
"type": "uri",
}}],
"position": "absolute",
"borderWidth": "2px",
"cornerRadius": "8px",
"offsetTop": "2px",
"offsetStart": "2px",
"borderColor": warnanya5,
"height": "60px",
"width": "60px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": text,
"weight": "bold",
"color": warnanya4,
"size": "xs",
"offsetStart": "30px",
"offsetTop": "70px"
}
],
"position": "absolute",
"borderColor": warnanya6,
"borderWidth": "2px",
"cornerRadius": "8px",
"offsetTop": "15px",
"backgroundColor": warnanya5,
"offsetStart": "60px",
"height": "20px",
"width": "151px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": text,
                "color": warnanya6,
                "size": "xs",
                "margin": "xxl",
                "style": "normal",
                "decoration": "underline",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "borderColor": warnanya4,
            "borderWidth": "2px",
            "cornerRadius": "8px",
            "margin": "none",
            "backgroundColor": warnanya5,
            "height": "20px",
            "width": "151px",
            "offsetTop": "35px",
            "offsetStart": "60px"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#2bff44",
"align": "center",
"size": "xs",
"offsetTop": "3px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "12px",
#"backgroundColor": "#33ffff",
"offsetStart": "70px",
"height": "20px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xxs",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~behboaedan021",   
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xxs",
"action": {
"type": "uri",
"uri": "Https://smule.com/rs__family",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xxs",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
},{
"type": "image",
 "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xxs",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "5px",
"offsetStart": "-100px",
"height": "200px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " 💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
"weight": "bold",
"color": warnanya6,
"align": "center",
"size": "xs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "63px",
#"backgroundColor": "#ff0000",
"offsetStart": "-5px",
"height": "15px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " 👿Like done....",
"weight": "bold",
"color": warnanya4,
"align": "center",
"size": "sm",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "-2px",
#"backgroundColor": "#ff0000",
"offsetStart": "120px",
"height": "30px",
"width": "100px"
},
{
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "25px",
            "height": "25px",
            "offsetTop": "55px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": warnanya4,
            "offsetBottom": "1px",
            "offsetStart": "121px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "25px",
            "height": "25px",
            "offsetTop": "55px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": warnanya5,
            "offsetBottom": "1px",
            "offsetStart": "150px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "25px",
            "height": "25px",
            "offsetTop": "55px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": warnanya6,
            "offsetBottom": "1px",
            "offsetStart": "180px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
                "aspectMode": "cover",
                "position": "absolute",
                "size": "full"
              }
            ],
            "width": "25px",
            "height": "25px",
            "offsetTop": "55px",
            "cornerRadius": "100px",
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": warnanya4,
            "offsetBottom": "1px",
            "offsetStart": "210px"
          },
          {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#2bff44",
"size": "xs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "35px",
#"backgroundColor": "#0000ff",
"offsetStart": "70px",
"height": "15px",
"width": "85px"
}
],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "cornerRadius": "15px",
        "position": "relative",
        "borderColor": warnanya5,
      },
      "styles": {
        "body": {         
         "backgroundColor": warnanya6,
        }
}
},
]
}
}
                cl.postTemplate(to, data)
            if msg.contentType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate12(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13: #or op.type == 124:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            sendTextTemplate12(msg.to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  sendTextTemplate12(msg.to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break
                                  
               if msg.contentType == 13: # or op.type == 124:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                sendTextTemplate12(msg.to,"ᴅᴏɴᴇ ᴊᴇᴘɪᴛ ᴊᴏᴍʙʟᴏ\n➡" + _name)
                                wait["Invi"] = False
                                break
#=============MEDIA FOTOBOT=============
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate12(msg.to,"Send gambarnya...")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate12(msg.to,"ᴠɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ ᴅᴏɴᴇ")
               if msg.contentType == 1:
                  if msg._from in admin:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate12(msg.to, "ᴅᴏɴᴇ ɢᴀᴍʙᴀʀ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in admin:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate12(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in admin:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate12(msg.to, "ᴅᴏɴᴇ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in admin:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate12(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate12(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate12(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate12(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate12(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate12(msg.to,"ᴡᴇs ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate12(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate12(msg.to,"✅sᴛᴀғғ ᴅɪʜᴀᴘᴜs")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate12(msg.to,"❎bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate12(msg.to,"✅sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate12(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate12(msg.to,"✅ᴀᴅᴍɪɴ ᴅɪʜᴀᴘᴜs")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate12(msg.to,"itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate12(msg.to,"❎Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate12(msg.to,"✅Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate12(msg.to,"✅Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate12(msg.to,"❎Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate12(msg.to,"✅Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate12(msg.to,"✅Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate12(msg.to,"✅Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate12(msg.to,"❎Contact itu tidak ada di Talkban")
#WITHLIST
                 if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in ban["blacklist"]:
                        sendFooter(to,"「 Blacklist 」\nContact Already In Blacklist -_-")
                        wait["wblacklist"] = False
                    else:
                        ban["blacklist"].append(msg.contentMetadata["mid"])
                        sendFooter(to,"「 Blacklist 」\nSuccess Add Contact To Blacklist ^_^")
                        wait["wblacklist"] = False
                 if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in ban["blacklist"]:
                        ban["blacklist"].remove(msg.contentMetadata["mid"])
                        sendFooter(to,"「 Blacklist 」\nSuccess Delete Contact From Blacklist ^_^")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        sendFooter(to,"「 Blacklist 」\nContact Not In Blacklist -_-")
                 if wait["wwhitelist"] == True:
                    if msg.contentMetadata["mid"] in settings["whitelist"]:
                        sendFooter(to,"「 Whitelist 」\nContact Already In Whitelist -_-")
                        wait["wwhitelist"] = False
                    else:
                        settings["whitelist"].append(msg.contentMetadata["mid"])
                        sendFooter(to,"「 Whitelist 」\nSuccess Add Contact To Whitelist ^_^")
                        wait["wwhitelist"] = False
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate12(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendTextTemplate12(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")
               if msg.contentType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate12(msg.to, "ᴅᴏɴᴇ ᴘɪᴄᴛ ɢʀᴜᴘ")
               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate906(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path5 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to, "Sukses..")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate906(msg.to, str(helpMessage))
                        if cmd == "bot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate12(msg.to, "ʙᴏᴛ ᴡᴇs ᴏɴ")
                        elif cmd == "bot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate12(msg.to, "ʙᴏᴛ ᴡᴇs ᴍᴏᴅᴀʀ")
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	sendTextTemplate12(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")
                        elif cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage1 = helpcreator()
                               sendTextTemplate23(msg.to, str(helpMessage1))
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpsetting()
                               sendTextTemplate23(msg.to, str(helpMessage2))
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = media()
                               sendTextTemplate23(msg.to, str(helpMessage3))
                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpgroup()       
                               sendTextTemplate23(msg.to, str(helpMessage4))
                        elif cmd == "help5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpadmin()
                               sendTextTemplate23(msg.to, str(helpMessage5))
                        elif cmd == "help6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpghost()
                               sendTextTemplate23(msg.to, str(helpMessage6))
                        elif cmd == "help wl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage7 = helpwl()
                               sendTextTemplate906(msg.to, str(helpMessage7))
                        elif cmd == "help bl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage8 = helpbl()
                               sendTextTemplate906(msg.to, str(helpMessage8))
                        elif cmd == "menu":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Me\n✒ Cvp\n✒ Setting\n✒ Runtime\n✒ Speed-Sp\n✒ Tag\n✒ Bye\n✒ Lvall\n✒ Friendlist\n✒ Gruplist\n✒ Open [qr]\n✒ Close [qr]", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Set tag: [text]\n✒ Set tag2: [text]\n✒ Rtag: [Nogc]\n✒ Jepit\n✒ Block\n✒ Addme @\n✒ Mybot\n✒ Listpending\n✒ Blockcontact\n✒ Lkstblock\n✒ Listmid\n✒ Addasis", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Broadcast: [text]\n✒ Ceksider\n✒ Cekleave\n✒ Cekpesan\n✒ Cekrespon\n✒ Cekrespon2\n✒ Set sider:\n✒ Set pesan:\n✒ Set respon:\n✒ Set respon2\n✒ Set welcome:\n✒ Set leave:", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Like on/off\n✒ On/Off [sider]\n✒ Stag: jumlah\n✒ Stag @\n✒ Call: jumlah\n✒ Call\n✒ Scallto\n✒ Post on/off\n✒ Sticker on/off\n✒ Invite on/off\n✒ Unsend on/off\n✒ Respon on/off ", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Respon2 on/off\n✒ Autoadd on/off\n✒ Autoleave on/off\n✒ Autoblock on/off\n✒ Jointicket on/off\n✒ Addmp3\n✒ Addaudio\n✒ Addimg\n✒ Dellsticker\n✒ Dellaudio\n✒ Dellmp3\n✒ Dellvideo ", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Dellimg\n✒ Liststicker\n✒ Listimage\n✒ Listvideo\n✒ Listaudio\n✒ Listmp3\n✒ Lihat [no]\n✒ Cctv metro\n✒ Smule id\n✒ Joox text\n✒ Mp4 text\n✒ Mp3 text ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Youtube text\n✒ Yutube text\n✒ Getid @\n✒ Getmid @\n✒ Getbio @\n✒ Getinfo @\n✒ Getprofile @\n✒ Getpicture @\n✒ Info @\n✒ Kepo @\n✒ Ppvideo @\n✒ Kontak @ ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Contact: mid\n✒ Gname text\n✒ Mymid\n✒ Mybio\n✒ Myfoto\n✒ Myname\n✒ Myprofile\n✒ Mypicture\n✒ Mycover\n✒ Updategrup\n✒ Gruppict\n✒ Infogrup [no] ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Infomem [no]\n✒ Staf @\n✒ Stafdell @\n✒ Admin @\n✒ Admindell @\n✒ Reboot\n✒ Ban @ ", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#000000"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Bl\n✒ Ban:on @\n✒ Unban:on @\n✒ Unban @\n✒ Banlist\n✒ Cb\n✒ Refresh\n✒ Menu js\n✒  Menu respon\n✒ Menu sticker", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == "menu js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Kiss @\n✒ Gkick @\n✒ Pelakor [virus]\n✒ Jilat [kickall\n &virus]\n✒ Rusak [kickall] ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == "menu respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Respon on/off \n✒ Respon2 on/off \n✒ Respon3 on/off\n✒ Respon4 on/off\n✒ Respon5 on/off\n✒ ==========\n✒ ==========\n✒ St on/off\n✒ Notif on/off ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == "menu sticker":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Sedih\n✒ Hajar\n✒ Bobok\n✒ Asem\n✒ Assalamualaikum\n✒ Sip\n✒ Nyimak\n✒ Sebel\n✒ Capek\n✒ Mmuach\n✒ Peluk\n✒ Kangen\n✒ Thanks\n✒ Ok\n✒ Cium", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == ".menu sticker":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:5",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "265px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "270px",
            "offsetStart": "-14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n✒ Asemm\n✒ Adem\n✒ Muach\n✒ ngintip\n haha\n✒ Wkwk\n✒ Amin\n✒ Kabur\n✒ Siap\n✒ Maaf\n✒ Walaikumsalam\n✒ Absen", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#00ff00",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#C0C0C0",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#000000"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd.startswith("menu "):
                           if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                ky = key["MENTIONEES"][0]["M"]                
                                m = cl.getContact(ky)                                
                                data = {
                                       "type": "flex",
                                       "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴍᴇ\n◯ ᴠᴘ\n◯ sᴇᴛᴛɪɴɢ\n◯ ʀᴜɴᴛɪᴍᴇ\n◯ sᴘᴇᴇᴅ\n◯ sᴘ\n◯ sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n◯ ʙʏᴇᴍᴇ\n◯ ʀᴇᴊᴇᴄᴛ\n◯ ғʀɪᴇɴᴅʟɪsᴛ", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ʙᴏᴛᴀᴅᴅ\n◯ ʙᴏᴛᴅᴇʟʟ\n◯ sᴛᴀғғ\n◯ sᴛᴀғᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴ\n◯ ʀᴇʙᴏᴏᴛ\n◯ ʙᴀɴ\n◯ ʙʟᴄ\n◯ ʙᴀɴ:", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ɢᴍɪᴅ\n◯ ɢᴇᴛ ɪᴅ\n◯ ɢᴇᴛᴍɪᴅ\n◯ ɢᴇᴛʙɪᴏ\n◯ ɢᴇᴛɪɴғᴏ\n◯ ɢᴇᴛᴘʀᴏғɪʟᴇ\n◯ ɢᴇᴛᴘɪᴄᴛᴜʀᴇ\n◯ ɪɴғᴏ\n◯ ᴋᴇᴘᴏ\n◯ ᴘᴘᴠɪᴅᴇᴏ", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴄᴇᴋ sɪᴅᴇʀ\n◯ ᴄᴇᴋ ʟᴇᴀᴠᴇ\n◯ ᴄᴇᴋ ᴘᴇsᴀɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ²\n◯ sᴇᴛ sɪᴅᴇʀ:\n◯ sᴇᴛ ᴘᴇsᴀɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ²:\n◯ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Addsticker\n◯ Addmp3\n◯ Addaudio\n◯ Addimg\n◯ Dellsticker\n◯ Dellaudio\n◯ Dellmp3\n◯ Dellvideo\n◯ Dellimg\n◯ Liststicker", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴊsɴᴀᴍᴇ:\n◯ ᴀᴊsғᴏᴛᴏ\n◯ ᴀᴊs ᴄᴀɴᴄᴇʟ\n◯ ᴀᴊs ᴋɪᴄᴋᴀʟ\n◯ ᴀᴊs ᴀʙsᴇɴ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴄᴀɴᴄᴇʟᴀʟʟ\n◯ ᴄʀᴏᴛ\n◯ ɢᴋɪᴄᴋ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋᴏɴᴛᴀᴋ\n◯ ᴄᴏɴᴛᴀᴄᴛ:\n◯ ɢɴᴀᴍᴇ\n◯ ᴍʏᴍɪᴅ\n◯ ᴍʏʙɪᴏ\n◯ ᴍʏғᴏᴛᴏ\n◯ ᴍʏɴᴀᴍᴇ\n◯ ᴍʏᴘʀᴏғɪʟᴇ\n◯ ᴍʏᴘɪᴄᴛᴜʀᴇ\n◯ ᴍʏᴄᴏᴠᴇʀ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ sᴇᴛ ʟᴇᴀᴠᴇ:\n◯ ʟɪᴋᴇ\n◯ ᴘᴏsᴛ\n◯ sᴛɪᴄᴋᴇʀ\n◯ ɪɴᴠɪᴛᴇ\n◯ ᴜɴsᴇɴᴅ\n◯ ʀᴇsᴘᴏɴ\n◯ ʀᴇsᴘᴏɴ²\n◯ ᴀᴜᴛᴏᴀᴅᴅ\n◯ ᴡᴇʟᴄᴏᴍᴇ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Listimage\n◯ Listvideo\n◯ Listaudio\n◯ Listmp3\n◯ Lihat\n◯ Cctv metro\n◯ Ocmp4\n◯ Joox\n◯ mp4\n◯ mp3", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴍᴇɴᴜ ʜᴇʟᴘ",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋɪᴄᴋ\n◯ sᴛᴀʏ\n◯ ᴊs ɪɴ-ᴏᴜᴛ\n◯ ɢʟɪsᴛᴊs\n◯ ᴋ1-ɪɴᴠɪᴛ\n◯ ᴀᴅᴅᴀsɪs\n◯ ʙʀᴏᴀᴅᴄᴀsᴛ:\n◯ ɢʀᴜᴘᴘɪᴄᴛ\n◯ ɪɴғᴏɢʀᴏᴜᴘ ɴᴏ\n◯ ɪɴғᴏᴍᴇᴍ ɴᴏ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                                cl.postTemplate(to, data)

                        elif cmd.startswith("rname "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.renameContact(ls,sep[1])
                                        cl.sendReplyMention(msg_id, to, "Succes change @! display name to {}".format(sep[1]), [ls])

                        elif cmd == "sett":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                cover = cl.getProfileCoverURL(sender)
                                listTimeLiking = time.time()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = ""
                                if settings["checkPost"] == True: md+="║║😘 Post : ✅\n"
                                else: md+="║║😈 Post : ❌\n"
                                if wait["likeOn"] == True: md+="║║😘 Like : ✅\n"
                                else: md+="║║😈 Like ❌\n"
                                if wait["contact"] == True: md+="║║😘 Contact : ✅\n"
                                else: md+="║║😈 Contact : ❌\n"
                                if wait["Mentionkick"] == True: md+="║║😘 Notag : ✅\n"
                                else: md+="║║😈 Notag : ❌\n"
                                if wait["detectMention"] == True: md+="║║😘 Respontag : ✅\n"
                                else: md+="║║😈 Respontag : ❌\n"
                                if wait["detectMention2"] == True: md+="║║😘 Respontag2 : ✅\n"
                                else: md+="║║😈 Respontag2 : ❌\n"
                                if wait["Unsend"] == True: md+="║║😘 Unsend : ✅\n"
                                else: md+="║║😈 Unsend : ❌\n"
                                if wait["autoAdd"] == True: md+="║║😘 Autoadd : ✅\n"
                                else: md+="║║😈 Autoadd : ❌\n"
                                if wait["autoLeave"] == True: md+="║║😘 Autoleave : ✅\n"
                                else: md+="║║😈 Autoleave : ❌\n"
                                if wait["autoJoin"] == True: md+="║║😘 Autojoin : ✅\n"
                                else: md+="║║😈 Autojoin : ❌\n"
                                if wait["sticker"] == True: md+="║║😘 Sticker : ✅\n"
                                else: md+="║║😈 Sticker ❌\n"
                                if settings["autoJoinTicket"] == True: md+="║║😘 Jointicket : ✅\n"
                                else: md+="║║😈 Jointicket : ❌\n"
                                if wait["autoReject"] == True: md+="║║😘 Autoreject : ✅\n"
                                else: md+="║║😈 Autoreject : ❌\n"
                                if wait["autoBlock"] == True: md+="║║😘 Autoblock : ✅\n"
                                else: md+="║║😈 Autoblock : ❌\n"
                                if settings["welcome"] == True: md+="║║😘 Welcome : ✅\n"
                                else: md+="║║😈 Welcome : ❌\n"
                                sendTextTemplate906(msg.to, "╔════════════════\n"+ md +"╚════════════════")

                        elif text.lower() == "mid" or text.lower() == "mid":
                            data = {
                            "type": "text",
                            "text": "{}".format(msg._from),
                            "sentBy": {
                            "label":      "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "suek" or text.lower() == "sue":
                            data = {
                            "type": "text",
                            "text": "ᴋᴀʟᴏ ɢᴀᴋ sᴜᴇᴋ ᴍᴀɴᴀ ʙɪsᴀ ᴘɪᴘɪs ᴋᴋ😂",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "dul" or text.lower() == "dudul":
                            data = {
                            "type": "text",
                            "text": "ᴅᴜᴅᴜʟ ɪᴛᴜ ᴍᴀɴɪs ᴋᴋ",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 ??𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "sem" or text.lower() == "asem":
                            data = {
                            "type": "text",
                            "text": "ᴋᴀsɪʜ ɢᴜʟᴀ ᴅᴜᴀ ᴋɪʟᴏ ʙɪᴀʀ ᴍᴀɴɪs ᴋᴋ😂",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "pagi" or text.lower() == "esok":
                            data = {
                            "type": "text",
                            "text": "ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ sɪᴋᴀᴛ ɢɪɢɪ ᴋᴋ",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "siang" or text.lower() == "terang":
                            data = {
                            "type": "text",
                            "text": "ᴜᴅᴀʜ sɪᴀɴɢ ʏᴀ ᴋᴋ",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "sore" or text.lower() == "petang":
                            data = {
                            "type": "text",
                            "text": "ɴᴀʜ ᴡᴀᴋᴛᴜɴʏᴀ ɴɪᴋᴜɴɢ ᴋᴋ",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "flex" or text.lower() == "flx":
                            data = {
                            "type": "text",
                            "text": "\n Url flex in bots\n \n \n line://app/1602687308-GXq4Vvk9\n",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "malam" or text.lower() == "mlm":
                            data = {
                            "type": "text",
                            "text": "malam kk udah waktunya bobok😂",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "njir" or text.lower() == "anjir":
                            data = {
                            "type": "text",
                            "text": "ᴅɪᴍᴀɴᴀ ʏᴀɴɢ ʙᴀɴᴊɪʀ ᴋᴋ",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "kantuk" or text.lower() == "ngantuk":
                            data = {
                            "type": "text",
                            "text": "ᴍᴀɴᴅɪ ᴋᴀʟᴏ ɴɢᴀɴᴛᴜᴋ ᴋᴋ😂",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "ange" or text.lower() == "angen":
                            data = {
                            "type": "text",
                            "text": "ᴊᴇᴘɪᴛɪɴ ᴅɪᴘɪɴᴛᴜ ʙɪᴀʀ sᴇᴍʙᴜʜ ᴋᴋ",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "jawab" or text.lower() == "wasalam":
                            data = {
                            "type": "text",
                            "text": "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "waallaikumsalam" or text.lower() == "walaikumsalam":
                            data = {
                            "type": "text",
                            "text": "ᴘɪɴᴛᴇʀ ᴘᴀsᴛɪ ʀᴀᴊɪɴ ᴍᴇɴᴀʙᴜɴɢ ɴɪʜ",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "asalamualaikum" or text.lower() == "asalam":
                            data = {
                            "type": "text",
                            "text": "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "kampret" or text.lower() == "pret":
                            data = {
                            "type": "text",
                            "text": "ᴋᴀʀᴘᴇᴛ ɪᴛᴜ ʙᴜᴀᴛ ᴅɪʟᴀɴᴛᴀɪ ʏᴀᴋᴀɴ😂",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "susu" or text.lower() == "susu":
                            data = {
                            "type": "text",
                            "text": "sᴜsᴜ ᴋᴇɴᴛᴀʟ ᴄᴀᴘ ɴɢᴜᴛᴀɴɢ😂",
                            "sentBy": {
                            "label": "   💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "kopi" or text.lower() == "ngopi":
                            data = {
                            "type": "text",
                            "text": "ɴɢᴏᴘɪ ᴍᴜʟᴜ ᴋᴀᴘᴀɴ ɴʏᴜsᴜɴʏᴀ",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)                                                   
                                                     
                        elif text.lower() == "sepi" or text.lower() == "sepi":
                            data = {
                            "type": "text",
                            "text": "ɪʏᴀ ᴋᴀᴋ sᴇᴘɪ ᴘᴀᴋᴇᴛᴀɴ ᴘᴀᴅᴀ ʟɪᴍɪᴛ😂",
                            "sentBy": {
                            "label": "  💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                            "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                            "linkUrl": "line://nv/profilePopup/mid=u4de05f388b68f9910a3fe75124bc7ab2"}}
                            cl.postTemplate(to, data)
                         
                        elif text.lower() == "sedih":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data) 
                        
                                    
                        elif text.lower() =="hajar":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="bobok":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/52002761/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                        
                        elif text.lower() =="kiss":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/13386301/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="asem":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/72847952/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="assalamualaikum":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://www.linkpicture.com/q/unnamed-1_12.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="sip":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/4976950/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="nyimak":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/72847962/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="sebel":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/15417576/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="capek":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/64774429/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="kopi":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/64774422/ANDROID/sticker.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                              
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="mmuach" or text.lower() =="emuach" or text.lower() =="emmuach":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27533208/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="peluk":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/20943951/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="kangen":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27533210/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="thanks" or text.lower() =="makasi" or text.lower() =="terimakasih":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27533215/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="ok" or text.lower() =="oke" or text.lower() =="okay":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27533213/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="cium":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/52002737/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="asemm":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://www.linkpicture.com/q/06e3ef23edf41d0fc0f95d8cf30f9aac.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="dudul" or text.lower() =="pekok":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://www.linkpicture.com/q/1e92d8921a24d912c16a9f6af8acc534.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif text.lower() =="adem":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://www.linkpicture.com/q/unnamed_30.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="muach":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27533209/IOS/sticker_animation@2x.png",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="ngintip":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://www.linkpicture.com/q/209563.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="haha":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/xHDXBrd/AW316783-23.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="wkwk":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/9e/bb/f7/9ebbf7a320a06fb9a254b2f521bbd4ec.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="amin":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/c5/1d/da/c51ddaae928617f00f962eb96fd4af33.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="kabur":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/FsTqdpd/fac502b083ab70051050890b99bb6e73.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="siap":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/TKZ2KVD/AW316783-09.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif text.lower() =="maaf":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/LJXgPb2/AW316783-21.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data) 

                        elif text.lower() =="walaikumsalam":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/cgXn5dL/AW1575362-01.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data) 

                        elif text.lower() =="absen":
                        	if wait["jumbosticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/Rytk8fV/AW316783-08.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~waentur01"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif ("Gname " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gname ","")
                              cl.updateGroup(X)

                        elif "Gruppict" in msg.text:
                          if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                cl.sendImageWithURL(msg.to,path)

                        elif "Getprofile " in msg.text:
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        profile = cl.getContact(mention['M'])
                                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                                    except Exception as e:
                                        pass

                        elif "Getinfo " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            try:
                                sendTextTemplate12(msg.to,"Nama:\n" + contact.displayName)
                                sendTextTemplate12(msg.to,"Bio:\n" + contact.statusMessage)
                                cl.sendImageWithURL(msg.to,image)
                            except:
                                pass

                        elif cmd == 'listblock':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            sendTextTemplate23(to, msgs)

                        elif "Getbio " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            try:
                                sendTextTemplate12(msg.to,contact.statusMessage)
                            except:
                                sendTextTemplate12(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

                        elif text.lower() == 'kalender':
                          if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendTextTemplate23(msg.to, readTime)

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Amid}, contentType=13)
                               
                        elif cmd == "myname":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate12(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))

                        elif cmd == "mybio":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate906(to, "[ sᴛᴀᴛᴜs ʟɪɴᴇ ]\n{}".format(contact.statusMessage))

                        elif cmd == "Picture":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideo":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mycover":
                          if msg._from in admin:
                            channel = cl.getProfileCoverURL(sender)
                            path = str(channel)
                            cl.sendImageWithURL(to, path)

                        elif cmd.startswith("bc "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate12(group," " + str(pesan))
                        
                        elif cmd.startswith("bc2 "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                    sendTextTemplate12(group, " ☕ ʙʀᴏᴀᴅᴄᴀsᴛ \n\n" + str(pesan))
                                    time.sleep(1)
                               sendTextTemplate12(to,"Succes bc to {} group ".format(str(len(group))))
#broadcast
                        elif cmd.startswith("bct: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"ʙʀᴏᴀᴅᴄᴀsᴛ\n\n " + str(pesan))
                                   time.sleep(1)
                               sendTextTemplate12(to,"Succes bc to {} group ".format(str(len(group))))
                        elif cmd.startswith("bc1 "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
                                   "type": "text",
                                   "text": " ☕ ʙʀᴏᴀᴅᴄᴀsᴛ \n\n" + str(pesan),
                                   "sentBy": {
                                   "label":      "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                   "iconUrl": "https://phoneky.co.uk/thumbs/screensavers/down/misc/skull_fQlRnZS6.gif",
                                   "linkUrl": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg"}}
                                   cl.postTemplate(group, data)
                                   time.sleep(1)
                               sendTextTemplate12(to,"Succes bc to {} group ".format(str(len(group))))
                        elif cmd.startswith("kbc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               contact = cl.getContact(sender)
                               txt = text.replace(sep[0] + " ","")
                               friends = cl.getAllContactIds()
                               for friend in friends:
                                   cl.sendMessage(friend, wait["broad"] + "\n" + format(str(txt) + "\n {} ".format(contact.displayName)))
                                   time.sleep(1)
                               sendTextTemplate12(to,"Succes bc to {} friend ".format(str(len(friends))))
                               
                        elif cmd == "Profile":
                          if msg._from in admin:
                            text = "~ Profile ~"
                            contact = cl.getContact(sender)
                            cover = cl.getProfileCoverURL(sender)
                            result = "╔══[ Details Profile ]"
                            result += "\n├≽ Display Name : @!"
                            result += "\n├≽ Mid : {}".format(contact.mid)
                            result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                            result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n├≽ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            cl.sendMentionWithFooter(to, text, result, [sender])

                        elif cmd.startswith("block"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "sᴜᴋsᴇs ʙʟᴏᴄᴋ ᴋᴏɴᴛᴀᴋ" + str(contact.displayName) + "ᴍᴀsᴜᴋ ᴅᴀғᴛᴀʀ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif cmd.startswith("addme "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "ʙᴇʀʜᴀsɪʟ ᴀᴅᴅ" + str(contact.displayName) + "ᴋᴜʀɪɴᴇᴍ ᴅᴜʟᴜ ʏᴀᴄʜ")

                        elif "Getmid " in msg.text:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        cl.sendMessage(msg.to,str(mention['M']))
                                    except Exception as e:
                                        pass

                        elif "Contact: " in msg.text:
                           if msg._from in admin:
                              mmid = msg.text.replace("Contact: ","")
                              msg.contentType = 13
                              msg.contentMetadata = {"mid":mmid}
                              cl.sendMessage(msg.to, None, contentMetadata={'mid': mmid}, contentType=13)
                              path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                              image = 'http://dl.profile.line.naver.jp'+path
                              cl.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("kontak"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.sendContact(to,str(ls))

                        elif cmd.startswith("ppvideo"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(to, str(path))

                        elif text.lower() == "dell":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate12(msg.to,"wis resik boooss")
                               except:
                                   pass

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate23(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               sendTextTemplate23(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate23(msg.to, "key Now「 " + str(wait["keyCommand"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate23(msg.to, "ɢᴀɢᴀʟ ɴɢᴜʙᴀʜ ᴋᴇʏ")
                               else:
                                   wait["keyCommand"] = str(key).lower()
                                   sendTextTemplate906(msg.to, "sᴜᴋsᴇs ɢᴀɴᴛɪ ᴋᴇʏ「{}」".format(str(key).lower()))
#remot tagall
                        elif cmd.startswith("rtag: "):
                            	Croot = msg.text.split(":")
                            	Pepek = msg.text.replace(Croot[0] + ":"," ")
                            	Peler = cl.getGroupIdsJoined()
                            	Pokeh = Peler[int(Pepek)-1]                                                            
                            	CokAnCok = cl.getGroup(Pokeh)                                                            
                            	OlengKiller = [contact.mid for contact in CokAnCok.members]
                            	Celik = len(OlengKiller)//19
                    	        for Manik in range(Celik+1):
                            		txt = u''
                    		        s=0
                            		Bohay=[]
                            		for Jilat in CokAnCok.members[Manik*19 : (Manik+1)*19]:
                            			Bohay.append(Jilat.mid)
                            		RemotOlengKiller(Pokeh, Bohay)                            
                    		        sendTextTemplate12(msg.to, "Done, ᴋᴜʀᴀᴡᴀ Done\ndi Group: \n " + str(CokAnCok.name))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               wait["keyCommand"]=""
                               sendTextTemplate906(msg.to, "succes resset key command")

                        elif cmd == "/reboot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "ʀᴇsᴛᴀʀᴛ ʙᴏᴛ")
                               wait["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate906(msg.to, "ᴅᴏɴᴇ ʙᴏs")

                        elif cmd == "uih":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(sender)
                                G = cl.getGroup(to)
                                data = {
                                "type": "flex",
                                "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#ff0000",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 1
"url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "4:4",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": cover, #https://obs.line-scdn.net/{}".format(cl.getContact(sender).displayName),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #Wall 2
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:2",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "110px",
"width": "110px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🖐️ ɪᴢɪɴ ᴘᴀᴍɪᴛ",
"weight": "bold",
"color": "#ff0000",
"align": "center",
"size": "xxs",
"offsetTop": "3px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "9px",
#"backgroundColor": "#33ffff",
"offsetStart": "7px",
"height": "20px",
"width": "80px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~waentur01",   
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/BomberBSSI",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
},{
"type": "image",
 "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "9px",
"offsetStart": "90px",
"height": "200px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "?? "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ff00ff",
"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "87px",
#"backgroundColor": "#ff0000",
"offsetStart": "1px",
"height": "15px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ff00ff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "98px",
#"backgroundColor": "#0000ff",
"offsetStart": "7px",
"height": "15px",
"width": "90px"
}
],
#"backgroundColor": "#ff0000",
"paddingAll": "0px"
}
},
]
}
}
                                cl.postTemplate(to, data)
                                cl.leaveGroup(to)

                        elif text.lower() == "lvall":
                            if msg._from in admin:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Pamit semua group")

                        elif text.lower() == "rjall":
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    sendTextTemplate906(msg.to, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate906(msg.to, "Nothing Invited")

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔽ʙᴏᴛ ʀᴜɴ : " +waktu(eltime)
                               sendTextTemplate23(msg.to,bot)

                        elif cmd == "listpending":
                          if wait["selfbot"] == True:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return cl.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    #cl.sendReplyMessage(msg_id, to, str(ret_))
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(str(ret_)),
                                        "sentBy": {
                                            "label": " 💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                                            "iconUrl": "https://cdn140.picsart.com/296661791123201.gif?c256x256",
                                            "linkUrl": "line://nv/profilePopup/mid=u00e287effe898e54347d2ee6502d2ec2"
                                        }
                                    }
                                    cl.postTemplate(to, data)



                        elif cmd == "listmem":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                sendTextTemplate23(to, ret_)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate12(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                sendTextTemplate12(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate12(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(danil.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔══「 Info Group 」"
                                ret_ += "\n┣[]► Nama Group : {}".format(G.name)
                                ret_ += "\n┣[]► ID Group : {}".format(G.id)
                                ret_ += "\n┣[]► Pembuat : {}".format(gCreator)
                                ret_ += "\n┣[]► Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┣[]► Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┣[]► Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣[]► Group Qr : {}".format(gQr)
                                ret_ += "\n┣[]► Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══「 Info Finish 」"
                                sendTextTemplate23(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = denal.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n┣[]► "+ str(no) + ". " + mem.displayName
                                sendTextTemplate12(to,"╔══「 Group Info 」\n┣[]► Group Name : " + str(G.name) + "\n┣══「Member List」" + ret_ + "\n╚══「Total %i Members」" % len(G.members))
                            except:
                                pass
                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠[]► " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
                        
                        elif cmd == "addbot":
                            try:
                                cl.sendMessage(msg.to, "⏳ᴛᴜɴɢɢᴜ sᴇʟᴀᴍᴀ 5 ᴍᴇɴɪᴛ")
                                cl.findAndAddContactsByMid(Amid)
                                time.sleep(5)
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
                            except:
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
#NOTIF SMULE
                        elif "https://www.smule.com" in msg.text.lower():
                            if wait["smule"] == True:
                                nm = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                nm1 = re.findall(nm, text)
                                nm2 = []
                                for nm3 in nm1:
                                    if nm3 not in nm2:
                                        nm2.append(nm3)
                                for nm4 in nm2:
                                    nm5 = nm4
                                    api = BEAPI("oSqSQY5q7sk9") #isi api kamu
                                    res = api.smulePost(nm5)
                                    cl.sendImageWithURL(to,res["result"]["performance"]["cover_url"])
                                    sendTextTemplate12(to,res["result"]["performance"]["title"])
                                    if "video" in res["result"]["performance"]["type"]:
                                        cl.sendVideoWithURL(to,res["result"]["performance"]["video_media_mp4_url"])
                                    else:
                                        cl.sendAudioWithURL(to,res["result"]["performance"]["media_url"])

                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(to,[target])
                                   except:
                                       pass

                        elif cmd == "gl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┣[]► " + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                        
                        elif cmd == "addbot":
                            try:
                                cl.sendMessage(msg.to, "⏳ᴛᴜɴɢɢᴜ sᴇʟᴀᴍᴀ 5 ᴍᴇɴɪᴛ")
                                cl.findAndAddContactsByMid(Amid)
                                time.sleep(5)
                                cl.findAndAddContactsByMid(Bmid)
                                time.sleep(5)
                                cl.findAndAddContactsByMid(Zmid)
                                time.sleep(5)
                                js1.findAndAddContactsByMid(mid)
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
                                js1.sendMessage(to, "✓sᴜᴄᴄᴇss")
                            except:
                                cl.sendMessage(to, "✓sᴜᴄᴄᴇss") 
                                js1.sendMessage(to, "✓sᴜᴄᴄᴇss")
           
                        elif cmd == "qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                sendTextTemplate12(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   if X.preventedJoinByTicket == True:
                                       X.preventedJoinByTicket = False
                                       cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                sendTextTemplate12(msg.to, "Nama : "+str(X.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate906(msg.to, "Url Closed")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  sendTextTemplate906(to, "ᴛᴏᴛᴀʟ {} ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate12(to, "ʙᴇʀsɪʜ")
                                  
                        elif cmd.startswith("topnews"):
                              if msg._from in owner or msg._from in admin or msg._from in mid: 
                                  dpk=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=dpk.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  sendTextTemplate23(msg.to, str(hasil))
                                  cl.sendImageWithURL(msg.to, str(path))          
                                  
                        elif cmd.startswith('like '):
                        	if msg._from in owner or msg._from in admin or msg._from in mid:
                                    try:
                                        typel = [1001,1002,1003,1004,1005,1006]
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        a = cl.getContact(u).mid
                                        s = cl.getContact(u).displayName
                                        hasil = cl.getHomeProfile(a)
                                        st = hasil['result']['feeds']
                                        for i in range(len(st)):
                                            test = st[i]
                                            result = test['post']['postInfo']['postId']
                                            cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                            cl.createComment(str(sender), str(result), 'Ikut bae lah')
                                        sendTextTemplate12(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                    except Exception as e:
                                        cl.sendMessage(receiver, str(e))                            
#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate906(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")

                        elif cmd == "myfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate906(msg.to,"☛ sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate12(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd == "si":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate12(msg.to, "►sɪᴅᴇʀ ᴅɪʜɪᴅᴜᴘᴋᴀɴ►")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate12(msg.to, "►sɪᴅᴇʀ ᴅɪᴍᴀᴛɪᴋᴀɴ►")
                              else:
                                  sendTextTemplate12(msg.to, ":")
#=========== [ Hiburan] ============#
                        elif cmd.startswith("cctv metro"):
                          if msg._from in admin:
                            ret_ = "Daftar Cctv Pantura\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\nUntuk melihat cctv,\nKetik Lihat (Nomer)"                            
                            sendTextTemplate23(to, ret_)

                        elif cmd.startswith("lihat"):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "LIPUTAN CCTV TERKINI \nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Ketik Lihat nomer cctv selanjutnya"
                                    sendTextTemplate23(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                except:
                                    sendTextTemplate12(to, "🚦Data cctv tidak ditemukan!")

#============Comen Tag=========
                        elif cmd in ('sem','cok','purel','halo','tag'):
                              if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭━━━━━╦════════╦━━━━━╮\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢Daftar_member\n│╰━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢Total :{}Tersangka\n│╰━━━━━━━━━━━━━━━━━━━╯\n╰━━━━━╩════════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢Total:{}Tersangka\n│╰━━━━━━━━━━━━━━━━━━━━╯\n╰━━━━━╩════════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                        elif cmd == "hem" or text.lower() == 'cipok':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                sendTextTemplate12(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif (wait["NGENTOT"] == cmd):
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                sendTextTemplate12(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif 'set tag: ' in cmd:
                           if msg._from in admin:
                              spl = cmd.replace('set tag: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate12(msg.to, "Gagal mengganti Set Tagall")
                              else:
                                  wait["NGENTOT"] = spl
                                  sendTextTemplate12(msg.to, "「Set Msg」\nSet Tagall diganti jadi :\n\n「{}」".format(str(spl)))

                        elif (wait["JANJUK"] == cmd):
                           if wait["selfbot"] == True:
                              if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭━━━━━╦════╦━━━━━╮\n│╭━━━━━━━━━━━━━━━╮\n╠❂࿇➢Daftar_member\n│╰━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━╮"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━╮\n╠❂࿇➢Total :{}Tersangka\n│╰━━━━━━━━━━━━━━━╯\n╰━━━━━╩════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━━━━╮\n╠❂࿇➢Total:{}Tersangka\n│╰━━━━━━━━━━━━━━━━╯\n╰━━━━━╩════╩━━━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)

                        elif 'set tag2: ' in cmd:
                           if msg._from in admin:
                              spl = cmd.replace('set tag2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Set Tagall")
                              else:
                                  wait["JANJUK"] = spl
                                  sendTextTemplate906(msg.to, "「Set Msg」\nSet Tagall diganti jadi :\n\n「{}」".format(str(spl)))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               start = time.time()
                               sendTextTemplate906("u1638c6ae2cb49719c33ab35b56b884be", '.')
                               elapsed_time = time.time() - start
                               sendTextTemplate12(msg.to, "%s s" % (elapsed_time))
                         
                        elif cmd.startswith("kutub"):
                          if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyCxNem5XpY70Wi21g1VAWs36jLbPzjTJzc".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "size": "micro",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#ffffff"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#ffffff",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#1C1C1C",
                                                    "size": "xxs"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "xs",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "xxs",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#000000"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#000000",
                                                    "size": "xxs",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#000000",
                                                    "size": "xxs",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=ytmp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=ytmp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#000000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=ytmp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    cl.postTemplate(to, data)
                        elif cmd.startswith("ytmp4 "):
                          try:
                            sendTextTemplate12(to, "Waitting...")
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            dl = str(key)
                            vid = pafy.new(dl)
                            stream = vid.streams
                            for s in stream:
                              start = timeit.timeit()
                              vin = s.url
                            cl.sendVideoWithURL(to,vin)
                          except Exception as e:
                            return sendTextTemplate12(to,"YOUTUBE PLEASE UPDATE\n\n"+str(e))
                        elif cmd.startswith("ytmp3 "):
                          try:
                            sendTextTemplate12(to, "Waitting...")
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            vid = pafy.new(key)
                            audio = vid.audiostreams
                            for audio in audios:
                              audio = audio.url
                            cl.sendAudioWithURL(to,audio)
                          except Exception as e:
                            return sendTextTemplate12(to,"YOUTUBE PLEASE UPDATE\n\n"+str(e))
                        elif cmd.startswith("mp3: "):
                         # if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                sendTextTemplate23(msg.to, "📀ᴍᴜsɪᴋ ᴀᴜᴅɪᴏ")
                                cl.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                        elif cmd.startswith("ytlink "):
                           sendTextTemplate906(to, "Waiting...")
                           sep = text.split(" ")
                           search = text.replace(sep[0] + " ","")
                           params = {"search_query": search}
                           with requests.session() as web:
                             web.headers["User-Agent"] = random.choice(set["userAgent"])
                             r = web.get("https://www.youtube.com/results", params = params)
                             soup = BeautifulSoup(r.content, "html5lib")
                             ret_ = "╭━━━━━[ Youtube link di tampilkan ]"
                             datas = []
                             for data in soup.select(".yt-lockup-title > a[title]"):
                               if "&lists" not in data["href"]:
                                 datas.append(data)
                             for data in datas:
                               ret_ += "\n"+St+"[ {} ]".format(str(data["title"]))
                               ret_ += "\n"+St+"https://www.youtube.com{}".format(str(data["href"]))
                             ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                             cl.sendVideoWithURL(msg.to, me)
                             cl.sendAudioWithURL(msg.to, me)
                             cl.sendMessage(Id, to, str(ret_))
                        elif cmd == "news":
                           r=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                           data = r.text
                           x = json.loads(data)
                           if x["articles"] != []:
                            ret_ = []
                            for tube in x["articles"]:
                             if len(ret_) >= 20:
                              pass
                            else:
                             ret_.append({"type":"bubble","styles":{"header":{"backgroundColor":"#002321","separator":True,"separatorColor":"#23FF00"},"body":{"backgroundColor":"#002321","separator":True,"separatorColor":"#23FF00"},"footer":{"backgroundColor":"#002321","separator":True,"separatorColor":"#23FF00"}},"hero":{"type":"image","url":tube["urlToImage"],"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","spacing":"md","layout":"vertical","contents":[{"type":"box","spacing":"none","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#002321","height":"sm","action":{"type":"uri","label":"SITUS","uri":"https://"+tube["source"]["name"]}},{"type":"separator","color":"#302100"},{"type":"button","flex":2,"style":"primary","color":"#002321","height":"sm","action":{"type":"uri","label":"RADAR","uri":tube["url"]}}]}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"vertical","contents":[{"type":"text","text":"NEWS","color":"#35FF00","size":"md","weight":"bold","align":"center"},{"type":"separator","color":"#81FF00"},{"type":"text","text":tube["title"],"color":"#35FF00","size":"xxs"}]},{"type":"button","margin":"sm","style":"primary","color":"#E51A00","height":"sm","action":{"type":"uri","label":"🅿🆁🅰🅽🅺🅱🅾🆃🆂","uri":"https://bit.ly/2xbVxlh"}}]}})
                            k = len(ret_)//10
                            for aa in range(k+1):
                              cl.postTemplate(to, data)(to, {"type":"flex","altText":"{} semok".format(meProfile.displayName),"contents":{"type":"carousel","contents":ret_[aa*10:(aa+1)*10]}})
                        elif cmd.startswith("s.youtube "):
                           sep = text.split(" ")
                           msgg = text.replace(sep[0] + " ","")
                           cl.sendImageURL(to,"http://api.screenshotmachine.com/?key=3ae749&dimension=1920x1080&format=jpg&url=https://www.youtube.com/results?search_query=/{}".format(msgg))
                        elif cmd == "tube":
                           imgs = "https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=chrominium-logo&text=PrankBots&doScale=true&scaleWidth=430&scaleHeight=100"
                           r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=30&q=PrankBots&type=video&key=AIzaSyB7Zb9VteS6NsZFPY41FhGRzvMzAc3HBpM")
                           data = r.text
                           x = json.loads(data)
                           if x["items"] != []:
                             ret_ = []
                             for tube in x["items"]:
                              if len(ret_) >= 20:
                                pass
                              else:
                                ret_.append({"type":"bubble","styles":{"header":{"backgroundColor":"#000080"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000","separator":True,"separatorColor":"#FF000B"}},"header":{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://i.ibb.co/T4wVtG2/20210109-123328.jpg","size":"full","aspectRatio":"3:1"}]},"hero":{"type":"image","url":"https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(tube['id']['videoId']),"size":"full","aspectRatio":"4:5","aspectMode":"cover"},"body":{"type":"box","spacing":"md","layout":"horizontal","contents":[{"type":"box","spacing":"none","layout":"vertical","contents":[{"type":"image","url":"https://raw.githubusercontent.com/prankbots/logo/master/youtube.png","aspectRatio":"1:1","flex":1,"gravity":"center"},{"type":"image","url":"https://i.ibb.co/T4wVtG2/20210109-123328.jpg","aspectRatio":"1:1","flex":1,"gravity":"top"}]},{"type":"box","contents":[{"type":"text","text":"🅹🆄🅳🆄🅻🆅🅸🅳🅴🅾","color":"#FF0031","size":"md","weight":"bold","flex":1,"gravity":"top","align":"center"},{"type":"text","text":"%s"%tube['snippet']['title'],"color":"#00FF30","size":"xs","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","margin":"lg","color":"#81FF00"},{"type":"text","text":"🅿🅴🅽🅲🅰🆁??🅰🅽","color":"#FF0031","size":"md","weight":"bold","flex":1,"gravity":"top","align":"center"},{"type":"image","url":imgs,"size":"full","aspectRatio":"3:1","gravity":"top"}],"flex":2,"layout":"vertical"}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#009705","height":"sm","action":{"type":"uri","label":"MP3","uri":"line://app/1623679774-k9nBDB6b?type=text&text=convertermp3%20https://www.youtube.com/watch?v={}".format(str(tube['id']['videoId']))}},{"flex":3,"type":"button","margin":"sm","style":"primary","color":"#0009A8","height":"sm","action":{"type":"uri","label":"VIDEO","uri":"https://www.youtube.com/watch?v={}".format(str(tube['id']['videoId']))}},{"flex":2,"type":"button","margin":"sm","style":"primary","color":"#009705","height":"sm","action":{"type":"uri","label":"MP4","uri":"line://app/1623679774-k9nBDB6b?type=text&text=convertermp4%20https://www.youtube.com/watch?v={}".format(str(tube['id']['videoId']))}}]},{"type":"button","margin":"sm","style":"primary","color":"#E51A00","height":"sm","action":{"type":"uri","label":"💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍","uri":"https://bit.ly/2xbVxlh"}}]}})
                             k = len(ret_)//10
                             for aa in range(k+1):
                               data = {
                                 "type": "flex",
                                 "altText": "{} mengirim kont".format(cl.getContact(sender).displayName),
                                 "contents": {
                                   "type": "carousel",
                                   "contents": ret_[aa*10 : (aa+1)*10]
                                 }
                               }
                               cl.postTemplate(to, data)
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    sendTextTemplate12(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    sendTextTemplate12(msg.to, "Gagal clone profile")
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  clProfile.displayName = str(myProfile["displayName"])
                                  clProfile.statusMessage = str(myProfile["statusMessage"])
                                  clPofile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                  cl.updateProfile(clProfile)
                                  sendTextTemplate12(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  sendTextTemplate12(msg.to, "Gagal restore profile")
                        
                        elif cmd.startswith("ytb"):
                          if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyCxNem5XpY70Wi21g1VAWs36jLbPzjTJzc".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "size": "kilo",
                                        "body": {
                                          "type": "box",
                                          "layout": "vertical",
                                          "contents": [
                                            {
                                              "type": "image",
                                              "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(tube['id']['videoId']),
                                              "size": "full",
                                              "aspectMode": "cover",
                                              "aspectRatio": "1:1",
                                              "gravity": "top"
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "contents": [
                                                {
                                                  "type": "box",
                                                  "layout": "vertical",
                                                  "contents": [
                                                    {
                                                      "type": "text",
                                                      "text": "%s" % tube['snippet']['title'],
                                                      "size": "sm",
                                                      "color": "#ffffff",
                                                      "weight": "bold",
                                                      "align": "center"
                                                    }
                                                  ]
                                                },
                                                {
                                                  "type": "box",
                                                  "layout": "horizontal",
                                                  "contents": [
                                                    {
                                                      "type": "text",
                                                      "text": "👍",
                                                      "size": "sm",
                                                      "color": "#ffffff",
                                                      "weight": "bold",
                                                      "align": "center"
                                                    },
                                                    {
                                                       "type": "text",
                                                       "text": "💬",
                                                       "align": "center"
                                                    },
                                                    {
                                                      "type": "text",
                                                      "text": "⏱",
                                                      "align": "center"
                                                    },
                                                    {
                                                      "type": "text",
                                                      "text": "🎦",
                                                      "align": "center"
                                                    }
                                                  ],
                                                  "borderWidth": "3px",
                                                  "borderColor": "#ffff00"
                                                },
                                                {
                                                  "type": "box",
                                                  "layout": "vertical",
                                                  "contents": [
                                                    {
                                                      "type": "text",
                                                      "text": "deskripsi\n%s" % tube['snippet']['description'],
                                                      "size": "xs",
                                                      "wrap": True
                                                    }
                                                  ],
                                                  "backgroundColor": "#ffff00",
                                                  "borderColor": "#ffff00",
                                                  "borderWidth": "2px",
                                                  "height": "80px"
                                                },
                                                {
                                                  "type": "box",
                                                  "layout": "horizontal",
                                                  "contents": [
                                                    {
                                                      "type": "text",
                                                      "text": "VIDEO",
                                                      "size": "md",
                                                      "color": "#ffffff",
                                                      "weight": "bold",
                                                      "align": "center",
                                                        "action": {
                                                        "type": "uri",
                                                        "label": "action",
                                                        "uri": "line://app/1623679774-k9nBDB6b?type=text&text=converter%20https://www.youtube.com/watch?v={}".format(str(tube['id']['videoId']))
                                                       }
                                                     },
                                                     {
                                                      "type": "text",
                                                      "text": "MP3",
                                                      "size": "md",
                                                      "color": "#ffffff",
                                                      "weight": "bold",
                                                      "align": "center",
                                                      "action": {
                                                        "type": "uri",
                                                        "label": "action",
                                                        "uri": "line://app/1623679774-k9nBDB6b?type=text&text=converter%20https://www.youtube.com/watch?v={}".format(str(tube['id']['videoId']))
                                                      }
                                                    }
                                                  ]
                                                }
                                              ],
                                              "position": "absolute",
                                              "offsetBottom": "0px",
                                              "offsetStart": "0px",
                                              "offsetEnd": "0px",
                                              "backgroundColor": "#000000aa",
                                              "paddingAll": "20px",
                                              "paddingTop": "18p",
                                              "borderColor": "#ff0000",
                                              "borderWidth": "2px",
                                              "height": "190px"
                                            }
                                          ],
                                          "paddingAll": "0px",
                                          "borderColor": "#ff0000",
                                          "borderWidth": "2px"
                                         }
                                     })
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                      data = {
                                        "type": "flex",
                                        "altText": "youtube",
                                        "contents": {
                                          "type": "carousel",
                                          "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                      }
                                      cl.postTemplate(to, data)
                        elif cmd.startswith("converter ") or cmd.startswith("yt-info "):
                          try:
                            sendTextTemplate906(to, "Waitting...")
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            vid = pafy.new(key)
                            stream = vid.streams
                            audio = vid.audiostreams
                            for s in stream:
                              start = timeit.timeit()
                              vin = s.url
                            for audio in audios:
                              audio = audio.url
                              judul = '•Judul: ' + str(vid.title)
                              author = '•Creator: ' + str(vid.author)
                              durasi = '•Durasi: ' + str(vid.duration)
                              suka = '•Like: ' + str(vid.likes)
                              dislike = '•Dislike : ' +str(vid.dislikes)
                              rating = '•rating: ' + str(vid.rating)
                              tonton = '•Ditonton    : ' +str(vid.viewcount)+ 'x'
                              kategori = '•kategori: ' + vid.category
                              penerbit = '•Penerbit : ' +str(vid.username)
                              img = "https://i3.ytimg.com/vi/{}/maxresdefault.jpg".format(str(vid.videoid))
                            data = {
                              "type": "flex",
                              "altText": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                              "contents": {
                                "type": "bubble",
                                "size": "micro",
                                "body": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "image",
                                      "url": img,
                                      "size": "full",
                                      "aspectMode": "cover",
                                      "aspectRatio": "1:1",
                                      "gravity": "top",
                                      "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": vin
                                      }
                                    },
                                    {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": judul,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px",
                                          "text": author
                                        },
                                        {
                                          "type": "text",
                                          "text": durasi,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "text": suka,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "text": dislike,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "text": rating,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "text": kategori,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "text": tonton,
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px"
                                        },
                                        {
                                          "type": "text",
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "xs",
                                          "offsetTop": "3px",
                                          "text": penerbit
                                        }
                                      ],
                                      "position": "absolute",
                                      "cornerRadius": "20px",
                                      "offsetTop": "5px",
                                      "backgroundColor": "#000080aa",
                                      "offsetStart": "5px",
                                      "height": "150px",
                                      "width": "250px",
                                      "borderColor": "#ffff00",
                                      "borderWidth": "3px"
                                    },
                                    {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "klik to play video",
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "md",
                                          "offsetTop": "3px",
                                          "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=convertermp4%20https://www.youtube.com/watch?v={}".format(str(vid.videoid))
                                          }
                                        }
                                      ],
                                      "position": "absolute",
                                      "cornerRadius": "20px",
                                      "offsetTop": "350px",
                                      "backgroundColor": "#000080",
                                      "height": "50px",
                                      "borderColor": "#ffff00",
                                      "borderWidth": "2px",
                                      "offsetStart": "90px"
                                    },
                                    {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "klik to pay audio",
                                          "color": "#ffffff",
                                          "align": "start",
                                          "size": "md",
                                          "offsetTop": "3px",
                                          "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=convertermp3%20https://www.youtube.com/watch?v={}".format(str(vid.videoid))
                                          }
                                        }
                                      ],
                                     "position": "absolute",
                                     "cornerRadius": "20px",
                                     "offsetTop": "300px",
                                     "backgroundColor": "#000080",
                                     "height": "50px",
                                     "borderColor": "#ffff00",
                                     "borderWidth": "3px",
                                      "offsetStart": "90px"
                                    }
                                  ],
                                  "paddingAll": "0px",
                                  "borderColor": "#ffff00",
                                  "borderWidth": "2px"
                                }
                              }
                            }
                            cl.postTemplate(to, data)
                          except Exception as e:
                            return sendTextTemplate906(to,"SABAR....\n\n"+str(e))
                        
                        elif cmd == "galeri":
                          sendTextTemplate906(to, plate["galery"])
                        elif cmd.startswith("convertermp4 "):
                          try:
                            sendTextTemplate906(to, "Waitting...")
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            dl = str(key)
                            vid = pafy.new(dl)
                            stream = vid.streams
                            for s in stream:
                              start = timeit.timeit()
                              vin = s.url
                            cl.sendVideoWithURL(to,vin)
                          except Exception as e:
                            return sendTextTemplate906(to,"YOUTUBE PLEASE UPDATE\n\n"+str(e))
                        elif cmd.startswith("convertermp3 "):
                          try:
                            sendTextTemplate906(to, "Waitting...")
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            vid = pafy.new(key)
                            audio = vid.audiostreams
                            for audio in audios:
                              audio = audio.url
                            cl.sendAudioWithURL(to,audio)
                          except Exception as e:
                            return sendTextTemplate906(to,"YOUTUBE PLEASE UPDATE\n\n"+str(e))
                        elif cmd.startswith("smule "):                       	
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split(" ")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "╔══[ ✯ ʟɪsᴛsᴍᴜʟᴇ ✯ ]"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n╠•➣" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n╚══[ ✯ʟɪsᴛsᴍᴜʟᴇ✯ ]"
                                ret_ += "\nᴋᴇᴛɪᴋ: sᴍᴜʟᴇ{}ɴᴏᴍᴏʀ".format(str(search))
                                sendTextTemplate23(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "\n╠•➣ᴊᴜᴅᴜʟ ʟᴀɢᴜ: "+str(b["title"])
                                    c += "\n╠•➣ᴄʀᴇᴀᴛᴏʀ: "+str(b["owner"]["handle"])
                                    c += "\n╠•➣ʟɪᴋᴇ: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\n╠•➣ᴄᴏᴍᴍᴇɴᴛ: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\n╠•➣sᴛᴀᴛᴜs ᴏᴄ: "+str(b["message"])
                                    c += "\n╠•➣ᴅɪ ᴅᴇɴɢᴀʀᴋᴀɴ: {}".format(b["stats"]["total_listens"])+" orang"
                                    c += "\n╚══[ ✯ᴡᴀɪᴛ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ✯ ]"
                                    hasil = "╔══[ ✯ ᴅᴇᴛᴀɪʟsᴍᴜʟᴇ ✯ ]"+str(c)
                                    dl = str(b["cover_url"])
                                    data = {
                                        "type": "flex",
                                        "altText": "Audio Smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000ff" #999999"
    },
    "footer": {
      "backgroundColor": "#0000ff" #2f2f4f" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
          },{
            "contents": [
              {
            "text": "⚡S̸͟͞E̸͟͞L̸͟͞F̸͟͞B̸͟͞O̸͟͞T̸͟͞ T̸͟͞E̸͟͞M̸͟͞P̸͟͞L̸͟͞A̸͟͞T̸͟͞E̸͟͞⚡",
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
 },
{
"type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQtKJ9DZZjfaSZtDWapDmdO1bVccjThrGsrLARUW0ZVu2SqHTTI",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~waentur01",             
           }, 
            "flex": 1   
            },
            {
     "type": "separator",
           "color": "#33ffff"
           },
           {
            "contents": [
            {           
           "type": "separator",
           "color": "#33ffff"
           },
           {
            "type": "image",
            "url": dl, #"https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/BomberBSSI",
            },         
            "flex": 1
}
],
   "type": "box",
   "spacing": "xs",
   "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
"contents": [{"type":"separator","color": "#33ffff"},{"contents": [{"text": "🎙️ᴊᴇᴍᴘᴏʟ: "+str(b["stats"]["total_loves"])+" like","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ɴʏɪᴍᴀᴋ: {}".format(b["stats"]["total_listens"])+" orang","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ᴠᴏᴄᴀʟ: "+str(b["owner"]["handle"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️"+str(b["title"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "xs","layout": "vertical"    
},{"type": "separator","color": "#33ffff"}],"type": "box","spacing": "xs","layout": "horizontal"   },{"type": "separator","color": "#33ffff"},{
"contents": [         
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~waentur01",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/BomberBSSI",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                    cl.postTemplate(to, data)
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            cl.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            cl.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    cl.sendReplyMessage(msg.id,msg.to,"Result Error:\n"+str(e))
#===========COMEN PANGGILAN======
                        elif cmd.startswith("tag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate906(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("call: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate906(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("stag"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage901(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        sendTextTemplate906(msg.to,"Jumlah melebihi 1000")
                        elif msg.text.lower().startswith("naik "):
                          if msg._from in admin:
                           if 'MENTION' in msg.contentMetadata.keys()!= None:
                               names = re.findall(r'@(\w+)', text)
                               mention = eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               lists = []
                               for mention in mentionees:
                                   if mention["M"] not in lists:
                                       lists.append(mention["M"])
                               for ls in lists:
                                   contact = cl.getContact(ls)                          
                                   jmlh = int(wait["limit"])
                                   sendTextTemplate906(msg.to, "Succes {} Call Grup".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                     for x in range(jmlh):
                                         try:
                                             mids = [contact.mid]
                                             cl.acquireGroupCallRoute(msg.to)
                                             cl.inviteIntoGroupCall(msg.to,mids)
                                         except Exception as e:
                                             cl.sendMessage(msg.to,str(e))
                                     else:
                                         sendTextTemplate12(msg.to,"")
                        elif cmd == "cpg":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate12(msg.to, "Sukses Call {} diGrup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate12(msg.to,"Jumlah melebihi batas")
                        elif cmd.startswith("scallto "):
                                dan = text.split(" ")
                                num = int(dan[1])
                                ret_ = "╭───[ Spamcall Mention ]"
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            group = cl.getGroup(to)
                                            members = [ls]
                                            cl.acquireGroupCallRoute(to)
                                            cl.inviteIntoGroupCall(to, contactIds=members)
                                        ret_ += "\n├ @!"
                                    ret_ += "\n╰───[ Total {} Spam call]".format(str(dan[1]))
                                    sendMention(to, ret_, lists)
#==========Comen Spam==={{{
                        elif cmd.startswith("unsend "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            args = text.replace(sep[0] + " ","")
                            ttl = "「UNSEND」"
                            mes = int(sep[1])
                            M = cl.getRecentMessageV2(to, 1001)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == cl.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                cl.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.daemon = True
                                thread1.start()
                                thread1.join()
                                cl.unsendMessage(msg.id)
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate906(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate906(msg.to, "「Dinonaktifkan」\n" + msgs)
#===============Coment kickall============
                        elif ("Kiss" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                       	cl.kickoutFromGroup(to,[target])
                                       except:
                                           sendTextTemplate906(msg.to,"Sorry kaki saya struk..")

                        elif "Gkick " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitetion(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif ("Awas" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           cl.kickoutFromGroup(msg.to, [target])
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           cl.sendMessage(to, "Kakiku Struk Boss")
                        elif cmd == "gasken" or text.lower() == '.kuy':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Kosong.....")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in admin:
                                       klist=[mid]
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.00001)
                                       print (msg.to, [x])
                          if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for a in admin:
                                    if a in targets:
                                        try:
                                            targets.remove(a)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist=[mid]
                                        cl.cancelGroupInvitation(msg.to, [x])
                                        cl.kickoutFromGroup(msg.to,[target])
                                        time.sleep(0.00001)
                                        print (msg.to,[g.mid])
                                    except:
                                        pass
                        elif cmd == ".jilat":
                          if wait["selfbot"] == True:                            
                               cl.sendMessage(msg.to, "ngeblank ya brooo maaf broo layar hpnya aq pinjam bentar    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")
                        elif cmd == ".pelakor":
                          if wait["selfbot"] == True:                            
                               cl.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.??.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.??.👿.")
#kickall
                        if "Tolak" in msg.text:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _dn in gMembMids:
                                  if _dn not in Bots:
                                    random.choice(KAC).cancelGroupInvitetion(to,[_dn])
                        if "!ngewe" in msg.text:
                          if msg._from in admin:
                             start = time.time()
                             time.sleep(0.00001)
                             nk0 = msg.text.replace("!ngewe","")
                             nk1 = nk0.lstrip()
                             nk2 = nk1.replace("@","")
                             nk3 = nk2.rstrip()
                             _name = nk3
                             gs = cl.getGroup(msg.to)
                             targets = []
                             for s in gs.members:
                                 if _name in s.displayName:
                                    targets.append(s.mid)
                             if targets == []:
                                 pass
                             else:
                                 for target in targets:
                                    if target not in Bots:
                                      try:
                                          wait["blacklist"][target] = True
                                          klist=[cl]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          pass
                                          
                        elif msg.text in ["Angewe"]:
                            if msg._from in admin:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                group = cl.getGroup(msg.to)
                                targets = [contact.mid for contact in group.members]
                                for target in targets:
                                    time.sleep(0.2)
                                    if target not in Bots:
                                        if target not in admin:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                            except:
                                                pass
                                   
                        elif cmd == "pites" or text.lower() == 'jilat':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Kosong.....")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Bots:
                                       klist=[mid]
                                       cl.cancelGroupInvitetion(to, [x])
                                       time.sleep(0.00001)
                                       print (msg.to, [x])
                          if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for a in admin:
                                    if a in targets:
                                        try:
                                            targets.remove(a)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist=[mid]
                                        cl.kickoutFromGroup(to,[target])
                                        time.sleep(0.00001)
                                        print (msg.to,[g.mid])
                                    except:
                                        pass
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.deleteSelfFromChat(msg.to)
                        elif msg.text in ["Asange"]:
                            if msg._from in admin:
                                X = cl.getGroup(msg.to)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)                                
                                group = cl.getGroup(msg.to)
                                targets = [contact.mid for contact in group.invitee]
                                for target in targets:
                                    time.sleep(0.4)
                                    if target not in Bots:
                                        if target not in admin:
                                            try:
                                                random.choice(KAC).cancelGroupInvitetion(msg.to,[target])
                                            except:
                                                pass
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                vl.updateGroup(G)
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to, "❂➢ʙʏᴇ ʙʏᴇ ғᴀᴍs "+str(G.name))
                                cl.deleteSelfFromChat(msg.to)

#=========COMEN RESPON======#
                        elif msg.text in ["Jepit"]:
                            if msg._from in admin:
                                wait["Invi"] = True
                                sendTextTemplate906(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        elif "Rusak" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("Rusak","")
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 cl.sendText(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[cl]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                wait["detectMention2"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = True
                                wait["detectMention"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "respon2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "respon3 on" or text.lower() == 'respon3 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention3"] = True
                                wait["detectMention2"] = False
                                wait["detectMention"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ3 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon3 off" or text.lower() == 'respon3 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention3"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ3 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "respon4 on" or text.lower() == 'respon4 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention4"] = True
                                wait["detectMention3"] = False
                                wait["detectMention2"] = False
                                wait["detectMention"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ4 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon4 off" or text.lower() == 'respon4 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention4"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ4 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "respon5 on" or text.lower() == 'respon5 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention5"] = True
                                wait["detectMention4"] = False
                                wait["detectMention3"] = False
                                wait["detectMention2"] = False
                                wait["detectMention"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ5 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon5 off" or text.lower() == 'respon5 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention5"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ5 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate906(msg.to,"ʀᴇsᴘᴏɴ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate906(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate906(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notif on" or text.lower() == 'notif on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["nCall"] = True
                                sendTextTemplate906(msg.to,"notifcall ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notif off" or text.lower() == 'notif off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["nCall"] = False
                                sendTextTemplate906(msg.to,"notifcall ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notifcall on" or text.lower() == 'notifcall on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = True
                                sendTextTemplate906(msg.to,"notifcall ᴍᴏᴅᴇ ᴏɴ")                                
                        elif cmd == "notifcall off" or text.lower() == 'notifcall off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = False
                                sendTextTemplate906(msg.to,"notifcall ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "yt on" or text.lower() == 'yt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["media"] = True
                                sendTextTemplate906(msg.to,"media ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "yt off" or text.lower() == 'yt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["media"] = False
                                sendTextTemplate906(msg.to,"media ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate906(msg.to,"ʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate906(msg.to,"ʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate906(msg.to,"ᴀᴅᴅ ᴍᴏᴅᴇ ᴏn")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate906(msg.to,"ᴀᴅᴅ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate906(msg.to,"sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate906(msg.to,"sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "stc on" or text.lower() == 'st on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["jumbosticker"] = True
                                sendTextTemplate906(msg.to,"sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "stc off" or text.lower() == 'st off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["jumbosticker"] = False
                                sendTextTemplate906(msg.to,"sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate906(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate906(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate906(msg.to,"ʙʟᴏᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                sendTextTemplate906(msg.to,"ʙʟᴏᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "post on" or text.lower() == 'post on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = True
                                sendTextTemplate906(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "post off" or text.lower() == 'post off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = False
                                sendTextTemplate906(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "like on" or text.lower() == 'like on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = True
                                sendTextTemplate906(msg.to,"ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "like off" or text.lower() == 'like off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = False
                                sendTextTemplate906(msg.to,"ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplate906(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplate906(msg.to,"ɪɴᴠɪᴛᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["Unsend"] = True
                                sendTextTemplate906(msg.to, "Unsend mode on")
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["Unsend"] = False
                                sendTextTemplate906(msg.to, "Unsend mode off")
                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                wait['autoReject'] = False
                                sendTextTemplate906(msg.to,"❎Reject already Off")
                            elif xres == "on":
                                wait['autoReject'] = True
                                sendTextTemplate906(msg.to,"✅Reject already On")
                        elif cmd == "autoread on":
                            if msg._from in admin:
                                if settings["autoRead"] == True:
                                    sendTextTemplate906(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate906(to, "Berhasil mengaktifkan auto read")

                        elif cmd == "autoread off":
                            if msg._from in admin:
                                if settings["autoRead"] == False:
                                    sendTextTemplate906(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate906(to, "Berhasil menonaktifkan auto read")
                        elif cmd.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    wait["comment"] = txt
                                    sendTextTemplate23(to, "❂Done Mengubah Pesan\n❂CommentTL:\n❂ {}".format(txt))
                                except:
                                    sendTextTemplate23(to, "❂Failed")
#==================================#
                        elif cmd == "refresh" or text.lower() == 'seger':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate12(msg.to,"Clean..")
                                sendTextTemplate12(msg.to,"Refresh done 💯")
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate906(msg.to,"✅Berhasil menambahkan admin")
                                       except:
                                           pass
#smule download
#==============================================================
                        elif "kutub" in msg.text.lower():
                            if wait["media"] == True:
                                try:
                                    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                    links = re.findall(regex, text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for urla in n_links:
                                        zagus = urla
                                        link = pafy.new(zagus)
                                        v=link.streams
                                        for a in v:
                                            mp3=a.url
                                        cl.sendAudioWithURL(to,mp3)
                                        for b in v:
                                            mp4=b.url
                                        cl.sendVideoWithURL(to,mp4)
                                except:pass
                                    #cl.sendMessage(to, str(e))
                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate906(msg.to,"✅Berhasil menambahkan staff")
                                       except:
                                           pass
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate906(msg.to,"✅Berhasil menghapus admin")
                                       except:
                                           pass
                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate906(msg.to,"✅Berhasil menghapus admin")
                                       except:
                                           pass
#===========COMMAND BLACKLIST============#                       
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate906(msg.to,"✅Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate906(msg.to,"✅menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate906(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate906(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "wanted" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate906(msg.to,"Tak ada daftar buronan")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate23(msg.to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))
                                   
                        elif cmd == "blc" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   sendTextTemplate906(msg.to,"Janda kosong")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "cban" or text.lower() == 'bebas':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」Bersih" % len(ragets)
                              sendTextTemplate906(msg.to,"Janda bodong dibebaskan" +mc)
#==========Setting bot========
                        elif 'Set hapus: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set hapus: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Pesan clear")
                              else:
                                  wait["dell"] = spl
                                  sendTextTemplate906(msg.to, "「clear」\clearl diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate906(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate906(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set ghost: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set ghost: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Ghost Msg")
                              else:
                                  wait["flexghost"] = spl
                                  sendTextTemplate906(msg.to, "「Ghost Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set autoleave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autoleave: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Autoleave Msg")
                              else:
                                  wait["autoLave"] = spl
                                  sendTextTemplate906(msg.to, "「Autoleave Msg」\nAutoleave Msg diganti jadi :\n\n「{}」".format(str(spl)))
                         elif 'Set bc: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set bc: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Broadcast Msg")
                              else:
                                  wait["broad"] = spl
                                  sendTextTemplate906(msg.to, "「Broadcast Msg」\n Broadcast Msg diganti jadi :\n\n「{}」".format(str(spl)))
         
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon3: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon3: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag3"] = spl
                                  sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon4: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon4: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag4"] = spl
                                  sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))                                                                
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate906(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate906(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Autoleave Msg」\nAutoleave Msg mu :\n\n「 " + str(wait["autoleave"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek respon2":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag2"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate906(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
#___________________HIBURAN____________________                                               
                        elif cmd == "me2" or text.lower() == 'gue':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                          #      cover = cl.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "♻️𝖉𝖚𝖉𝖚𝖑 𝖇𝖔𝖙𝖘♻️",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000ff"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#ff0000"            
      },
      {
        "type": "separator",
        "color": "#ff0000"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#ff0000"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#ff0000"
         },
         {
            "text": "♻️𝖉𝖚𝖉𝖚𝖑",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "𝖇𝖔𝖙𝖘♻️️",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#ff0000"
           },
             {
            "text": "ᴱᴸᴵᵀᴱ",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#ff0000"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~waentur01",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#ff0000"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(sender).displayName),
"weight": "bold",
"color": "#000080",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#ff0000"
},{
"type": "text",
"text": "🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"ᴡɪʙ"),
"weight": "bold",
"color": "#000080",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#ff0000"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#ff0000"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#ff0000"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#ff0000"
            },
           {
          "type": "text",
"text": "sᴛᴀᴛᴜs ",
"weight": "bold",
"color": "#000080",
"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#ff0000"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#ff0000"
            },
           {
          "text": "{}".format(status.statusMessage),
           "size": "xxs",
          "align": "center",
           "color": "#000080",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#ff0000"
         },
         {
            "text": "♻️𝖉𝖚𝖉𝖚𝖑 ",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#ff0000"
           },
             {
            "text": "𝖇𝖔𝖙𝖘♻️",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#ff0000"
           },
             {
            "text": "ᴱᴸᴵᵀᴱ",
            "size": "xxs",
            "color": "#000080",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#ff0000"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#ff0000"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/T4wVtG2/20210109-123328.jpg",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~waentur01",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/h9nLycK/1617387582638.gif", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/joker_alva",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#ff0000"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#000080",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#ff0000"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                warna6 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                                warnanya6 = random.choice(warna6)
                                warna4 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                                warnanya4 = random.choice(warna4)
                                warna5 = ("#76560B","#696969","#09616B","#8B055A","#03137F","#6A037F","#7F3403")
                                warnanya5 = random.choice(warna5)
                                status = cl.getContact(sender)
                                cover = cl.getProfileCoverURL(sender)
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": warnanya5,
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": warnanya6,
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": warnanya4,
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xxs",
                "color": warnanya4,
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": warnanya6,
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": warnanya4,
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": warnanya6,
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": warnanya4,
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(sender)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": warnanya5,
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": warnanya6,
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": warnanya4,
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "💎𝒅𝒖𝒅𝒖𝒍 𝒃𝒐𝒕𝒔✍",
                "size": "xxs",
                "color": warnanya5,
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": warnanya6,
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": warnanya4,
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/h9nLycK/1617387582638.gif",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": warnanya5,
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": warnanya6,
        "cornerRadius": "10px",
        "height": "200px"      
      }
      }
  ]
}
                                cl.postFlex(to, data)
                        elif cmd == "mempict":
                              if msg._from in admin:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~waentur01"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{} membagikan janda".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)        
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            #if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate12(msg.to, "Aing Lebet: %s" % str(group.name))
#===========add img============#                                                                                
                        elif text.lower() == "cekbot":
                            if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u1638c6ae2cb49719c33ab35b56b884be"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u1638c6ae2cb49719c33ab35b56b884be"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "😠"
                               else:sil = "😥"
                               if has1 == "OK":sil1 = "😠"
                               else:sil1 = "😥"
                               sendTextTemplate12(to, "Kick: {} \nInvite: {}".format(sil1,sil))
#===============HIBURAN============================#
                        elif cmd.startswith("addmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(msg.to,"Silahkan kirim mp3 nya...") 
                                else:
                                    sendTextTemplate12(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(msg.to, "Done hapus mp3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate12(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Music ❳════\n"
                                for audio in audios:
                                    ret_ += "┣[]◇  " + audio.title() + "\n"
                                ret_ += "╚═══❲ {} Record  ❳════".format(str(len(audios)))
                                sendTextTemplate12(to, ret_)

                        elif cmd.startswith("addsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("Sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(to, "Silahkan kirim stickernya...") 
                                else:
                                    sendTextTemplate12(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate12(to, "Sticker ada di list") 
                                                   
                        elif cmd == "liststicker":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Sticker ❳════\n"
                                for sticker in stickers:
                                    ret_ += "┣[]◇  " + sticker.title() + "\n"
                                ret_ += "╚═══❲  {} Stickers  ❳════".format(str(len(stickers)))
                                sendTextTemplate12(to, ret_)

                        elif cmd.startswith("addimg "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(to, "Silahkan kirim fotonya")
                                else:
                                    sendTextTemplate12(to, "Foto Udah dalam list")

                        elif cmd.startswith("dellimg "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate12(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate12(to, "Foto ada dalam list")

                        elif cmd == "listimage":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Image 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Image 」".format(str(len(audios)))
                                sendTextTemplate12(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate12(to, "Silahkan kirim video nya...")
                                else:
                                    sendTextTemplate12(to, "video sudah ada")
                        elif cmd.startswith("dellvideo "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate12(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate12(to, "video tidak ada")

                        elif cmd == "listvideo":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Video 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Video 」".format(str(len(audios)))
                                sendTextTemplate12(to, ret_)
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
    	logError(e)                      
                                     
                               
