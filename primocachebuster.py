import os
import sys
from subprocess import PIPE, Popen  # 执行系统命令


def print_(text_='', color='default'):
    text = str(text_)
    if color == 'default':
        print(text)
    elif color == 'black':
        print("\033[0;30;40m" + text + "\033[0m")
    elif color == 'red':
        print("\033[0;31;40m" + text + "\033[0m")
    elif color == 'green':
        print("\033[0;32;40m" + text + "\033[0m")
    elif color == 'yellow':
        print("\033[0;33;40m" + text + "\033[0m")
    elif color == 'blue':
        print("\033[0;34;40m" + text + "\033[0m")
    elif color == 'purple':
        print("\033[0;35;40m" + text + "\033[0m")
    elif color == 'cyan':
        print("\033[0;36;40m" + text + "\033[0m")
    elif color == 'white':
        print("\033[0;37;40m" + text + "\033[0m")

def executeCommandLine(cli):
        try:
            # 返回的是 Popen 实例对象
            proc = Popen(
                str(cli),  # cmd特定的查询空间的命令
                stdin=None,  # 标准输入 键盘
                stdout=PIPE,  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
                stderr=PIPE,  # 标准错误，保存到管道
                shell=True)

            # print(proc.communicate()) # 标准输出的字符串+标准错误的字符串
            outinfo, errinfo = proc.communicate()
            outinfo = outinfo.decode('gbk')
            errinfo = errinfo.decode('gbk')
            infos = {'outinfo': outinfo, 'errinfo': errinfo}
            # print(outinfo.decode('gbk'))  # 外部程序(windows系统)决定编码格式
            # print(errinfo.decode('gbk'))
            return infos
        except Exception as e:
            print('\033[0;31m' + str(e.args) + '\033[0m')
            return

def kill_process():
    process = ['FancyCcV.exe', 'fcsetup.exe', 'rxpcc.exe']
    for i in range(0,len(process)):
        t = process[i]
        print_('kill ' + t)
        o = executeCommandLine('taskkill /F /IM {}'.format(t))
        if o['errinfo'] == '':
            print_('OK.', 'green')
        else:
            # print_(o['outinfo'])
            print_(o['errinfo'], 'red')

def rm_reg_file():
    sys32 = os.environ.get('WINDIR') + '\\System32\\'
    o = executeCommandLine('dir /A /B {} | findstr .gaa'.format(sys32))
    fucking_files = o['outinfo'].splitlines()
    if o['errinfo'] != '':
        print_(o['errinfo'], 'red')
    print_('found {} in {}'.format(str(fucking_files),sys32), 'green')
    
    for i in range(0,len(fucking_files)):
        t = sys32 + fucking_files[i]
        print_('delete ' + t)
        o = executeCommandLine('del /F /A /S /Q {}'.format(t))
        if o['errinfo'] == '':
            print_('OK.', 'green')
        else:
            # print_(o['outinfo'])
            print_(o['errinfo'], 'red')

if __name__ == '__main__':
    if sys.platform != 'win32':
        exit()

    print_('#### kill PrimoCache ...', 'cyan')
    kill_process()
    print_('#### let PrimoCache try-out period never end ...', 'cyan')
    rm_reg_file()
    print_('#### enjoy :)', 'cyan')
