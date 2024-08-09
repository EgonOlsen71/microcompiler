import math
import random
import time
import keyboard
import re
import struct
def INIT():
    global VAR_I
    global VAR_J
    global VAR_K
    global VAR_L
    global VAR_E
    global VAR_F
    global VAR_G
    global VAR_H
    global VAR_Q
    global VAR_R
    global VAR_S
    global VAR_T
    global VAR_M
    global VAR_N_STRVAR
    global VAR_N
    global VAR_O
    global VAR_P
    global VAR_HF
    global VAR_A
    global VAR_B
    global VAR_C
    global VAR_D
    global CMD_NUM
    global VAR_HU
    global _zeroflag
    global CONST_16
    global CONST_17
    global CONST_14
    global VAR_S2_STRVAR
    global CONST_15
    global CONST_12
    global CONST_13
    global CONST_10
    global CONST_11
    global VAR_U
    global VAR_V
    global VAR_W
    global VAR_ER
    global VAR_H_int
    global JUMP_TARGET
    global VAR_E2_STRVAR
    global VAR_L1_STRVAR
    global D_REG
    global VAR_S_array
    global VAR_XA
    global CONST_123
    global CONST_41
    global CONST_122
    global CONST_42
    global CONST_125
    global CONST_124
    global CONST_40
    global CONST_127
    global CONST_126
    global CONST_129
    global CONST_128
    global CONST_49
    global CONST_47
    global CONST_48
    global CONST_45
    global CONST_46
    global CONST_121
    global CONST_43
    global CONST_120
    global CONST_44
    global VAR_LP
    global CONST_119
    global _timeOffset
    global CONST_112
    global CONST_52
    global CONST_111
    global CONST_53
    global CONST_114
    global CONST_50
    global CONST_113
    global CONST_51
    global CONST_116
    global CONST_115
    global G_REG
    global CONST_118
    global CONST_117
    global CONST_58
    global CONST_59
    global CONST_56
    global CONST_57
    global CONST_110
    global CONST_54
    global CONST_55
    global _stack
    global CONST_109
    global CONST_108
    global CONST_101
    global CONST_100
    global CONST_20
    global CONST_103
    global CONST_102
    global CONST_105
    global CONST_104
    global CONST_107
    global CONST_106
    global CONST_27
    global CONST_28
    global CONST_25
    global CONST_26
    global CONST_23
    global CONST_24
    global _inputQueue
    global Y_REG
    global CONST_21
    global CONST_22
    global _datas
    global CONST_18
    global CONST_19
    global VAR_S_STRVAR
    global CONST_30
    global CONST_31
    global CONST_38
    global CONST_39
    global C_REG
    global CONST_36
    global CONST_37
    global CONST_34
    global CONST_35
    global CONST_32
    global CONST_33
    global CONST_29
    global CONST_85
    global CONST_86
    global CONST_83
    global CONST_84
    global CONST_81
    global CONST_82
    global CONST_80
    global CONST_89
    global _dataPtr
    global CONST_87
    global CONST_88
    global VAR_Z_STRVAR
    global F_REG
    global _memory
    global CONST_96
    global CONST_97
    global CONST_94
    global CONST_95
    global CONST_92
    global CONST_93
    global CONST_90
    global CONST_91
    global CONST_98
    global CONST_99
    global VAR_N_array
    global CONST_63
    global CONST_64
    global CONST_61
    global CONST_62
    global CONST_60
    global CONST_69
    global CONST_67
    global CONST_68
    global CONST_65
    global CONST_66
    global _time
    global VAR_A2_STRVAR
    global B_REG
    global CONST_134
    global CONST_74
    global CONST_133
    global CONST_75
    global CONST_136
    global CONST_72
    global CONST_135
    global CONST_73
    global CONST_70
    global CONST_71
    global CONST_130
    global CONST_78
    global CONST_79
    global CONST_132
    global CONST_76
    global CONST_131
    global CONST_77
    global VAR_L2_STRVAR
    global X_REG
    global VAR_A1_STRVAR
    global E_REG
    global VAR_X_STRVAR
    global VAR_T_STRVAR
    global VAR_TI_STRVAR
    global VAR_E3
    global VAR_E1
    global VAR_E4
    global VAR_S1_STRVAR
    global CONST_9
    global CONST_7
    global CONST_8
    global CONST_5
    global CONST_6
    global CONST_3
    global CONST_4
    global CONST_1
    global A_REG
    global VAR_A_array
    global CONST_2
    global _line
    global CONST_0
    global _forstack
    global USR_PARAM
    global VAR_B_STRVAR
    global VAR_ST
    global VAR_L_array
    X_REG=0.0
    Y_REG=0.0
    C_REG=0.0
    D_REG=0.0
    E_REG=0.0
    F_REG=0.0
    A_REG=0
    B_REG=0
    G_REG=0
    CMD_NUM=0
    CHANNEL=0
    JUMP_TARGET=""
    USR_PARAM=0
    _line=""
    _stack=[]
    _forstack=[]
    _memory=[0] * 65535
    _zeroflag=0
    _timeOffset=0
    _time=0
    _inputQueue=[]
    CONST_0=147
    CONST_1="{control-q}{lgrn}Micro Compiler"
    CONST_2="by Vic Cortes, published in RUN 07/86"
    CONST_3="compiled to Python using MOSpeed by EgonOlsen71"
    CONST_4="visit https://www.jpct.de/mc/ for details"
    CONST_5=0
    CONST_6=169
    CONST_7=1
    CONST_8=2
    CONST_9=173
    CONST_10=3
    CONST_11=174
    CONST_12=162
    CONST_13=194
    CONST_14=912
    CONST_15="{ctrl 9}overflow"
    CONST_16=172
    CONST_17=170
    CONST_18=109
    CONST_19=24
    CONST_20=171
    CONST_21=237
    CONST_22=56
    CONST_23=175
    CONST_24=45
    CONST_25=176
    CONST_26=13
    CONST_27=4
    CONST_28=168
    CONST_29=138
    CONST_30=152
    CONST_31=133
    CONST_32=97
    CONST_33=134
    CONST_34=98
    CONST_35=32
    CONST_36=34
    CONST_37=35
    CONST_38=5
    CONST_39=6
    CONST_40=160
    CONST_41=7
    CONST_42=8
    CONST_43=177
    CONST_44=9
    CONST_45=10
    CONST_46=65
    CONST_47=91
    CONST_48=57
    CONST_49=48
    CONST_50="{ctrl 9}error bei"
    CONST_51=827
    CONST_52=58
    CONST_53=47
    CONST_54=65536
    CONST_55=90
    CONST_56=59
    CONST_57=44
    CONST_58=41
    CONST_59=680
    CONST_60=256
    CONST_61=255
    CONST_62="000000"
    CONST_63="{left}"
    CONST_64=828
    CONST_65=128
    CONST_66=204
    CONST_67=127
    CONST_68=185
    CONST_69=139
    CONST_70=167
    CONST_71=829
    CONST_72=136
    CONST_73=144
    CONST_74=142
    CONST_75=96
    CONST_76=158
    CONST_77=153
    CONST_78=151
    CONST_79=129
    CONST_80=130
    CONST_81=143
    CONST_82=137
    CONST_83=76
    CONST_84=141
    CONST_85=64
    CONST_86="{ctrl 9}error"
    CONST_87=842
    CONST_88=178
    CONST_89=179
    CONST_90=180
    CONST_91=228
    CONST_92=240
    CONST_93=197
    CONST_94=208
    CONST_95=199
    CONST_96=29
    CONST_97=210
    CONST_98=165
    CONST_99=205
    CONST_100=189
    CONST_101=40
    CONST_102=30
    CONST_103=831
    CONST_104=11
    CONST_105=20
    CONST_106=21
    CONST_107=54
    CONST_108=225
    CONST_109=145
    CONST_110=15
    CONST_111="test.comp"
    CONST_112=49152
    CONST_113="{control-q}source name"
    CONST_114=""
    CONST_115="*"
    CONST_116="start address"
    CONST_117="?redo from start"
    CONST_118=116
    CONST_119=164
    CONST_120="0:"
    CONST_121="{control-q}errors"
    CONST_122="address range:"
    CONST_123=-1.0
    CONST_124=" compiled, time:"
    CONST_125="{control-q}1=save 2=comp 3=quit"
    CONST_126="1"
    CONST_127="2"
    CONST_128="3"
    CONST_129=731
    CONST_130=".ml"
    CONST_131="{control-q}name"
    CONST_132="s0:"
    CONST_133=253
    CONST_134="saved "
    CONST_135=191
    CONST_136="disk error"
    _dataPtr=0
    _datas=[133,99,134,100,162,0,134,101,134,102,160,16,144,34,6,97,38,98,38,101,38,102,56,165,101,229,99,170,165,102,229,100,144,6,134,101,133,102,230,97,136,208,227,165,97,166,98,96,70,102,102,101,102,98,102,97,136,48,240,144,243,24,165,101,101,99,133,101,165,102,101,100,133,102,24,144,227,-1]
    VAR_G=0.0
    VAR_A=0.0
    VAR_L=0.0
    VAR_K=0.0
    VAR_V=0.0
    VAR_H=0.0
    VAR_C=0.0
    VAR_P=0.0
    VAR_U=0.0
    VAR_ER=0.0
    VAR_O=0.0
    VAR_B=0.0
    VAR_S=0.0
    VAR_D=0.0
    VAR_N=0.0
    VAR_T=0.0
    VAR_H_int=0
    VAR_M=0.0
    VAR_S_array=[0]*256
    VAR_L_array=[0]*256
    VAR_F=0.0
    VAR_J=0.0
    VAR_ST=0.0
    VAR_Q=0.0
    VAR_I=0.0
    VAR_W=0.0
    VAR_R=0.0
    VAR_N_array=[0]*64
    VAR_A_array=[0]*64
    VAR_LP=0.0
    VAR_HU=0.0
    VAR_HF=0.0
    VAR_XA=0.0
    VAR_E1=0.0
    VAR_E3=0.0
    VAR_E4=0.0
    VAR_E=0.0
    VAR_A1_STRVAR=""
    VAR_A2_STRVAR=""
    VAR_TI_STRVAR=""
    VAR_L1_STRVAR=""
    VAR_L2_STRVAR=""
    VAR_Z_STRVAR=""
    VAR_S1_STRVAR=""
    VAR_S2_STRVAR=""
    VAR_B_STRVAR=""
    VAR_S_STRVAR=""
    VAR_E2_STRVAR=""
    VAR_X_STRVAR=""
    VAR_N_STRVAR=""
    VAR_T_STRVAR=""
def PROGRAMSTART():
    START()
    return 0
def line_0():
    return 10
def line_10():
    global Y_REG
    global CONST_1
    global A_REG
    global CONST_0
    Y_REG=CONST_0
    CHR()
    STROUT()
    A_REG=CONST_1
    STROUT()
    LINEBREAK()
    return 12
def line_12():
    global A_REG
    global CONST_2
    A_REG=CONST_2
    STROUT()
    LINEBREAK()
    return 13
def line_13():
    global CONST_3
    global A_REG
    A_REG=CONST_3
    STROUT()
    LINEBREAK()
    return 14
def line_14():
    global CONST_4
    global A_REG
    A_REG=CONST_4
    STROUT()
    LINEBREAK()
    LINEBREAK()
    return 15
def line_15():
    return 20
def line_20():
    global VAR_G
    global Y_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_G=Y_REG
    GOSUB("GOSUBCONT0")
    return 1780
def GOSUBCONT0():
    return 590
def line_30():
    return 40
def line_40():
    GOSUB("GOSUBCONT1")
    return 400
def GOSUBCONT1():
    global VAR_K
    global VAR_L
    global VAR_A
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_6
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_6) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    VAR_K=Y_REG
    return 50
def line_50():
    global _zeroflag
    global VAR_V
    global Y_REG
    global CONST_5
    Y_REG=VAR_V
    _zeroflag=(0 if Y_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP0"
    return "SKIP0"
def NSKIP0():
    global VAR_K
    global VAR_H
    global VAR_A
    global CONST_10
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_9
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_9) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_10
    VAR_K=Y_REG
    return "SKIP0"
def SKIP0():
    return 60
def line_60():
    global VAR_K
    global VAR_H
    global VAR_A
    global VAR_C
    global CONST_11
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_K
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_11) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_C
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 70
def line_70():
    global _zeroflag
    global VAR_V
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_V
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP1"
    return "SKIP1"
def NSKIP1():
    global VAR_H
    global VAR_A
    global CONST_12
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_12) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return "SKIP1"
def SKIP1():
    return 80
def line_80():
    global VAR_K
    global VAR_A
    global Y_REG
    global X_REG
    Y_REG=VAR_K
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_90():
    return 100
def line_100():
    global VAR_P
    global _zeroflag
    global CONST_13
    global VAR_U
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_P=Y_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_13
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP2"
    return "SKIP2"
def NSKIP2():
    global VAR_P
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=CONST_7
    VAR_P=Y_REG
    return "SKIP2"
def SKIP2():
    return 110
def line_110():
    GOSUB("GOSUBCONT2")
    return 40
def GOSUBCONT2():
    return 120
def line_120():
    global _zeroflag
    global CONST_14
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_14
    X_REG=VAR_U
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP3"
    return "SKIP3"
def NSKIP3():
    global CONST_15
    global VAR_ER
    global Y_REG
    global X_REG
    global CONST_7
    global A_REG
    A_REG=CONST_15
    STROUT()
    LINEBREAK()
    Y_REG=CONST_7
    X_REG=VAR_ER
    X_REG=X_REG+Y_REG
    VAR_ER=X_REG
    return "RETURN"
    return "SKIP3"
def SKIP3():
    return 130
def line_130():
    global VAR_O
    global VAR_B
    global _zeroflag
    global VAR_U
    global Y_REG
    global _memory
    global X_REG
    global CONST_9
    global CONST_5
    Y_REG=CONST_5
    VAR_O=Y_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    VAR_B=X_REG
    Y_REG=CONST_9
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP4"
    return "SKIP4"
def NSKIP4():
    return 280
    return "SKIP4"
def SKIP4():
    return 140
def line_140():
    global VAR_B
    global _zeroflag
    global CONST_16
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_16
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP5"
    return "SKIP5"
def NSKIP5():
    return 280
    return "SKIP5"
def SKIP5():
    return 150
def line_150():
    global VAR_B
    global _zeroflag
    global CONST_17
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_17
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP6"
    return "SKIP6"
def NSKIP6():
    global VAR_O
    global VAR_A
    global Y_REG
    global CONST_18
    global CONST_19
    global _memory
    global X_REG
    global CONST_7
    Y_REG=CONST_18
    VAR_O=Y_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_19) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "SKIP6"
def SKIP6():
    return 160
def line_160():
    global VAR_B
    global _zeroflag
    global CONST_20
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_20
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP7"
    return "SKIP7"
def NSKIP7():
    global VAR_O
    global VAR_A
    global Y_REG
    global CONST_21
    global CONST_22
    global _memory
    global X_REG
    global CONST_7
    Y_REG=CONST_21
    VAR_O=Y_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_22) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "SKIP7"
def SKIP7():
    return 170
def line_170():
    global VAR_B
    global _zeroflag
    global CONST_23
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_23
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP8"
    return "SKIP8"
def NSKIP8():
    global VAR_O
    global CONST_24
    global Y_REG
    Y_REG=CONST_24
    VAR_O=Y_REG
    return "SKIP8"
def SKIP8():
    return 180
def line_180():
    global VAR_B
    global _zeroflag
    global CONST_25
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_25
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP9"
    return "SKIP9"
def NSKIP9():
    global VAR_O
    global CONST_26
    global Y_REG
    Y_REG=CONST_26
    VAR_O=Y_REG
    return "SKIP9"
def SKIP9():
    return 190
def line_190():
    global VAR_O
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_O
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP10"
    return "SKIP10"
def NSKIP10():
    return 320
    return "SKIP10"
def SKIP10():
    return 200
def line_200():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT3")
    return 400
def GOSUBCONT3():
    global VAR_K
    global VAR_L
    global VAR_O
    global VAR_A
    global _stack
    global CONST_27
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _stack.append(Y_REG)
    Y_REG=CONST_27
    X_REG=VAR_O
    X_REG=X_REG-Y_REG
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    VAR_K=Y_REG
    return 210
def line_210():
    global _zeroflag
    global VAR_V
    global Y_REG
    global CONST_5
    Y_REG=VAR_V
    _zeroflag=(0 if Y_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP11"
    return "SKIP11"
def NSKIP11():
    global VAR_K
    global VAR_H
    global VAR_O
    global VAR_A
    global CONST_10
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_8
    Y_REG=VAR_A
    _stack.append(Y_REG)
    X_REG=VAR_O
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_10
    VAR_K=Y_REG
    return "SKIP11"
def SKIP11():
    return 220
def line_220():
    global VAR_K
    global VAR_A
    global CONST_28
    global Y_REG
    global CONST_29
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_K
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_28) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_29) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 230
def line_230():
    global VAR_H
    global VAR_O
    global VAR_A
    global VAR_C
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _stack.append(Y_REG)
    X_REG=VAR_O
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_C
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 240
def line_240():
    global _zeroflag
    global VAR_V
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_V
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP12"
    return "SKIP12"
def NSKIP12():
    global VAR_H
    global VAR_O
    global VAR_A
    global _stack
    global CONST_27
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _stack.append(Y_REG)
    Y_REG=CONST_27
    X_REG=VAR_O
    X_REG=X_REG-Y_REG
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return "SKIP12"
def SKIP12():
    return 250
def line_250():
    global VAR_K
    global VAR_A
    global CONST_17
    global Y_REG
    global CONST_30
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_K
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_17) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_30) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 260
def line_260():
    return 120
def line_270():
    return 280
def line_280():
    global VAR_A
    global CONST_10
    global VAR_U
    global CONST_27
    global Y_REG
    global CONST_31
    global CONST_34
    global CONST_32
    global CONST_33
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_32) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_34) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT4")
    return 40
def GOSUBCONT4():
    return 290
def line_290():
    global VAR_G
    global VAR_A
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_19
    global _memory
    global X_REG
    global CONST_9
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    VAR_G=Y_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_19) & 255
    Y_REG=CONST_9
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP13"
    return "SKIP13"
def NSKIP13():
    global VAR_A
    global Y_REG
    global CONST_22
    global _memory
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_22) & 255
    return "SKIP13"
def SKIP13():
    return 300
def line_300():
    global VAR_S
    global VAR_D
    global CONST_10
    global Y_REG
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    VAR_D=X_REG
    GOSUB("GOSUBCONT5")
    return 570
def GOSUBCONT5():
    global VAR_L
    global VAR_H
    global VAR_A
    global CONST_10
    global _stack
    global CONST_27
    global Y_REG
    global CONST_35
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 120
def line_310():
    return 320
def line_320():
    global VAR_P
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_P
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP14"
    return "SKIP14"
def NSKIP14():
    return "RETURN"
    return "SKIP14"
def SKIP14():
    return 330
def line_330():
    global VAR_A
    global Y_REG
    global CONST_31
    global CONST_36
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 340
def line_340():
    global VAR_A
    global CONST_10
    global Y_REG
    global CONST_37
    global CONST_33
    global _memory
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_37) & 255
    return 350
def line_350():
    global VAR_A
    global CONST_12
    global CONST_27
    global Y_REG
    global CONST_38
    global _memory
    global X_REG
    global CONST_5
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_12) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    return 360
def line_360():
    global VAR_A
    global CONST_41
    global CONST_40
    global Y_REG
    global CONST_39
    global _memory
    global X_REG
    global CONST_5
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_40) & 255
    Y_REG=CONST_41
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    return 370
def line_370():
    global VAR_A
    global CONST_42
    global CONST_43
    global CONST_44
    global Y_REG
    global CONST_36
    global _memory
    global X_REG
    Y_REG=CONST_42
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_43) & 255
    Y_REG=CONST_44
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 380
def line_380():
    global VAR_P
    global VAR_A
    global VAR_U
    global CONST_45
    global Y_REG
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_45
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=CONST_5
    VAR_P=Y_REG
    return 120
def line_390():
    return 400
def line_400():
    global VAR_N
    global _zeroflag
    global VAR_U
    global VAR_V
    global CONST_46
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_N=Y_REG
    Y_REG=CONST_5
    VAR_V=Y_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_46
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP15"
    return "SKIP15"
def NSKIP15():
    return 420
    return "SKIP15"
def SKIP15():
    return 410
def line_410():
    global _zeroflag
    global VAR_U
    global CONST_47
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_47
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP16"
    return "SKIP16"
def NSKIP16():
    return 490
    return "SKIP16"
def SKIP16():
    return 420
def line_420():
    global VAR_T
    global _zeroflag
    global CONST_17
    global VAR_U
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_T=Y_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_17
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP17"
    return "SKIP17"
def NSKIP17():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 440
    return "SKIP17"
def SKIP17():
    return 430
def line_430():
    global _zeroflag
    global VAR_U
    global CONST_20
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_20
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP18"
    return "SKIP18"
def NSKIP18():
    global VAR_T
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=CONST_7
    VAR_T=Y_REG
    return "SKIP18"
def SKIP18():
    return 440
def line_440():
    global _zeroflag
    global VAR_U
    global CONST_49
    global CONST_48
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_48
    X_REG= (-1 if X_REG>Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_49
    X_REG= (-1 if X_REG<Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP19"
    return "SKIP19"
def NSKIP19():
    global VAR_U
    global VAR_ER
    global CONST_50
    global CONST_51
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global A_REG
    A_REG=CONST_50
    STROUT()
    Y_REG=CONST_51
    X_REG=VAR_U
    X_REG=X_REG-Y_REG
    REALOUT()
    CRSRRIGHT()
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    REALOUT()
    CHECKCMD()
    LINEBREAK()
    Y_REG=CONST_7
    X_REG=VAR_ER
    X_REG=X_REG+Y_REG
    VAR_ER=X_REG
    return "SKIP19"
def SKIP19():
    return 450
def line_450():
    global _zeroflag
    global VAR_U
    global CONST_52
    global CONST_53
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_52
    X_REG= (-1 if X_REG<Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_53
    X_REG= (-1 if X_REG>Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP20"
    return "SKIP20"
def NSKIP20():
    global VAR_N
    global CONST_10
    global VAR_U
    global CONST_49
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global A_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    _stack.append(X_REG)
    X_REG=VAR_N
    A_REG=CONST_10
    Y_REG=X_REG
    X_REG=X_REG*pow(2,A_REG)
    A_REG=CONST_7
    Y_REG=Y_REG*pow(2,A_REG)
    X_REG=X_REG+Y_REG
    Y_REG=_stack.pop()
    X_REG=X_REG+Y_REG
    Y_REG=CONST_49
    X_REG=X_REG-Y_REG
    VAR_N=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 450
    return "SKIP20"
def SKIP20():
    return 460
def line_460():
    global VAR_T
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_T
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP21"
    return "SKIP21"
def NSKIP21():
    global VAR_N
    global VAR_D
    global Y_REG
    Y_REG=VAR_N
    VAR_D=Y_REG
    return 570
    return "SKIP21"
def SKIP21():
    return 470
def line_470():
    global VAR_N
    global VAR_D
    global CONST_54
    global Y_REG
    global X_REG
    Y_REG=VAR_N
    X_REG=CONST_54
    X_REG=X_REG-Y_REG
    VAR_D=X_REG
    return 570
def line_480():
    return 490
def line_490():
    global VAR_D
    global VAR_U
    global VAR_V
    global Y_REG
    global _memory
    global X_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    VAR_V=X_REG
    Y_REG=VAR_V
    VAR_D=Y_REG
    return 500
def line_500():
    global VAR_T
    global _zeroflag
    global VAR_U
    global CONST_55
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    VAR_T=X_REG
    Y_REG=CONST_55
    X_REG=VAR_T
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP22"
    return "SKIP22"
def NSKIP22():
    return 560
    return "SKIP22"
def SKIP22():
    return 510
def line_510():
    global VAR_T
    global _zeroflag
    global Y_REG
    global CONST_35
    global X_REG
    global CONST_5
    Y_REG=CONST_35
    X_REG=VAR_T
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP23"
    return "SKIP23"
def NSKIP23():
    return 560
    return "SKIP23"
def SKIP23():
    return 520
def line_520():
    global VAR_T
    global _zeroflag
    global CONST_56
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_56
    X_REG=VAR_T
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP24"
    return "SKIP24"
def NSKIP24():
    return 560
    return "SKIP24"
def SKIP24():
    return 530
def line_530():
    global VAR_T
    global _zeroflag
    global CONST_57
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_57
    X_REG=VAR_T
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP25"
    return "SKIP25"
def NSKIP25():
    return 560
    return "SKIP25"
def SKIP25():
    return 540
def line_540():
    global VAR_T
    global _zeroflag
    global CONST_58
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_58
    X_REG=VAR_T
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP26"
    return "SKIP26"
def NSKIP26():
    return 560
    return "SKIP26"
def SKIP26():
    return 550
def line_550():
    global VAR_T
    global _zeroflag
    global Y_REG
    global CONST_37
    global X_REG
    global CONST_5
    Y_REG=CONST_37
    X_REG=VAR_T
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP27"
    return "SKIP27"
def NSKIP27():
    return 500
    return "SKIP27"
def SKIP27():
    return 560
def line_560():
    global VAR_D
    global CONST_46
    global CONST_59
    global Y_REG
    global X_REG
    global CONST_8
    Y_REG=CONST_46
    X_REG=VAR_D
    X_REG=X_REG-Y_REG
    VAR_D=X_REG
    X_REG=VAR_D
    Y_REG=CONST_8
    X_REG=X_REG*Y_REG
    Y_REG=CONST_59
    X_REG=X_REG+Y_REG
    VAR_D=X_REG
    return 570
def line_570():
    global VAR_L
    global VAR_H
    global VAR_C
    global VAR_D
    global VAR_H_int
    global Y_REG
    global CONST_61
    global CONST_60
    global X_REG
    global CONST_7
    Y_REG=CONST_60
    X_REG=VAR_D
    X_REG=X_REG/Y_REG
    VAR_H_int=X_REG
    VAR_H_int=int(VAR_H_int)
    Y_REG=VAR_H_int
    VAR_H=Y_REG
    X_REG=VAR_H
    Y_REG=CONST_60
    X_REG=X_REG*Y_REG
    Y_REG=X_REG
    X_REG=VAR_D
    X_REG=X_REG-Y_REG
    VAR_L=X_REG
    Y_REG=CONST_7
    X_REG=VAR_L
    X_REG=X_REG+Y_REG
    Y_REG=CONST_61
    X_REG=int(X_REG) & int(Y_REG)
    VAR_C=X_REG
    return "RETURN"
def line_580():
    return 590
def line_590():
    global C_REG
    global CONST_62
    global VAR_A2_STRVAR
    global B_REG
    global VAR_A1_STRVAR
    global CONST_8
    global A_REG
    C_REG=CONST_8
    GETSTRCHANNEL()
    VAR_A1_STRVAR=A_REG
    GETSTRCHANNEL()
    VAR_A2_STRVAR=A_REG
    B_REG=CONST_62
    WRITETID(B_REG)
    return 600
def line_600():
    global VAR_T
    global _zeroflag
    global VAR_L1_STRVAR
    global _stack
    global Y_REG
    global C_REG
    global VAR_Z_STRVAR
    global B_REG
    global VAR_L2_STRVAR
    global X_REG
    global CONST_8
    global CONST_5
    global A_REG
    C_REG=CONST_8
    GETSTRCHANNEL()
    VAR_L1_STRVAR=A_REG
    GETSTRCHANNEL()
    VAR_L2_STRVAR=A_REG
    B_REG=VAR_Z_STRVAR
    A_REG=VAR_L2_STRVAR
    CONCAT()
    B_REG=A_REG
    ASC()
    _stack.append(X_REG)
    B_REG=VAR_Z_STRVAR
    A_REG=VAR_L1_STRVAR
    CONCAT()
    B_REG=A_REG
    ASC()
    Y_REG=_stack.pop()
    X_REG=X_REG+Y_REG
    VAR_T=X_REG
    Y_REG=CONST_5
    X_REG=VAR_T
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP28"
    return "SKIP28"
def NSKIP28():
    return 1920
    return "SKIP28"
def SKIP28():
    return 610
def line_610():
    global VAR_T
    global VAR_S2_STRVAR
    global _stack
    global Y_REG
    global C_REG
    global VAR_Z_STRVAR
    global CONST_60
    global B_REG
    global X_REG
    global VAR_S1_STRVAR
    global CONST_8
    global A_REG
    C_REG=CONST_8
    GETSTRCHANNEL()
    VAR_S1_STRVAR=A_REG
    GETSTRCHANNEL()
    VAR_S2_STRVAR=A_REG
    B_REG=VAR_Z_STRVAR
    A_REG=VAR_S2_STRVAR
    CONCAT()
    B_REG=A_REG
    ASC()
    Y_REG=CONST_60
    X_REG=X_REG*Y_REG
    _stack.append(X_REG)
    B_REG=VAR_Z_STRVAR
    A_REG=VAR_S1_STRVAR
    CONCAT()
    B_REG=A_REG
    ASC()
    Y_REG=_stack.pop()
    X_REG=X_REG+Y_REG
    VAR_T=X_REG
    return 620
def line_620():
    global VAR_T
    global VAR_M
    global VAR_A
    global VAR_S_array
    global G_REG
    global _stack
    global Y_REG
    global CONST_63
    global X_REG
    global CONST_7
    global A_REG
    global VAR_L_array
    Y_REG=VAR_M
    _stack.append(Y_REG)
    X_REG=_stack.pop()
    Y_REG=VAR_T
    G_REG=VAR_S_array
    ARRAYSTORE_REAL()
    Y_REG=VAR_M
    _stack.append(Y_REG)
    X_REG=_stack.pop()
    Y_REG=VAR_A
    G_REG=VAR_L_array
    ARRAYSTORE_REAL()
    Y_REG=CONST_7
    X_REG=VAR_M
    X_REG=X_REG+Y_REG
    VAR_M=X_REG
    A_REG=CONST_63
    STROUT()
    X_REG=VAR_T
    REALOUT()
    CRSRRIGHT()
    return 630
def line_630():
    global VAR_F
    global _zeroflag
    global Y_REG
    global CONST_5
    Y_REG=VAR_F
    _zeroflag=(0 if Y_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP29"
    return "SKIP29"
def NSKIP29():
    global VAR_F
    global VAR_T
    global VAR_A
    global CONST_41
    global CONST_42
    global CONST_45
    global CONST_44
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_5
    Y_REG=VAR_F
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    VAR_T=X_REG
    Y_REG=CONST_7
    X_REG=VAR_F
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    Y_REG=CONST_8
    X_REG=VAR_T
    X_REG=X_REG-Y_REG
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_41
    X_REG=VAR_F
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    Y_REG=CONST_42
    X_REG=VAR_T
    X_REG=X_REG-Y_REG
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_44
    X_REG=VAR_F
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    Y_REG=CONST_45
    X_REG=VAR_T
    X_REG=X_REG-Y_REG
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_5
    VAR_F=Y_REG
    return "SKIP29"
def SKIP29():
    return 640
def line_640():
    global VAR_J
    global _zeroflag
    global Y_REG
    global _memory
    global CONST_64
    global X_REG
    global CONST_5
    Y_REG=CONST_64
    VAR_J=Y_REG
    X_REG=int(_memory[653]) & 255;
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP30"
    return "SKIP30"
def NSKIP30():
    return 640
    return "SKIP30"
def SKIP30():
    return 650
def line_650():
    global _zeroflag
    global Y_REG
    global C_REG
    global CONST_8
    global CONST_5
    global A_REG
    global VAR_B_STRVAR
    C_REG=CONST_8
    GETSTRCHANNEL()
    VAR_B_STRVAR=A_REG
    READSTATUS()
    Y_REG=tmpy
    _zeroflag=(0 if Y_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP31"
    return "SKIP31"
def NSKIP31():
    return 1920
    return "SKIP31"
def SKIP31():
    return 660
def line_660():
    global VAR_J
    global VAR_Q
    global VAR_B
    global _zeroflag
    global _stack
    global Y_REG
    global CONST_35
    global VAR_Z_STRVAR
    global _memory
    global B_REG
    global X_REG
    global CONST_5
    global A_REG
    global VAR_B_STRVAR
    B_REG=VAR_Z_STRVAR
    A_REG=VAR_B_STRVAR
    CONCAT()
    B_REG=A_REG
    ASC()
    VAR_B=X_REG
    Y_REG=VAR_J
    _stack.append(Y_REG)
    X_REG=VAR_B
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_35
    X_REG=VAR_B
    X_REG= (-1 if X_REG!=Y_REG else 0)
    Y_REG=X_REG
    X_REG=VAR_Q
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP32"
    return "SKIP32"
def NSKIP32():
    global VAR_J
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_J
    X_REG=X_REG+Y_REG
    VAR_J=X_REG
    return "SKIP32"
def SKIP32():
    return 670
def line_670():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_36
    global X_REG
    global CONST_5
    Y_REG=CONST_36
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP33"
    return "SKIP33"
def NSKIP33():
    global VAR_Q
    global Y_REG
    global X_REG
    Y_REG=VAR_Q
    X_REG=not Y_REG
    VAR_Q=X_REG
    return "SKIP33"
def SKIP33():
    return 680
def line_680():
    global VAR_Q
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_65
    global X_REG
    global CONST_5
    Y_REG=CONST_65
    X_REG=VAR_B
    X_REG= (-1 if X_REG<Y_REG else 0)
    Y_REG=VAR_Q
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP34"
    return "SKIP34"
def NSKIP34():
    global A_REG
    global VAR_B_STRVAR
    A_REG=VAR_B_STRVAR
    STROUT()
    return "SKIP34"
def SKIP34():
    return 690
def line_690():
    global VAR_B
    global _memory
    global X_REG
    global CONST_5
    X_REG=VAR_B
    _memory[780]=int(X_REG) & 255;
    _memory[15]=int(CONST_5) & 255;
    return 700
def line_700():
    global VAR_Q
    global VAR_B
    global _zeroflag
    global _stack
    global Y_REG
    global CONST_67
    global CONST_66
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_Q
    X_REG= (-1 if X_REG==Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_66
    X_REG=VAR_B
    X_REG= (-1 if X_REG<Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_67
    X_REG=VAR_B
    X_REG= (-1 if X_REG>Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP35"
    return "SKIP35"
def NSKIP35():
    global _memory
    global CONST_61
    global CONST_68
    global CONST_65
    _memory[782]=int(CONST_61) & 255;
    _memory[768]=int(CONST_68) & 255;
    _memory[783]=int(CONST_65) & 255;
    SYSCALL("$a717()")
    return "SKIP35"
def SKIP35():
    return 710
def line_710():
    global VAR_Q
    global _zeroflag
    global Y_REG
    global _memory
    global CONST_69
    global CONST_5
    _memory[768]=int(CONST_69) & 255;
    Y_REG=VAR_Q
    _zeroflag=(0 if Y_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP36"
    return "SKIP36"
def NSKIP36():
    return 650
    return "SKIP36"
def SKIP36():
    return 720
def line_720():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_35
    global X_REG
    global CONST_5
    Y_REG=CONST_35
    X_REG=VAR_B
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP37"
    return "SKIP37"
def NSKIP37():
    LINEBREAK()
    GOSUB("GOSUBCONT6")
    return 770
def GOSUBCONT6():
    return 600
    return "SKIP37"
def SKIP37():
    return 730
def line_730():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_70
    global X_REG
    global CONST_5
    Y_REG=CONST_70
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP38"
    return "SKIP38"
def NSKIP38():
    GOSUB("GOSUBCONT7")
    return 770
def GOSUBCONT7():
    return 640
    return "SKIP38"
def SKIP38():
    return 740
def line_740():
    global VAR_B
    global _zeroflag
    global CONST_52
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_52
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP39"
    return "SKIP39"
def NSKIP39():
    global VAR_J
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_J
    X_REG=X_REG-Y_REG
    VAR_J=X_REG
    GOSUB("GOSUBCONT8")
    return 770
def GOSUBCONT8():
    return 640
    return "SKIP39"
def SKIP39():
    return 750
def line_750():
    return 650
def line_760():
    return 770
def line_770():
    global VAR_J
    global VAR_B
    global VAR_U
    global Y_REG
    global _memory
    global CONST_71
    global X_REG
    global CONST_7
    global CONST_5
    X_REG=int(_memory[828]) & 255;
    VAR_B=X_REG
    Y_REG=CONST_71
    VAR_U=Y_REG
    Y_REG=VAR_J
    _memory[int(Y_REG)]=int(CONST_5) & 255
    Y_REG=CONST_7
    X_REG=VAR_J
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    return 780
def line_780():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_72
    global X_REG
    global CONST_5
    Y_REG=CONST_72
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP40"
    return "SKIP40"
def NSKIP40():
    return 940
    return "SKIP40"
def SKIP40():
    return 790
def line_790():
    global VAR_B
    global _zeroflag
    global _stack
    global Y_REG
    global CONST_65
    global CONST_74
    global CONST_73
    global X_REG
    global CONST_5
    Y_REG=CONST_73
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_74
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_65
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP41"
    return "SKIP41"
def NSKIP41():
    global VAR_A
    global Y_REG
    global _memory
    global CONST_75
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_75) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
    return "SKIP41"
def SKIP41():
    return 800
def line_800():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_76
    global X_REG
    global CONST_5
    Y_REG=CONST_76
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP42"
    return "SKIP42"
def NSKIP42():
    return 1680
    return "SKIP42"
def SKIP42():
    return 810
def line_810():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_69
    global X_REG
    global CONST_5
    Y_REG=CONST_69
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP43"
    return "SKIP43"
def NSKIP43():
    return 1040
    return "SKIP43"
def SKIP43():
    return 820
def line_820():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_77
    global X_REG
    global CONST_5
    Y_REG=CONST_77
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP44"
    return "SKIP44"
def NSKIP44():
    return 1170
    return "SKIP44"
def SKIP44():
    return 830
def line_830():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_78
    global X_REG
    global CONST_5
    Y_REG=CONST_78
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP45"
    return "SKIP45"
def NSKIP45():
    return 1720
    return "SKIP45"
def SKIP45():
    return 840
def line_840():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_79
    global X_REG
    global CONST_5
    Y_REG=CONST_79
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP46"
    return "SKIP46"
def NSKIP46():
    return 1510
    return "SKIP46"
def SKIP46():
    return 850
def line_850():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_80
    global X_REG
    global CONST_5
    Y_REG=CONST_80
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP47"
    return "SKIP47"
def NSKIP47():
    return 1650
    return "SKIP47"
def SKIP47():
    return 860
def line_860():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_81
    global X_REG
    global CONST_5
    Y_REG=CONST_81
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP48"
    return "SKIP48"
def NSKIP48():
    return "RETURN"
    return "SKIP48"
def SKIP48():
    return 870
def line_870():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_82
    global X_REG
    global CONST_5
    Y_REG=CONST_82
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP49"
    return "SKIP49"
def NSKIP49():
    global VAR_O
    global Y_REG
    global CONST_83
    Y_REG=CONST_83
    VAR_O=Y_REG
    return 1480
    return "SKIP49"
def SKIP49():
    return 880
def line_880():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_84
    global X_REG
    global CONST_5
    Y_REG=CONST_84
    X_REG=VAR_B
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP50"
    return "SKIP50"
def NSKIP50():
    global VAR_O
    global Y_REG
    global CONST_35
    Y_REG=CONST_35
    VAR_O=Y_REG
    return 1480
    return "SKIP50"
def SKIP50():
    return 890
def line_890():
    global VAR_B
    global _zeroflag
    global CONST_49
    global CONST_55
    global _stack
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_55
    X_REG=VAR_B
    X_REG= (-1 if X_REG>Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_49
    X_REG=VAR_B
    X_REG= (-1 if X_REG<Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP51"
    return "SKIP51"
def NSKIP51():
    return 920
    return "SKIP51"
def SKIP51():
    return 900
def line_900():
    global VAR_B
    global _zeroflag
    global Y_REG
    global CONST_85
    global X_REG
    global CONST_5
    Y_REG=CONST_85
    X_REG=VAR_B
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP52"
    return "SKIP52"
def NSKIP52():
    return 950
    return "SKIP52"
def SKIP52():
    return 910
def line_910():
    global VAR_B
    global _zeroflag
    global CONST_52
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_52
    X_REG=VAR_B
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP53"
    return "SKIP53"
def NSKIP53():
    global VAR_O
    global VAR_U
    global Y_REG
    global CONST_83
    global CONST_64
    Y_REG=CONST_64
    VAR_U=Y_REG
    Y_REG=CONST_83
    VAR_O=Y_REG
    return 1480
    return "SKIP53"
def SKIP53():
    return 920
def line_920():
    global VAR_U
    global VAR_ER
    global CONST_51
    global Y_REG
    global CONST_86
    global _memory
    global X_REG
    global CONST_7
    global A_REG
    A_REG=CONST_86
    STROUT()
    Y_REG=CONST_51
    X_REG=VAR_U
    X_REG=X_REG-Y_REG
    REALOUT()
    CRSRRIGHT()
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    REALOUT()
    CHECKCMD()
    LINEBREAK()
    Y_REG=CONST_7
    X_REG=VAR_ER
    X_REG=X_REG+Y_REG
    VAR_ER=X_REG
    return "RETURN"
def line_930():
    return 940
def line_940():
    global VAR_I
    global _stack
    global Y_REG
    global CONST_87
    global CONST_64
    global CONST_7
    Y_REG=CONST_64
    VAR_I=Y_REG
    Y_REG=CONST_87
    _stack.append(Y_REG)
    Y_REG=CONST_7
    _stack.append(Y_REG)
    INITFOR("FORLOOP0","VAR_I")
    return "FORLOOP0"
def FORLOOP0():
    global VAR_I
    global _zeroflag
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    global A_REG
    Y_REG=VAR_I
    _stack.append(Y_REG)
    Y_REG=CONST_7
    X_REG=VAR_I
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    NEXT("0")
    _zeroflag=(0 if A_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "($JUMP)"
    return 950
def line_950():
    global _zeroflag
    global VAR_U
    global CONST_46
    global Y_REG
    global _memory
    global CONST_64
    global X_REG
    global CONST_5
    Y_REG=CONST_64
    VAR_U=Y_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_46
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP54"
    return "SKIP54"
def NSKIP54():
    return 920
    return "SKIP54"
def SKIP54():
    return 960
def line_960():
    global _zeroflag
    global VAR_U
    global CONST_55
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_55
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP55"
    return "SKIP55"
def NSKIP55():
    return 920
    return "SKIP55"
def SKIP55():
    return 970
def line_970():
    global _zeroflag
    global VAR_U
    global Y_REG
    global CONST_88
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_88
    X_REG= (-1 if X_REG!=Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP56"
    return "SKIP56"
def NSKIP56():
    return 920
    return "SKIP56"
def SKIP56():
    return 980
def line_980():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT9")
    return 100
def GOSUBCONT9():
    global VAR_D
    global _memory
    global X_REG
    X_REG=int(_memory[828]) & 255;
    VAR_D=X_REG
    return 990
def line_990():
    GOSUB("GOSUBCONT10")
    return 560
def GOSUBCONT10():
    return 1000
def line_1000():
    global VAR_L
    global VAR_H
    global VAR_A
    global _stack
    global Y_REG
    global CONST_84
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_84) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1010
def line_1010():
    global VAR_H
    global VAR_A
    global VAR_C
    global CONST_10
    global _stack
    global CONST_27
    global Y_REG
    global CONST_38
    global _memory
    global CONST_74
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_74) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_C
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1020
def line_1020():
    global VAR_A
    global Y_REG
    global CONST_39
    global X_REG
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1030():
    return 1040
def line_1040():
    GOSUB("GOSUBCONT11")
    return 100
def GOSUBCONT11():
    global _zeroflag
    global VAR_U
    global VAR_W
    global CONST_43
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    VAR_W=X_REG
    Y_REG=CONST_43
    X_REG=VAR_W
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP57"
    return "SKIP57"
def NSKIP57():
    return 920
    return "SKIP57"
def SKIP57():
    return 1050
def line_1050():
    global _zeroflag
    global VAR_W
    global Y_REG
    global CONST_89
    global X_REG
    global CONST_5
    Y_REG=CONST_89
    X_REG=VAR_W
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP58"
    return "SKIP58"
def NSKIP58():
    return 920
    return "SKIP58"
def SKIP58():
    return 1060
def line_1060():
    global VAR_A
    global CONST_10
    global VAR_U
    global CONST_27
    global Y_REG
    global CONST_31
    global CONST_36
    global CONST_37
    global CONST_33
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_37) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 1070
def line_1070():
    global _zeroflag
    global VAR_U
    global VAR_W
    global CONST_43
    global _stack
    global Y_REG
    global CONST_89
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_43
    X_REG= (-1 if X_REG==Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_89
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP59"
    return "SKIP59"
def NSKIP59():
    global VAR_U
    global VAR_W
    global Y_REG
    global CONST_90
    global X_REG
    global CONST_7
    Y_REG=CONST_90
    VAR_W=Y_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return "SKIP59"
def SKIP59():
    return 1080
def line_1080():
    global _zeroflag
    global VAR_U
    global VAR_W
    global CONST_43
    global _stack
    global Y_REG
    global CONST_89
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_89
    X_REG= (-1 if X_REG==Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_43
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP60"
    return "SKIP60"
def NSKIP60():
    global VAR_U
    global VAR_W
    global Y_REG
    global CONST_90
    global X_REG
    global CONST_7
    Y_REG=CONST_90
    VAR_W=Y_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return "SKIP60"
def SKIP60():
    return 1090
def line_1090():
    GOSUB("GOSUBCONT12")
    return 100
def GOSUBCONT12():
    global VAR_F
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_37
    global _memory
    global CONST_92
    global CONST_91
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_91) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_37) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_92) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_27) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=VAR_A
    VAR_F=Y_REG
    return 1100
def line_1100():
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_38
    global CONST_39
    global CONST_36
    global _memory
    global CONST_93
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_39) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_93) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 1110
def line_1110():
    global VAR_A
    global CONST_42
    global Y_REG
    global _memory
    global CONST_94
    global CONST_92
    global X_REG
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_92) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_94) & 255
    Y_REG=CONST_42
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_92) & 255
    return 1120
def line_1120():
    global _zeroflag
    global VAR_W
    global Y_REG
    global CONST_88
    global X_REG
    global CONST_5
    Y_REG=CONST_88
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP61"
    return "SKIP61"
def NSKIP61():
    global VAR_A
    global CONST_42
    global Y_REG
    global _memory
    global CONST_94
    global X_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_94) & 255
    Y_REG=CONST_42
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_94) & 255
    return "SKIP61"
def SKIP61():
    return 1130
def line_1130():
    global _zeroflag
    global VAR_W
    global Y_REG
    global CONST_89
    global X_REG
    global CONST_5
    Y_REG=CONST_89
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP62"
    return "SKIP62"
def NSKIP62():
    global VAR_A
    global CONST_25
    global Y_REG
    global _memory
    global CONST_73
    global X_REG
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_73) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_25) & 255
    return "SKIP62"
def SKIP62():
    return 1140
def line_1140():
    global _zeroflag
    global VAR_W
    global CONST_43
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_43
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP63"
    return "SKIP63"
def NSKIP63():
    global VAR_A
    global CONST_25
    global Y_REG
    global _memory
    global CONST_73
    global X_REG
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_25) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_73) & 255
    return "SKIP63"
def SKIP63():
    return 1150
def line_1150():
    global VAR_A
    global CONST_45
    global _stack
    global Y_REG
    global CONST_39
    global _memory
    global X_REG
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    Y_REG=VAR_A
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_45
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1160():
    return 1170
def line_1170():
    global _zeroflag
    global VAR_U
    global VAR_W
    global Y_REG
    global CONST_35
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    VAR_W=X_REG
    Y_REG=CONST_35
    X_REG=VAR_W
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP64"
    return "SKIP64"
def NSKIP64():
    return 1450
    return "SKIP64"
def SKIP64():
    return 1180
def line_1180():
    global _zeroflag
    global VAR_U
    global VAR_W
    global CONST_56
    global _stack
    global Y_REG
    global CONST_35
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_35
    X_REG= (-1 if X_REG<Y_REG else 0)
    _stack.append(X_REG)
    Y_REG=CONST_56
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) & int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP65"
    return "SKIP65"
def NSKIP65():
    return "RETURN"
    return "SKIP65"
def SKIP65():
    return 1190
def line_1190():
    global _zeroflag
    global VAR_W
    global CONST_56
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_56
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP66"
    return "SKIP66"
def NSKIP66():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 1170
    return "SKIP66"
def SKIP66():
    return 1200
def line_1200():
    global _zeroflag
    global VAR_W
    global Y_REG
    global CONST_95
    global X_REG
    global CONST_5
    Y_REG=CONST_95
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP67"
    return "SKIP67"
def NSKIP67():
    return 1300
    return "SKIP67"
def SKIP67():
    return 1210
def line_1210():
    global _zeroflag
    global VAR_W
    global Y_REG
    global CONST_36
    global X_REG
    global CONST_5
    Y_REG=CONST_36
    X_REG=VAR_W
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP68"
    return "SKIP68"
def NSKIP68():
    return 1340
    return "SKIP68"
def SKIP68():
    return 1220
def line_1220():
    return 1230
def line_1230():
    global VAR_A
    global Y_REG
    global CONST_35
    global _memory
    global CONST_96
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_6
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_6) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_96) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    return 1240
def line_1240():
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_38
    global _memory
    global CONST_97
    global CONST_61
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_97) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_61) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1250
def line_1250():
    GOSUB("GOSUBCONT13")
    return 100
def GOSUBCONT13():
    global VAR_A
    global Y_REG
    global CONST_36
    global CONST_33
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 1260
def line_1260():
    global VAR_A
    global CONST_17
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_36
    global _memory
    global CONST_98
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_17) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_98) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 1270
def line_1270():
    global VAR_A
    global CONST_41
    global CONST_100
    global Y_REG
    global CONST_38
    global CONST_39
    global CONST_35
    global _memory
    global CONST_99
    global X_REG
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_99) & 255
    Y_REG=CONST_41
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_100) & 255
    return 1280
def line_1280():
    global VAR_A
    global CONST_42
    global Y_REG
    global X_REG
    Y_REG=CONST_42
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1170
def line_1290():
    return 1300
def line_1300():
    global _zeroflag
    global VAR_U
    global CONST_101
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_101
    X_REG= (-1 if X_REG!=Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP69"
    return "SKIP69"
def NSKIP69():
    return 920
    return "SKIP69"
def SKIP69():
    return 1310
def line_1310():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT14")
    return 100
def GOSUBCONT14():
    global VAR_A
    global Y_REG
    global CONST_35
    global _memory
    global CONST_97
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_35) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_97) & 255
    return 1320
def line_1320():
    global VAR_A
    global CONST_10
    global VAR_U
    global Y_REG
    global _memory
    global CONST_61
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_61) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 1170
def line_1330():
    return 1340
def line_1340():
    global VAR_A
    global VAR_D
    global CONST_45
    global Y_REG
    global X_REG
    Y_REG=CONST_45
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_D=X_REG
    GOSUB("GOSUBCONT15")
    return 570
def GOSUBCONT15():
    global VAR_A
    global Y_REG
    global _memory
    global CONST_6
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_6) & 255
    return 1350
def line_1350():
    global VAR_L
    global VAR_H
    global VAR_A
    global CONST_10
    global CONST_40
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_40) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1360
def line_1360():
    global VAR_A
    global CONST_20
    global CONST_102
    global CONST_27
    global Y_REG
    global CONST_38
    global CONST_39
    global CONST_35
    global _memory
    global X_REG
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_102) & 255
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_20) & 255
    return 1370
def line_1370():
    global VAR_A
    global CONST_41
    global CONST_42
    global CONST_44
    global Y_REG
    global CONST_19
    global _memory
    global CONST_73
    global X_REG
    global CONST_5
    Y_REG=CONST_41
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_19) & 255
    Y_REG=CONST_42
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_73) & 255
    Y_REG=CONST_44
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    return 1380
def line_1380():
    global VAR_I
    global VAR_A
    global VAR_W
    global CONST_45
    global CONST_44
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_44
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_W=X_REG
    Y_REG=CONST_45
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=CONST_5
    VAR_I=Y_REG
    return 1390
def line_1390():
    global VAR_I
    global _zeroflag
    global CONST_14
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_7
    X_REG=VAR_I
    X_REG=X_REG+Y_REG
    VAR_I=X_REG
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    Y_REG=CONST_14
    X_REG=VAR_U
    X_REG= (-1 if X_REG>Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP70"
    return "SKIP70"
def NSKIP70():
    return 1430
    return "SKIP70"
def SKIP70():
    return 1400
def line_1400():
    global _zeroflag
    global VAR_U
    global Y_REG
    global CONST_36
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_36
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP71"
    return "SKIP71"
def NSKIP71():
    return 1430
    return "SKIP71"
def SKIP71():
    return 1410
def line_1410():
    global _zeroflag
    global VAR_U
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_5
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP72"
    return "SKIP72"
def NSKIP72():
    return 1430
    return "SKIP72"
def SKIP72():
    return 1420
def line_1420():
    global VAR_A
    global VAR_U
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _stack.append(Y_REG)
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1390
def line_1430():
    global VAR_I
    global VAR_A
    global VAR_W
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=VAR_W
    _stack.append(Y_REG)
    X_REG=VAR_I
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_5) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1440
def line_1440():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 1170
def line_1450():
    global VAR_A
    global CONST_26
    global Y_REG
    global CONST_35
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_6
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_6) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_26) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    return 1460
def line_1460():
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_38
    global _memory
    global CONST_97
    global CONST_61
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_97) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_61) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1470():
    return 1480
def line_1480():
    global VAR_O
    global VAR_A
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_5
    Y_REG=VAR_A
    _stack.append(Y_REG)
    X_REG=VAR_O
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    GOSUB("GOSUBCONT16")
    return 400
def GOSUBCONT16():
    return 1490
def line_1490():
    global VAR_R
    global VAR_N
    global VAR_A
    global CONST_10
    global G_REG
    global _stack
    global Y_REG
    global VAR_N_array
    global X_REG
    global CONST_7
    global VAR_A_array
    Y_REG=CONST_7
    X_REG=VAR_R
    X_REG=X_REG+Y_REG
    VAR_R=X_REG
    Y_REG=VAR_R
    _stack.append(Y_REG)
    X_REG=_stack.pop()
    Y_REG=VAR_N
    G_REG=VAR_N_array
    ARRAYSTORE_REAL()
    Y_REG=VAR_R
    _stack.append(Y_REG)
    X_REG=_stack.pop()
    Y_REG=VAR_A
    G_REG=VAR_A_array
    ARRAYSTORE_REAL()
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1500():
    return 1510
def line_1510():
    global VAR_U
    global CONST_103
    global Y_REG
    Y_REG=CONST_103
    VAR_U=Y_REG
    GOSUB("GOSUBCONT17")
    return 100
def GOSUBCONT17():
    return 1520
def line_1520():
    global VAR_A
    global CONST_10
    global VAR_LP
    global Y_REG
    global CONST_83
    global _memory
    global X_REG
    Y_REG=VAR_A
    VAR_LP=Y_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_83) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1530
def line_1530():
    global VAR_HU
    global VAR_U
    global Y_REG
    global CONST_71
    Y_REG=VAR_U
    VAR_HU=Y_REG
    Y_REG=CONST_71
    VAR_U=Y_REG
    GOSUB("GOSUBCONT18")
    return 40
def GOSUBCONT18():
    global VAR_HU
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_HU
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    return 1540
def line_1540():
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_31
    global CONST_36
    global CONST_37
    global CONST_33
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_37) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1550
def line_1550():
    global VAR_F
    global VAR_HF
    global VAR_W
    global CONST_43
    global Y_REG
    Y_REG=VAR_F
    VAR_HF=Y_REG
    Y_REG=CONST_43
    VAR_W=Y_REG
    GOSUB("GOSUBCONT19")
    return 1090
def GOSUBCONT19():
    global VAR_F
    global VAR_HF
    global Y_REG
    Y_REG=VAR_HF
    VAR_F=Y_REG
    return 1560
def line_1560():
    global VAR_A
    global CONST_10
    global CONST_44
    global CONST_104
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_10) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_8) & 255
    Y_REG=CONST_44
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_104) & 255
    return 1570
def line_1570():
    global VAR_A
    global CONST_27
    global CONST_25
    global Y_REG
    global _memory
    global CONST_92
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_25) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG-Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_92) & 255
    return 1580
def line_1580():
    global VAR_A
    global CONST_10
    global VAR_XA
    global Y_REG
    global CONST_83
    global _memory
    global X_REG
    Y_REG=VAR_A
    VAR_XA=Y_REG
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_83) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1590
def line_1590():
    global _zeroflag
    global VAR_U
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    global CONST_6
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_6
    X_REG= (-1 if X_REG!=Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP73"
    return "SKIP73"
def NSKIP73():
    global VAR_A
    global CONST_12
    global CONST_10
    global CONST_27
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    global CONST_5
    global CONST_6
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_6) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_7) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_12) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1610
    return "SKIP73"
def SKIP73():
    return 1600
def line_1600():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT20")
    return 100
def GOSUBCONT20():
    return 1610
def line_1610():
    global VAR_B
    global CONST_17
    global VAR_U
    global Y_REG
    global CONST_64
    Y_REG=CONST_64
    VAR_U=Y_REG
    Y_REG=CONST_17
    VAR_B=Y_REG
    GOSUB("GOSUBCONT21")
    return 150
def GOSUBCONT21():
    return 1620
def line_1620():
    global VAR_A
    global VAR_D
    global Y_REG
    Y_REG=VAR_A
    VAR_D=Y_REG
    GOSUB("GOSUBCONT22")
    return 570
def GOSUBCONT22():
    global VAR_L
    global VAR_H
    global VAR_LP
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_7
    X_REG=VAR_LP
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_LP
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1630
def line_1630():
    global VAR_D
    global _memory
    global X_REG
    X_REG=int(_memory[829]) & 255;
    VAR_D=X_REG
    GOSUB("GOSUBCONT23")
    return 990
def GOSUBCONT23():
    return "RETURN"
def line_1640():
    return 1650
def line_1650():
    global VAR_D
    global CONST_10
    global VAR_LP
    global Y_REG
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_LP
    X_REG=X_REG+Y_REG
    VAR_D=X_REG
    GOSUB("GOSUBCONT24")
    return 570
def GOSUBCONT24():
    global VAR_L
    global VAR_H
    global VAR_A
    global VAR_D
    global CONST_10
    global _stack
    global Y_REG
    global CONST_83
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_83) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    Y_REG=VAR_A
    VAR_D=Y_REG
    GOSUB("GOSUBCONT25")
    return 570
def GOSUBCONT25():
    return 1660
def line_1660():
    global VAR_L
    global VAR_H
    global VAR_XA
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=CONST_7
    X_REG=VAR_XA
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_XA
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return "RETURN"
def line_1670():
    return 1680
def line_1680():
    GOSUB("GOSUBCONT26")
    return 100
def GOSUBCONT26():
    global VAR_A
    global CONST_105
    global Y_REG
    global CONST_31
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_105) & 255
    return 1690
def line_1690():
    global VAR_A
    global CONST_10
    global CONST_106
    global Y_REG
    global CONST_33
    global _memory
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_106) & 255
    return 1700
def line_1700():
    global VAR_A
    global CONST_41
    global CONST_108
    global CONST_107
    global CONST_27
    global Y_REG
    global CONST_38
    global CONST_39
    global CONST_35
    global _memory
    global X_REG
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_35) & 255
    Y_REG=CONST_38
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_107) & 255
    Y_REG=CONST_39
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_108) & 255
    Y_REG=CONST_41
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1710():
    return 1720
def line_1720():
    GOSUB("GOSUBCONT27")
    return 100
def GOSUBCONT27():
    global VAR_A
    global Y_REG
    global CONST_31
    global CONST_36
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_31) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    return 1730
def line_1730():
    global VAR_A
    global CONST_10
    global CONST_27
    global Y_REG
    global CONST_37
    global CONST_33
    global _memory
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_33) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_37) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1740
def line_1740():
    global _zeroflag
    global VAR_U
    global CONST_57
    global Y_REG
    global _memory
    global X_REG
    global CONST_5
    Y_REG=VAR_U
    X_REG=_memory[int(Y_REG) & 65535];
    Y_REG=CONST_57
    X_REG= (-1 if X_REG!=Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP74"
    return "SKIP74"
def NSKIP74():
    return 920
    return "SKIP74"
def SKIP74():
    return 1750
def line_1750():
    global VAR_U
    global Y_REG
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_U
    X_REG=X_REG+Y_REG
    VAR_U=X_REG
    GOSUB("GOSUBCONT28")
    return 100
def GOSUBCONT28():
    global VAR_A
    global CONST_40
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_40) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_5) & 255
    return 1760
def line_1760():
    global VAR_A
    global CONST_10
    global CONST_109
    global CONST_27
    global Y_REG
    global CONST_36
    global _memory
    global X_REG
    global CONST_8
    Y_REG=CONST_8
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_109) & 255
    Y_REG=CONST_10
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_36) & 255
    Y_REG=CONST_27
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return "RETURN"
def line_1770():
    return 1780
def line_1780():
    return 1790
def line_1790():
    global VAR_I
    global VAR_J
    global VAR_K
    global VAR_A
    global VAR_B
    global VAR_D
    global VAR_U
    global VAR_V
    global Y_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_A=Y_REG
    Y_REG=CONST_5
    VAR_B=Y_REG
    Y_REG=CONST_5
    VAR_U=Y_REG
    Y_REG=CONST_5
    VAR_I=Y_REG
    Y_REG=CONST_5
    VAR_J=Y_REG
    Y_REG=CONST_5
    VAR_K=Y_REG
    Y_REG=CONST_5
    VAR_V=Y_REG
    Y_REG=CONST_5
    VAR_D=Y_REG
    return 1800
def line_1800():
    global VAR_L
    global VAR_H
    global VAR_C
    global VAR_W
    global Y_REG
    global CONST_5
    Y_REG=CONST_5
    VAR_C=Y_REG
    Y_REG=CONST_5
    VAR_H=Y_REG
    Y_REG=CONST_5
    VAR_L=Y_REG
    Y_REG=CONST_5
    VAR_W=Y_REG
    return 1810
def line_1810():
    global CONST_110
    global _memory
    global CONST_5
    _memory[53281]=int(CONST_5) & 255;
    _memory[53280]=int(CONST_5) & 255;
    _memory[646]=int(CONST_110) & 255;
    return 1820
def line_1820():
    global VAR_S
    global CONST_112
    global CONST_111
    global Y_REG
    global VAR_S_STRVAR
    global VAR_Z_STRVAR
    global B_REG
    global CONST_5
    global A_REG
    B_REG=CONST_111
    VAR_S_STRVAR=B_REG
    Y_REG=CONST_112
    VAR_S=Y_REG
    Y_REG=CONST_5
    CHR()
    VAR_Z_STRVAR=A_REG
    return 1830
def line_1830():
    return "INPUT0"
def INPUT0():
    global _zeroflag
    global CONST_113
    global VAR_S_STRVAR
    global A_REG
    CLEARQUEUE()
    A_REG=CONST_113
    STROUT()
    QMARKOUT1()
    INPUTSTR()
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP1"
    VAR_S_STRVAR=A_REG
    return "EMPTYINPUTSKIP1"
def EMPTYINPUTSKIP1():
    global _zeroflag
    global X_REG
    global CONST_5
    QUEUESIZE()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "INPUTCHECK0"
    EXTRAIGNORED()
    return "INPUTCHECK0"
def INPUTCHECK0():
    return 1840
def line_1840():
    global _zeroflag
    global CONST_114
    global CONST_115
    global _stack
    global Y_REG
    global VAR_S_STRVAR
    global B_REG
    global X_REG
    global CONST_5
    global A_REG
    RESTORE()
    B_REG=CONST_114
    A_REG=VAR_S_STRVAR
    SEQ()
    _stack.append(X_REG)
    B_REG=CONST_115
    A_REG=VAR_S_STRVAR
    SEQ()
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP75"
    return "SKIP75"
def NSKIP75():
    END()
    return
    return "SKIP75"
def SKIP75():
    return 1850
def line_1850():
    return "INPUT1"
def INPUT1():
    global _zeroflag
    global CONST_116
    global CONST_117
    global X_REG
    global CONST_5
    global A_REG
    CLEARQUEUE()
    A_REG=CONST_116
    STROUT()
    QMARKOUT1()
    INPUTNUMBER()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "INPUT1_0"
    A_REG=CONST_117
    STROUT()
    LINEBREAK()
    return "INPUT1"
def INPUT1_0():
    global VAR_S
    global _zeroflag
    global Y_REG
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP2"
    VAR_S=Y_REG
    return "EMPTYINPUTSKIP2"
def EMPTYINPUTSKIP2():
    global _zeroflag
    global X_REG
    global CONST_5
    QUEUESIZE()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "INPUTCHECK1"
    EXTRAIGNORED()
    return "INPUTCHECK1"
def INPUTCHECK1():
    global VAR_S
    global VAR_A
    global Y_REG
    global CONST_39
    global X_REG
    LINEBREAK()
    Y_REG=CONST_39
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 1860
def line_1860():
    global VAR_A
    global VAR_D
    global Y_REG
    Y_REG=VAR_A
    VAR_D=Y_REG
    GOSUB("GOSUBCONT29")
    return 570
def GOSUBCONT29():
    global VAR_L
    global VAR_H
    global VAR_S
    global _stack
    global Y_REG
    global CONST_83
    global _memory
    global X_REG
    global CONST_7
    global CONST_8
    Y_REG=VAR_S
    _memory[int(Y_REG)]=int(CONST_83) & 255
    Y_REG=CONST_7
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_8
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1870
def line_1870():
    global VAR_S
    global CONST_10
    global CONST_119
    global CONST_118
    global CONST_27
    global Y_REG
    global CONST_38
    global CONST_83
    global _memory
    global X_REG
    Y_REG=CONST_10
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_83) & 255
    Y_REG=CONST_27
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_118) & 255
    Y_REG=CONST_38
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    Y_REG=X_REG
    _memory[int(Y_REG)]=int(CONST_119) & 255
    return 1880
def line_1880():
    global CONST_10
    global D_REG
    global CONST_42
    global CONST_120
    global G_REG
    global CONST_110
    global _stack
    global CONST_27
    global Y_REG
    global VAR_S_STRVAR
    global C_REG
    global B_REG
    global X_REG
    global CONST_8
    global A_REG
    Y_REG=CONST_110
    _stack.append(Y_REG)
    Y_REG=CONST_42
    _stack.append(Y_REG)
    D_REG=CONST_110
    C_REG=_stack.pop()
    X_REG=_stack.pop()
    Y_REG=CONST_10
    OPEN()
    Y_REG=CONST_8
    _stack.append(Y_REG)
    Y_REG=CONST_42
    _stack.append(Y_REG)
    Y_REG=CONST_8
    _stack.append(Y_REG)
    B_REG=VAR_S_STRVAR
    A_REG=CONST_120
    CONCAT()
    G_REG=A_REG
    D_REG=_stack.pop()
    C_REG=_stack.pop()
    X_REG=_stack.pop()
    Y_REG=CONST_27
    OPEN()
    return 1890
def line_1890():
    global _zeroflag
    global CONST_110
    global _stack
    global Y_REG
    global C_REG
    global VAR_E1
    Y_REG=CONST_110
    _stack.append(Y_REG)
    CLEARQUEUE()
    C_REG=_stack.pop()
    INPUTNUMBERCHANNEL()
    _stack.append(C_REG)
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP3"
    VAR_E1=Y_REG
    return "EMPTYINPUTSKIP3"
def EMPTYINPUTSKIP3():
    global _zeroflag
    global VAR_E2_STRVAR
    global _stack
    global C_REG
    global A_REG
    C_REG=_stack.pop()
    INPUTSTRCHANNEL()
    _stack.append(C_REG)
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP4"
    VAR_E2_STRVAR=A_REG
    return "EMPTYINPUTSKIP4"
def EMPTYINPUTSKIP4():
    global _zeroflag
    global _stack
    global Y_REG
    global C_REG
    global VAR_E3
    C_REG=_stack.pop()
    INPUTNUMBERCHANNEL()
    _stack.append(C_REG)
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP5"
    VAR_E3=Y_REG
    return "EMPTYINPUTSKIP5"
def EMPTYINPUTSKIP5():
    global _zeroflag
    global _stack
    global Y_REG
    global C_REG
    global VAR_E4
    C_REG=_stack.pop()
    INPUTNUMBERCHANNEL()
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP6"
    VAR_E4=Y_REG
    return "EMPTYINPUTSKIP6"
def EMPTYINPUTSKIP6():
    global _zeroflag
    global Y_REG
    global X_REG
    global VAR_E1
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_E1
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP76"
    return "SKIP76"
def NSKIP76():
    return "RETURN"
    return "SKIP76"
def SKIP76():
    return 1900
def line_1900():
    global VAR_E2_STRVAR
    global X_REG
    global VAR_E3
    global VAR_E1
    global VAR_E4
    global A_REG
    X_REG=VAR_E1
    REALOUT()
    CRSRRIGHT()
    A_REG=VAR_E2_STRVAR
    STROUT()
    X_REG=VAR_E3
    REALOUT()
    CRSRRIGHT()
    X_REG=VAR_E4
    REALOUT()
    CHECKCMD()
    LINEBREAK()
    return 1910
def line_1910():
    return 1920
def line_1920():
    global CONST_110
    global X_REG
    global CONST_8
    X_REG=CONST_8
    CLOSE()
    X_REG=CONST_110
    CLOSE()
    return 1930
def line_1930():
    global VAR_R
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_R
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP77"
    return "SKIP77"
def NSKIP77():
    return 1980
    return "SKIP77"
def SKIP77():
    return 1940
def line_1940():
    global VAR_I
    global VAR_R
    global _stack
    global Y_REG
    global CONST_7
    Y_REG=CONST_7
    VAR_I=Y_REG
    Y_REG=VAR_R
    _stack.append(Y_REG)
    Y_REG=CONST_7
    _stack.append(Y_REG)
    INITFOR("FORLOOP1","VAR_I")
    return "FORLOOP1"
def FORLOOP1():
    global VAR_I
    global VAR_N
    global VAR_D
    global VAR_W
    global G_REG
    global Y_REG
    global VAR_N_array
    global X_REG
    global CONST_5
    global VAR_A_array
    X_REG=VAR_I
    G_REG=VAR_N_array
    ARRAYACCESS_REAL()
    VAR_N=X_REG
    X_REG=VAR_I
    G_REG=VAR_A_array
    ARRAYACCESS_REAL()
    VAR_W=X_REG
    Y_REG=CONST_5
    VAR_D=Y_REG
    return 1950
def line_1950():
    global VAR_T
    global VAR_M
    global _stack
    global Y_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_5
    VAR_T=Y_REG
    Y_REG=VAR_M
    _stack.append(Y_REG)
    Y_REG=CONST_7
    _stack.append(Y_REG)
    INITFOR("FORLOOP2","VAR_T")
    return "FORLOOP2"
def FORLOOP2():
    global VAR_T
    global VAR_N
    global _zeroflag
    global VAR_S_array
    global G_REG
    global Y_REG
    global X_REG
    global CONST_5
    X_REG=VAR_T
    G_REG=VAR_S_array
    ARRAYACCESS_REAL()
    Y_REG=VAR_N
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP78"
    return "SKIP78"
def NSKIP78():
    global VAR_T
    global VAR_M
    global VAR_D
    global G_REG
    global Y_REG
    global X_REG
    global VAR_L_array
    X_REG=VAR_T
    G_REG=VAR_L_array
    ARRAYACCESS_REAL()
    VAR_D=X_REG
    Y_REG=VAR_M
    VAR_T=Y_REG
    return "SKIP78"
def SKIP78():
    return 1960
def line_1960():
    global _zeroflag
    global CONST_5
    global A_REG
    NEXT("VAR_T")
    _zeroflag=(0 if A_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "($JUMP)"
    GOSUB("GOSUBCONT30")
    return 570
def GOSUBCONT30():
    global VAR_L
    global VAR_W
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    Y_REG=CONST_7
    X_REG=VAR_W
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 1970
def line_1970():
    global VAR_H
    global _zeroflag
    global VAR_W
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_8
    global CONST_5
    global A_REG
    Y_REG=CONST_8
    X_REG=VAR_W
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    NEXT("VAR_I")
    _zeroflag=(0 if A_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "($JUMP)"
    return 1980
def line_1980():
    global VAR_G
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    Y_REG=CONST_5
    X_REG=VAR_G
    X_REG= (-1 if X_REG==Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP79"
    return "SKIP79"
def NSKIP79():
    return 2030
    return "SKIP79"
def SKIP79():
    return 1990
def line_1990():
    global VAR_A
    global VAR_D
    global Y_REG
    Y_REG=VAR_A
    VAR_D=Y_REG
    GOSUB("GOSUBCONT31")
    return 570
def GOSUBCONT31():
    global VAR_L
    global VAR_H
    global VAR_S
    global _stack
    global CONST_27
    global Y_REG
    global CONST_38
    global _memory
    global X_REG
    Y_REG=CONST_27
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_L
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_38
    X_REG=VAR_S
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    X_REG=VAR_H
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    return 2000
def line_2000():
    global VAR_D
    global _zeroflag
    global Y_REG
    global X_REG
    global CONST_5
    READNUMBER()
    VAR_D=Y_REG
    Y_REG=CONST_5
    X_REG=VAR_D
    X_REG= (-1 if X_REG<Y_REG else 0)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP80"
    return "SKIP80"
def NSKIP80():
    return 2030
    return "SKIP80"
def SKIP80():
    return 2010
def line_2010():
    global VAR_A
    global VAR_D
    global _stack
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    Y_REG=VAR_A
    _stack.append(Y_REG)
    X_REG=VAR_D
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_A=X_REG
    return 2020
def line_2020():
    return 2000
def line_2030():
    global VAR_E
    global VAR_A
    global Y_REG
    global _memory
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=VAR_A
    _memory[int(Y_REG)]=int(CONST_5) & 255
    Y_REG=CONST_7
    X_REG=VAR_A
    X_REG=X_REG+Y_REG
    VAR_E=X_REG
    return 2040
def line_2040():
    global VAR_ER
    global CONST_121
    global X_REG
    global A_REG
    A_REG=CONST_121
    STROUT()
    X_REG=VAR_ER
    REALOUT()
    CHECKCMD()
    LINEBREAK()
    return 2050
def line_2050():
    global VAR_E
    global VAR_S
    global CONST_123
    global CONST_122
    global Y_REG
    global CONST_63
    global X_REG
    global A_REG
    A_REG=CONST_122
    STROUT()
    X_REG=VAR_S
    REALOUT()
    CRSRRIGHT()
    A_REG=CONST_63
    STROUT()
    X_REG=VAR_E
    Y_REG=CONST_123
    X_REG=X_REG*Y_REG
    REALOUT()
    CHECKCMD()
    LINEBREAK()
    return 2060
def line_2060():
    global CONST_124
    global VAR_S_STRVAR
    global A_REG
    A_REG=VAR_S_STRVAR
    STROUT()
    A_REG=CONST_124
    STROUT()
    READTID()
    A_REG=tmpy
    STROUT()
    LINEBREAK()
    return 2070
def line_2070():
    global CONST_125
    global _memory
    global CONST_5
    global A_REG
    A_REG=CONST_125
    STROUT()
    LINEBREAK()
    _memory[198]=int(CONST_5) & 255;
    return 2080
def line_2080():
    global _zeroflag
    global CONST_126
    global B_REG
    global X_REG
    global VAR_X_STRVAR
    global CONST_5
    global A_REG
    GETSTR()
    VAR_X_STRVAR=A_REG
    B_REG=CONST_126
    A_REG=VAR_X_STRVAR
    SEQ()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP81"
    return "SKIP81"
def NSKIP81():
    return 2170
    return "SKIP81"
def SKIP81():
    return 2100
def line_2100():
    global _zeroflag
    global CONST_127
    global B_REG
    global X_REG
    global VAR_X_STRVAR
    global CONST_5
    global A_REG
    B_REG=CONST_127
    A_REG=VAR_X_STRVAR
    SEQ()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP82"
    return "SKIP82"
def NSKIP82():
    GOSUB("GOSUBCONT32")
    return 1820
def GOSUBCONT32():
    return 590
    return "SKIP82"
def SKIP82():
    return 2110
def line_2110():
    global _zeroflag
    global CONST_128
    global B_REG
    global X_REG
    global VAR_X_STRVAR
    global CONST_5
    global A_REG
    B_REG=CONST_128
    A_REG=VAR_X_STRVAR
    SEQ()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP83"
    return "SKIP83"
def NSKIP83():
    END()
    return
    return "SKIP83"
def SKIP83():
    return 2130
def line_2130():
    return 2080
def line_2140():
    global VAR_I
    global CONST_129
    global CONST_59
    global _stack
    global Y_REG
    global CONST_7
    Y_REG=CONST_59
    VAR_I=Y_REG
    Y_REG=CONST_129
    _stack.append(Y_REG)
    Y_REG=CONST_7
    _stack.append(Y_REG)
    INITFOR("FORLOOP3","VAR_I")
    return "FORLOOP3"
def FORLOOP3():
    global VAR_I
    global _zeroflag
    global Y_REG
    global _memory
    global CONST_5
    global A_REG
    Y_REG=VAR_I
    _memory[int(Y_REG)]=int(CONST_5) & 255
    NEXT("0")
    _zeroflag=(0 if A_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "($JUMP)"
    return 2150
def line_2150():
    global VAR_S
    global X_REG
    X_REG=VAR_S
    SYSTEMCALLDYN()
    return 2070
def line_2160():
    return 2170
def line_2170():
    global VAR_N_STRVAR
    global _stack
    global CONST_26
    global VAR_S_STRVAR
    global C_REG
    global B_REG
    global CONST_130
    global A_REG
    B_REG=CONST_130
    _stack.append(B_REG)
    C_REG=CONST_26
    B_REG=VAR_S_STRVAR
    LEFT()
    B_REG=_stack.pop()
    CONCAT()
    VAR_N_STRVAR=A_REG
    return "INPUT2"
def INPUT2():
    global VAR_N_STRVAR
    global _zeroflag
    global CONST_131
    global A_REG
    CLEARQUEUE()
    A_REG=CONST_131
    STROUT()
    QMARKOUT1()
    INPUTSTR()
    INPUTLENGTHCHECK()
    if _zeroflag==0:
        return "EMPTYINPUTSKIP7"
    VAR_N_STRVAR=A_REG
    return "EMPTYINPUTSKIP7"
def EMPTYINPUTSKIP7():
    global _zeroflag
    global X_REG
    global CONST_5
    QUEUESIZE()
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "INPUTCHECK2"
    EXTRAIGNORED()
    return "INPUTCHECK2"
def INPUTCHECK2():
    return 2180
def line_2180():
    global VAR_N_STRVAR
    global D_REG
    global CONST_42
    global G_REG
    global CONST_110
    global _stack
    global CONST_27
    global Y_REG
    global C_REG
    global B_REG
    global CONST_132
    global X_REG
    global VAR_T_STRVAR
    global A_REG
    Y_REG=CONST_110
    _stack.append(Y_REG)
    Y_REG=CONST_42
    _stack.append(Y_REG)
    Y_REG=CONST_110
    _stack.append(Y_REG)
    B_REG=VAR_N_STRVAR
    A_REG=CONST_132
    CONCAT()
    G_REG=A_REG
    D_REG=_stack.pop()
    C_REG=_stack.pop()
    X_REG=_stack.pop()
    Y_REG=CONST_27
    OPEN()
    X_REG=CONST_110
    CLOSE()
    B_REG=VAR_N_STRVAR
    VAR_T_STRVAR=B_REG
    return 2190
def line_2190():
    global VAR_I
    global _stack
    global Y_REG
    global B_REG
    global VAR_T_STRVAR
    global CONST_7
    Y_REG=CONST_7
    VAR_I=Y_REG
    B_REG=VAR_T_STRVAR
    LEN()
    _stack.append(X_REG)
    Y_REG=CONST_7
    _stack.append(Y_REG)
    INITFOR("FORLOOP4","VAR_I")
    return "FORLOOP4"
def FORLOOP4():
    global VAR_I
    global _zeroflag
    global D_REG
    global _stack
    global CONST_103
    global Y_REG
    global C_REG
    global _memory
    global B_REG
    global X_REG
    global VAR_T_STRVAR
    global CONST_7
    global CONST_5
    global A_REG
    Y_REG=VAR_I
    X_REG=CONST_103
    X_REG=X_REG+Y_REG
    _stack.append(X_REG)
    C_REG=VAR_I
    D_REG=CONST_7
    B_REG=VAR_T_STRVAR
    MID()
    B_REG=A_REG
    ASC()
    Y_REG=_stack.pop()
    _memory[int(Y_REG)]=int(X_REG) & 255
    NEXT("0")
    _zeroflag=(0 if A_REG==CONST_5 else 1)
    if _zeroflag==0:
        return "($JUMP)"
    return 2200
def line_2200():
    global CONST_10
    global CONST_85
    global _memory
    global B_REG
    global X_REG
    global VAR_T_STRVAR
    global CONST_7
    _memory[782]=int(CONST_10) & 255;
    _memory[781]=int(CONST_85) & 255;
    B_REG=VAR_T_STRVAR
    LEN()
    _memory[780]=int(X_REG) & 255;
    SYSCALL("$ffbd()")
    _memory[780]=int(CONST_7) & 255;
    return 2210
def line_2210():
    global CONST_42
    global _memory
    global CONST_7
    _memory[781]=int(CONST_42) & 255;
    _memory[782]=int(CONST_7) & 255;
    SYSCALL("$ffba()")
    return 2220
def line_2220():
    global VAR_E
    global VAR_S
    global Y_REG
    global _memory
    global CONST_60
    global CONST_133
    global X_REG
    Y_REG=CONST_60
    X_REG=VAR_S
    X_REG=X_REG/Y_REG
    _memory[254]=int(X_REG) & 255;
    X_REG=int(_memory[254]) & 255;
    Y_REG=CONST_60
    X_REG=X_REG*Y_REG
    Y_REG=X_REG
    X_REG=VAR_S
    X_REG=X_REG-Y_REG
    _memory[253]=int(X_REG) & 255;
    _memory[780]=int(CONST_133) & 255;
    Y_REG=CONST_60
    X_REG=VAR_E
    X_REG=X_REG/Y_REG
    _memory[782]=int(X_REG) & 255;
    return 2230
def line_2230():
    global VAR_E
    global VAR_N_STRVAR
    global Y_REG
    global _memory
    global CONST_60
    global CONST_134
    global X_REG
    global A_REG
    X_REG=int(_memory[782]) & 255;
    Y_REG=CONST_60
    X_REG=X_REG*Y_REG
    Y_REG=X_REG
    X_REG=VAR_E
    X_REG=X_REG-Y_REG
    _memory[781]=int(X_REG) & 255;
    SYSCALL("$ffd8()")
    A_REG=CONST_134
    STROUT()
    A_REG=VAR_N_STRVAR
    STROUT()
    LINEBREAK()
    return 2240
def line_2240():
    global _zeroflag
    global _stack
    global Y_REG
    global _memory
    global CONST_135
    global X_REG
    global CONST_7
    global CONST_5
    Y_REG=CONST_135
    READSTATUS()
    X_REG=tmpy
    X_REG=int(X_REG) & int(Y_REG)
    _stack.append(X_REG)
    X_REG=int(_memory[783]) & 255;
    Y_REG=CONST_7
    X_REG=int(X_REG) & int(Y_REG)
    Y_REG=_stack.pop()
    X_REG=int(X_REG) or int(Y_REG)
    _zeroflag=(0 if X_REG==CONST_5 else 1)
    if _zeroflag==1:
        return "NSKIP84"
    return "SKIP84"
def NSKIP84():
    global CONST_136
    global A_REG
    A_REG=CONST_136
    STROUT()
    LINEBREAK()
    return "SKIP84"
def SKIP84():
    return 2250
def line_2250():
    return 2070
def line_2260():
    return 2270
def line_2270():
    return 2280
def line_2280():
    return 2290
def line_2290():
    return 2300
def line_2300():
    return 2310
def line_2310():
    return 2320
def line_2320():
    return 2330
def line_2330():
    return 2340
def line_2340():
    return 2350
def line_2350():
    return 2360
def line_2360():
    END()
    return
# *** SUBROUTINES ***
restart = False
running = True
keyPressed = None
lineNumber = 0
timeOut=0
funcName = "PROGRAMSTART"
tymp=0
status=0
_files = dict()
_fileTypes = dict()

def getMemory():
    global _memory
    return _memory
    
def signum(value):
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0
    
def isNumber(var):
    if isinstance(var, (int, float)):
        return True
    if len(var)==0:
        return False
    try:
        val = float(var)
        return True
    except ValueError:
        return False


def registerKey():
    global keyPressed
    global _memory
    k = keyboard.read_key()
    keyPressed=k
    _memory[198]=1

def execute():
    global running
    global restart
    while True:
        reinit()
        while running:
            executeLine()
        if not restart:
            break

def reinit():
    global running
    global restart
    global lineNumer
    global funcName
    lineNumber = 0
    funcName = "PROGRAMSTART"
    restart=False
    running=True

def executeLine():
    global JUMP_TARGET
    global lineNumber
    global running
    global funcName
    nextLine = globals()[funcName]()
    if nextLine != None:
        lineNumber = nextLine
        if lineNumber == "($JUMP)":
            lineNumber = JUMP_TARGET
        if isNumber(lineNumber):
            funcName = "line_" + str(lineNumber)
        else:
            funcName = lineNumber
    else:
        running = False

def START():
    global _memory
    INIT()
    _memory[646]=14

def RUN():
    global running
    global restart
    running=False
    restart=True

def RESTARTPRG():
    global running
    global restart
    running=False
    restart=True

def END():
    global _line
    if len(_line)>0:
        print(_line)

def CLEARQUEUE():
    global _inputQueue
    _inputQueue=[]

def QUEUESIZE():
    global _inputQueue
    global X_REG
    X_REG=len(_inputQueue)

def EXTRAIGNORED():
    out("?extra ignored!")

def INPUTNUMBER():
    global Y_REG
    global X_REG
    inp=input()
    if isNumber(inp):
        Y_REG=float(inp)
        X_REG=0
    else:
        X_REG=-1

def INPUTSTR():
    global A_REG
    A_REG=input()

def GETSTR():
    global A_REG
    A_REG=get()

def GETNUMBER():
    global Y_REG
    fk=get()
    if isNumber(fk):
        Y_REG=float(fk)
    else:
        out("?syntax error")


def isNaN(number):
    return math.isnan(number)

def isNumeric(number):
    return isNumber(number)

def parseFloat(number):
    return float(number)

def GOSUB(gosubCont):
    global _forstack
    _forstack.append(gosubCont)
    _forstack.append(0)

def pop(arr):
    return arr.pop()
    
def throw(txt):
    raise Exception(txt)

def RETURN():
    global _forstack
    val = 0
    if len(_forstack)==0:
        throw("RETURN without GOSUB error!")
    while True:
        val = _forstack.pop()
        if val == 1:
            _forstack.pop()
            _forstack.pop()
            _forstack.pop()
            _forstack.pop()
        if val==0:
            break
    val = _forstack.pop()
    return val

def adjustStack(variable):
    global _forstack
    i=len(_forstack)
    while i>0:
        type=_forstack[i-1]
        if type == 0:
            return
        vary = _forstack[i-2]
        addr = _forstack[i-3]
        end = _forstack[i-4]
        step = _forstack[i-5]
        i=i-5
        if vary == variable:
            _forstack=_forstack[0:i]
            return

def INITFOR(addr, variable):
    global _stack
    global _forstack
    adjustStack(variable)
    _forstack.append(_stack.pop())
    _forstack.append(_stack.pop())
    _forstack.append(addr)
    _forstack.append(variable)
    _forstack.append(1)

def NEXT(variable):
    global JUMP_TARGET
    global A_REG
    global _forstack
    found = False
    while True:
        if len(_forstack)==0:
            throw("NEXT without FOR error!")
        type=_forstack.pop()
        if type==0:
            throw("NEXT without FOR error!")
        stvar=_forstack.pop()
        addr=_forstack.pop()
        end=_forstack.pop()
        step=_forstack.pop()
        found = (variable == "0" or variable == stvar)
        if found:
            break
    globals()[stvar]+=step
    vv = globals()[stvar]    
    if (step >= 0 and vv <= end) or (step < 0 and vv >= end):
        _forstack.append(step)
        _forstack.append(end)
        _forstack.append(addr)
        _forstack.append(stvar)
        _forstack.append(1)
        A_REG = 0
        JUMP_TARGET = addr
        return
    A_REG = 1


def ARRAYACCESS_REAL():
    global G_REG
    global X_REG
    X_REG = G_REG[int(X_REG)]
    if X_REG == None:
        X_REG = 0

def ARRAYACCESS_INTEGER():
    global G_REG
    global X_REG
    X_REG = G_REG[int(X_REG)]
    if X_REG == None:
        X_REG = 0
    X_REG=int(X_REG)

def ARRAYACCESS_STRING():
    global G_REG
    global X_REG
    global A_REG
    A_REG = str(G_REG[int(X_REG)])
    if A_REG == None:
        A_REG = ""

def ARRAYSTORE_REAL():
    global G_REG
    global Y_REG
    global X_REG
    G_REG[int(X_REG)] = Y_REG

def ARRAYSTORE_INTEGER():
    global G_REG
    global Y_REG
    global X_REG
    G_REG[int(X_REG)] = int(Y_REG)

def ARRAYSTORE_STRING():
    global G_REG
    global X_REG
    global A_REG
    G_REG[int(X_REG)] = A_REG

def STR():
    global Y_REG
    global A_REG
    A_REG=str(Y_REG)
    if A_REG.endswith(".0"):
        A_REG=A_REG.replace(".0", "")

def VAL():
    global B_REG
    global X_REG
    if B_REG==None:
        X_REG=0
        return
    nums = B_REG.replace(" ","")
    num = ""
    for char in nums:
        if char not in "0123456789.":
            break
        num+=char
    try:
        X_REG=float(num)
    except:
        X_REG=0

def LEN():
    global B_REG
    global X_REG
    if B_REG == None:
        X_REG = 0
        return
    X_REG=len(B_REG)

def CHR():
    global Y_REG
    global A_REG
    A_REG=chr(int(Y_REG))


def ASC():
    global B_REG
    global X_REG
    if B_REG == None or len(B_REG)==0:
        X_REG=0
        return
    X_REG=ord(B_REG[0])

def POS():
    global X_REG
    global _line
    X_REG=len(_line)

def TAB():
    global Y_REG
    global _line
    tb=int(Y_REG)
    tb-=len(_line)
    for i in range(0,tb):
        _line+=" "

def SPC():
    global Y_REG
    global _line
    tb=int(Y_REG)
    for i in range(0,tb):
        _line+=" "

def FRE():
    global X_REG
    X_REG=65535

def CONCAT():
    global B_REG
    global A_REG
    A_REG=A_REG+B_REG

def CHARAT():
    global D_REG
    D_REG=1
    MID()

def MID():
    global D_REG
    global C_REG
    global B_REG
    global A_REG
    if B_REG == None or C_REG > len(B_REG):
        A_REG=""
        return
    end=C_REG-1 + D_REG
    if D_REG==-1:
        end=len(B_REG)
    A_REG=B_REG[C_REG-1:end]

def LEFT():
    global C_REG
    global B_REG
    global A_REG
    if C_REG > len(B_REG):
        A_REG=B_REG
        return
    if C_REG==0:
        A_REG=""
        return
    A_REG=B_REG[:C_REG]

def RIGHT():
    global C_REG
    global B_REG
    global A_REG
    if C_REG > len(B_REG):
        A_REG=B_REG
        return
    if C_REG==0:
        A_REG=""
        return
    A_REG=B_REG[len(B_REG)-C_REG:]

def SEQ():
    global B_REG
    global X_REG
    global A_REG
    if A_REG == B_REG:
        X_REG=-1
    else: 
        X_REG=0

def SNEQ():
    global B_REG
    global X_REG
    global A_REG
    if A_REG == B_REG:
        X_REG=0
    else: 
        X_REG=-1

def SGT():
    global B_REG
    global X_REG
    global A_REG
    if A_REG > B_REG:
        X_REG=-1
    else: 
        X_REG=0

def SLT():
    global B_REG
    global X_REG
    global A_REG
    if A_REG < B_REG:
        X_REG=-1
    else: 
        X_REG=0

def SGTEQ():
    global B_REG
    global X_REG
    global A_REG
    if A_REG >= B_REG:
        X_REG=-1
    else: 
        X_REG=0

def SLTEQ():
    global B_REG
    global X_REG
    global A_REG
    if A_REG <= B_REG:
        X_REG=-1
    else: 
        X_REG=0

def COMPACT():
    pass

def COMPACTMAX():
    pass

def SYSTEMCALLDYN():
    pass

def APPENDSYSCHAR():
    pass

def INPUTLENGTHCHECK():
    global _zeroflag
    global A_REG
    if A_REG==None or len(A_REG)==0:
        _zeroflag=0
    else:
        _zeroflag = 1

def SETUPMULTIPARS():
    pass

def COPYSTRINGPAR():
    pass

def COPYREALPAR():
    pass

def ADDCOLON():
    pass

def PULLDOWNMULTIPARS():
    pass

def STROUT():
    global A_REG
    out(A_REG)

def QMARKOUT1():
    out("?")

def CRSRRIGHT():
    out(" ")

def QMARKOUT2():
    out("??")

def REALOUT():
    global X_REG
    out(X_REG)

def INTOUT():
    global X_REG
    out(X_REG)

def CHECKCMD():
    pass

def LINEBREAK():
    out("\n")

def TABOUT():
    out("\t")

def millis():
    return int(time.perf_counter() * 1000)

def WRITETID(value):
    global _timeOffset
    global _time
    _time = millis()
    _timeOffset = int(value[0:2])* 1000 * 60 * 60 + int(value[2:4]) * 1000 * 60 + int(value[4:6]) * 1000

def READTI():
    global _timeOffset
    global _time
    global tmpy
    t=millis()
    t=int((t-_time+_timeOffset)/(1000.0/60.0))
    tmpy=t

def READTID():
    global _timeOffset
    global _time
    global tmpy
    t=millis()
    t=t-_time+_timeOffset
    h=int(t/(1000 * 60 * 60))
    m=int(((t-(h*(1000 * 60 * 60)))/(1000 * 60)))
    s=int((t-(h*(1000 * 60 * 60))-m*(1000 * 60))/1000)
    h=fill(h)
    m=fill(m)
    s=fill(s)
    tmpy= h+m+s

def fill(num):
    num=str(num)
    if len(num)==1:
        num="0"+num
    return num

def READSTATUS():
    global status
    global tmpy
    tmpy=status
    status=0

def RESTORE():
    global _dataPtr
    _dataPtr=0

def READSTR():
    global _datas
    global _dataPtr
    global A_REG
    A_REG=_datas[_dataPtr]
    _dataPtr+=1

def READNUMBER():
    global Y_REG
    global _datas
    global _dataPtr
    num=_datas[_dataPtr]
    _dataPtr+=1
    
    if isinstance(num, str) and (num == "." or len(num) == 0):
        num=0
    Y_REG=num

def FINX():
    throw("Fast inc optimization not supported for target PY!")

def FDEX():
    throw("Fast dec optimization not supported for target PY!")

def FASTFOR():
    throw("Fast for optimization not supported for target PY!")

def OPEN():
    global _files
    global D_REG
    global G_REG
    global Y_REG
    global C_REG
    global X_REG
    global _fileTypes
    count = int(Y_REG)
    parts = G_REG.split(",") if count>3 else []
    mode = "r"
    fileName = parts[0] if len(parts)>0 else ""
    secAddr = int(D_REG)
    device = int(C_REG)
    number = int(X_REG)
    if "r" in parts:
        mode = "r"
    else:
        if "w" in parts:
            mode = "w"
    if count>2:
        if secAddr==0:
            mode = "r"
        else:
            if secAddr==1:
                mode = "w"
        
    fileName = fileName.split(":")[-1]
        
    key = getFileKey(number)
    _fileTypes[key]="s"
    if mode=="r":
        _fileTypes[key]="p"
    if "s" in parts:
        _fileTypes[key]="s"
    if "p" in parts:
        _fileTypes[key]="p"
        
    if secAddr==15:
        diskOperation(fileName)
        _files[key]="command channel"
        return
    
    fileHandle = _files.get(key)
    if fileHandle != None:
        throw("File already open error!")
    if mode=="r":
        fileHandle = open(fileName, mode+"b")
    else:
        fileHandle = open(fileName, mode, encoding="ascii")
    _files[key]=fileHandle

def CLOSE():
    global _files
    global X_REG
    key = getFileKey(X_REG)
    fileHandle = _files.get(key)
    if fileHandle == None:
        throw("File not open error: "+key)
    if fileHandle!="command channel":
        fileHandle.close()
    _files.pop(key)

def CMD():
    out("[CMD not supported for PY, call ignored!]")

def diskOperation(fileName):
    pass

def readChar(fileHandle, mode="s"):
    global status
    status = 0
    char = fileHandle.read(1)
    if not char:
        status = 64
        return ""
    chs = fileHandle.read(1)
    if not chs:
        status = 64
    fileHandle.seek(-1, 1)
    if mode=="s":
        char = char.decode("ascii")
        if ord(char)==10:
            char = chr(13)
        return convertChar(char)
    return char[0].to_bytes(1, byteorder='big').decode('latin-1')

def REM():
    out("[inline assembly ignored!]")

def LOCKCHANNEL():
    pass

def UNLOCKCHANNEL():
    pass

def STROUTCHANNEL():
    global _files
    global C_REG
    global A_REG
    fileHandle = openFile(C_REG)
    fileHandle.write(convertString(A_REG))

def REALOUTCHANNEL():
    out("[PRINT# not supported for PY, redirected to normal PRINT]")
    REALOUT()

def LINEBREAKCHANNEL():
    global A_REG
    A_REG="\n"
    STROUTCHANNEL()

def INTOUTCHANNEL():
    out("[PRINT# not supported for PY, redirected to normal PRINT]")
    INTOUT()

def INPUTNUMBERCHANNEL():
    global Y_REG
    global X_REG
    global A_REG
    INPUTSTRCHANNEL()
    X_REG=0
    Y_REG=0
    if A_REG=="ok":
        X_REG=0
        Y_REG=0
        return
    if not isNumeric(A_REG):
        X_REG=-1
        return
    if A_REG!="":
        Y_REG=float(A_REG)
        X_REG=0

def openFile(number):
    key = getFileKey(number)
    fileHandle = _files.get(key)
    if fileHandle == None:
        throw("File not open error: "+key)
    return fileHandle

def getFileKey(number):
    return "file"+str(int(number))

def INPUTSTRCHANNEL():
    global _files
    global status
    global C_REG
    global _fileTypes
    global A_REG
    fileHandle = openFile(C_REG)
    key = getFileKey(C_REG)
    if fileHandle=="command channel":
        A_REG="ok"
        return
    A_REG=""
    stops = "\n\r:,"
    while True:
        char = readChar(fileHandle, _fileTypes.get(key))
        if char=="" or char in stops or status==64:
            return
        A_REG+=char

def GETSTRCHANNEL():
    global _files
    global C_REG
    global _fileTypes
    global A_REG
    fileHandle = openFile(C_REG)
    key = getFileKey(C_REG)
    A_REG = readChar(fileHandle, _fileTypes.get(key))

def GETNUMBERCHANNEL():
    global X_REG
    out("[GET# not supported for PY, call ignored]")
    X_REG=0

def TABOUTCHANNEL():
    out("[TAB not supported for PY in file mode, redirected to normal TAB]")
    TAB()

def SPCOUTCHANNEL():
    out("[SPC not supported for PY in file mode, redirected to normal SPC]")
    SPC()

def TABCHANNEL():
    out("[TAB not supported for PY in file mode, redirected to normal TAB]")
    TAB()

def SPCCHANNEL():
    out("[SPC not supported for PY in file mode, redirected to normal SPC]")
    SPC()

def LOAD():
    out("[LOAD not supported for PY in file mode, call ignored]")

def SAVE():
    out("[SAVE not supported for PY in file mode, call ignored]")

def VERIFY():
    out("[VERIFY not supported for PY in file mode, call ignored]")

def USR():
    global X_REG
    global _memory 
    global USR_PARAM
    addr=_memory[785] + 256*_memory[786]
    USR_PARAM=X_REG
    callStr="$"+hex(addr)
    out("[Calling user function named "+callStr+"]")
    globals()[callStr]()

def SYSCALL(addr):
    global _memory
    global VAR_S
    global VAR_E
    global VAR_N_STRVAR
    if addr=="$ffd8()":
        submem = _memory[int(VAR_S):int(VAR_E)+1]
		
        data = b''.join(struct.pack('c', i.to_bytes(1, byteorder='big')) for i in [int(VAR_S) & 255, int(VAR_S/256)])
        data += b''.join(struct.pack('c', i.to_bytes(1, byteorder='big') if i is not None else 0) for i in submem)

        with open(VAR_N_STRVAR, 'wb') as file:
            file.write(data)

def input():
    global _inputQueue
    global _line
    if len(_inputQueue)>0:
        return _inputQueue.pop()
        
    inp=__builtins__.input(_line+" ")
    _line=""
    if inp == None or len(inp)==0:
        return ""
    parts=inp.split(",")
    
    _inputQueue.extend(parts)
    ret = _inputQueue.pop()
    return ret

def get():
    flushOut()
    key = ""
    event = keyboard.read_event(True)
    if event.event_type == keyboard.KEY_UP:
        key = event.name
    return key

def flushOut():
    global _line
    if len(_line)>0:
        print(_line)
        _line = ""

def cleanBrackets(txt):
    pattern = r'\{.*?\}'
    return re.sub(pattern, '', txt)

def out(txt):
    global _line
    if isinstance(txt, str) and  "\n" in txt:
        _line += txt[0:len(txt)-1]
        print(cleanBrackets(_line))
        _line = ""
    else:
        org=txt
        txt = str(txt)
        if isinstance(org, (float, int)) and org>=0:
            txt=" "+txt
        if txt.endswith(".0"):
            txt=txt.replace(".0", "")
        _line += cleanBrackets(txt)

def convertString(txt):
    return txt
    res = []
    for char in text:
        res.append(convertChar(char))
    return "".join(res)

def convertChar(char):
        return char
        # disabled for now...
        charlow = char.lower()
        if charlow in "abcdefghijklmnopqrstuvwxyz":
            if char.islower():
                return char.upper()
            else:
                return char.lower()
        else:
            return char

execute()
