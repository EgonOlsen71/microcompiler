var _self=self;
var instance=null;
var conInstance=null;
if (self) {
self.addEventListener('message', function(e) {
if (instance) {
instance.registerKey(e.data);
} else {
instance=new Compiled();
if(e.data=="run") {
instance.execute(true);
} else {
var comp=instance;
var cons=new CbmConsole();
conInstance=cons;
cons.inject(comp, e.data);
comp.execute(true);
}
}
}, false);
}
function executeAsync(srcFile, func, cons) {
var worker=new Worker(srcFile);
worker.addEventListener('message', func, false);
if (cons) {
worker.postMessage("console");
} else {
worker.postMessage("run");
}
return worker;
}
function CbmConsole() {
this.x=0;
this.y=0;
this.width=40;
this.height=25;
this.vidMem=new Array(1000);
this.colMem=new Array(1000);
this.bgColor=6;
this.fontColor=14;
this.map = {};
this.charset=null;
this.graphicsMode=true;
this.reverseMode=false;
this.compiledCode=null;
var _selfy=this;
this.getPokeValue = function(ch) {
if (Number.isInteger(ch)) {
ch=String.fromCharCode(ch);
}
return _selfy.charset.charCodeAt(_selfy.getConvertedChar(ch)+(_selfy.graphicsMode?0:256));
}
this.clearScreen = function() {
for (var i=0; i<_selfy.width*_selfy.height; i++) {
_selfy.vidMem[i]=32;
_selfy.colMem[i]=_selfy.fontColor;
_selfy.x=0;
_selfy.y=0;
}
}
this.shiftRight = function(pos) {
var offset = pos;
var end = _selfy.y * _selfy.width + (((_selfy.y & 1) == 1) ? (_selfy.width-1) : (2*_selfy.width-1));
if (_selfy.vidMem[end] != 32) {
return;
}
for (var i = end; i > offset; i--) {
_selfy.vidMem[i] = _selfy.vidMem[i - 1];
_selfy.colMem[i] = _selfy.colMem[i - 1];
}
_selfy.vidMem[offset]=_selfy.getPokeValue(32);
_selfy.colMem[offset]=_selfy.fontColor;
}
this.processControlCode = function(code, pos, withSpc) {
var col=_selfy.compiledCode.getMemory()[646];
if (withSpc && code==32) {
if (_selfy.reverseMode) {
_selfy.setAtCursor(pos);
} else {
_selfy.clearAtCursor(pos);
}
_selfy.x++;
}
else {
switch(code) {
case 147:
_selfy.clearScreen();
_selfy.x=0;
_selfy.y=0;
break;
case 19:
_selfy.x=0;
_selfy.y=0;
break;
case 29:
_selfy.x++;
break;
case 157:
_selfy.x--;
break;
case 17:
_selfy.y++;
break;
case 145:
_selfy.y--;
break;
case 144:
col = 0;
break;
case 5:
col = 1;
break;
case 28:
col = 2;
break;
case 159:
col = 3;
break;
case 156:
col = 4;
break;
case 30:
col = 5;
break;
case 31:
col = 6;
break;
case 158:
col = 7;
break;
case 129:
col = 8;
break;
case 149:
col = 9;
break;
case 150:
col = 10;
break;
case 151:
col = 11;
break;
case 152:
col = 12;
break;
case 153:
col = 13;
break;
case 154:
col = 14;
break;
case 155:
col = 15;
break;
case 18:
_selfy.reverseMode = true;
break;
case 146:
_selfy.reverseMode = false;
break;
case 20:
_selfy.x--;
_selfy.clearAtCursor(pos);
break;
case 148:
_selfy.shiftRight(pos);
_selfy.clearAtCursor(pos);
break;
case 13:
_selfy.reverseMode = false;
_selfy.y++;
break;
case 14:
_selfy.graphicsMode=false;
break;
case 142:
_selfy.graphicsMode=true;
break;
default:
_selfy.vidMem[pos]=_selfy.getPokeValue(String.fromCharCode(code));
_selfy.colMem[pos]=_selfy.fontColor;
_selfy.x++;
break;
}
}
if (col!=-1) {
_selfy.fontColor=col;
_selfy.compiledCode.getMemory()[646]=col;
}
}
this.clearAtCursor = function(pos) {
_selfy.vidMem[pos]=_selfy.getPokeValue(32);
_selfy.colMem[pos]=_selfy.fontColor;
_selfy.x++;
}
this.setAtCursor = function(pos) {
_selfy.vidMem[pos]=_selfy.getPokeValue(160);
_selfy.colMem[pos]=_selfy.fontColor;
_selfy.x++;
}
this.inject = function(compiledCode, conElem) {
compiledCode.superOut=compiledCode.out;
_selfy.con=conElem;
_selfy.fillMap();
_selfy.charset=_selfy.createCharsetMapping();
_selfy.compiledCode=compiledCode;
compiledCode.convert = function(c) {
if (c >= 'a' && c <= 'z') {
c = String.fromCharCode(c.charCodeAt(0) - 32);
} else if (c >= 'A' && c <= 'Z') {
c = String.fromCharCode(c.charCodeAt(0) + 32);
}
return c;
}
compiledCode.out = function(val) {
if (val==null) {
return;
}
val=""+val;
for(var i=0; i<val.length; i++) {
var c=val.charAt(i);
var pos=_selfy.x+_selfy.width*_selfy.y;
var col=_selfy.compiledCode.getMemory()[646];
_selfy.fontColor=col;
if (c=='{') {
var end=val.indexOf('}', i);
if (end!=-1) {
var subs=val.substring(i,end+1);
i=end;
var code=_selfy.getCode(subs);
if (code!=-1) {
_selfy.processControlCode(code, pos, true);
}
continue;
}
}
if (_selfy.isChar(c)) {
_selfy.processControlCode(c.charCodeAt(0), pos, false);
} else {
if (_selfy.isBreak(c)) {
_selfy.x=0;
_selfy.y++;
_selfy.reverseMode = false;
}
}
if (_selfy.x==_selfy.width) {
_selfy.x=0;
_selfy.y++;
}
if (_selfy.y>=_selfy.height) {
_selfy.y=_selfy.height-1;
for (var p=_selfy.width;p<_selfy.width*_selfy.height;p++) {
_selfy.vidMem[p-_selfy.width]=_selfy.vidMem[p];
_selfy.colMem[p-_selfy.width]=_selfy.colMem[p];
}
for (var p=_selfy.width*(_selfy.height-1);p<_selfy.width*_selfy.height;p++) {
_selfy.vidMem[p]=32;
_selfy.colMem[p]=_selfy.fontColor;
}
}
}
_self.postMessage([_selfy.vidMem, _selfy.colMem, _selfy.bgColor]);
};
compiledCode.get = function() {
var key=this.keyPressed;
if (!key) {
return ""
}
this.timeOut=20;
this.keyPressed=null;
this._memory[198]=0;
return key.substring(0,1);
};
}
this.isChar = function(c) {
return c!="\r" && c!="\n";
}
this.isBreak = function(c) {
return c=="\r" || c=="\n";
}
this.getConvertedChar = function(c) {
if (c >= 'a' && c <= 'z') {
c = c.charCodeAt(0) - 96;
//} else if (c >= 'A' && c <= 'Z') {
//	c = c.charCodeAt(0) + 32;
} else {
c=c.charCodeAt(0);
}
c+=(_selfy.reverseMode?128:0);
return c;
}
this.setCharAt = function(str, index, replacement) {
return str.substr(0, index) + replacement+ str.substr(index + replacement.length);
}
this.createCharsetMapping = function() {
var sb="";
sb+="@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?`abcdefghijklmnopqrstuvwxyz{|}~";
sb+="��������������������������������";
sb+="����������������������������������������������������������������";
for (var i = 0; i < 32; i++) {
sb+=String.fromCharCode(i + 128);
}
sb+=String.fromCharCode(224);
for (var i = 0; i < 31; i++) {
sb+=String.fromCharCode(i + 256);
}
sb+="@";
for (var i = 0; i < 26; i++) {
sb+=String.fromCharCode(i + 287);
}
sb+="[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?`";
sb+="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sb+="{|}~���������������������������������";
for (var i = 0; i < 26; i++) {
sb+=String.fromCharCode(i + 313);
}
sb+="�������������������������������������";
sb+=String.fromCharCode(128);
sb+="��������������������������";
for (var i = 27; i < 32; i++) {
sb+=String.fromCharCode(i + 128);
}
sb+=String.fromCharCode(224);
for (var i = 0; i < 31; i++) {
sb+=String.fromCharCode(i + 256);
}
_selfy.setCharAt(sb, 94 + 256, '?');
_selfy.setCharAt(sb,95 + 256, '�');
_selfy.setCharAt(sb,105 + 256, '?');
_selfy.setCharAt(sb,122 + 256, '?');
_selfy.setCharAt(sb,94 + 128 + 256, '�');
_selfy.setCharAt(sb,95 + 128 + 256, '?');
_selfy.setCharAt(sb,105 + 128 + 256, '?');
_selfy.setCharAt(sb,122 + 128 + 256, '?');
return sb;
}
this.getCode = function(placeHolder) {
placeHolder = placeHolder.replace("{", "").replace("}", "").toLowerCase().trim();
if (_selfy.map[placeHolder]) {
return _selfy.map[placeHolder];
}
return -1;
}
this.fillMap = function() {
_selfy.add(32, "space");
_selfy.add(144, "black", "blk", "ctrl-1");
_selfy.add(5, "white", "wht", "ctrl-2", "ctrl-e");
_selfy.add(28, "red", "ctrl-3", "ctrl-pound", "ctrl-�");
_selfy.add(159, "cyan", "cyn", "ctrl-4");
_selfy.add(156, "purple", "pur", "pink", "cm-3");
_selfy.add(30, "green", "grn", "ctrl-6", "ctrl-up arrow", "ctrl-?");
_selfy.add(31, "blue", "blu", "ctrl-7", "ctrl-=");
_selfy.add(158, "yellow", "yel", "ctrl-8");
_selfy.add(129, "orange", "orng", "orn", "cm-1");
_selfy.add(149, "brown", "brn", "cm-2");
_selfy.add(150, "light red", "lred");
_selfy.add(151, "dark grey", "dark gray", "gry1", "cm-4");
_selfy.add(152, "grey", "gray", "gry2", "cm-5");
_selfy.add(153, "light green", "lgrn", "cm-6");
_selfy.add(154, "light blue", "lblu", "cm-7");
_selfy.add(155, "light grey", "light gray", "gry3", "cm-8");
_selfy.add(18, "reverse on", "rvon", "rvson", "ctrl-r", "ctrl-9");
_selfy.add(146, "reverse off", "rvof", "rvsoff", "ctrl-0");
_selfy.add(17, "cursor down", "down", "ctrl-q");
_selfy.add(145, "cursor up", "up", "shift-cursor down", "shift-down", "sh-cursor down", "sh-down");
_selfy.add(157, "cursor left", "left", "shift-cursor-right", "shift-right", "sh-cursor-right", "sh-right");
_selfy.add(29, "cursor right", "rght", "right", "ctrl-;");
_selfy.add(20, "del", "delete", "ctrl-t");
_selfy.add(14, "ctrl-n");
_selfy.add(13, "return", "ret", "ctrl-m");
_selfy.add(148, "insert", "inst", "shift-delete", "sh-delete", "shift-del", "sh-del");
_selfy.add(147, "clear", "clr", "shift-home", "sh-home", "clr/home");
_selfy.add(19, "home", "ctrl-s");
_selfy.add(133, "f1");
_selfy.add(134, "f3");
_selfy.add(135, "f5");
_selfy.add(136, "f7");
_selfy.add(8, "ctrl-h");
_selfy.add(9, "ctrl-i");
_selfy.add(14, "ctrl+n", "ctrl-n");
_selfy.add(142, "ctrl+/", "ctrl-/");
_selfy.add(165, "ctrl-g");
_selfy.add(137, "f2", "shift-f1", "sh-f1");
_selfy.add(138, "f4", "shift-f3", "sh-f3");
_selfy.add(139, "f6", "shift-f5", "sh-f5");
_selfy.add(140, "f8", "shift-f7", "sh-f7");
_selfy.add(92, "pound", "�");
_selfy.add(160, "shift-space", "sh-space");
_selfy.add(33, "shift-1", "sh-1");
_selfy.add(34, "shift-2", "sh-2");
_selfy.add(35, "shift-3", "sh-3");
_selfy.add(36, "shift-4", "sh-4");
_selfy.add(37, "shift-5", "sh-5");
_selfy.add(38, "shift-6", "sh-6");
_selfy.add(39, "shift-7", "sh-7");
_selfy.add(40, "shift-8", "sh-8");
_selfy.add(41, "shift-9", "sh-9");
_selfy.add(42, "*", "asterisk");
_selfy.add(43, "+", "plus");
_selfy.add(44, ",", "comma");
_selfy.add(45, "-", "minus");
_selfy.add(46, ".", "period");
_selfy.add(47, "/", "slash");
_selfy.add(58, ":", "colon");
_selfy.add(59, ";", "semicolon");
_selfy.add(60, "shift-comma", "shift-,", "sh-comma", "sh-,");
_selfy.add(61, "equal", "equals", "eq", "=");
_selfy.add(62, "shift-period", "shift-.", "sh-period", "sh-.");
_selfy.add(63, "shift-slash", "shift-/", "sh-slash", "sh-/");
_selfy.add(64, "@", "at");
_selfy.add(91, "shift-colon", "shift-:", "sh-colon", "sh-:");
_selfy.add(93, "shift-semicolon", "shift-;", "sh-semicolon", "sh-;");
_selfy.add(94, "?", "^", "up arrow");
_selfy.add(95, "?", "left arrow");
_selfy.add(141, "shift-return", "sh-return", "shift-ret", "sh-ret");
_selfy.add(161, "cm-k");
_selfy.add(162, "cm-i");
_selfy.add(163, "cm-t");
_selfy.add(164, "cm-@", "cm-at");
_selfy.add(165, "cm-g");
_selfy.add(166, "cm-+", "cm-plus");
_selfy.add(167, "cm-m");
_selfy.add(168, "cm-�", "cm-pound");
_selfy.add(169, "shift-�", "shift-pound", "sh-�", "sh-pound");
_selfy.add(170, "cm-n");
_selfy.add(171, "cm-q");
_selfy.add(172, "cm-d");
_selfy.add(173, "cm-z");
_selfy.add(174, "cm-s");
_selfy.add(175, "cm-p");
_selfy.add(176, "cm-a");
_selfy.add(177, "cm-e");
_selfy.add(178, "cm-r");
_selfy.add(179, "cm-w");
_selfy.add(180, "cm-h");
_selfy.add(181, "cm-j");
_selfy.add(182, "cm-l");
_selfy.add(183, "cm-y");
_selfy.add(184, "cm-u");
_selfy.add(185, "cm-o");
_selfy.add(186, "shift-@", "shift-at", "sh-@", "sh-at");
_selfy.add(187, "cm-f");
_selfy.add(188, "cm-c");
_selfy.add(189, "cm-x");
_selfy.add(190, "cm-v");
_selfy.add(191, "cm-b");
_selfy.add(192, "shift-*", "shift-asterisk", "sh-*", "sh-asterisk");
_selfy.add(219, "shift-+", "shift-plus", "sh-+", "sh-plus");
_selfy.add(220, "cm--", "cm-minus");
_selfy.add(221, "shift--", "shift-minus", "sh--", "sh-minus");
_selfy.add(222, "shift-?", "shift-up arrow", "sh-?", "sh-up arrow");
_selfy.add(223, "cm-*", "cm-asterisk");
for (var i = 65; i < 91; i++) {
var c = String.fromCharCode(i - 65 + 97);
_selfy.add(i, "shift-" + c, "sh-" + c);
}
}
this.add = function() {
var code=arguments[0];
for (var i = 1; i < arguments.length; i++) {
var placy=arguments[i];
_selfy.map[placy]=code;
_selfy.map[placy.replace("ctrl", "ct")]=code;
_selfy.map[placy.replace("ctrl", "control")]=code;
_selfy.map[placy.replace("-", " ")]=code;
_selfy.map[placy.replace("ctrl", "ct").replace("-", " ")]=code;
_selfy.map[placy.replace("ctrl", "control").replace("-", " ")]=code;
}
}
_selfy.clearScreen();
}
function Compiled(input, output) {
	this.blob=input;
this.outputter=function(txt) {console.log(txt);}
if (output) {this.outputter=output;}
this.INIT = function() {
this.blobCount=0;
this.X_REG=0.0;
this.Y_REG=0.0;
this.C_REG=0.0;
this.D_REG=0.0;
this.E_REG=0.0;
this.F_REG=0.0;
this.A_REG=0;
this.B_REG=0;
this.G_REG=0;
this.CMD_NUM=0;
this.CHANNEL=0;
this.JUMP_TARGET="";
this.USR_PARAM=0;
this._line="";
this._stack=new Array();
this._forstack=new Array();
this._memory=new Array(65535);
this._zeroflag=0
this._timeOffset=0
this._time=0
this._inputQueue=new Array();
this.CONST_0=147;
this.CONST_1="{control-q}{lgrn}micro compiler";
this.CONST_2=0;
this.CONST_3=169;
this.CONST_4=1;
this.CONST_5=2;
this.CONST_6=173;
this.CONST_7=3;
this.CONST_8=174;
this.CONST_9=162;
this.CONST_10=194;
this.CONST_11=912;
this.CONST_12="{ctrl 9}overflow";
this.CONST_13=172;
this.CONST_14=170;
this.CONST_15=109;
this.CONST_16=24;
this.CONST_17=171;
this.CONST_18=237;
this.CONST_19=56;
this.CONST_20=175;
this.CONST_21=45;
this.CONST_22=176;
this.CONST_23=13;
this.CONST_24=4;
this.CONST_25=168;
this.CONST_26=138;
this.CONST_27=152;
this.CONST_28=133;
this.CONST_29=97;
this.CONST_30=134;
this.CONST_31=98;
this.CONST_32=32;
this.CONST_33=34;
this.CONST_34=35;
this.CONST_35=5;
this.CONST_36=6;
this.CONST_37=160;
this.CONST_38=7;
this.CONST_39=8;
this.CONST_40=177;
this.CONST_41=9;
this.CONST_42=10;
this.CONST_43=65;
this.CONST_44=91;
this.CONST_45=57;
this.CONST_46=48;
this.CONST_47="{ctrl 9}error bei";
this.CONST_48=827;
this.CONST_49=58;
this.CONST_50=47;
this.CONST_51=65536;
this.CONST_52=90;
this.CONST_53=59;
this.CONST_54=44;
this.CONST_55=41;
this.CONST_56=680;
this.CONST_57=256;
this.CONST_58=255;
this.CONST_59="000000";
this.CONST_60="{left}";
this.CONST_61=828;
this.CONST_62=128;
this.CONST_63=167;
this.CONST_64=829;
this.CONST_65=136;
this.CONST_66=144;
this.CONST_67=142;
this.CONST_68=96;
this.CONST_69=158;
this.CONST_70=139;
this.CONST_71=153;
this.CONST_72=151;
this.CONST_73=129;
this.CONST_74=130;
this.CONST_75=143;
this.CONST_76=137;
this.CONST_77=76;
this.CONST_78=141;
this.CONST_79=64;
this.CONST_80="{ctrl 9}error";
this.CONST_81=842;
this.CONST_82=178;
this.CONST_83=179;
this.CONST_84=180;
this.CONST_85=228;
this.CONST_86=240;
this.CONST_87=197;
this.CONST_88=208;
this.CONST_89=199;
this.CONST_90=29;
this.CONST_91=210;
this.CONST_92=165;
this.CONST_93=205;
this.CONST_94=189;
this.CONST_95=40;
this.CONST_96=30;
this.CONST_97=831;
this.CONST_98=11;
this.CONST_99=20;
this.CONST_100=21;
this.CONST_101=54;
this.CONST_102=225;
this.CONST_103=145;
this.CONST_104=15;
this.CONST_105="test.comp";
this.CONST_106=49152;
this.CONST_107="*";
this.CONST_108="Start address";
this.CONST_109="?redo from start";
this.CONST_110=116;
this.CONST_111=164;
this.CONST_112="{control-q}errors";
this.CONST_113="adressbereich";
this.CONST_114=-1.0;
this.CONST_115=" kompiliert, zeit:";
this._dataPtr=0;
this._datas=[133,99,134,100,162,0,134,101,134,102,160,16,144,34,6,97,38,98,38,101,38,102,56,165,101,229,99,170,165,102,229,100,144,6,134,101,133,102,230,97,136,208,227,165,97,166,98,96,70,102,102,101,102,98,102,97,136,48,240,144,243,24,165,101,101,99,133,101,165,102,101,100,133,102,24,144,227,-1];
this.VAR_G=0.0;
this.VAR_A=0.0;
this.VAR_L=0.0;
this.VAR_K=0.0;
this.VAR_V=0.0;
this.VAR_H=0.0;
this.VAR_C=0.0;
this.VAR_P=0.0;
this.VAR_U=0.0;
this.VAR_ER=0.0;
this.VAR_O=0.0;
this.VAR_B=0.0;
this.VAR_S=0.0;
this.VAR_D=0.0;
this.VAR_N=0.0;
this.VAR_T=0.0;
this.VAR_H_int=0;
this.VAR_M=0.0;
this.VAR_S_array=new Array();
this.VAR_L_array=new Array();
this.VAR_F=0.0;
this.VAR_J=0.0;
this.VAR_ST=0.0;
this.VAR_Q=0.0;
this.VAR_I=0.0;
this.VAR_W=0.0;
this.VAR_R=0.0;
this.VAR_N_array=new Array();
this.VAR_A_array=new Array();
this.VAR_LP=0.0;
this.VAR_HU=0.0;
this.VAR_HF=0.0;
this.VAR_XA=0.0;
this.VAR_E=0.0;
this.VAR_A1$="";
this.VAR_A2$="";
this.VAR_TI$="";
this.VAR_L1$="";
this.VAR_L2$="";
this.VAR_Z$="";
this.VAR_S1$="";
this.VAR_S2$="";
this.VAR_B$="";
this.VAR_S$="";
}
//
this.PROGRAMSTART = function() {
this.START();
return 10;
} 
//
this.line_0 = function() {
return 10;
} 
//
this.line_10 = function() {
//
this.COMPACTMAX();
this.Y_REG=this.CONST_0;
// ignored: CHGCTX #1
this.CHR();
this.STROUT();
//
this.A_REG=this.CONST_1;
this.STROUT();
this.LINEBREAK();
return 20;
} 
//
this.line_15 = function() {
//
return 20;
} 
//
this.line_20 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_G=this.Y_REG;
//
this.GOSUB("GOSUBCONT0");
return 1780;
} 
//
this.GOSUBCONT0 = function() {
//
return 590;
} 
//
this.line_30 = function() {
//
return 40;
} 
//
this.line_40 = function() {
//
this.GOSUB("GOSUBCONT1");
return 400;
} 
//
this.GOSUBCONT1 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_3) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.VAR_K=this.Y_REG;
return 50;
} 
//
this.line_50 = function() {
//
this.Y_REG=this.VAR_V;
if ((this.Y_REG==this.CONST_2?0:1)==1) {
return "NSKIP79";}
return "SKIP79";
} 
//
this.NSKIP79 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_6) & 255;
this.Y_REG=this.CONST_5;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
//
this.Y_REG=this.CONST_7;
this.VAR_K=this.Y_REG;
return 60;
} 
//
this.SKIP79 = function() {
return 60;
} 
//
this.line_60 = function() {
//
this.Y_REG=this.VAR_K;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_8) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_C;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 70;
} 
//
this.line_70 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_V;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP80";}
return "SKIP80";
} 
//
this.NSKIP80 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_9) & 255;
this.Y_REG=this.CONST_4;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 80;
} 
//
this.SKIP80 = function() {
return 80;
} 
//
this.line_80 = function() {
//
this.Y_REG=this.VAR_K;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_90 = function() {
//
return 100;
} 
//
this.line_100 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_P=this.Y_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_10;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP81";}
return "SKIP81";
} 
//
this.NSKIP81 = function() {
//
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
//
this.Y_REG=this.CONST_4;
this.VAR_P=this.Y_REG;
return 110;
} 
//
this.SKIP81 = function() {
return 110;
} 
//
this.line_110 = function() {
//
this.GOSUB("GOSUBCONT2");
return 40;
} 
//
this.GOSUBCONT2 = function() {
return 120;
} 
//
this.line_120 = function() {
//
this.Y_REG=this.CONST_11;
this.X_REG=this.VAR_U;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP82";}
return "SKIP82";
} 
//
this.NSKIP82 = function() {
//
//
this.A_REG=this.CONST_12;
this.STROUT();
this.LINEBREAK();
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_ER;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_ER=this.X_REG;
return "RETURN";
//
return 130;
} 
//
this.SKIP82 = function() {
return 130;
} 
//
this.line_130 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_O=this.Y_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.VAR_B=this.X_REG;
//
this.Y_REG=this.CONST_6;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP83";}
return "SKIP83";
} 
//
this.NSKIP83 = function() {
return 280;
//
return 140;
} 
//
this.SKIP83 = function() {
return 140;
} 
//
this.line_140 = function() {
//
this.Y_REG=this.CONST_13;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP84";}
return "SKIP84";
} 
//
this.NSKIP84 = function() {
return 280;
//
return 150;
} 
//
this.SKIP84 = function() {
return 150;
} 
//
this.line_150 = function() {
//
this.Y_REG=this.CONST_14;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP85";}
return "SKIP85";
} 
//
this.NSKIP85 = function() {
//
//
this.Y_REG=this.CONST_15;
this.VAR_O=this.Y_REG;
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_16) & 255;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 160;
} 
//
this.SKIP85 = function() {
return 160;
} 
//
this.line_160 = function() {
//
this.Y_REG=this.CONST_17;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP86";}
return "SKIP86";
} 
//
this.NSKIP86 = function() {
//
//
this.Y_REG=this.CONST_18;
this.VAR_O=this.Y_REG;
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_19) & 255;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 170;
} 
//
this.SKIP86 = function() {
return 170;
} 
//
this.line_170 = function() {
//
this.Y_REG=this.CONST_20;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP87";}
return "SKIP87";
} 
//
this.NSKIP87 = function() {
//
//
this.Y_REG=this.CONST_21;
this.VAR_O=this.Y_REG;
return 180;
} 
//
this.SKIP87 = function() {
return 180;
} 
//
this.line_180 = function() {
//
this.Y_REG=this.CONST_22;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP88";}
return "SKIP88";
} 
//
this.NSKIP88 = function() {
//
//
this.Y_REG=this.CONST_23;
this.VAR_O=this.Y_REG;
return 190;
} 
//
this.SKIP88 = function() {
return 190;
} 
//
this.line_190 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_O;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP89";}
return "SKIP89";
} 
//
this.NSKIP89 = function() {
return 320;
//
return 200;
} 
//
this.SKIP89 = function() {
return 200;
} 
//
this.line_200 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT3");
return 400;
} 
//
this.GOSUBCONT3 = function() {
//
this.Y_REG=this.VAR_A;
this._stack.push(this.Y_REG);
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_O;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.VAR_K=this.Y_REG;
return 210;
} 
//
this.line_210 = function() {
//
this.Y_REG=this.VAR_V;
if ((this.Y_REG==this.CONST_2?0:1)==1) {
return "NSKIP90";}
return "SKIP90";
} 
//
this.NSKIP90 = function() {
this.Y_REG=this.VAR_A;
//
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_O;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
this.Y_REG=this.CONST_5;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
//
this.Y_REG=this.CONST_7;
this.VAR_K=this.Y_REG;
return 220;
} 
//
this.SKIP90 = function() {
return 220;
} 
//
this.line_220 = function() {
//
this.Y_REG=this.VAR_K;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_25) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_26) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 230;
} 
//
this.line_230 = function() {
//
this.Y_REG=this.VAR_A;
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_O;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_C;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 240;
} 
//
this.line_240 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_V;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP91";}
return "SKIP91";
} 
//
this.NSKIP91 = function() {
this.Y_REG=this.VAR_A;
//
this._stack.push(this.Y_REG);
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_O;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
this.Y_REG=this.CONST_4;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 250;
} 
//
this.SKIP91 = function() {
return 250;
} 
//
this.line_250 = function() {
//
this.Y_REG=this.VAR_K;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_14) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_27) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 260;
} 
//
this.line_260 = function() {
//
return 120;
} 
//
this.line_270 = function() {
//
return 280;
} 
//
this.line_280 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_29) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_31) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT4");
return 40;
} 
//
this.GOSUBCONT4 = function() {
return 290;
} 
//
this.line_290 = function() {
//
this.Y_REG=this.CONST_4;
this.VAR_G=this.Y_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_16) & 255;
//
this.Y_REG=this.CONST_6;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP92";}
return "SKIP92";
} 
//
this.NSKIP92 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_19) & 255;
return 300;
} 
//
this.SKIP92 = function() {
return 300;
} 
//
this.line_300 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_D=this.X_REG;
//
this.GOSUB("GOSUBCONT5");
return 570;
} 
//
this.GOSUBCONT5 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return 120;
} 
//
this.line_310 = function() {
//
return 320;
} 
//
this.line_320 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_P;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP93";}
return "SKIP93";
} 
//
this.NSKIP93 = function() {
return "RETURN";
//
return 330;
} 
//
this.SKIP93 = function() {
return 330;
} 
//
this.line_330 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 340;
} 
//
this.line_340 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_34) & 255;
return 350;
} 
//
this.line_350 = function() {
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_9) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
return 360;
} 
//
this.line_360 = function() {
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_37) & 255;
//
this.Y_REG=this.CONST_38;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
return 370;
} 
//
this.line_370 = function() {
//
this.Y_REG=this.CONST_39;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_40) & 255;
//
this.Y_REG=this.CONST_41;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 380;
} 
//
this.line_380 = function() {
//
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_P=this.Y_REG;
//
return 120;
} 
//
this.line_390 = function() {
//
return 400;
} 
//
this.line_400 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_N=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_V=this.Y_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_43;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP94";}
return "SKIP94";
} 
//
this.NSKIP94 = function() {
return 420;
//
return 410;
} 
//
this.SKIP94 = function() {
return 410;
} 
//
this.line_410 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_44;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP95";}
return "SKIP95";
} 
//
this.NSKIP95 = function() {
return 490;
//
return 420;
} 
//
this.SKIP95 = function() {
return 420;
} 
//
this.line_420 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_T=this.Y_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_14;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP96";}
return "SKIP96";
} 
//
this.NSKIP96 = function() {
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 440;
//
return 430;
} 
//
this.SKIP96 = function() {
return 430;
} 
//
this.line_430 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_17;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP97";}
return "SKIP97";
} 
//
this.NSKIP97 = function() {
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
//
this.Y_REG=this.CONST_4;
this.VAR_T=this.Y_REG;
return 440;
} 
//
this.SKIP97 = function() {
return 440;
} 
//
this.line_440 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_45;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_46;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP98";}
return "SKIP98";
} 
//
this.NSKIP98 = function() {
//
//
this.A_REG=this.CONST_47;
this.STROUT();
//
if (this.VAR_ER>1000) {
    throw "too many errors!";
}
//
this.Y_REG=this.CONST_48;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG-this.Y_REG;
this.REALOUT();
this.CRSRRIGHT();
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.REALOUT();
this.CHECKCMD();
this.LINEBREAK();
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_ER;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_ER=this.X_REG;
return 450;
} 
//
this.SKIP98 = function() {
return 450;
} 
//
this.line_450 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_49;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_50;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) & Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP99";}
return "SKIP99";
} 
//
this.NSKIP99 = function() {
//
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_N;
this.X_REG=this.X_REG*this.Y_REG;
this.Y_REG=this._stack.pop();
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.CONST_46;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_N=this.X_REG;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 450;
//
return 460;
} 
//
this.SKIP99 = function() {
return 460;
} 
//
this.line_460 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP100";}
return "SKIP100";
} 
//
this.NSKIP100 = function() {
//
//
this.Y_REG=this.VAR_N;
this.VAR_D=this.Y_REG;
return 570;
//
return 470;
} 
//
this.SKIP100 = function() {
return 470;
} 
//
this.line_470 = function() {
//
this.Y_REG=this.VAR_N;
this.X_REG=this.CONST_51;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_D=this.X_REG;
//
return 570;
} 
//
this.line_480 = function() {
//
return 490;
} 
//
this.line_490 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.VAR_V=this.X_REG;
//
this.Y_REG=this.VAR_V;
this.VAR_D=this.Y_REG;
return 500;
} 
//
this.line_500 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.VAR_T=this.X_REG;
//
this.Y_REG=this.CONST_52;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP101";}
return "SKIP101";
} 
//
this.NSKIP101 = function() {
return 560;
//
return 510;
} 
//
this.SKIP101 = function() {
return 510;
} 
//
this.line_510 = function() {
//
this.Y_REG=this.CONST_32;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP102";}
return "SKIP102";
} 
//
this.NSKIP102 = function() {
return 560;
//
return 520;
} 
//
this.SKIP102 = function() {
return 520;
} 
//
this.line_520 = function() {
//
this.Y_REG=this.CONST_53;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP103";}
return "SKIP103";
} 
//
this.NSKIP103 = function() {
return 560;
//
return 530;
} 
//
this.SKIP103 = function() {
return 530;
} 
//
this.line_530 = function() {
//
this.Y_REG=this.CONST_54;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP104";}
return "SKIP104";
} 
//
this.NSKIP104 = function() {
return 560;
//
return 540;
} 
//
this.SKIP104 = function() {
return 540;
} 
//
this.line_540 = function() {
//
this.Y_REG=this.CONST_55;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP105";}
return "SKIP105";
} 
//
this.NSKIP105 = function() {
return 560;
//
return 550;
} 
//
this.SKIP105 = function() {
return 550;
} 
//
this.line_550 = function() {
//
this.Y_REG=this.CONST_34;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP106";}
return "SKIP106";
} 
//
this.NSKIP106 = function() {
return 500;
//
return 560;
} 
//
this.SKIP106 = function() {
return 560;
} 
//
this.line_560 = function() {
//
this.Y_REG=this.CONST_43;
this.X_REG=this.VAR_D;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_D=this.X_REG;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_D;
this.X_REG=this.X_REG*this.Y_REG;
this.Y_REG=this.CONST_56;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_D=this.X_REG;
return 570;
} 
//
this.line_570 = function() {
//
this.Y_REG=this.CONST_57;
this.X_REG=this.VAR_D;
this.X_REG=this.X_REG/this.Y_REG;
this.VAR_H_int=this.X_REG;
this.VAR_H_int=Math.floor(this.VAR_H_int);
//
this.Y_REG=this.VAR_H_int;
this.VAR_H=this.Y_REG;
//
this.Y_REG=this.CONST_57;
this.X_REG=this.VAR_H;
this.X_REG=this.X_REG*this.Y_REG;
this.Y_REG=this.X_REG;
this.X_REG=this.VAR_D;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_L=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_L;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.CONST_58;
this.X_REG=Math.floor(this.X_REG) & Math.floor(this.Y_REG);
this.VAR_C=this.X_REG;
//
return "RETURN";
} 
//
this.line_580 = function() {
//
return 590;
} 
//
this.line_590 = function() {
//
this.C_REG=this.CONST_5;
this.GETSTRCHANNEL();
this.VAR_A1$=this.A_REG;
this.GETSTRCHANNEL();
this.VAR_A2$=this.A_REG;
//
this.B_REG=this.CONST_59;
this.WRITETID(this.B_REG);
return 600;
} 
//
this.line_600 = function() {
//
this.C_REG=this.CONST_5;
this.GETSTRCHANNEL();
this.VAR_L1$=this.A_REG;
this.GETSTRCHANNEL();
this.VAR_L2$=this.A_REG;
//
this.COMPACTMAX();
this.B_REG=this.VAR_Z$;
this.A_REG=this.VAR_L2$;
this.CONCAT();
this.B_REG=this.A_REG;
// ignored: CHGCTX #0
this.ASC();
this._stack.push(this.X_REG);
// ignored: CHGCTX #1
this.B_REG=this.VAR_Z$;
this.A_REG=this.VAR_L1$;
this.CONCAT();
this.B_REG=this.A_REG;
// ignored: CHGCTX #0
this.ASC();
this.Y_REG=this._stack.pop();
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_T=this.X_REG;
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_T;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP107";}
return "SKIP107";
} 
//
this.NSKIP107 = function() {
return 1920;
//
return 610;
} 
//
this.SKIP107 = function() {
return 610;
} 
//
this.line_610 = function() {
//
this.C_REG=this.CONST_5;
this.GETSTRCHANNEL();
this.VAR_S1$=this.A_REG;
this.GETSTRCHANNEL();
this.VAR_S2$=this.A_REG;
//
this.COMPACTMAX();
this.B_REG=this.VAR_Z$;
this.A_REG=this.VAR_S2$;
this.CONCAT();
this.B_REG=this.A_REG;
// ignored: CHGCTX #0
this.ASC();
this.Y_REG=this.CONST_57;
this.X_REG=this.X_REG*this.Y_REG;
this._stack.push(this.X_REG);
// ignored: CHGCTX #1
this.B_REG=this.VAR_Z$;
this.A_REG=this.VAR_S1$;
this.CONCAT();
this.B_REG=this.A_REG;
// ignored: CHGCTX #0
this.ASC();
this.Y_REG=this._stack.pop();
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_T=this.X_REG;
return 620;
} 
//
this.line_620 = function() {
//
this.Y_REG=this.VAR_M;
this.X_REG=this.Y_REG;
this.Y_REG=this.VAR_T;
this.G_REG=this.VAR_S_array;
this.ARRAYSTORE_REAL();
//
this.Y_REG=this.VAR_M;
this.X_REG=this.Y_REG;
this.Y_REG=this.VAR_A;
this.G_REG=this.VAR_L_array;
this.ARRAYSTORE_REAL();
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_M;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_M=this.X_REG;
//
this.A_REG=this.CONST_60;
this.STROUT();
//
this.X_REG=this.VAR_T;
this.REALOUT();
this.CRSRRIGHT();
return 630;
} 
//
this.line_630 = function() {
//
this.Y_REG=this.VAR_F;
if ((this.Y_REG==this.CONST_2?0:1)==1) {
return "NSKIP108";}
return "SKIP108";
} 
//
this.NSKIP108 = function() {
//
//
this.Y_REG=this.VAR_F;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_T=this.X_REG;
this.Y_REG=this.CONST_4;
//
this.X_REG=this.VAR_F;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_T;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
this.Y_REG=this.CONST_38;
//
this.X_REG=this.VAR_F;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_39;
this.X_REG=this.VAR_T;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
this.Y_REG=this.CONST_41;
//
this.X_REG=this.VAR_F;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_T;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
//
this.Y_REG=this.CONST_2;
this.VAR_F=this.Y_REG;
return 640;
} 
//
this.SKIP108 = function() {
return 640;
} 
//
this.line_640 = function() {
//
this.Y_REG=this.CONST_61;
this.VAR_J=this.Y_REG;
//

return "SKIP109";
} 
//
this.SKIP109 = function() {
return 650;
} 
//
this.line_650 = function() {
//
this.C_REG=this.CONST_5;
this.GETSTRCHANNEL();
this.VAR_B$=this.A_REG;
//
this.READSTATUS();
this.Y_REG=this.tmpy;
if ((this.Y_REG==this.CONST_2?0:1)==1) {
return "NSKIP110";}
return "SKIP110";
} 
//
this.NSKIP110 = function() {
return 1920;
//
return 660;
} 
//
this.SKIP110 = function() {
return 660;
} 
//
this.line_660 = function() {
//
this.COMPACTMAX();
this.B_REG=this.VAR_Z$;
this.A_REG=this.VAR_B$;
this.CONCAT();
this.B_REG=this.A_REG;
// ignored: CHGCTX #0
this.ASC();
this.VAR_B=this.X_REG;
//
this.Y_REG=this.VAR_J;
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_B;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_32;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG!=this.Y_REG?-1:0);
this.Y_REG=this.X_REG;
this.X_REG=this.VAR_Q;
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP111";}
return "SKIP111";
} 
//
this.NSKIP111 = function() {
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_J;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_J=this.X_REG;
return 670;
} 
//
this.SKIP111 = function() {
return 670;
} 
//
this.line_670 = function() {
//
this.Y_REG=this.CONST_33;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP112";}
return "SKIP112";
} 
//
this.NSKIP112 = function() {
//
//
this.Y_REG=this.VAR_Q;
this.X_REG=~this.Y_REG;
this.VAR_Q=this.X_REG;
return 680;
} 
//
this.SKIP112 = function() {
return 680;
} 
//
this.line_680 = function() {
//
this.Y_REG=this.CONST_62;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
this.Y_REG=this.VAR_Q;
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP113";}
return "SKIP113";
} 
//
this.NSKIP113 = function() {
//
//
this.A_REG=this.VAR_B$;
this.STROUT();
return 690;
} 
//
this.SKIP113 = function() {
return 690;
} 
//
this.line_690 = function() {
//
this.X_REG=this.VAR_B;
this._memory[780]=Math.floor(this.X_REG) & 255;
//
this._memory[15]=Math.floor(this.CONST_2) & 255;
return 710;
} 
//
this.line_700 = function() {
//
return 710;
} 
//
this.line_710 = function() {
//
this.Y_REG=this.VAR_Q;
if ((this.Y_REG==this.CONST_2?0:1)==1) {
return "NSKIP114";}
return "SKIP114";
} 
//
this.NSKIP114 = function() {
return 650;
//
return 720;
} 
//
this.SKIP114 = function() {
return 720;
} 
//
this.line_720 = function() {
//
this.Y_REG=this.CONST_32;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP115";}
return "SKIP115";
} 
//
this.NSKIP115 = function() {
this.LINEBREAK();
this.GOSUB("GOSUBCONT6");
return 770;
} 
//
this.GOSUBCONT6 = function() {
return 600;
//
//
return 730;
} 
//
this.SKIP115 = function() {
return 730;
} 
//
this.line_730 = function() {
//
this.Y_REG=this.CONST_63;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP116";}
return "SKIP116";
} 
//
this.NSKIP116 = function() {
this.GOSUB("GOSUBCONT7");
//
return 770;
} 
//
this.GOSUBCONT7 = function() {
return 640;
//
return 740;
} 
//
this.SKIP116 = function() {
return 740;
} 
//
this.line_740 = function() {
//
this.Y_REG=this.CONST_49;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP117";}
return "SKIP117";
} 
//
this.NSKIP117 = function() {
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_J;
this.X_REG=this.X_REG-this.Y_REG;
this.VAR_J=this.X_REG;
this.GOSUB("GOSUBCONT8");
//
return 770;
} 
//
this.GOSUBCONT8 = function() {
return 640;
//
return 750;
} 
//
this.SKIP117 = function() {
return 750;
} 
//
this.line_750 = function() {
//
return 650;
} 
//
this.line_760 = function() {
//
return 770;
} 
//
this.line_770 = function() {
//
this.X_REG=Math.floor(this._memory[828]) & 255;
this.VAR_B=this.X_REG;
//
this.Y_REG=this.CONST_64;
this.VAR_U=this.Y_REG;
//
this.Y_REG=this.VAR_J;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_J;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
return 780;
} 
//
this.line_780 = function() {
//
this.Y_REG=this.CONST_65;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP118";}
return "SKIP118";
} 
//
this.NSKIP118 = function() {
return 940;
//
return 790;
} 
//
this.SKIP118 = function() {
return 790;
} 
//
this.line_790 = function() {
//
this.Y_REG=this.CONST_66;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_67;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_62;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP119";}
return "SKIP119";
} 
//
this.NSKIP119 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_68) & 255;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return "RETURN";
//
return 800;
} 
//
this.SKIP119 = function() {
return 800;
} 
//
this.line_800 = function() {
//
this.Y_REG=this.CONST_69;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP120";}
return "SKIP120";
} 
//
this.NSKIP120 = function() {
return 1680;
//
return 810;
} 
//
this.SKIP120 = function() {
return 810;
} 
//
this.line_810 = function() {
//
this.Y_REG=this.CONST_70;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP121";}
return "SKIP121";
} 
//
this.NSKIP121 = function() {
return 1040;
//
return 820;
} 
//
this.SKIP121 = function() {
return 820;
} 
//
this.line_820 = function() {
//
this.Y_REG=this.CONST_71;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP122";}
return "SKIP122";
} 
//
this.NSKIP122 = function() {
return 1170;
//
return 830;
} 
//
this.SKIP122 = function() {
return 830;
} 
//
this.line_830 = function() {
//
this.Y_REG=this.CONST_72;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP123";}
return "SKIP123";
} 
//
this.NSKIP123 = function() {
return 1720;
//
return 840;
} 
//
this.SKIP123 = function() {
return 840;
} 
//
this.line_840 = function() {
//
this.Y_REG=this.CONST_73;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP124";}
return "SKIP124";
} 
//
this.NSKIP124 = function() {
return 1510;
//
return 850;
} 
//
this.SKIP124 = function() {
return 850;
} 
//
this.line_850 = function() {
//
this.Y_REG=this.CONST_74;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP125";}
return "SKIP125";
} 
//
this.NSKIP125 = function() {
return 1650;
//
return 860;
} 
//
this.SKIP125 = function() {
return 860;
} 
//
this.line_860 = function() {
//
this.Y_REG=this.CONST_75;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP126";}
return "SKIP126";
} 
//
this.NSKIP126 = function() {
return "RETURN";
//
return 870;
} 
//
this.SKIP126 = function() {
return 870;
} 
//
this.line_870 = function() {
//
this.Y_REG=this.CONST_76;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP127";}
return "SKIP127";
} 
//
this.NSKIP127 = function() {
//
//
this.Y_REG=this.CONST_77;
this.VAR_O=this.Y_REG;
return 1480;
//
return 880;
} 
//
this.SKIP127 = function() {
return 880;
} 
//
this.line_880 = function() {
//
this.Y_REG=this.CONST_78;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP128";}
return "SKIP128";
} 
//
this.NSKIP128 = function() {
//
//
this.Y_REG=this.CONST_32;
this.VAR_O=this.Y_REG;
return 1480;
//
return 890;
} 
//
this.SKIP128 = function() {
return 890;
} 
//
this.line_890 = function() {
//
this.Y_REG=this.CONST_52;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_46;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) | Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP129";}
return "SKIP129";
} 
//
this.NSKIP129 = function() {
return 920;
//
return 900;
} 
//
this.SKIP129 = function() {
return 900;
} 
//
this.line_900 = function() {
//
this.Y_REG=this.CONST_79;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP130";}
return "SKIP130";
} 
//
this.NSKIP130 = function() {
return 950;
//
return 910;
} 
//
this.SKIP130 = function() {
return 910;
} 
//
this.line_910 = function() {
//
this.Y_REG=this.CONST_49;
this.X_REG=this.VAR_B;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP131";}
return "SKIP131";
} 
//
this.NSKIP131 = function() {
//
//
this.Y_REG=this.CONST_61;
this.VAR_U=this.Y_REG;
//
//
this.Y_REG=this.CONST_77;
this.VAR_O=this.Y_REG;
return 1480;
//
return 920;
} 
//
this.SKIP131 = function() {
return 920;
} 
//
this.line_920 = function() {
//
this.A_REG=this.CONST_80;
this.STROUT();
//
this.Y_REG=this.CONST_48;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG-this.Y_REG;
this.REALOUT();
this.CRSRRIGHT();
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.REALOUT();
this.CHECKCMD();
this.LINEBREAK();
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_ER;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_ER=this.X_REG;
//
return "RETURN";
} 
//
this.line_930 = function() {
//
return 940;
} 
//
this.line_940 = function() {
//
this.Y_REG=this.CONST_61;
this.VAR_I=this.Y_REG;
//
this.Y_REG=this.CONST_81;
this._stack.push(this.Y_REG);
//
this.Y_REG=this.CONST_4;
this._stack.push(this.Y_REG);
//
this.INITFOR("FORLOOP0","VAR_I");
return "FORLOOP0";
} 
//
this.FORLOOP0 = function() {
//
this.Y_REG=this.VAR_I;
this._stack.push(this.Y_REG);
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_I;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
//
this.NEXT("0");
if ((this.A_REG==this.CONST_2?0:1)==0) {
return "($JUMP)";}
return 950;
} 
//
this.line_950 = function() {
//
this.Y_REG=this.CONST_61;
this.VAR_U=this.Y_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_43;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP132";}
return "SKIP132";
} 
//
this.NSKIP132 = function() {
return 920;
//
return 960;
} 
//
this.SKIP132 = function() {
return 960;
} 
//
this.line_960 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_52;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP133";}
return "SKIP133";
} 
//
this.NSKIP133 = function() {
return 920;
//
return 970;
} 
//
this.SKIP133 = function() {
return 970;
} 
//
this.line_970 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_82;
this.X_REG=(this.X_REG!=this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP134";}
return "SKIP134";
} 
//
this.NSKIP134 = function() {
return 920;
//
return 980;
} 
//
this.SKIP134 = function() {
return 980;
} 
//
this.line_980 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT9");
return 100;
} 
//
this.GOSUBCONT9 = function() {
//
this.X_REG=Math.floor(this._memory[828]) & 255;
this.VAR_D=this.X_REG;
return 990;
} 
//
this.line_990 = function() {
//
this.GOSUB("GOSUBCONT10");
return 560;
} 
//
this.GOSUBCONT10 = function() {
return 1000;
} 
//
this.line_1000 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_78) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1010;
} 
//
this.line_1010 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_67) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_C;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1020;
} 
//
this.line_1020 = function() {
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1030 = function() {
//
return 1040;
} 
//
this.line_1040 = function() {
//
this.GOSUB("GOSUBCONT11");
return 100;
} 
//
this.GOSUBCONT11 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.VAR_W=this.X_REG;
//
this.Y_REG=this.CONST_40;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP135";}
return "SKIP135";
} 
//
this.NSKIP135 = function() {
return 920;
//
return 1050;
} 
//
this.SKIP135 = function() {
return 1050;
} 
//
this.line_1050 = function() {
//
this.Y_REG=this.CONST_83;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP136";}
return "SKIP136";
} 
//
this.NSKIP136 = function() {
return 920;
//
return 1060;
} 
//
this.SKIP136 = function() {
return 1060;
} 
//
this.line_1060 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_34) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 1070;
} 
//
this.line_1070 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_40;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_83;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) & Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP137";}
return "SKIP137";
} 
//
this.NSKIP137 = function() {
//
//
this.Y_REG=this.CONST_84;
this.VAR_W=this.Y_REG;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 1080;
} 
//
this.SKIP137 = function() {
return 1080;
} 
//
this.line_1080 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_83;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_40;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) & Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP138";}
return "SKIP138";
} 
//
this.NSKIP138 = function() {
//
//
this.Y_REG=this.CONST_84;
this.VAR_W=this.Y_REG;
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 1090;
} 
//
this.SKIP138 = function() {
return 1090;
} 
//
this.line_1090 = function() {
//
this.GOSUB("GOSUBCONT12");
return 100;
} 
//
this.GOSUBCONT12 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_85) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_34) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_86) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_24) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.VAR_A;
this.VAR_F=this.Y_REG;
return 1100;
} 
//
this.line_1100 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_36) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_87) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 1110;
} 
//
this.line_1110 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_86) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_88) & 255;
//
this.Y_REG=this.CONST_39;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_86) & 255;
return 1120;
} 
//
this.line_1120 = function() {
//
this.Y_REG=this.CONST_82;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP139";}
return "SKIP139";
} 
//
this.NSKIP139 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_88) & 255;
this.Y_REG=this.CONST_39;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_88) & 255;
return 1130;
} 
//
this.SKIP139 = function() {
return 1130;
} 
//
this.line_1130 = function() {
//
this.Y_REG=this.CONST_83;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP140";}
return "SKIP140";
} 
//
this.NSKIP140 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_66) & 255;
this.Y_REG=this.CONST_5;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_22) & 255;
return 1140;
} 
//
this.SKIP140 = function() {
return 1140;
} 
//
this.line_1140 = function() {
//
this.Y_REG=this.CONST_40;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP141";}
return "SKIP141";
} 
//
this.NSKIP141 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_22) & 255;
this.Y_REG=this.CONST_5;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_66) & 255;
return 1150;
} 
//
this.SKIP141 = function() {
return 1150;
} 
//
this.line_1150 = function() {
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.Y_REG=this.VAR_A;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1160 = function() {
//
return 1170;
} 
//
this.line_1170 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.VAR_W=this.X_REG;
//
this.Y_REG=this.CONST_32;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP142";}
return "SKIP142";
} 
//
this.NSKIP142 = function() {
return 1450;
//
return 1180;
} 
//
this.SKIP142 = function() {
return 1180;
} 
//
this.line_1180 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_32;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
this._stack.push(this.X_REG);
this.Y_REG=this.CONST_53;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
this.Y_REG=this._stack.pop();
this.X_REG=Math.floor(this.X_REG) & Math.floor(this.Y_REG);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP143";}
return "SKIP143";
} 
//
this.NSKIP143 = function() {
return "RETURN";
//
return 1190;
} 
//
this.SKIP143 = function() {
return 1190;
} 
//
this.line_1190 = function() {
//
this.Y_REG=this.CONST_53;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP144";}
return "SKIP144";
} 
//
this.NSKIP144 = function() {
//
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 1170;
//
return 1200;
} 
//
this.SKIP144 = function() {
return 1200;
} 
//
this.line_1200 = function() {
//
this.Y_REG=this.CONST_89;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP145";}
return "SKIP145";
} 
//
this.NSKIP145 = function() {
return 1300;
//
//
//
return 1210;
} 
//
this.SKIP145 = function() {
return 1210;
} 
//
this.line_1210 = function() {
//
this.Y_REG=this.CONST_33;
this.X_REG=this.VAR_W;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP146";}
return "SKIP146";
} 
//
this.NSKIP146 = function() {
return 1340;
//
//
//
return 1220;
} 
//
this.SKIP146 = function() {
return 1230;
} 
//
this.line_1220 = function() {
//
return 1230;
} 
//
this.line_1230 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_3) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_90) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
return 1240;
} 
//
this.line_1240 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_91) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_58) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1250;
} 
//
this.line_1250 = function() {
//
this.GOSUB("GOSUBCONT13");
return 100;
} 
//
this.GOSUBCONT13 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 1260;
} 
//
this.line_1260 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_14) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_92) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 1270;
} 
//
this.line_1270 = function() {
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_93) & 255;
//
this.Y_REG=this.CONST_38;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_94) & 255;
return 1280;
} 
//
this.line_1280 = function() {
//
this.Y_REG=this.CONST_39;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return 1170;
} 
//
this.line_1290 = function() {
//
return 1300;
} 
//
this.line_1300 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_95;
this.X_REG=(this.X_REG!=this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP147";}
return "SKIP147";
} 
//
this.NSKIP147 = function() {
return 920;
//
return 1310;
} 
//
this.SKIP147 = function() {
return 1310;
} 
//
this.line_1310 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT14");
return 100;
} 
//
this.GOSUBCONT14 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_91) & 255;
return 1320;
} 
//
this.line_1320 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_58) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
return 1170;
} 
//
this.line_1330 = function() {
//
return 1340;
} 
//
this.line_1340 = function() {
//
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_D=this.X_REG;
//
this.GOSUB("GOSUBCONT15");
return 570;
} 
//
this.GOSUBCONT15 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_3) & 255;
return 1350;
} 
//
this.line_1350 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_37) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1360;
} 
//
this.line_1360 = function() {
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_96) & 255;
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_17) & 255;
return 1370;
} 
//
this.line_1370 = function() {
//
this.Y_REG=this.CONST_38;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_16) & 255;
//
this.Y_REG=this.CONST_39;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_66) & 255;
//
this.Y_REG=this.CONST_41;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
return 1380;
} 
//
this.line_1380 = function() {
//
this.Y_REG=this.CONST_41;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_W=this.X_REG;
//
this.Y_REG=this.CONST_42;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_I=this.Y_REG;
return 1390;
} 
//
this.line_1390 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_I;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_I=this.X_REG;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.Y_REG=this.CONST_11;
this.X_REG=this.VAR_U;
this.X_REG=(this.X_REG>this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP148";}
return "SKIP148";
} 
//
this.NSKIP148 = function() {
return 1430;
//
return 1400;
} 
//
this.SKIP148 = function() {
return 1400;
} 
//
this.line_1400 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_33;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP149";}
return "SKIP149";
} 
//
this.NSKIP149 = function() {
return 1430;
//
return 1410;
} 
//
this.SKIP149 = function() {
return 1410;
} 
//
this.line_1410 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_2;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP150";}
return "SKIP150";
} 
//
this.NSKIP150 = function() {
return 1430;
//
return 1420;
} 
//
this.SKIP150 = function() {
return 1420;
} 
//
this.line_1420 = function() {
//
this.Y_REG=this.VAR_A;
this._stack.push(this.Y_REG);
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return 1390;
} 
//
this.line_1430 = function() {
//
this.Y_REG=this.VAR_W;
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_I;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1440;
} 
//
this.line_1440 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
return 1170;
} 
//
this.line_1450 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_3) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_23) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
return 1460;
} 
//
this.line_1460 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_91) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_58) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1470 = function() {
//
return 1480;
} 
//
this.line_1480 = function() {
//
this.Y_REG=this.VAR_A;
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_O;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
this.GOSUB("GOSUBCONT16");
return 400;
} 
//
this.GOSUBCONT16 = function() {
return 1490;
} 
//
this.line_1490 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_R;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_R=this.X_REG;
//
this.Y_REG=this.VAR_R;
this.X_REG=this.Y_REG;
this.Y_REG=this.VAR_N;
this.G_REG=this.VAR_N_array;
this.ARRAYSTORE_REAL();
//
this.Y_REG=this.VAR_R;
this.X_REG=this.Y_REG;
this.Y_REG=this.VAR_A;
this.G_REG=this.VAR_A_array;
this.ARRAYSTORE_REAL();
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1500 = function() {
//
return 1510;
} 
//
this.line_1510 = function() {
//
this.Y_REG=this.CONST_97;
this.VAR_U=this.Y_REG;
//
this.GOSUB("GOSUBCONT17");
return 100;
} 
//
this.GOSUBCONT17 = function() {
return 1520;
} 
//
this.line_1520 = function() {
//
this.Y_REG=this.VAR_A;
this.VAR_LP=this.Y_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_77) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1530;
} 
//
this.line_1530 = function() {
//
this.Y_REG=this.VAR_U;
this.VAR_HU=this.Y_REG;
//
this.Y_REG=this.CONST_64;
this.VAR_U=this.Y_REG;
//
this.GOSUB("GOSUBCONT18");
return 40;
} 
//
this.GOSUBCONT18 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_HU;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
return 1540;
} 
//
this.line_1540 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_34) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1550;
} 
//
this.line_1550 = function() {
//
this.Y_REG=this.VAR_F;
this.VAR_HF=this.Y_REG;
//
this.Y_REG=this.CONST_40;
this.VAR_W=this.Y_REG;
//
this.GOSUB("GOSUBCONT19");
return 1090;
} 
//
this.GOSUBCONT19 = function() {
//
this.Y_REG=this.VAR_HF;
this.VAR_F=this.Y_REG;
return 1560;
} 
//
this.line_1560 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_7) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_5) & 255;
//
this.Y_REG=this.CONST_41;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_98) & 255;
return 1570;
} 
//
this.line_1570 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_22) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG-this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_86) & 255;
return 1580;
} 
//
this.line_1580 = function() {
//
this.Y_REG=this.VAR_A;
this.VAR_XA=this.Y_REG;
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_77) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1590;
} 
//
this.line_1590 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_3;
this.X_REG=(this.X_REG!=this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP151";}
return "SKIP151";
} 
//
this.NSKIP151 = function() {
this.Y_REG=this.VAR_A;
//
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_3) & 255;
this.Y_REG=this.CONST_4;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_4) & 255;
this.Y_REG=this.CONST_5;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_9) & 255;
this.Y_REG=this.CONST_7;
//
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1610;
//
return 1600;
} 
//
this.SKIP151 = function() {
return 1600;
} 
//
this.line_1600 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT20");
return 100;
} 
//
this.GOSUBCONT20 = function() {
return 1610;
} 
//
this.line_1610 = function() {
//
this.Y_REG=this.CONST_61;
this.VAR_U=this.Y_REG;
//
this.Y_REG=this.CONST_14;
this.VAR_B=this.Y_REG;
//
this.GOSUB("GOSUBCONT21");
return 150;
} 
//
this.GOSUBCONT21 = function() {
return 1620;
} 
//
this.line_1620 = function() {
//
this.Y_REG=this.VAR_A;
this.VAR_D=this.Y_REG;
//
this.GOSUB("GOSUBCONT22");
return 570;
} 
//
this.GOSUBCONT22 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_LP;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_LP;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1630;
} 
//
this.line_1630 = function() {
//
this.X_REG=Math.floor(this._memory[829]) & 255;
this.VAR_D=this.X_REG;
//
this.GOSUB("GOSUBCONT23");
return 990;
} 
//
this.GOSUBCONT23 = function() {
//
return "RETURN";
} 
//
this.line_1640 = function() {
//
return 1650;
} 
//
this.line_1650 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_LP;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_D=this.X_REG;
//
this.GOSUB("GOSUBCONT24");
return 570;
} 
//
this.GOSUBCONT24 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_77) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
this.Y_REG=this.VAR_A;
this.VAR_D=this.Y_REG;
//
this.GOSUB("GOSUBCONT25");
return 570;
} 
//
this.GOSUBCONT25 = function() {
return 1660;
} 
//
this.line_1660 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_XA;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_XA;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
return "RETURN";
} 
//
this.line_1670 = function() {
//
return 1680;
} 
//
this.line_1680 = function() {
//
this.GOSUB("GOSUBCONT26");
return 100;
} 
//
this.GOSUBCONT26 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_99) & 255;
return 1690;
} 
//
this.line_1690 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_100) & 255;
return 1700;
} 
//
this.line_1700 = function() {
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_32) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_101) & 255;
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_102) & 255;
//
this.Y_REG=this.CONST_38;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1710 = function() {
//
return 1720;
} 
//
this.line_1720 = function() {
//
this.GOSUB("GOSUBCONT27");
return 100;
} 
//
this.GOSUBCONT27 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_28) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
return 1730;
} 
//
this.line_1730 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_30) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_34) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1740;
} 
//
this.line_1740 = function() {
//
this.Y_REG=this.VAR_U;
this.X_REG=this._memory[Math.floor(this.Y_REG) & 65535];
this.Y_REG=this.CONST_54;
this.X_REG=(this.X_REG!=this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP152";}
return "SKIP152";
} 
//
this.NSKIP152 = function() {
return 920;
//
return 1750;
} 
//
this.SKIP152 = function() {
return 1750;
} 
//
this.line_1750 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_U;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_U=this.X_REG;
//
this.GOSUB("GOSUBCONT28");
return 100;
} 
//
this.GOSUBCONT28 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_37) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
return 1760;
} 
//
this.line_1760 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_103) & 255;
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_33) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
//
return "RETURN";
} 
//
this.line_1770 = function() {
//
return 1790;
} 
//
this.line_1780 = function() {
return 1790;
} 
//
this.line_1790 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_A=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_B=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_U=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_I=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_J=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_K=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_V=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_D=this.Y_REG;
return 1800;
} 
//
this.line_1800 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_C=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_H=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_L=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_W=this.Y_REG;
return 1810;
} 
//
this.line_1810 = function() {
//
this._memory[53281]=Math.floor(this.CONST_2) & 255;
//
this._memory[53280]=Math.floor(this.CONST_2) & 255;
//
this._memory[646]=Math.floor(this.CONST_104) & 255;
return 1820;
} 
//
this.line_1820 = function() {
//
this.B_REG=this.CONST_105;
this.VAR_S$=this.B_REG;
//
this.Y_REG=this.CONST_106;
this.VAR_S=this.Y_REG;
//
this.COMPACTMAX();
this.Y_REG=this.CONST_2;
// ignored: CHGCTX #1
this.CHR();
this.VAR_Z$=this.A_REG;
return 1840;
} 
//
this.line_1830 = function() {
//
return 1840;
} 
//
this.line_1840 = function() {
//
this.RESTORE();
//
this.B_REG=this.CONST_107;
this.A_REG=this.CONST_105;
// ignored: CHGCTX #0
this.SEQ();
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP153";}
return "SKIP153";
} 
//
this.NSKIP153 = function() {
//
//
this.END();
return;
} 
//
this.SKIP153 = function() {
return "INPUT1";
} 
//
this.line_1850 = function() {
//
return "INPUT1";
} 
//
this.INPUT1 = function() {
this.CLEARQUEUE();
this.COMPACTMAX();
this.A_REG=this.CONST_108;
this.STROUT();
this.QMARKOUT1();
this.INPUTNUMBER();
if ((this.X_REG==this.CONST_2?0:1)==0) {
return "INPUT1_0";}
this.A_REG=this.CONST_109;
this.STROUT();
this.LINEBREAK();
return "INPUT1";
} 
//
this.INPUT1_0 = function() {
this.VAR_S=this.Y_REG;
this.QUEUESIZE();
if ((this.X_REG==this.CONST_2?0:1)==0) {
return "INPUTCHECK1";}
this.EXTRAIGNORED();
return "INPUTCHECK1";
} 
//
this.INPUTCHECK1 = function() {
//
this.LINEBREAK();
//
this.Y_REG=this.CONST_36;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 1860;
} 
//
this.line_1860 = function() {
//
this.Y_REG=this.VAR_A;
this.VAR_D=this.Y_REG;
//
this.GOSUB("GOSUBCONT29");
return 570;
} 
//
this.GOSUBCONT29 = function() {
//
this.Y_REG=this.VAR_S;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_77) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1870;
} 
//
this.line_1870 = function() {
//
this.Y_REG=this.CONST_7;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_77) & 255;
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_110) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this.Y_REG=this.X_REG;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_111) & 255;
return 1910;
} 
//
this.line_1880 = function() {
//
return 1910;
} 
//
this.line_1910 = function() {
//
return "RETURN";
} 
//
this.line_1920 = function() {
//
return 1930;
} 
//
this.line_1930 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_R;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP154";}
return "SKIP154";
} 
//
this.NSKIP154 = function() {
return 1980;
//
return 1940;
} 
//
this.SKIP154 = function() {
return 1940;
} 
//
this.line_1940 = function() {
//
this.Y_REG=this.CONST_4;
this.VAR_I=this.Y_REG;
//
this.Y_REG=this.VAR_R;
this._stack.push(this.Y_REG);
//
this.Y_REG=this.CONST_4;
this._stack.push(this.Y_REG);
//
this.INITFOR("FORLOOP1","VAR_I");
return "FORLOOP1";
} 
//
this.FORLOOP1 = function() {
//
this.X_REG=this.VAR_I;
this.G_REG=this.VAR_N_array;
// ignored: CHGCTX #0
this.ARRAYACCESS_REAL();
this.VAR_N=this.X_REG;
//
this.X_REG=this.VAR_I;
this.G_REG=this.VAR_A_array;
// ignored: CHGCTX #0
this.ARRAYACCESS_REAL();
this.VAR_W=this.X_REG;
//
this.Y_REG=this.CONST_2;
this.VAR_D=this.Y_REG;
return 1950;
} 
//
this.line_1950 = function() {
//
this.Y_REG=this.CONST_2;
this.VAR_T=this.Y_REG;
//
this.Y_REG=this.VAR_M;
this._stack.push(this.Y_REG);
//
this.Y_REG=this.CONST_4;
this._stack.push(this.Y_REG);
//
this.INITFOR("FORLOOP2","VAR_T");
return "FORLOOP2";
} 
//
this.FORLOOP2 = function() {
//
this.X_REG=this.VAR_T;
this.G_REG=this.VAR_S_array;
// ignored: CHGCTX #0
this.ARRAYACCESS_REAL();
this.Y_REG=this.VAR_N;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP155";}
return "SKIP155";
} 
//
this.NSKIP155 = function() {
//
//
this.X_REG=this.VAR_T;
this.G_REG=this.VAR_L_array;
// ignored: CHGCTX #0
this.ARRAYACCESS_REAL();
this.VAR_D=this.X_REG;
//
//
this.Y_REG=this.VAR_M;
this.VAR_T=this.Y_REG;
return 1960;
} 
//
this.SKIP155 = function() {
return 1960;
} 
//
this.line_1960 = function() {
//
//
this.NEXT("VAR_T");
if ((this.A_REG==this.CONST_2?0:1)==0) {
return "($JUMP)";}
//
this.GOSUB("GOSUBCONT30");
return 570;
} 
//
this.GOSUBCONT30 = function() {
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_W;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 1970;
} 
//
this.line_1970 = function() {
//
this.Y_REG=this.CONST_5;
this.X_REG=this.VAR_W;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
//
this.NEXT("VAR_I");
if ((this.A_REG==this.CONST_2?0:1)==0) {
return "($JUMP)";}
return 1980;
} 
//
this.line_1980 = function() {
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_G;
this.X_REG=(this.X_REG==this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP156";}
return "SKIP156";
} 
//
this.NSKIP156 = function() {
return 2030;
//
return 1990;
} 
//
this.SKIP156 = function() {
return 1990;
} 
//
this.line_1990 = function() {
//
this.Y_REG=this.VAR_A;
this.VAR_D=this.Y_REG;
//
this.GOSUB("GOSUBCONT31");
return 570;
} 
//
this.GOSUBCONT31 = function() {
//
this.Y_REG=this.CONST_24;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_L;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_35;
this.X_REG=this.VAR_S;
this.X_REG=this.X_REG+this.Y_REG;
this._stack.push(this.X_REG);
this.X_REG=this.VAR_H;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
return 2000;
} 
//
this.line_2000 = function() {
//
this.READNUMBER();
this.VAR_D=this.Y_REG;
//
this.Y_REG=this.CONST_2;
this.X_REG=this.VAR_D;
this.X_REG=(this.X_REG<this.Y_REG?-1:0);
if ((this.X_REG==this.CONST_2?0:1)==1) {
return "NSKIP157";}
return "SKIP157";
} 
//
this.NSKIP157 = function() {
return 2030;
//
return 2010;
} 
//
this.SKIP157 = function() {
return 2010;
} 
//
this.line_2010 = function() {
//
this.Y_REG=this.VAR_A;
this._stack.push(this.Y_REG);
this.X_REG=this.VAR_D;
this.Y_REG=this._stack.pop();
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.X_REG) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_A=this.X_REG;
return 2020;
} 
//
this.line_2020 = function() {
//
return 2000;
} 
//
this.line_2030 = function() {
//
this.Y_REG=this.VAR_A;
this._memory[Math.floor(this.Y_REG)]=Math.floor(this.CONST_2) & 255;
//
this.Y_REG=this.CONST_4;
this.X_REG=this.VAR_A;
this.X_REG=this.X_REG+this.Y_REG;
this.VAR_E=this.X_REG;
return 2040;
} 
//
this.line_2040 = function() {
//
this.A_REG=this.CONST_112;
this.STROUT();
//
this.X_REG=this.VAR_ER;
this.REALOUT();
this.CHECKCMD();
this.LINEBREAK();
return 2050;
} 
//
this.line_2050 = function() {
//
this.A_REG=this.CONST_113;
this.STROUT();
//
this.X_REG=this.VAR_S;
this.REALOUT();
this.CRSRRIGHT();
//
this.A_REG=this.CONST_60;
this.STROUT();
//
this.Y_REG=this.CONST_114;
this.X_REG=this.VAR_E;
this.X_REG=this.X_REG*this.Y_REG;
this.REALOUT();
this.CHECKCMD();
this.LINEBREAK();
return 2060;
} 
//
this.line_2060 = function() {
//
this.A_REG=this.CONST_105;
this.STROUT();
//
this.A_REG=this.CONST_115;
this.STROUT();
//
this.READTID();
this.A_REG=this.tmpy;
this.STROUT();
this.LINEBREAK();
return 2070;
} 
//
this.line_2070 = function() {
//
this.END();
return;
} 
//
this.line_2260 = function() {
//
return 2280;
} 
//
this.line_2270 = function() {
return 2290;
} 
//
this.line_2280 = function() {
return 2300;
} 
//
this.line_2290 = function() {
return 2310;
} 
//
this.line_2300 = function() {
return 2320;
} 
//
this.line_2310 = function() {
return 2330;
} 
//
this.line_2320 = function() {
return 2340;
} 
//
this.line_2330 = function() {
return 2350;
} 
//
this.line_2340 = function() {
return 2360;
} 
//
this.line_2350 = function() {
return 2360;
} 
//
this.line_2360 = function() {
//
this.END();
return;
}
// *** SUBROUTINES ***
this.restart = false;
this.running = true;
this.keyPressed=null;
this.lineNumber = 0;
this.timeOut=0;
this.funcName = "PROGRAMSTART";
this.batchSize=500;
this.tmpy=0;
this.disk=new Disk(this);
function File() {
this.name;
this.content=new Array();
}
function FilePointer() {
this.channel=0;
this.file=null;
this.position=0;
this.disk=null;
this.master=null;
this.readString = function() {
return this.readLine();
}
this.readLine = function() {
var ret="";
var content=this.file.content;
for (var i=this.position; i<content.length; i++) {
var c=content[i];
this.position++;
c=this.master.convert(c);
if (c==',' || c==':' || c=='\n' || c=='\r') {
if (c=='\n' && i<content.length-1 && content [i+1]=='\r') {
this.position++;
}
if (c=='\r' && i<content.length-1 && content [i+1]=='\n') {
this.position++;
}
if (i==content.length-1) {
this.disk.flagError();
}
return ret;
}
ret=ret+c;
}
this.disk.flagError();
return ret;
}
}
function Disk(master) {
this.files=new Array();
this.openFiles=new Array();
this.status=0;
this.master=master;
this.init = function() {
this.status=0;
}
this.getStatus = function() {
return this.status;
}
this.flagError = function() {
this.status=64;
}
this.get = function(channel) {
for (var i=0; i<this.openFiles.length; i++) {
var file=this.openFiles[i];
if (file.channel==channel) {
return file;
}
}
console.log("Channel "+channel+" not open");
return null;
}
this.open = function(channel, device, subAddr, name) {
this.close(channel);
name=name.toLowerCase();
var parts=name.split(",");
var type="s";
var mode="r";
if (parts.length>1) {
name=parts[0];
if (parts.length==1) {
mode=parts[1];
}
if (parts.length==2) {
mode=parts[2];
type=parts[1];
}
if (mode.length>1) {
mode=mode.substring(0,1);
}
}
if (subAddr==0) {
mode="r";
}
if (subAddr==1) {
mode="w";
}
var found=null;
for (var i=0; i<this.files.length; i++) {
var file=this.files[i];
if (file.name==name) {
found=file;
break;
}
}
this.init();
if (!found) {
found=new File();
found.name=name;
if (mode=="r") {
var xhr = new XMLHttpRequest();
console.log("grabbing file "+name);
xhr.open('GET', name, false);
xhr.overrideMimeType("text/plain; charset=x-user-defined");
xhr.onload = function() {
if (xhr.status === 200) {
found.content=xhr.responseText.split('');
//console.log("debug: "+xhr.responseText);
console.log("file "+name+" loaded from remote");
}
else {
console.log("file "+name+" not found");
found.content=new Array();
}
};
xhr.send();
}
this.files.push(found);
}
if (mode=="w") {
found.content=new Array();
console.log("emtpy file "+name+" created");
}
console.log("file "+name+" opened");
var pointer=new FilePointer();
pointer.file=found;
pointer.channel=channel;
pointer.position=0;
pointer.disk=this;
pointer.master=this.master;
this.openFiles.push(pointer);
}
this.close = function(channel) {
this.init();
for (var i=0; i<this.openFiles.length; i++) {
var file=this.openFiles[i];
if (file.channel==channel) {
console.log("closed channel "+channel+"/"+file.file.name);
this.openFiles.splice(i, 1);
break;
}
}
}
}
this.getMemory = function() {
return this._memory;
}
this.registerKey= function(key) {
var k=key[1];
var ctx=this;
if (k.length>1) {
k=String.fromCharCode(key[2]);
}
if (key[0]) {
this.keyPressed=k;
this._memory[198]=1;
self.setTimeout(function() {
ctx.keyPressed=null;
ctx._memory[198]=0;
}, 200);
} else {
this.keyPressed=null;
this._memory[198]=0;
}
}
this.execute = function(threaded) {
if (!threaded) {
do  {
this.reinit();
while (this.running) {
this.executeLine(threaded);
}
} while(this.restart);
} else {
this.reinit();
this.executeThreaded();
}
}
this.executeThreaded = function() {
var cnt=0;
do {
if (this.restart) {
this.reinit();
}
this.executeLine(true);
} while(this.running && cnt++<this.batchSize);
if (this.running) {
var ctx=this;
self.setTimeout(function() {
ctx.executeThreaded();
}, this.timeOut);
this.timeOut=0;
}
}
this.reinit = function() {
this.lineNumber = 0;
this.funcName = "PROGRAMSTART";
this.restart=false;
this.running=true;
}
this.executeLine = function(threaded) {
var nextLine = this[this.funcName]();
if (nextLine != null) {
this.lineNumber = nextLine;
if (this.lineNumber == "($JUMP)") {
this.lineNumber = this.JUMP_TARGET;
}
if (Number.isInteger(this.lineNumber)) {
this.funcName = "line_" + this.lineNumber;
} else {
this.funcName = this.lineNumber;
}
} else {
this.running = false;
}
if (threaded) {
_self.postMessage(this.funcName);
}
}
this.START = function() {
this.INIT();
if (!Array.prototype.fill) {
for (var i=0; i<this._memory.length; i++) {
this._memory[i]=0;
}
} else {
this._memory.fill(0);
}
this._memory[646]=14;
}
this.RUN = function() {
this.running=false;
this.restart=true;
}
this.RESTARTPRG = function() {
// This is not correct behaviour as BASIC does it, because it doesn't preserve the variables, but...who cares?
this.running=false;
this.restart=true;
}
this.END = function() {
//
}
this.CLEARQUEUE = function() {
this._inputQueue=new Array();
}
this.QUEUESIZE = function() {
this.X_REG=this._inputQueue.length;
}
this.EXTRAIGNORED = function() {
out("?extra ignored!");
}
this.INPUTNUMBER = function() {
var inp=this.input();
if (this.isNumeric(inp)) {
this.Y_REG=parseFloat(inp);
this.X_REG=0;
} else {
this.X_REG=-1;
}
}
this.INPUTSTR = function() {
var inp=this.input();
this.A_REG=inp;
}
this.GETSTR = function() {
this.A_REG=this.get();
}
this.GETNUMBER = function() {
this.Y_REG=0;
var fk=this.get();
if (fk && this.isNumeric(fk)) {
this.Y_REG=parseFloat(fk);
} else {
out("?syntax error");
}
}
this.isNumeric = function(num) {
return !isNaN(parseFloat(num));
}
this.GOSUB = function(gosubCont) {
this._forstack.push(gosubCont);
this._forstack.push(0);
}
this.RETURN = function() {
var val = 0;
if (this._forstack.length == 0) {
throw "RETURN without GOSUB error!";
}
do {
val = this._forstack.pop();
if (val == 1) {
// skip FORs
this._forstack.pop();
this._forstack.pop();
this._forstack.pop();
this._forstack.pop();
}
} while (val != 0);
return this._forstack.pop();
}
this.adjustStack = function(variable) {
for (var i=this._forstack.length; i>0;) {
var type = this._forstack[i-1];
if (type==0) {
return;
}
var stvar = this._forstack[i-2];
var addr = this._forstack[i-3];
var end = this._forstack[i-4];
var step = this._forstack[i-5];
i-=5;
if (stvar==variable) {
this._forstack=this._forstack.slice(0,i);
return;
}
}
}
this.INITFOR = function(addr, variable) {
this.adjustStack(variable);
this._forstack.push(this._stack.pop()); // step
this._forstack.push(this._stack.pop()); // end
this._forstack.push(addr); // address
this._forstack.push(variable); // var ref
this._forstack.push(1); // type
}
this.NEXT = function(variable) {
var found = false;
do {
if (this._forstack.length == 0) {
throw "NEXT without FOR error!";
}
var type = this._forstack.pop();
if (type == 0) {
throw "NEXT without FOR error!";
}
var stvar = this._forstack.pop();
var addr = this._forstack.pop();
var end = this._forstack.pop();
var step = this._forstack.pop();
found = variable == "0" || variable == stvar;
} while (!found);
this[stvar] += step;
if ((step >= 0 && this[stvar] <= end) || (step < 0 && this[stvar] >= end)) {
// restore stack content if needed
this._forstack.push(step); // step
this._forstack.push(end); // end
this._forstack.push(addr); // address
this._forstack.push(stvar); // var ref
this._forstack.push(1); // type
this.A_REG = 0;
this.JUMP_TARGET = addr;
return;
}
this.A_REG = 1;
return;
}
this.ARRAYACCESS_REAL = function() {
this.X_REG = this.G_REG[Math.floor(this.X_REG)];
if (this.X_REG==null) {
this.X_REG=0;
}
}
this.ARRAYACCESS_INTEGER = function() {
this.X_REG = this.G_REG[Math.floor(this.X_REG)];
if (this.X_REG==null) {
this.X_REG=0;
}
this.X_REG=Math.floor(this.X_REG);
}
this.ARRAYACCESS_STRING = function() {
this.A_REG = this.G_REG[Math.floor(this.X_REG)];
if (this.A_REG==null) {
this.A_REG="";
}
}
this.ARRAYSTORE_REAL = function() {
this.G_REG[Math.floor(this.X_REG)] = this.Y_REG;
}
this.ARRAYSTORE_INTEGER = function() {
this.G_REG[Math.floor(this.X_REG)] = Math.floor(this.Y_REG);
}
this.ARRAYSTORE_STRING = function() {
this.G_REG[Math.floor(this.X_REG)] = this.A_REG;
}
this.STR = function() {
this.A_REG=this.Y_REG.toString(10);
}
this.VAL = function() {
this.X_REG=parseFloat((""+this.B_REG).replace(/ /g,""));
}
this.LEN = function() {
if (this.B_REG==null) {
this.B_REG="";
}
this.X_REG=this.B_REG.length;
}
this.CHR = function() {
this.A_REG=String.fromCharCode(Math.floor(this.Y_REG));
}
this.ASC = function() {
if (this.B_REG.length==0) {
this.X_REG=0;
return;
}
var cc=this.B_REG.charCodeAt(0);
var c=this.B_REG.charAt(0);
if (c>='a' && c<='z') {
cc-=32;
}
this.X_REG=cc;
}
this.POS = function() {
this.X_REG=this._line.length;
}
this.TAB = function() {
var tb=Math.floor(this.Y_REG);
tb-=this._line.length;
for (var i=0;i<tb; i++) {
this._line+=" ";
}
}
this.SPC = function() {
var tb=Math.floor(this.Y_REG);
for (var i=0;i<tb; i++) {
this._line+=" ";
}
}
this.FRE = function() {
this.X_REG=65535;
}
this.CONCAT = function() {
this.A_REG=this.A_REG+this.B_REG;
}
this.MID = function() {
if (this.C_REG>this.B_REG.length) {
this.A_REG="";
return;
}
var end=this.C_REG-1+this.D_REG;
if (this.D_REG===-1) {
end=this.B_REG.length;
}
this.A_REG=this.B_REG.substring(this.C_REG-1, end);
}
this.LEFT = function() {
if (this.C_REG>this.B_REG.length) {
this.A_REG=this.B_REG;
return;
}
if (this.C_REG===0) {
this.A_REG="";
return;
}
this.A_REG=this.B_REG.substring(0, this.C_REG);
}
this.RIGHT = function() {
if (this.C_REG>this.B_REG.length) {
this.A_REG=this.B_REG;
return;
}
if (this.C_REG===0) {
this.A_REG="";
return;
}
this.A_REG=this.B_REG.substring(this.B_REG.length-this.C_REG);
}
this.SEQ = function() {
this.X_REG=(this.A_REG===this.B_REG?-1:0);
}
this.SNEQ = function() {
this.X_REG=(this.A_REG===this.B_REG?0:-1);
}
this.SGT = function() {
this.X_REG=(this.A_REG>this.B_REG?-1:0);
}
this.SLT = function() {
this.X_REG=(this.A_REG<this.B_REG?-1:0);
}
this.SGTEQ = function() {
this.X_REG=(this.A_REG>=this.B_REG?-1:0);
}
this.SLTEQ = function() {
this.X_REG=(this.A_REG<=this.B_REG?-1:0);
}
this.COMPACT = function() {
// Nothing to do in this context
}
this.COMPACTMAX = function() {
// Nothing to do in this context
}
this.SYSTEMCALLDYN = function() {
// Nothing to do in this context
}
this.APPENDSYSCHAR = function() {
// Nothing to do in this context
}
this.SETUPMULTIPARS = function() {
// Nothing to do in this context
}
this.COPYSTRINGPAR = function() {
// Nothing to do in this context
}
this.COPYREALPAR = function() {
// Nothing to do in this context
}
this.ADDCOLON = function() {
// Nothing to do in this context
}
this.PULLDOWNMULTIPARS = function() {
// Nothing to do in this context
}
this.STROUT = function() {
this.out(this.A_REG);
}
this.QMARKOUT1 = function() {
this.out("?");
}
this.CRSRRIGHT = function() {
this.out(" ");
}
this.QMARKOUT2 = function() {
this.out("??");
}
this.REALOUT = function() {
this.out(this.X_REG);
}
this.INTOUT = function() {
this.out(this.X_REG);
}
this.CHECKCMD = function() {
//
}
this.LINEBREAK = function() {
this.out("\n");
}
this.TABOUT = function() {
this.out("\t");
}
this.WRITETID = function(value) {
var d = new Date();
this._time = d.getTime();
this._timeOffset = parseInt(value.substring(0, 2), 10) * 1000 * 60 * 60
+ parseInt(value.substring(2, 4), 10) * 1000 * 60
+ parseInt(value.substring(4, 6), 10) * 1000;
}
this.READTI = function() {
var d = new Date();
var t=d.getTime();
t=Math.floor((t-this._time+this._timeOffset)/(1000.0/60.0));
//console.log("ti: "+t+"/"+this._time+"/"+this._timeOffset+"/"+(t-this._time+this._timeOffset));
this.tmpy=t;
}
this.READTID = function() {
var d = new Date();
var t=d.getTime();
t=(t-this._time+this._timeOffset);
var h=Math.floor(t/(1000 * 60 * 60));
var m=Math.floor((t-(h*(1000 * 60 * 60)))/(1000 * 60));
var s=Math.floor((t-(h*(1000 * 60 * 60))-m*(1000 * 60))/1000);
h=this.fill(h);
m=this.fill(m);
s=this.fill(s);
this.tmpy= h+m+s;
}
this.fill = function(num) {
num=num.toString(10);
if (num.length==1) {
num="0"+num;
}
return num;
}
this.READSTATUS = function() {
this.tmpy= this.disk.getStatus();
}
this.RESTORE = function() {
this._dataPtr=0;
}
this.READSTR = function() {
this.A_REG=this._datas[this._dataPtr++];
}
this.READNUMBER = function() {
var n=this._datas[this._dataPtr++];
if (n=="" || n==".") {
n=0;
}
this.Y_REG=n;
}
this.FINX = function() {
throw new Error("Fast inc optimization not supported for target JS!");
}
this.FDEX = function() {
throw new Error("Fast dec optimization not supported for target JS!");
}
this.FASTFOR = function() {
throw new Error("Fast for optimization not supported for target JS!");
}
this.OPEN = function() {
this.disk.open(this.X_REG, this.C_REG, this.D_REG, this.B_REG);
}
this.CLOSE = function() {
this.disk.close(this.X_REG);
}
this.CMD = function() {
console.log("[CMD not supported for JS, call ignored: "+this.X_REG+"]");
}
this.STROUTCHANNEL = function() {
console.log("[PRINT# not supported for JS, redirected to normal PRINT]");
this.STROUT();
}
this.REALOUTCHANNEL = function() {
console.log("[PRINT# not supported for JS, redirected to normal PRINT]");
this.REALOUT();
}
this.LINEBREAKCHANNEL = function() {
console.log("[PRINT# not supported for JS, redirected to normal PRINT]");
this.LINEBREAK();
}
this.INTOUTCHANNEL = function() {
console.log("[PRINT# not supported for JS, redirected to normal PRINT]");
this.INTOUT();
}
this.INPUTNUMBERCHANNEL = function() {
var fp=this.disk.get(this.C_REG);
var inp=fp.readString();
if (this.isNumeric(inp)) {
this.Y_REG=parseFloat(inp);
this.X_REG=0;
} else {
this.X_REG=-1;
}
}
this.INPUTSTRCHANNEL = function() {
var fp=this.disk.get(this.C_REG);
this.A_REG=fp.readString();
}
this.GETSTRCHANNEL = function() {
if (this.blobCount>65536) {
    throw "out of range!";
}
this.A_REG=String.fromCharCode(this.blob[this.blobCount++]);
}
this.GETNUMBERCHANNEL = function() {
console.log("[GET# not supported for JS, call ignored]");
this.X_REG=0;
}
this.TABOUTCHANNEL = function() {
console.log("[TAB not supported for JS in file mode, redirected to normal TAB]");
this.TAB();
}
this.SPCOUTCHANNEL = function() {
console.log("[SPC not supported for JS in file mode, redirected to normal SPC]");
this.SPC();
}
this.TABCHANNEL = function() {
console.log("[TAB not supported for JS in file mode, redirected to normal TAB]");
this.TAB();
}
this.SPCCHANNEL = function() {
console.log("[SPC not supported for JS in file mode, redirected to normal SPC]");
this.SPC();
}
this.LOAD = function() {
console.log("[LOAD not supported for JS in file mode, call ignored]");
}
this.SAVE = function() {
console.log("[SAVE not supported for JS in file mode, call ignored]");
}
this.VERIFY = function() {
console.log("[VERIFY not supported for JS in file mode, call ignored]");
}
this.REM = function() {
console.log("[inline assembly ignored]");
}
this.USR = function() {
var addr=this._memory[785] + 256*this._memory[786];
this.USR_PARAM=this.X_REG;
var callStr="$"+addr.toString(16);
console.log("[Calling user function named "+callStr+"]");
try {
this[callStr]();
} catch(e) {
console.log("[Function call failed]");
}
}
// Here start the input/output code, that might be adopted to fit ones needs...
this.input = function() {
if (this._inputQueue.length>0) {
return this._inputQueue.pop();
}
var inp=prompt(this._line);
this._line="";
if (inp) {
var parts=inp.split(",");
parts.reverse();
this._inputQueue.push.apply(this._inputQueue, parts);
return this._inputQueue.pop();
} else {
return "";
}
}
// GET relies on INPUT here, because due to the single threaded nature of
// Javascript, the concept of a BASIC program constantly polling the keyboard
// doesn't really work in this context unless you stuff the compiled program
// into a web worker or something like that.
this.get = function() {
var key=this.input();
if (!key) {
return ""
}
return key.substring(0,1);
}
this.out = function(txt) {
if (txt.indexOf && txt.indexOf("\n") != -1) {
this._line += txt;
this.outputter(this._line);
this._line = "";
} else {
this._line += txt;
}
}
this.convert = function(c) {
return c;
}
}
