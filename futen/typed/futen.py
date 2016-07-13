import sys
# import io
import argparse
import os

#from jinja2 import environment
#from jinja2_loaders import FileSystemLoader

from retic import String, Void, List
from paramiko_config import SSHConfig


#@fields({environ: environment.Environment})
#class TemplateInventoryRenderer(object):
#
#    def __init__(self:TemplateInventoryRenderer, template_dir:String)->Void:
#        # print ("Template_dir: ", type (template_dir))
#        loader = FileSystemLoader(template_dir)
#        self.environ = environment.Environment(loader)
#
#    def render(self:TemplateInventoryRenderer, template_name:String, args:Dict(String,String))->String:
#        # print("Template_name: ", type(template_name))
#        template = self.environ.get_template(template_name)
#        return template.render(**args)


def parse(lines:List(String))->SSHConfig:
    print("Lines: ", type(lines))
    #config = ''.join(lines)
    #fd = io.StringIO(config)
    parser = SSHConfig()
    parser.parse(lines)
    return parser

def get_netloc(entry:Dict(String,Dyn), parser:SSHConfig)->Tuple(String,String):
    print("Entry: ", type(entry))
    hostname = entry.get('host')[0]
    if hostname == '*':
        return ("*", "")
    port = parser.lookup(hostname).get('port')
    print(hostname)
    print(port)
    return (hostname, port)


def get_netlocs(lines:List(String))->Dict(String,String):
    parser = parse(lines)
    entries = parser._config
    print(entries)
    netlocs = {}
    for entry in entries:
        netloc = get_netloc(entry, parser)
        if not netloc:
            continue
        hostname, port = netloc
        print("port = %s" % port)
        if port:
            netlocs[hostname] = port
    return netlocs


def execute(lines:List(String), args:List(String))->String:
    print("Args: ", type(args))
    netlocs = get_netlocs(lines)

    if args.template_file:
        print("GOT TEMPLATE FILE") #bg: this is important
        #dirpath, filename = os.path.split(args.template_file)
        #renderer = TemplateInventoryRenderer(dirpath)
        #template_context = dict([
        #    (hostname, '%s:%s' % (hostname, port))
        #    for hostname, port in netlocs.items()
        #])
        #return renderer.render(filename, template_context)

    return '\n'.join(
        ['%s:%s' % (hostname, port) for hostname, port in netlocs.items()]
    )

###bg: unused
# def _validate(args):
#     pass
# 
# 
# def _parse_args():
#     description = 'Ansible inventory file generating script'
#     ' from OpenSSH configuration file'
#     arg_parser = argparse.ArgumentParser(description=description)
# 
#     option_t_help = 'Use template file'
#     arg_parser.add_argument(
#         '-t', '--template-file',
#         type=str,
#         required=False,
#         help=option_t_help,
#     )
# 
#     args = arg_parser.parse_args()
#     _validate(args)
# 
#     return args
# 
# 
# def main():
#     try:
#         lines = sys.stdin.readlines()
#         args = _parse_args()
#         result = execute(lines, args)
#         print(result)
#     except BaseException as e:
#         print('Error: %s' % e, file=sys.stderr)
# 
# 
# if __name__ == '__main__':
#     main()
