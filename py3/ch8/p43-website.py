import os
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

def mkdir_helper(dname):
    try:
        os.mkdir(dname)
    except FileExistsError:
        # keep silent
        pass
    print('Created {}'.format(dname))


def copytree_helper(src, dest):
    try:
        shutil.copytree(src, dest)
    except FileExistsError:
        pass
    print('Created {}'.format(dest))


site = input('Site name: ')
author = input('Author: ')
js = input('Want a folder for js(Y/n)?')
css = input('Want a folder for CSS(Y/n)?')

mkdir_helper('./{}'.format(site))

if js.lower() != "n":
    #mkdir_helper('./{}/js'.format(site))
    copytree_helper('./templates/js', './{}/js'.format(site))

if css.lower() != "n":
    copytree_helper('./templates/static', './{}/static'.format(site))
    '''
    try:
        shutil.copytree('./templates/static', './{}/static'.format(site))
        #mkdir_helper('./{}/css'.format(site))
    except FileExistsError:
        pass
    '''

env = Environment(
        #loader=PackageLoader('thisApplication', 'templates/html'),
        loader=FileSystemLoader('templates/html'),
        autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')
r_data = {
        'title': site,
        'author': author
        }
tabs = [
        {'name': 'Sun', 'image': 'static/Heraldic_Sun.svg'},
        {'name': 'Moon', 'image': 'static/Moon_symbol_crescent.svg'},
        {'name': 'Star', 'image': 'static/Five_Pointed_Star_Solid.svg'},
]

content = template.render(r_data=r_data, tabs=tabs)
'''
content = ('<!doctype html>\n<html>\n\n<head>\n<meta name="author" content="' +
           author + '">\n<title>"' + site + '"</title>\n</head>\n\n</html>')
'''
with open("{}/index.html".format(site), "wt", encoding="utf-8") as outf:
    outf.write(content)

print('Created ./{}/index.html'.format(site))
