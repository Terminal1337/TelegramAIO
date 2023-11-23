from smsactivate.api import SMSActivateAPI
from pathlib import Path
import subprocess
from  utils import number
import names,pathlib,random
import httpx
import time,ctypes
import asyncio
import pyrogram
from pyrogram import enums
from pyrogram import Client
import json
from colorama import Fore,init
import os, sys
# init(convert=True)
import httpx,requests
import json

with open('./config.json') as f:
    settings = json.load(f)
    f.close()
if settings['5sim']['active']:
    api_name = '5sim'
    key = settings['5sim']['key']
elif settings['sms-activate']['active']:
    api_name= "sms-activate"
    sa = SMSActivateAPI(settings['sms-activate']['key'])




ctypes.windll.kernel32.SetConsoleTitleW("LimitedGram v1.1 | [Parsing Config] | Dev : @ratelimit | Discord : Terminal#1337")
time.sleep(1)
with open('config.json') as config:
    config = json.load(config)
ctypes.windll.kernel32.SetConsoleTitleW("LimitedGram v1.1 | [Parsed Config] | Dev : @ratelimit | Discord : Terminal#1337")

count = 0
class main(object):
    def __init__(self):
        self.api_hash = config['api_hash']
        self.api_id = config['api_id']
        self.app = Client('adasdad',api_hash=self.api_hash,api_id=self.api_id)
        self.app.start()
        self.chat_id = ""
        ctypes.windll.kernel32.SetConsoleTitleW("LimitedGram v1.1 | [Main Menu] | Dev : @ratelimit | Discord : Terminal#1337")
        print("""

[38;2;5;189;245m [38;2;9;187;245m [38;2;13;185;245m [38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m [38;2;29;177;245m_[38;2;33;175;245m [38;2;37;173;245m [38;2;41;171;245m [38;2;45;169;245m [38;2;49;167;245m [38;2;53;165;245m [38;2;57;163;245m [38;2;61;161;245m [38;2;65;159;245m [38;2;69;157;245m [38;2;73;155;245m [38;2;77;153;245m_[38;2;81;151;245m [38;2;85;149;245m_[38;2;89;147;245m [38;2;93;145;245m [38;2;97;143;245m [38;2;101;141;245m [38;2;105;139;245m [38;2;109;137;245m [38;2;113;135;245m [38;2;117;133;245m [38;2;121;131;245m [38;2;125;129;245m [38;2;129;127;245m [38;2;133;125;245m_[38;2;137;123;245m [38;2;141;121;245m [38;2;145;119;245m [38;2;149;117;245m_[38;2;153;115;245m_[38;2;157;113;245m_[38;2;161;111;245m [38;2;165;109;245m [38;2;169;107;245m [38;2;173;105;245m [38;2;177;103;245m [38;2;181;101;245m [38;2;185;99;245m [38;2;189;97;245m [38;2;193;95;245m [38;2;197;93;245m [38;2;201;91;245m [38;2;205;89;245m [38;2;209;87;245m [38;2;213;85;245m [38;2;217;83;245m [38;2;221;81;245m [38;2;225;79;245m [38;2;229;77;245m [38;2;233;75;245m [38;2;237;73;245m [38;2;241;71;245m 
[38;2;5;189;245m [38;2;9;187;245m [38;2;13;185;245m/[38;2;17;183;245m [38;2;21;181;245m/[38;2;25;179;245m([38;2;29;177;245m_[38;2;33;175;245m)[38;2;37;173;245m_[38;2;41;171;245m [38;2;45;169;245m_[38;2;49;167;245m_[38;2;53;165;245m [38;2;57;163;245m_[38;2;61;161;245m_[38;2;65;159;245m_[38;2;69;157;245m [38;2;73;155;245m([38;2;77;153;245m_[38;2;81;151;245m)[38;2;85;149;245m [38;2;89;147;245m|[38;2;93;145;245m_[38;2;97;143;245m [38;2;101;141;245m_[38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m [38;2;117;133;245m [38;2;121;131;245m_[38;2;125;129;245m_[38;2;129;127;245m|[38;2;133;125;245m [38;2;137;123;245m|[38;2;141;121;245m [38;2;145;119;245m/[38;2;149;117;245m [38;2;153;115;245m_[38;2;157;113;245m [38;2;161;111;245m\[38;2;165;109;245m_[38;2;169;107;245m [38;2;173;105;245m_[38;2;177;103;245m_[38;2;181;101;245m [38;2;185;99;245m_[38;2;189;97;245m_[38;2;193;95;245m [38;2;197;93;245m_[38;2;201;91;245m [38;2;205;89;245m_[38;2;209;87;245m [38;2;213;85;245m_[38;2;217;83;245m_[38;2;221;81;245m [38;2;225;79;245m_[38;2;229;77;245m_[38;2;233;75;245m_[38;2;237;73;245m 
[38;2;5;189;245m [38;2;9;187;245m/[38;2;13;185;245m [38;2;17;183;245m/[38;2;21;181;245m [38;2;25;179;245m|[38;2;29;177;245m [38;2;33;175;245m|[38;2;37;173;245m [38;2;41;171;245m'[38;2;45;169;245m_[38;2;49;167;245m [38;2;53;165;245m`[38;2;57;163;245m [38;2;61;161;245m_[38;2;65;159;245m [38;2;69;157;245m\[38;2;73;155;245m|[38;2;77;153;245m [38;2;81;151;245m|[38;2;85;149;245m [38;2;89;147;245m_[38;2;93;145;245m_[38;2;97;143;245m/[38;2;101;141;245m [38;2;105;139;245m_[38;2;109;137;245m [38;2;113;135;245m\[38;2;117;133;245m/[38;2;121;131;245m [38;2;125;129;245m_[38;2;129;127;245m`[38;2;133;125;245m [38;2;137;123;245m|[38;2;141;121;245m/[38;2;145;119;245m [38;2;149;117;245m/[38;2;153;115;245m_[38;2;157;113;245m\[38;2;161;111;245m/[38;2;165;109;245m [38;2;169;107;245m'[38;2;173;105;245m_[38;2;177;103;245m_[38;2;181;101;245m/[38;2;185;99;245m [38;2;189;97;245m_[38;2;193;95;245m`[38;2;197;93;245m [38;2;201;91;245m|[38;2;205;89;245m [38;2;209;87;245m'[38;2;213;85;245m_[38;2;217;83;245m [38;2;221;81;245m`[38;2;225;79;245m [38;2;229;77;245m_[38;2;233;75;245m [38;2;237;73;245m\
[38;2;5;189;245m/[38;2;9;187;245m [38;2;13;185;245m/[38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m|[38;2;29;177;245m [38;2;33;175;245m|[38;2;37;173;245m [38;2;41;171;245m|[38;2;45;169;245m [38;2;49;167;245m|[38;2;53;165;245m [38;2;57;163;245m|[38;2;61;161;245m [38;2;65;159;245m|[38;2;69;157;245m [38;2;73;155;245m|[38;2;77;153;245m [38;2;81;151;245m|[38;2;85;149;245m [38;2;89;147;245m|[38;2;93;145;245m|[38;2;97;143;245m [38;2;101;141;245m [38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m/[38;2;117;133;245m [38;2;121;131;245m([38;2;125;129;245m_[38;2;129;127;245m|[38;2;133;125;245m [38;2;137;123;245m/[38;2;141;121;245m [38;2;145;119;245m/[38;2;149;117;245m_[38;2;153;115;245m\[38;2;157;113;245m\[38;2;161;111;245m|[38;2;165;109;245m [38;2;169;107;245m|[38;2;173;105;245m [38;2;177;103;245m|[38;2;181;101;245m [38;2;185;99;245m([38;2;189;97;245m_[38;2;193;95;245m|[38;2;197;93;245m [38;2;201;91;245m|[38;2;205;89;245m [38;2;209;87;245m|[38;2;213;85;245m [38;2;217;83;245m|[38;2;221;81;245m [38;2;225;79;245m|[38;2;229;77;245m [38;2;233;75;245m|[38;2;237;73;245m [38;2;241;71;245m|
[38;2;5;189;245m\[38;2;9;187;245m_[38;2;13;185;245m_[38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m/[38;2;29;177;245m_[38;2;33;175;245m|[38;2;37;173;245m_[38;2;41;171;245m|[38;2;45;169;245m [38;2;49;167;245m|[38;2;53;165;245m_[38;2;57;163;245m|[38;2;61;161;245m [38;2;65;159;245m|[38;2;69;157;245m_[38;2;73;155;245m|[38;2;77;153;245m_[38;2;81;151;245m|[38;2;85;149;245m\[38;2;89;147;245m_[38;2;93;145;245m_[38;2;97;143;245m\[38;2;101;141;245m_[38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m|[38;2;117;133;245m\[38;2;121;131;245m_[38;2;125;129;245m_[38;2;129;127;245m,[38;2;133;125;245m_[38;2;137;123;245m\[38;2;141;121;245m_[38;2;145;119;245m_[38;2;149;117;245m_[38;2;153;115;245m_[38;2;157;113;245m/[38;2;161;111;245m|[38;2;165;109;245m_[38;2;169;107;245m|[38;2;173;105;245m [38;2;177;103;245m [38;2;181;101;245m\[38;2;185;99;245m_[38;2;189;97;245m_[38;2;193;95;245m,[38;2;197;93;245m_[38;2;201;91;245m|[38;2;205;89;245m_[38;2;209;87;245m|[38;2;213;85;245m [38;2;217;83;245m|[38;2;221;81;245m_[38;2;225;79;245m|[38;2;229;77;245m [38;2;233;75;245m|[38;2;237;73;245m_[38;2;241;71;245m|

[38;2;5;189;245m[[38;2;8;187;245mT[38;2;11;185;245me[38;2;14;183;245ml[38;2;17;181;245me[38;2;20;179;245mg[38;2;23;177;245mr[38;2;26;175;245ma[38;2;29;173;245mm[38;2;32;171;245m [38;2;35;169;245mA[38;2;38;167;245mI[38;2;41;165;245mO[38;2;44;163;245m [38;2;47;161;245m|[38;2;50;159;245m [38;2;53;157;245mV[38;2;56;155;245me[38;2;59;153;245mr[38;2;62;151;245ms[38;2;65;149;245mi[38;2;68;147;245mo[38;2;71;145;245mn[38;2;74;143;245m [38;2;77;141;245m:[38;2;80;139;245m [38;2;83;137;245mB[38;2;86;135;245me[38;2;89;133;245mt[38;2;92;131;245ma[38;2;95;129;245m [38;2;98;127;245m([38;2;101;125;245m1[38;2;104;123;245m.[38;2;107;121;245m1[38;2;110;119;245m)[38;2;113;117;245m [38;2;116;115;245m|[38;2;119;113;245m [38;2;122;111;245mD[38;2;125;109;245me[38;2;128;107;245mv[38;2;131;105;245m [38;2;134;103;245m:[38;2;137;101;245m [38;2;140;99;245m@[38;2;143;97;245mr[38;2;146;95;245ma[38;2;149;93;245mt[38;2;152;91;245me[38;2;155;89;245ml[38;2;158;87;245mi[38;2;161;85;245mm[38;2;164;83;245mi[38;2;167;81;245mt[38;2;170;79;245m [38;2;173;77;245m|[38;2;176;75;245m [38;2;179;73;245mP[38;2;182;71;245mu[38;2;185;69;245mr[38;2;188;67;245mc[38;2;191;65;245mh[38;2;194;63;245ma[38;2;197;61;245ms[38;2;200;59;245me[38;2;203;57;245m [38;2;206;55;245m=[38;2;209;53;245m [38;2;212;51;245mC[38;2;215;49;245mo[38;2;218;47;245mo[38;2;221;45;245mk[38;2;224;43;245mi[38;2;227;41;245me[38;2;230;39;245m]

[38;2;5;189;245mM[38;2;40;167;240me[38;2;75;145;235mn[38;2;110;123;230mu[38;2;145;101;225m:[38;2;180;79;220m 
[38;2;5;189;245m [38;2;13;184;244m [38;2;21;179;243m|[38;2;29;174;242m [38;2;37;169;241m-[38;2;45;164;240m [38;2;53;159;239m0[38;2;61;154;238m1[38;2;69;149;237m)[38;2;77;144;236m [38;2;85;139;235mO[38;2;93;134;234mp[38;2;101;129;233mt[38;2;109;124;232mi[38;2;117;119;231mo[38;2;125;114;230mn[38;2;133;109;229m [38;2;141;104;228m:[38;2;149;99;227m [38;2;157;94;226m[[38;2;165;89;225mJ[38;2;173;84;224mo[38;2;181;79;223mi[38;2;189;74;222mn[38;2;197;69;221me[38;2;205;64;220mr[38;2;213;59;219m]
[38;2;5;189;245m [38;2;13;184;244m [38;2;21;179;243m|[38;2;29;174;242m [38;2;37;169;241m-[38;2;45;164;240m [38;2;53;159;239m0[38;2;61;154;238m2[38;2;69;149;237m)[38;2;77;144;236m [38;2;85;139;235mO[38;2;93;134;234mp[38;2;101;129;233mt[38;2;109;124;232mi[38;2;117;119;231mo[38;2;125;114;230mn[38;2;133;109;229m [38;2;141;104;228m:[38;2;149;99;227m [38;2;157;94;226m[[38;2;165;89;225mL[38;2;173;84;224me[38;2;181;79;223ma[38;2;189;74;222mv[38;2;197;69;221me[38;2;205;64;220mr[38;2;213;59;219m]
[38;2;5;189;245m [38;2;12;185;244m [38;2;19;181;243m|[38;2;26;177;242m [38;2;33;173;241m-[38;2;40;169;240m [38;2;47;165;239m0[38;2;54;161;238m3[38;2;61;157;237m)[38;2;68;153;236m [38;2;75;149;235mO[38;2;82;145;234mp[38;2;89;141;233mt[38;2;96;137;232mi[38;2;103;133;231mo[38;2;110;129;230mn[38;2;117;125;229m [38;2;124;121;228m:[38;2;131;117;227m [38;2;138;113;226m[[38;2;145;109;225mG[38;2;152;105;224mr[38;2;159;101;223mo[38;2;166;97;222mu[38;2;173;93;221mp[38;2;180;89;220m [38;2;187;85;219mP[38;2;194;81;218ma[38;2;201;77;217mr[38;2;208;73;216ms[38;2;215;69;215me[38;2;222;65;214mr[38;2;229;61;213m]
[38;2;5;189;245m [38;2;11;185;244m [38;2;17;181;243m|[38;2;23;177;242m [38;2;29;173;241m-[38;2;35;169;240m [38;2;41;165;239m0[38;2;47;161;238m4[38;2;53;157;237m)[38;2;59;153;236m [38;2;65;149;235mO[38;2;71;145;234mp[38;2;77;141;233mt[38;2;83;137;232mi[38;2;89;133;231mo[38;2;95;129;230mn[38;2;101;125;229m [38;2;107;121;228m:[38;2;113;117;227m [38;2;119;113;226m[[38;2;125;109;225mP[38;2;131;105;224ma[38;2;137;101;223mr[38;2;143;97;222ms[38;2;149;93;221me[38;2;155;89;220md[38;2;161;85;219m [38;2;167;81;218mT[38;2;173;77;217mo[38;2;179;73;216m [38;2;185;69;215mC[38;2;191;65;214mh[38;2;197;61;213ma[38;2;203;57;212mn[38;2;209;53;211mn[38;2;215;49;210me[38;2;221;45;209ml[38;2;227;41;208m]
[38;2;5;189;245m [38;2;10;186;245m [38;2;15;183;245m|[38;2;20;180;245m [38;2;25;177;245m-[38;2;30;174;245m [38;2;35;171;245m0[38;2;40;168;245m5[38;2;45;165;245m)[38;2;50;162;245m [38;2;55;159;245mO[38;2;60;156;245mp[38;2;65;153;245mt[38;2;70;150;245mi[38;2;75;147;245mo[38;2;80;144;245mn[38;2;85;141;245m [38;2;90;138;245m:[38;2;95;135;245m [38;2;100;132;245m[[38;2;105;129;245mM[38;2;110;126;245ma[38;2;115;123;245ms[38;2;120;120;245ms[38;2;125;117;245m [38;2;130;114;245mU[38;2;135;111;245ms[38;2;140;108;245me[38;2;145;105;245mr[38;2;150;102;245mn[38;2;155;99;245ma[38;2;160;96;245mm[38;2;165;93;245me[38;2;170;90;245m [38;2;175;87;245mC[38;2;180;84;245mh[38;2;185;81;245me[38;2;190;78;245mc[38;2;195;75;245mk[38;2;200;72;245me[38;2;205;69;245mr[38;2;210;66;245m]
[38;2;5;189;245m [38;2;13;184;244m [38;2;21;179;243m|[38;2;29;174;242m [38;2;37;169;241m-[38;2;45;164;240m [38;2;53;159;239m0[38;2;61;154;238m6[38;2;69;149;237m)[38;2;77;144;236m [38;2;85;139;235mO[38;2;93;134;234mp[38;2;101;129;233mt[38;2;109;124;232mi[38;2;117;119;231mo[38;2;125;114;230mn[38;2;133;109;229m [38;2;141;104;228m:[38;2;149;99;227m [38;2;157;94;226m[[38;2;165;89;225mM[38;2;173;84;224ma[38;2;181;79;223ms[38;2;189;74;222ms[38;2;197;69;221m [38;2;205;64;220mD[38;2;213;59;219mM[38;2;221;54;218m]
[38;2;5;189;245m [38;2;13;184;244m [38;2;21;179;243m|[38;2;29;174;242m [38;2;37;169;241m-[38;2;45;164;240m [38;2;53;159;239m0[38;2;61;154;238m7[38;2;69;149;237m)[38;2;77;144;236m [38;2;85;139;235mO[38;2;93;134;234mp[38;2;101;129;233mt[38;2;109;124;232mi[38;2;117;119;231mo[38;2;125;114;230mn[38;2;133;109;229m [38;2;141;104;228m:[38;2;149;99;227m [38;2;157;94;226m[[38;2;165;89;225mG[38;2;173;84;224me[38;2;181;79;223mn[38;2;189;74;222me[38;2;197;69;221mr[38;2;205;64;220ma[38;2;213;59;219mt[38;2;221;54;218mo[38;2;229;49;217mr[38;2;237;44;216m]
[38;2;5;189;245m [38;2;13;184;244m [38;2;21;179;243m|[38;2;29;174;242m [38;2;37;169;241m-[38;2;45;164;240m [38;2;53;159;239m0[38;2;61;154;238m8[38;2;69;149;237m)[38;2;77;144;236m [38;2;85;139;235mO[38;2;93;134;234mp[38;2;101;129;233mt[38;2;109;124;232mi[38;2;117;119;231mo[38;2;125;114;230mn[38;2;133;109;229m [38;2;141;104;228m:[38;2;149;99;227m [38;2;157;94;226m[[38;2;165;89;225mM[38;2;173;84;224ma[38;2;181;79;223ms[38;2;189;74;222ms[38;2;197;69;221m [38;2;205;64;220mD[38;2;213;59;219mM[38;2;221;54;218m]
[38;2;5;189;245m [38;2;12;185;244m [38;2;19;181;243m|[38;2;26;177;242m [38;2;33;173;241m-[38;2;40;169;240m [38;2;47;165;239m0[38;2;54;161;238m9[38;2;61;157;237m)[38;2;68;153;236m [38;2;75;149;235mO[38;2;82;145;234mp[38;2;89;141;233mt[38;2;96;137;232mi[38;2;103;133;231mo[38;2;110;129;230mn[38;2;117;125;229m [38;2;124;121;228m:[38;2;131;117;227m [38;2;138;113;226m[[38;2;145;109;225mM[38;2;152;105;224ma[38;2;159;101;223ms[38;2;166;97;222ms[38;2;173;93;221m [38;2;180;89;220mR[38;2;187;85;219me[38;2;194;81;218ma[38;2;201;77;217mc[38;2;208;73;216mt[38;2;215;69;215mi[38;2;222;65;214mo[38;2;229;61;213mn[38;2;236;57;212m]
[38;2;5;189;245m [38;2;11;185;244m [38;2;17;181;243m|[38;2;23;177;242m [38;2;29;173;241m-[38;2;35;169;240m [38;2;41;165;239m1[38;2;47;161;238m0[38;2;53;157;237m)[38;2;59;153;236m [38;2;65;149;235mO[38;2;71;145;234mp[38;2;77;141;233mt[38;2;83;137;232mi[38;2;89;133;231mo[38;2;95;129;230mn[38;2;101;125;229m [38;2;107;121;228m:[38;2;113;117;227m [38;2;119;113;226m[[38;2;125;109;225mS[38;2;131;105;224me[38;2;137;101;223ms[38;2;143;97;222ms[38;2;149;93;221mi[38;2;155;89;220mo[38;2;161;85;219mn[38;2;167;81;218m [38;2;173;77;217mC[38;2;179;73;216mr[38;2;185;69;215me[38;2;191;65;214ma[38;2;197;61;213mt[38;2;203;57;212mo[38;2;209;53;211mr[38;2;215;49;210m]

""")
        self.action = input(f"{Fore.BLUE} Task [>] {Fore.RESET}")
        if self.action == "1":
            self.joiner()
        if self.action == "2":
            self.leaver()
        if self.action == "3":
            self.parser()
        if self.action == "4":
            self.massADD()
        if self.action == "5":
            self.usernameChecker()
        if self.action == "6":
            self.massDM()
        if self.action == "7":
            self.Gen()
        if self.action == "8":
            self.MassReaction()
        if self.action == "10":
            self.SessionCreate()
        ctypes.windll.kernel32.SetConsoleTitleW("LimitedGram v1.1 | [Loader Initiated] | Dev : @ratelimit | Discord : Terminal#1337")
        time.sleep(0.5)
    def joiner(self):
        groups = input(f"{Fore.RED}INF: {Fore.RESET}{Fore.CYAN}Enter The Group/Channel File [>] {Fore.RESET}")
        try:
            groups = open(groups).read().split('\n')
            for i in groups:
                print(i)
                self.app.join_chat(i)
                print(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Joined Channel [>]{Fore.RESET}{Fore.LIGHTMAGENTA_EX} @{i} {Fore.RESET}")
                time.sleep(config['cooldown'])
        except Exception as e:
            print(e)
            with open('data/error.log','w') as f:
                f.write(str(e))
                f.close
            print(f"{Fore.RED}INFO : {Fore.RESET} Error has been logged in data/error.log file :(")
        input()
        self.app.stop()
        os.system('cls')
        main()
    def leaver(self):
        try:
            chat_id = input(f"{Fore.RED}INFO : {Fore.RESET}{Fore.BLUE} Enter Chat ID [>] {Fore.RESET}")
            self.app.leave_chat(chat_id)
            print(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Left Channel [>]{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{chat_id}{Fore.RESET}")
            
        except Exception as e:
            with open('data/error.log','a') as f:
                f.write(str(e)+'\n')
                f.close()
        input()
        self.app.stop()
        os.system('cls')
        main()
    username = ""
    def parser(self):
        global count
        count = 0
        ctypes.windll.kernel32.SetConsoleTitleW('LimitedGram v1.1 | [Module : Parser] | Dev : @ratelimit | Discord : Terminal#1337')
        mem_list = []
        global username
        n = 0
        self.chat_id = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Chat ID [>]{Fore.RESET}")
        self.name = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Chat Name [>]{Fore.RESET}")
        try:
            with open(f"data/{self.name}.txt",'a') as f:
                k = -1001400035854
                for i in self.app.get_chat_members(int(self.chat_id)):
                    i = str(i);i = json.loads(i)#dict
                    
                    try:
                        username = i['user']['username']
                        f.write(username+'\n')
                        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SCRAPED] {Fore.RESET}{Fore.LIGHTBLUE_EX}ID : {i['user']['id']}{Fore.RESET} | {Fore.RESET}{Fore.LIGHTBLUE_EX}User : {i['user']['username']}{Fore.RESET} | {Fore.RESET}{Fore.LIGHTBLUE_EX}Restricted :{i['user']['is_restricted']}{Fore.RESET} | {Fore.RESET}{Fore.LIGHTBLUE_EX}Verified :{i['user']['is_verified']}{Fore.RESET} | {Fore.RESET}{Fore.LIGHTBLUE_EX}Premium :{i['user']['is_premium']}{Fore.RESET}")
                        time.sleep(config['cooldown'])
                        count += 1
                        ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedGram v1.1 | [Module : Parser] | Parsed : {str(count)} | Dev : @ratelimit | Discord : Terminal#1337')

                    except:
                        time.sleep(config['cooldown'])
                        pass


                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.GREEN} Successfully Parsed {self.app.get_chat_members_count(self.chat_id)} Members in {self.name}.txt")

        except Exception as e:
            with open('error.log','a') as f:
                f.write(str(e)+'\n')
                f.close()
            print(f"{Fore.RED}INFO : {Fore.RESET} Error has been logged in data/error.log file :(")
        input()
        self.app.stop()
        os.system('cls')
        main()
    def massDM(self):
        global count
        count = 0
        ctypes.windll.kernel32.SetConsoleTitleW('LimitedGram v1.1 | [Module : MASSDM] | Dev : @ratelimit | Discord : Terminal#1337')
        self.name = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Username List [>]{Fore.RESET}")
        self.message = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Message [>]{Fore.RESET}")
        try:
            users = open(self.name).read().split('\n')
            with open('data/sentdm.txt','a') as f:
                for i in users:
                    self.app.send_message(i,self.message)
                    print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SENT]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} successfully sent dm to {Fore.LIGHTCYAN_EX}{i}{Fore.RESET}")
                    f.write(i+'\n')
                    time.sleep(config['cooldown'])
                    count += 1
                
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Send DM to All Parsed Members {Fore.LIGHTCYAN_EX}{i}{Fore.RESET} to {self.message}")
                ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedGram v1.1 | [Module : Parser] | Sent : {str(count)} | Dev : @ratelimit | Discord : Terminal#1337')
        except:
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SENT]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} failed to send dm to {Fore.LIGHTCYAN_EX}{i}{Fore.RESET}")
            pass
        input()
        self.app.stop()
        os.system('cls')
        main()
    def massADD(self):
        global count ; count = 0
        ctypes.windll.kernel32.SetConsoleTitleW('LimitedGram v1.1 | [Module : GROUP TO CHANNEL] | Dev : @ratelimit | Discord : Terminal#1337')
        self.name = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Username List [>]{Fore.RESET}")
        self.message = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Group/Channel tag [>]{Fore.RESET}")
        users = open(self.name).read().split('\n')
        for i in users:
            try:
                self.app.add_chat_members(self.message,i)
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[ADDED]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} Added {Fore.LIGHTCYAN_EX}{i}{Fore.RESET} to {self.message}")
                ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedGram v1.1 | [Module : Parser] | Parsed : {str(count)} | Dev : @ratelimit | Discord : Terminal#1337')
                time.sleep(int(config['cooldown']))
            except:
                pass
            # print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[ADDED]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} Added {Fore.LIGHTCYAN_EX}{i}{Fore.RESET} to {self.message}")
            count += 1
        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Added All Parsed Members {Fore.LIGHTCYAN_EX}{i}{Fore.RESET} to {self.message}")
        input()
        self.app.stop()
        os.system('cls')
        main()
    def MassReaction(self):
        self.msg_id = int(input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Message ID [>]{Fore.RESET}"))
        self.reaction = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Reaction ID [>]{Fore.RESET}")
        self.chat_id = int(input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Chat ID [>]{Fore.RESET}"))
        try:
            self.app.send_reaction(chat_id=self.chat_id,message_id=self.msg_id,emoji=self.reaction)
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Added All Reactions {Fore.RESET}")
        except Exception as e:
            with open("errors/log.txt",'a') as f:
                print(e)
                f.write(str(e.with_traceback())); f.close()
    def AccountManager(self):
        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[Methods]{Fore.RESET}{Fore.LIGHTBLUE_EX} Available Modules For Manager :- {Fore.LIGHTCYAN_EX}{Fore.RESET}")
        print('')
        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[1]{Fore.RESET}{Fore.LIGHTBLUE_EX} Profile Picture Changer {Fore.LIGHTCYAN_EX}{Fore.RESET}")
        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[2]{Fore.RESET}{Fore.LIGHTBLUE_EX} Username Changer {Fore.LIGHTCYAN_EX}{Fore.RESET}")
        self.action = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Action [>]{Fore.RESET}")
        if self.action == '1':
            flist = []
            for p in pathlib.Path('.').iterdir():
                if p.is_file():
                    flist.append(str(p))
            self.app.set_profile_photo(photo=random.choice(flist))
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Added Profile Pictures{Fore.RESET}")
        elif self.action == '2':
            self.username_list = open('data/usernames/usernames.txt').read().splitlines()
            self.app.set_username(username=random.choice(self.username_list))
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Changed All Usernames{Fore.RESET}")
        else:
            self.app.stop()
            main()

        

    def usernameChecker(self):
        global count ; count = 0
        ctypes.windll.kernel32.SetConsoleTitleW('LimitedGram v1.1 | [Module : USERNAME CHECKER] | Dev : @ratelimit | Discord : Terminal#1337')
        self.name = input(f"{Fore.RED}INFO: {Fore.RESET}{Fore.CYAN}Username List [>]{Fore.RESET}")
        users = open(self.name).read().split('\n')
        for i in users:
            try:
                self.app.get_users(i)
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[CLAIMED]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} Got Claimed Username [>] {Fore.LIGHTCYAN_EX}{i}{Fore.RESET}")
                with open('data/claimed.txt','a') as f:
                    f.write(i+'\n')
                    f.close()
                    count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedGram v1.1 | [Module : Parser] | Parsed : {str(count)} | Dev : @ratelimit | Discord : Terminal#1337')
                    time.sleep(config['cooldown'])

            except:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[UNCLAIMED]{Fore.RESET}{Fore.LIGHTBLUE_EX}Token {self.api_hash} Got Unclaimed Username [>] {Fore.LIGHTCYAN_EX}{i}{Fore.RESET}")
                with open('data/unclaimed.txt','a') as f:
                    f.write(i+'\n')
                    f.close()
                    time.sleep(config['cooldown'])
        print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SUCCESS]{Fore.RESET}{Fore.LIGHTBLUE_EX} Checked All Usernames {Fore.RESET}")
        self.app.stop()
        input()
        self.app.stop()
        os.system('cls')
        main()
    resp = False
    def getBalance(self):

        if api_name == "5sim":
            headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
            balance = requests.get('https://5sim.net/v1/user/profile', headers=headers)
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {balance.text} {Fore.RESET}")
            return balance.json()
    def getNumber(self):
        if api_name == "5sim":
            headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
            ph = requests.get(f"https://5sim.net/v1/user/buy/activation/{settings['5sim']['country']}/{settings['5sim']['provider']}/telegram", headers=headers)
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {ph.text} {Fore.RESET}")
            if "not enough rating" in ph.text:
                return False
            if "no free phones" in ph.text:
                # print(ph.text)
                return False
            else:
                return ph.json()
        if api_name == "sms-activate":
            r = sa.getNumberV2(service='tg',country='33')
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {r} {Fore.RESET}")
            return r

    def getCode(self,id):
        if api_name == "5sim":
            headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
            check = requests.get(f"https://5sim.net/v1/user/check/"+str(id), headers=headers)
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {check.text} {Fore.RESET}")
            # print(check)
            return check.json()
        if api_name == "sms-activate":
            re = sa.getNumberV2(service='tg',country='6')
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {re} {Fore.RESET}")
            return True

    def Cancel(self,id):
        if api_name == "5sim":
            headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
            cancelled = requests.get('https://5sim.net/v1/user/cancel/' + str(id), headers=headers)
            if config['debug']:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {cancelled.text} {Fore.RESET}")
            if "you need to wait time" in cancelled.text:
                return False
            try:

                if cancelled.json()['status'] != "CANCELED":
                    return False
                else:
                    return True
            except:
                return False
        if api_name == "sms-activate":
            pass
    cancel_tries = 0
    def Gen(self):
        ctypes.windll.kernel32.SetConsoleTitleW('LimitedGram v1.1 | [Module : Generator] | Dev : @ratelimit | Discord : Terminal#1337')
        global resp,phone_number
        phone_number = ''
        # global phone_number,ign
        r= self.getNumber() 
        try:

            if r == False:
                print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[UNAVAILABLE]{Fore.RESET}{Fore.LIGHTBLUE_EX}{phone_number} No Phone Numbers Available {Fore.LIGHTCYAN_EX}{Fore.RESET}")
                self.Gen()
        except:
            pass
        phone_number = "+"+r['phoneNumber']
        ign = r['activationId']
        try:
            
            Client.send_code(phone_number=phone_number)
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[SENT] {Fore.RESET}{Fore.LIGHTBLUE_EX}{phone_number}{Fore.RESET}{Fore.LIGHTMAGENTA_EX} sent Get Code Request {Fore.LIGHTCYAN_EX}{Fore.RESET}{Fore.LIGHTBLACK_EX} [{ign}]{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[BANNED] {Fore.RESET}{Fore.LIGHTBLUE_EX}{phone_number} Failed To Send Get Code Request {Fore.LIGHTCYAN_EX}{Fore.RESET}{Fore.LIGHTBLACK_EX} [{ign}]{Fore.RESET}")
            if api_name == "5sim":

                while True:
                    resp = self.Cancel(ign)
                    if resp:
                        break
            elif api_name == "sms-activate":
                self.activate = config['sms-activate']['key']
                r = requests.get(f'https://api.sms-activate.org/stubs/handler_api.php?api_key={self.activate}&action=setStatus&status=8&id={ign}&forward=$forward')
                if config['debug']:
                    print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[DEBUG]{Fore.RESET}{Fore.LIGHTBLUE_EX} {r.text} {Fore.RESET}")
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[CANCELLED]{Fore.RESET}{Fore.LIGHTBLUE_EX}{phone_number} Successfully Cancelled {Fore.LIGHTBLACK_EX} [{ign}]{Fore.RESET}{Fore.LIGHTCYAN_EX}| Remaining Balance : {sa.getBalanceAndCashBack()['balance']}{Fore.RESET}")
            self.Gen()
            


        code = self.getCode(ign)
        print('got code',code)
    def SessionCreate(self):
        while True:
            self.newapi_id = input(f"{Fore.BLUE}[INPUT]{Fore.RESET}{Fore.CYAN} Enter The Api ID [>] {Fore.RESET}")
            self.newapi_hash = input(f"{Fore.BLUE}[INPUT]{Fore.RESET}{Fore.CYAN} Enter The Api Hash [>] {Fore.RESET}")
            self.newName = input(f"{Fore.BLUE}[INPUT]{Fore.RESET}{Fore.CYAN} Enter The Session Name [>] {Fore.RESET}")
            self.newclient = Client(self.newName,api_id=self.newapi_id,api_hash=self.newapi_hash)
            self.newclient.start() ; self.newclient.stop()
            subprocess.getoutput(f'cp .\{self.newName}* .\data\sessions')
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[CREATED]{Fore.RESET}{Fore.LIGHTBLUE_EX}{self.newapi_hash} Successfully Created Session {Fore.LIGHTBLACK_EX} [{self.newName}]{Fore.RESET}{Fore.LIGHTCYAN_EX}{Fore.RESET}")
            os.system('cd .\data\sessions')
            l = input("Add Another Acc? [Y/n]")
            if l == "Y" or "y":
                pass
            else:
                break
        self.app.stop()
        main()





main()

