top = '.'
out = 'build'

def options(opt):
    opt.load('python')

def configure(conf):
    conf.load('python')
    conf.check_python_version((2,7,0))

    try:
        conf.check_python_module('pythonosc')
    except:
        print('pythonosc missing: pip install python-osc')
       

def build(bld):
    bld(features='py',
        source=bld.path.ant_glob('MirrorheadOSC/*.py'),
        install_from='.')
