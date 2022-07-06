from tkinter import Tk
import os
import sys
import click

def Delete_from_String_all_Characters_Unsuitable_For_FileName(pc:str):
    pc = pc.strip()
    lc_suitable_simbols = 'qwertyuiopasdfghjklzxcvbnm'
    lc_suitable_simbols = lc_suitable_simbols + lc_suitable_simbols.upper() + ',.1234567890-!_ '
    lc_result = ''
    for ch in pc:
        if ch in lc_suitable_simbols:
            lc_result = lc_result + ch
    return lc_result.strip()

def Get_Clipboard_Text():
    lc_result = ''
    try:
        tk = Tk()
        lc_result = tk.clipboard_get()
        tk.destroy()
    except: click.echo(click.style("Read clipboard error:", fg='bright_red'))
    return lc_result


def Get_File_name_from_First_String(pc_source:str):
    ll = pc_source.split('\n')
    lc_result = ''
    for lc in ll:
        lc_result_cadidate = Delete_from_String_all_Characters_Unsuitable_For_FileName(lc.strip())
        if len(lc_result_cadidate)>5:
            lc_result = lc_result_cadidate
            break
    return lc_result


####################################################################################################################
lc_text = Get_Clipboard_Text()

if len(sys.argv)>=2:
    lc_filename = Delete_from_String_all_Characters_Unsuitable_For_FileName(sys.argv[1])
else:
    lc_prefer_filename = Get_File_name_from_First_String(lc_text)
    click.echo(click.style("Enter the file name:", fg='bright_red'), nl=False)
    click.echo(click.style(f"[{lc_prefer_filename}]", fg='bright_white'), nl=False)
    lc_filename = click.prompt(text='', type=str, default=lc_prefer_filename, show_default=False)
    lc_filename = Delete_from_String_all_Characters_Unsuitable_For_FileName(lc_filename)
    if len(lc_filename)==0:
        click.echo(click.style("File name didn't define", fg='bright_red'))
        exit()

if '.' not in lc_filename:
    lc_filename += '.txt'


if len(lc_text)==0:
    click.echo(click.style("Clipboard text is empty", fg='bright_red'))
    exit()

target_file = open(lc_filename, mode='w', encoding='utf-8', errors = 'ignore')
target_file.write(lc_text)
target_file.flush()
target_file.close()

ln_filesize = '{0:,}'.format(os.path.getsize(lc_filename)).replace(',', ' ')

click.echo(
            click.style(f"{lc_filename}", fg='bright_yellow', bold=True)+
            click.style("   -   ", fg='bright_cyan')+
            click.style("File size:  ", fg='bright_green')+
            click.style(f"{ln_filesize}", fg='bright_blue'),
            nl=False)

click.echo(click.style('',fg='reset'), nl=False)