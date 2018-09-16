# --*-- coding:UTF-8 --*--
import subprocess,os
import xlwt,openpyxl
import configparser
from openpyxl.styles import PatternFill, Border,Side, Alignment,protection,Font,colors
'''格式化log输出的集中方式 stackoverflow
    
down vote
accepted
to output to a file:

git log > filename.log
To specify a format, like you want everything on one line

git log --pretty=oneline >filename.log
or you want it a format to be emailed via a program like sendmail

git log --pretty=email |email-sending-script.sh
to generate JSON, YAML or XML it looks like you need to do something like:

git log --pretty=format:"%h%x09%an%x09%ad%x09%s"
'''
if __name__ == '__main__':
    _PATH = r'D:\scripts\WlanRealeaseScripts'
    sonDirs = os.listdir(_PATH)
    FILE = open('WlanLog.conf',mode='w+',encoding='utf-8')
    wb  = openpyxl.Workbook()
    wlan_log = wb.create_sheet('WlanLog', 0)
    # row_index = 0
    # colum_index = 0
    conf_parse = configparser.ConfigParser()
    conf_parse.read(filenames='WlanLog.conf')

    tile_font_style = Font(name='Times New Roman',
                      size=13,
                      bold=True,
                      italic=False,
                      vertAlign=None,
                      underline='none',
                      strike=False,
                      color=colors.YELLOW)
    title_fill_style = PatternFill(fill_type='solid',
                                   start_color=colors.GREEN,
                                   end_color=colors.BLACK)
    title_border_style= Border(left=Side(border_style=None,
                                         color=colors.BLACK),
                               right=Side(border_style=None,
                                         color=colors.BLACK),
                               top=Side(border_style=None,
                                         color=colors.BLACK),
                               bottom=Side(border_style=None,
                                         color=colors.BLACK)
                               )
    title_alig_style = Alignment(horizontal='center',
                                 vertical='center')

    # C1 = wlan_log.cell(row=row_index, column=colum_index, value= 'Path')
    title_cells = wlan_log.iter_cols(min_col=1, max_col=4, max_row=1)
    row_index = 1
    colum_index = 1
    title_string = ['commitId', 'commitor', 'commit_date', 'contents']
    for colum in range(1, 5):
        C = wlan_log.cell(row=row_index, column=colum, value=title_string[colum - 1])
        C.font = tile_font_style
        C.fill = title_fill_style
        C.border = title_border_style
        C.alignment = title_alig_style
    wb.save('Wlan Log.xlsx')
    row_index+=1
    colum_index+=1
    cmd = "git log --name-status --date=iso  --pretty=format:" \
          "\"commit_id=%h;%n commitor=%cn;%n commit_date=%cd;%n" \
          "contents=%s;%ndiifs=\""
    for dir in sonDirs:
        if os.path.isdir(dir):
            os.chdir(dir)
            SB = subprocess.Popen(cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                                  encoding='utf-8')
            try:
                outs, errors = SB.communicate(timeout=60)
            except subprocess.TimeoutExpired as e:
                SB.kill()
                print(e)
            print(outs, errors)
            SPLIT_FLAG = 'commit_id'
            log_sections = str(outs).split(SPLIT_FLAG)
            for section in log_sections:
                if section is not '':
                    FILE.write(('[%s]\n' % (section[2:8])))
                    FILE.write(SPLIT_FLAG+section+'\n')

    sections = conf_parse.sections()
    for section in sections:
        print(section['commit_id'])
        print(section['commitor'])
        print(section['commit_date'])
        print(section['contents'])
        print(section['diifs'])
    FILE.close()

