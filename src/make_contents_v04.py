#coding: utf-8
import os
import sys
import argparse
import json
import subprocess
from decimal import Decimal, ROUND_HALF_UP
from PIL import Image
#===============================================================
#
#===============================================================
# mkdict_cls
# mklist_inlines

# is_inline_single_decoration
# is_inline_single_id
# is_inline_double_link
# is_inline_double_id
# get_line_single_decoration
# get_line_single_id
# get_line_double_link
# get_line_double_id
# get_line_ref_link

# get_dir_raw_contents
# get_dir_img_this
# get_f_css_src

# is_on_head
# check_block_end
# check_block_begin

# get_image_from_drive

# format_page_head
# format_page_body_tag_begin
# format_page_body_title
# format_page_body_route
# format_page_body_tag_end

# format_content_lastUpdate
# format_content_inlines
# format_content_src
# format_content_table
# format_content_img
# format_content_body_main
# format_content
# format_content_Photos_FY

# format_index_body_main
# format_index_body_main_photos
# format_index_body_main_photos_tmb
# format_index

# read_index

# make_all
#===============================================================
#
#===============================================================
def mklist_inlines():
    def mkdict_cls(typ, tag, nam, cls, is_double=False):
        return {kw.inline_typ: typ,
                kw.inline_tag: tag, 
                kw.inline_nam: nam, 
                kw.inline_cls: cls, 
                kw.inline_is_double: is_double}

    # type
    # 0: single decoration
    # 1: single id
    # 2: double link
    # 3: double id

    inlines = [
      mkdict_cls(0, 'span', 'idx1'  , 'index1' ),
      mkdict_cls(0, 'span', 'idx2'  , 'index2' ),
      mkdict_cls(0, 'span', 'idx3'  , 'index3' ),
      mkdict_cls(0, 'span', 'w'     , 'word'   ),  # both margins
      mkdict_cls(0, 'span', 'wl'    , 'word-l' ),
      mkdict_cls(0, 'span', 'wr'    , 'word-r' ),
      mkdict_cls(0, 'span', 'v'     , 'var'    ),  # both margins
      mkdict_cls(0, 'span', 'vl'    , 'var-l'  ),
      mkdict_cls(0, 'span', 'vr'    , 'var-r'  ),
      mkdict_cls(0, 'span', 'vn'    , 'var-n'  ),
      mkdict_cls(0, 'span', 's'     , 'src'    ),  # both margins
      mkdict_cls(0, 'span', 'sl'    , 'src-l'  ),
      mkdict_cls(0, 'span', 'sr'    , 'src-r'  ),
      mkdict_cls(0, 'span', 'sn'    , 'src-n'  ),
      mkdict_cls(0, 'span', 'i'     , 'it'     ),  # both margins
      mkdict_cls(0, 'span', 'il'    , 'it-l'   ),
      mkdict_cls(0, 'span', 'ir'    , 'it-r'   ),
      mkdict_cls(0, 'span', 'in'    , 'it-n'   ),
      mkdict_cls(0, 'span', 'b'     , 'bld'    ),  # both margins
      mkdict_cls(0, 'span', 'bl'    , 'bld-l'  ),
      mkdict_cls(0, 'span', 'br'    , 'bld-r'  ),
      mkdict_cls(0, 'span', 'bn'    , 'bld-n'  ),
      mkdict_cls(0, 'span', 'b1'    , 'bld1'   ),  # both margins
      mkdict_cls(0, 'span', 'b1l'   , 'bld1-l' ),
      mkdict_cls(0, 'span', 'b1r'   , 'bld1-r' ),
      mkdict_cls(0, 'span', 'b1n'   , 'bld1-n' ),
      mkdict_cls(0, 'span', 'b2'    , 'bld2'   ),  # both margins
      mkdict_cls(0, 'span', 'b2l'   , 'bld2-l' ),
      mkdict_cls(0, 'span', 'b2r'   , 'bld2-r' ),
      mkdict_cls(0, 'span', 'b2n'   , 'bld2-n' ),
      mkdict_cls(0, 'span', 'b3'    , 'bld3'   ),  # both margins
      mkdict_cls(0, 'span', 'b3l'   , 'bld3-l' ),
      mkdict_cls(0, 'span', 'b3r'   , 'bld3-r' ),
      mkdict_cls(0, 'span', 'b3n'   , 'bld3-n' ),
      mkdict_cls(0, 'span', 'c'     , 'comment'),
      mkdict_cls(0, 'span', 'ls-dir', 'ls-dir' ),
      mkdict_cls(0, 'span', 'ls-txt', 'ls-txt' ),
      mkdict_cls(0, 'span', 'ls-ex' , 'ls-ex'  ),
      mkdict_cls(0, 'u'   , 'u'     , 'underlined'),
      mkdict_cls(0, 'span', 'c-red'   , 'c-red'   ),
      mkdict_cls(0, 'span', 'c-gray'  , 'c-gray'  ),
      mkdict_cls(0, 'span', 'c-silver', 'c-silver'),
      mkdict_cls(1, 'span', 'id'    , ''       ),
      mkdict_cls(2, 'a'   , 'a'     , ''          , True),
      mkdict_cls(2, 'a'   , 'ac'    , 'colored'   , True),
      mkdict_cls(2, 'a'   , 'au'    , 'underlined', True),
      mkdict_cls(3, 'a'   , 'aid'   , ''          , True),
    ]

    return inlines
#===============================================================
#
#===============================================================
def is_inline_single_decoration(nam):
    for inline in inlines:
        if inline[kw.inline_nam] == nam:
            if inline[kw.inline_typ] == 0:
                return True
    return False
#===============================================================
# id
#===============================================================
def is_inline_single_id(nam):
    for inline in inlines:
        if inline[kw.inline_nam] == nam:
            if inline[kw.inline_typ] == 1:
                return True
    return False
#===============================================================
# a, ac, au
#===============================================================
def is_inline_double_link(nam):
    for inline in inlines:
        if inline[kw.inline_nam] == nam:
            if inline[kw.inline_typ] == 2:
                return True
    return False
#===============================================================
# aid
#===============================================================
def is_inline_double_id(nam):
    for inline in inlines:
        if inline[kw.inline_nam] == nam:
            if inline[kw.inline_typ] == 3:
                return True
    return False
#===============================================================
#
#===============================================================
def get_line_single_decoration(cls, content):
    return f"<span class='{cls}'>{content}</span>"
#===============================================================
#
#===============================================================
def get_line_single_id(id):
    return f"<span id='{id}'></span>"
#===============================================================
#
#===============================================================
def get_line_double_link(cls, url, name):
    return f"<a class='{cls}' href=\"{url}\">{name}</a>"
#===============================================================
#
#===============================================================
def get_line_double_id(id, name):
    return f"<a href=\"#{id}\">{name}</a>"
#===============================================================
#
#===============================================================
def get_line_ref_link(url, title):

    if url == const.ref_link_none:
        return '  + (No link)'
    else:
        return f'  + <a href="{url}">{title}</a>'
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def get_dir_raw_contents(dirName):
    return f'{const.dir_raw}/{dirName}/{const.dirName_contents}/'
#===============================================================
#
#===============================================================
def get_dir_img_this(path_raw, dir_raw_contents, dirName):
    dir_img_contents = f'{const.dir_page_base}/{dirName}/{const.dirName_img}/'

    return path_raw.replace(dir_raw_contents,dir_img_contents).replace(const.ext_raw,'')
#===============================================================
#
#===============================================================
def get_f_css_src(language: str) -> str:
    return f'css/src/{language}.css'
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def is_on_head(line, key):
    res = False
    if len(line) >= len(key):
        res = line[:len(key)] == key

    return res
#===============================================================
#
#===============================================================
def check_block_end(iLine, blockName_present, blockName_end):
    if blockName_present is None:
        raise Exception(f'@ line {iLine+1}; block "{blockName_end}" is not opened.')
    if blockName_present != blockName_end:
        raise Exception(f'@ line {iLine+1}; block "{blockName_present}" is not closed.')
#===============================================================
#
#===============================================================
def check_block_begin(iLine, blockName_present, blockName_begin):
    if blockName_begin == const.blockName_index:
        raise Exception(
            f'@ line {iLine+1}; '\
            f'block "{const.blockName_index}" may not be in any block.'
        )
    elif blockName_begin == const.blockName_contents:
        if blockName_present in [const.blockName_index] + const.blockNames_special:
            raise Exception(
              f'@ line {iLine+1}; '\
              f'block "{const.blockName_contents}" in block "{blockName_present}" is not allowed.'
            )
    elif blockName_begin == const.blockName_ref:
        raise Exception(
            f'@ line {iLine+1}; block "{const.blockName_ref}" may not be in any block.'
        )
#===============================================================
#
#===============================================================
#
#
#
#
#
#==============================================================
#
#==============================================================
def get_image_from_drive(
    cls, url_drive, fid, extension, dir_img_this, 
    dirName, toBeUpdated,
):
    proc = sys._getframe().f_code.co_name

    def calc_size_thumbnail(width_org, height_org, width_tmb_max, height_tmb_max):
        compress = min(1.0, max(width_tmb_max/float(width_org), height_tmb_max/float(height_org)))
        width_tmb, height_tmb = int(round(width_org*compress)), int(round(height_org*compress))

        return width_tmb, height_tmb

    # Get url
    if 'https://drive.google.com/open?id=' in url_drive:
        url = url_drive.replace('open?id=', 'uc?export=download&id=')
    elif 'https://drive.google.com/file/d/' in url_drive:
        url = url_drive.replace('file/d/', 'uc?export=download&id=')\
                       .replace('/view?usp=sharing', '')\
                       .replace('/view?usp=drive_link', '')
    else:
        raise Exception(f'Invalid format of url: {url}')

    # Settings
    size_fmt = 600*600
    width_tmb_max, height_tmb_max = 300, 200
    extension     = '.' + extension
    extension_fmt = '.png'

    # Make directories
    dir_img_raw = os.path.join(dir_img_this,'raw')
    dir_img_fmt = os.path.join(dir_img_this,'fmt')
    dir_img_tmb = os.path.join(dir_img_this,'tmb')

    if not os.path.isdir(dir_img_raw):
        print(f'[{proc}] mkdir {dir_img_raw}')
        os.makedirs(dir_img_raw)
    if not os.path.isdir(dir_img_fmt):
        print('[{proc}] mkdir {dir_img_fmt}')
        os.makedirs(dir_img_fmt)
    if dirName in [const.category_Photos]:
        if not os.path.isdir(dir_img_tmb):
            print('[{proc}] mkdir {dir_img_tmb}')
            os.makedirs(dir_img_tmb)

    # Set paths
    if fid is None:
        if 'https://drive.google.com/open?id=' in url_drive:
            fid = url.split('id=')[1].strip()
        elif 'https://drive.google.com/file/d/' in url_drive:
            fid = url.split('id=')[1]

    path_raw = os.path.join(dir_img_raw, fid+extension)
    path_fmt = os.path.join(dir_img_fmt, fid+extension_fmt)
    path_tmb = os.path.join(dir_img_tmb, fid+extension_fmt)

    print(f'[{proc}] {url}')
    print(f' {""*len(proc)}  -> {path_raw.replace(const.dir_top,"")}')


    if not toBeUpdated:
        for nam, path in zip(['raw', 'fmt', 'tmb'], [path_raw, path_fmt, path_tmb]):
            if not os.path.isfile(path):
                raise Exception(
                    f'{nam} figure does not exist. Path: {path}'
                )
        width_tmb, height_tmb = Image.open(path_raw).size
        aspect_tmb = float(height_tmb) / width_tmb
        info_photo = ({kw.path_raw:path_raw,
                       kw.path_tmb:path_tmb,
                       kw.aspect_tmb:aspect_tmb})

        line = fmt.img_src.format(cls=cls,
                                  url=path_raw.replace(const.dir_top, const.url),
                                  src=path_fmt.replace(const.dir_top, const.url))

        return line, info_photo
    

    # Download the image
    if os.path.isfile(path_raw):
        print(f'[{proc}] raw fig. exists.')
    else:
        print('f[{proc}] Downloading.')
        subprocess.call(('wget', '-O', path_raw, url))
        #subprocess.call(('wget', '-nv', url, '-O', '{}'.format(path_raw)))
        if not os.path.isfile(path_raw):
            raise Exception(f'Downloading failed: {path_raw}')
        elif os.path.getsize(path_raw) == 0:
            os.remove(path_raw)
            raise Exception(f'Downloaded file is empty: {path_raw}')
        else:
            print(f'[{proc}] Successfully downloaded.')

    width_raw, height_raw = Image.open(path_raw).size
    size_raw = width_raw * height_raw

    # Check if need to resize
    needToResize = True
    if os.path.isfile(path_fmt):
        width_now, height_now = Image.open(path_fmt).size
        size_now = width_now * height_now
        if size_now == size_fmt:
            print(f'[{proc}] fmt fig. exists.')
            needToResize = False

    # Resize
    if needToResize:
        if size_raw > size_fmt:
            coef = (float(size_fmt) / size_raw)**0.5
            width_fmt  = Decimal(str(width_raw *coef)).quantize(Decimal('0'), ROUND_HALF_UP)
            height_fmt = Decimal(str(height_raw*coef)).quantize(Decimal('0'), ROUND_HALF_UP)

            img = Image.open(path_raw)
            img.thumbnail((width_fmt,height_fmt), Image.ANTIALIAS)
            img.save(path_fmt, extension_fmt.replace('.',''))
            print(f'[{proc}] path_fmt: {path_fmt.replace(const.dir_top,"")}')
            print(f'[{proc}]   (width, height) raw: ({width_raw}, {height_raw}), '\
                  f'fmt: ({width_fmt}, {height_fmt})')
        else:
            if not os.path.isfile(path_fmt):
                img = Image.open(path_raw)
                width_now, height_now = img.size
                img.save(path_fmt, extension_fmt.replace('.',''))
                print(f'[{proc}] path_fmt: {path_fmt}')
                print(f'[{proc}]   (width, height) raw: ({width_raw}, {height_raw}), '\
                      f'fmt: ({width_now}, {height_now})')

    if dirName == const.category_Photos:
        # Check if need to make thumbnail
        needToMakeThumbnail = True
        if os.path.isfile(path_tmb):
            width_tmb, height_tmb = Image.open(path_tmb).size
            width_tmb_this, height_tmb_this = \
                calc_size_thumbnail(width_raw, height_raw, width_tmb_max, height_tmb_max)

            if (width_tmb <= width_tmb_this or height_tmb <= height_tmb_this) and\
                    width_tmb <= width_tmb_max or height_tmb <= height_tmb_max:
                print(f'[{proc}] tmb fig. exists.')
                needToMakeThumbnail = False

        # Make thumbnail
        if needToMakeThumbnail:
            img_tmb = Image.open(path_raw)
            width_tmb, height_tmb = \
                calc_size_thumbnail(width_raw, height_raw, width_tmb_max, height_tmb_max)
            img_tmb.thumbnail((width_tmb,height_tmb), Image.ANTIALIAS)
            img_tmb.save(path_tmb, extension_fmt.replace('.',''))

            print(f'[{proc}]  path_tmb: {path_tmb.replace(const.dir_top,"")}')
            print(f'[{proc}]    (width, height) raw: ({width_raw}, {height_raw}), '\
                  f'tmb: ({width_tmb}, {height_tmb})')

        aspect_tmb = float(height_tmb) / width_tmb

        info_photo = ({kw.path_raw:path_raw,
                       kw.path_tmb:path_tmb,
                       kw.aspect_tmb:aspect_tmb})
    else:
        info_photo = None

    line = fmt.img_src.format(cls=cls,
                              url=path_raw.replace(const.dir_top, const.url),
                              src=path_fmt.replace(const.dir_top, const.url))

    return line, info_photo
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def format_page_head(title):
    line = f'\
<!DOCTYPE html>\n\
<html>\n\
<head>\n\
  <title>{title}</title>\n\
  <meta name="viewport" content="width=device-width">\n\
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\
  <meta http-equiv="Content-Style-Sheet" content="text/css">\n\
  <link rel="icon" href="{const.url}/img/icon/favicon_03-5.ico" />\n\
  <link rel="stylesheet" type="text/css" href="{const.url}/css/common.css" media="all">\n\
  <link rel="stylesheet" type="text/css" href="{const.url}/css/src/common.css" media="all">\n\
'
    for language in const.extension.keys():
        f_css = get_f_css_src(language)
        if not os.path.isfile(f_css): continue
        line += f'\
  <link rel="stylesheet" type="text/css" href="{const.url}/{f_css}" media="all">\n\
'

    line += '\
  <script type="text/javascript" src="{const.url}/js/highlight.min.js"></script>\n\
  <script>hljs.highlightAll();</script>\n\
  <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n\
</head>\n\
\n'

    return [line]
#===============================================================
#
#===============================================================
def format_page_body_tag_begin():
    line = '\
<body>\n\
'
    return [line]
#===============================================================
#
#===============================================================
def format_page_body_title(title):
    line = f'\
  <!-- Title -->\n\
  <ul class=\'indexBox\'>\n\
    <div class=\'title\'>\n\
      {title}\n\
    </div>\n\
  </ul>\n\
'

    return [line]
#===============================================================
#
#===============================================================
def format_page_body_route(dirName, route):
    line_route = \
    f'&gt; <u><a href="{const.url_page}/{dirName}/index{const.ext_platform}.html">{dirName}</a></u>\n'

    for rt in route:
        line_route += ' &gt; ' + rt

    line = f'\
  <!-- Route -->\n\
  <ul class=\'indexBox\'>\n\
    <div class=\'route\'>\n\
      <u><a href="{const.url}/index{const.ext_platform}.html">Top</a></u>\n\
      {line_route}\n\
    </div>\n\
  </ul>\n'

    return [line]
#===============================================================
#
#===============================================================
def format_page_body_tag_end():
    line = '\
</body>\n\
</html>\n\
'
    return [line]
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def format_content_lastUpdate(lines):
    proc = sys._getframe().f_code.co_name

    lines_fmt = []

    lines_fmt.append("<div class='lastUpdate'>")
    lines_fmt += [line.rstrip() for line in lines]
    lines_fmt.append("</div>")

    return lines_fmt
#===============================================================
#
#===============================================================
def format_content_inlines(line_in, iLine, remove_inlines=False):
    proc = sys._getframe().f_code.co_name

    def raise_error_for_title(nam_inline):
        raise Exception(
            f'Unexpected type of inline tag "{nam_inline}" was used for page title. '\
            f'line_in: {line_in}'
        )

    line = line_in
    #print('[{}] input: {}'.format(proc, line))

    #mathjax_empty = '/w{\(\)}'

    # Replace inline mathjax with '/w{\(\)}'
    #contents_mathjax = []
    #loc_mathjax_right = 0
    #while '\(' in line[loc_mathjax_right:]:
    #    loc_mathjax_left  = line[loc_mathjax_right:].index('\(') + loc_mathjax_right
    #    loc_mathjax_right = line[loc_mathjax_right:].index('\)') + loc_mathjax_right
    #    contents_mathjax.append(line[loc_mathjax_left+2:loc_mathjax_right])
    #    line = line[:loc_mathjax_left] + mathjax_empty + line[loc_mathjax_right+2:]
    #    loc_mathjax_right = loc_mathjax_left + len(mathjax_empty)
    #    #print('[{}] mathjax: {}'.format(proc, contents_mathjax[-1]))
    #print('[{}] line: {}'.format(proc, line))

    # Format inlines
    def iInline_tag(line, loc0):
        line_this = line[loc0:]
        #print(f'0 line_this: {line_this}')
        while '/' in line_this and '{' in line_this:
            #print(f'1 line_this: {line_this}')
            loc0_slash = line_this.index('/')
            if '{' not in line_this[loc0_slash+1:]:
                break
            inline_nam = line_this[loc0_slash+1:line_this[loc0_slash+1:].index('{')+loc0_slash+1]
            #print(f'inline_nam: {inline_nam}')

            for iInline, inline in enumerate(inlines):
                if inline[kw.inline_nam] == inline_nam:
                    #print(f'inline nam: {inline_nam} tag: {inline[kw.inline_tag]}')
                    #print(line_this)
                    return iInline

            line_this = line_this[loc0_slash+1:]
            #print('2 line_this: {}'.format(line_this))

        return None

    counter = 0
    loc0 = 0
    while True:
        counter += 1
        iInline = iInline_tag(line, loc0)
        if iInline is None: break

        nam_inline = inlines[iInline][kw.inline_nam]
        cls_inline = inlines[iInline][kw.inline_cls]

        head_inline = '/' + nam_inline + '{'
        loc_inline_left = line.index(head_inline)
        loc0 = loc_inline_left + len(head_inline)
        depth = 1

        while depth > 0:
            left_exist  = '{' in line[loc0:]
            right_exist = '}' in line[loc0:]

            if not right_exist:
                raise Exception(f'Invalid syntax @ line {iLine+1}: \n{line}')

            loc_bracket_right = line[loc0:].index('}') + loc0

            if left_exist:
                loc_bracket_left = line[loc0:].index('{') + loc0
                is_left = loc_bracket_left < loc_bracket_right
            else:
                is_left = False

            if is_left:
                depth += 1
                loc0 = loc_bracket_left + 1
            else:
                depth -= 1
                loc0 = loc_bracket_right + 1
            #print('[{}] depth: {} line: {}'.format(proc, depth, line[loc0:]))

        loc_inline_right = loc0
        content = line[loc_inline_left+len(head_inline):loc_inline_right-1]
        #print('[{}] content: {}'.format(proc, content))

        if is_inline_single_decoration(nam_inline):
            if remove_inlines:
                inline_formatted = content
            else:
                inline_formatted = get_line_single_decoration(cls_inline, content)

        elif is_inline_single_id(nam_inline):
            if remove_inlines:
                raise_error_for_title(nam_inline)
            else:
                inline_formatted = get_line_single_id(content)

        elif is_inline_double_link(nam_inline):
            if remove_inlines:
                raise_error_for_title(nam_inline)
            else:
                try:
                    loc_url_left = line[loc0:].index('{') + loc0
                    loc_url_right = line[loc0:].index('}') + loc0
                except ValueError as e:
                    raise Exception(f'ValueError: {e} \n{line}')

                url = line[loc_url_left+1:loc_url_right]
                inline_formatted = get_line_double_link(cls_inline, url, content)
                loc_inline_right = loc_url_right + 1

        elif is_inline_double_id(nam_inline):
            if remove_inlines:
                raise_error_for_title(nam_inline)
            else:
                try:
                    loc_tid_left = line[loc0:].index('{') + loc0
                    loc_tid_right = line[loc0:].index('}') + loc0
                except:
                    raise Exception(f'Failed to get parentheses of tid.\n{line}')

                tid = line[loc_tid_left+1:loc_tid_right]
                inline_formatted = get_line_double_id(tid, content)
                loc_inline_right = loc_tid_right + 1

        else:
            raise Exception(f'`nam_inline` "{nam_inline}" matched nothing. line: \n{line}')

        line = line[:loc_inline_left] + inline_formatted + line[loc_inline_right:]
        loc0 = loc_inline_left
        #print('[{}] inline_formatted: {}'.format(proc, inline_formatted))

        if counter == 20:
            raise Exception('The number of inlines tags exceeded the upper limit.')

    #for content in contents_mathjax:
    #    line = line.replace('\(\)','\('+content+'\)',1)

    return line
#===============================================================
#
#===============================================================
def format_content_src(lines_src:list, language:str, ext: str):
    if language is None:
        line = f'<pre><code>'
    else:
        line = f'<pre><code class="language-{language}">'

    #for l in lines_src:
    #    line += l + '\n'

    if ext is None:
        ext = const.extension[language]

    f_src = f'tmp/tmp.{ext}'
    f_html = f'tmp/tmp.{ext}.html'

    with open(f_src, 'w') as fp:
        for l in lines_src:
            fp.write(l + '\n')

    cp = subprocess.run(
      f'vim -c ":TOhtml | :w! {f_html} | :q! | :q" {f_src}',
      shell=True,
    )

    lhtml = open(f_html, 'r').readlines()

    # lhtml_style 0: pre {...}, 1: body {...}, 2: * { font-size ... }
    lhtml_style = lhtml[lhtml.index('<style>\n')+2:lhtml.index('</style>\n')-1][3:]
    lhtml_body = lhtml[lhtml.index("<pre id='vimCodeElement'>\n")+1:lhtml.index("</pre>\n")]

    # read style
    lst_className_short = []
    for l in lhtml_style:
        className = l.split()[0][1:]
        is_ok = False
        if language in className:
            if className.index(language) == 0:
                is_ok = True
        if not is_ok:
            lst_className_short.append(className)
            className = language + className

        style = l[l.index('{'):l.index('}')+1]

        if className not in vimStyle[language].keys():
            vimStyle_notfound[language][className] = style

    # modify class names in body
    for i, l in enumerate(lhtml_body):
        if f'<span class="' not in l: continue
        is_ok = False
        while not is_ok:
            is_ok = True
            for cshort in lst_className_short:
                key = f'<span class="{cshort}">'
                if key in l:
                    is_ok = False
                    loc = l.index(key)
                    l = l[:loc] + f'<span class="{language}{cshort}">' + l[loc+len(key):]
        lhtml_body[i] = l
    
    for l in lhtml_body:
        line += l

    line += '</code></pre>'

    return line
#===============================================================
#
#===============================================================
def format_content_table(lines, iLine0, write_head, nLines_format_cell):
    proc = sys._getframe().f_code.co_name

    def get_cols(line):
        cols = []

        loc = 0
        loc_now = 0
        #print('[{}] len(line): {}'.format(proc, len(line)))
        while '|' in line[loc_now:]:
            #print('[{}] loc: {} loc_now: {} line: {}'.format(proc, loc, loc_now, line[loc_now:]))
            if '\|' in line[loc_now:]:
                loc_div = line[loc_now:].index('|')
                loc_esc = line[loc_now:].index('\|')
                #print('[{}] loc_div: {} loc_esc: {}'.format(proc, loc_div, loc_esc))
                if loc_div < loc_esc:
                    cols.append(line[loc:loc_now+loc_div])
                    #print('[{}] append "{}"'.format(proc, line[loc:loc_now+loc_div]))
                    loc = loc_now + loc_div + 1
                loc_now += loc_div + 1
                #print('[{}] loc_now: {} line: {}'.format(proc, loc_now, line[loc_now:]))
                if loc_now == len(line) or '|' not in line[loc_now:]:
                    cols.append(line[loc:])
            else:
                #print('[{}] line: {}'.format(proc, line[loc:]))
                cols.append(line[loc:loc_now] + line[loc_now:].split('|')[0])
                if len(line[loc_now:].split('|')) > 1:
                    cols += line[loc_now:].split('|')[1:]
                break
        for i in range(len(cols)):
            while ('\|') in cols[i]:
                cols[i] = cols[i].replace('\|', '|')
        #print('[{}] {} {}'.format(proc, len(cols), cols))

        if nCols is not None:
            if len(cols) != nCols:
                raise Exception(
                    f'@ line {iLine}; The number of contents mismatch. nCols: {nCols}\n'\
                    f'{lines[iLine].rstrip()}'\
                    f'{cols}'
                )

        return cols

    def remove_empty_lines(lines_in):
        lines = []
        for line in lines_in:
            if len(line.strip()) == 0:
                continue
            elif line.strip()[0] == '#':
                continue
            else:
                lines.append(line)
        return lines

    lines = remove_empty_lines(lines)
    nLines = len(lines)
    if nLines == 0:
        return []

    iLine = nLines_format_cell
    nCols = None

    # Get formats
    widths = None
    aligns = None
    wraps  = None
    classes = None

    if nLines_format_cell > 0:
        nComps_widths = 0
        nComps_aligns = 0
        nComps_wraps = 0
        nComps_classes = 0

        for iLine_format in range(nLines_format_cell):
            comps = lines[iLine_format].strip().split()
        tag = comps[0]

        if tag == const.table_tag_width:
            widths = comps[1:]
            nComps_widths = len(widths)
        elif tag == const.table_tag_align:
            aligns = comps[1:]
            nComps_aligns = len(aligns)
        elif tag == const.table_tag_wrap:
            wraps = comps[1:]
            nComps_wraps = len(wraps)
        elif tag == const.table_tag_class:
            classes = comps[1:]
            nComps_classes = len(classes)
        else:
            print('*** {} ***'.format(proc))
            raise Exception(
                f'@ line {iLine-1}; Unknown tag "{tag}"\n'\
                f'{lines[iLine]}'
            )

        nComps_max = max(nComps_widths, nComps_aligns, 
                         nComps_wraps, nComps_classes)

        list_nComps = [nComps_widths, nComps_aligns, 
                       nComps_wraps, nComps_classes]
        is_ok = all([n == 0 or n == max(list_nComps) for n in list_nComps])
        if not is_ok:
            quit()

    # Get nCols
    cols = get_cols(lines[iLine])
    iLine += 1
  
    nCols = len(cols)

    # Fotmat widths
    if widths is None:
        widths = [''] * nCols
    else:
        for i in range(nCols):
            if widths[i] == const.table_fmt_miss:
                widths[i] = ''
            else:
                widths[i] = 'width:'+widths[i]+'%'

    # Format aligns
    if aligns is None:
        aligns = [''] * nCols
    else:
        for i in range(nCols):
            if aligns[i] == const.table_fmt_miss:
                aligns[i] = ''
            else:
                aligns[i] = ' align="{}"'.format(aligns[i])

    # Format wraps
    if wraps is None:
        wraps = [['','']] * nCols
    else:
        for i in range(nCols):
            if wraps[i] == const.table_fmt_miss:
                wraps[i] = ['','']
            else:
                wraps[i] = ['/'+wraps[i]+'{','}']

    # Format classes
    if classes is None:
        classes = [''] * nCols
    else:
        for i in range(nCols):
            if classes[i] == const.table_fmt_miss:
                classes[i] = ''
            else:
                classes[i] = ' class="{}"'.format(classes[i])

    lines_fmt = []

    lines_fmt.append('<table border="1" class="std">')
    lines_fmt.append('  <colgroup>')
    for width in widths:
        lines_fmt.append(f'    <col style="{width}">')
    lines_fmt.append('  </colgroup>')

    lines_fmt.append('  <tr>')

    iLine = nLines_format_cell

    # Write the head
    if write_head:
        cols = get_cols(lines[iLine])
        iLine += 1
        for col, wrap in zip(cols, wraps):
            lines_fmt.append(    '<th>{col}</th>'.format(
                             col=format_content_inlines(
                               wrap[0]+col.strip()+wrap[1],iLine0+iLine)))
        lines_fmt.append('  </tr>')
        lines_fmt.append('  <tr>')

    # Write the contents
    while iLine < nLines:
        cols = get_cols(lines[iLine])
        iLine += 1
        for col, align, wrap in zip(cols, aligns, wraps):
            lines_fmt.append('    <td{align}>{col}</td>'.format(
              align=align, 
              col=format_content_inlines(wrap[0]+col.rstrip()+wrap[1],iLine0+iLine)
            ))
        lines_fmt.append('  </tr>')
        lines_fmt.append('  <tr>')

    del(lines_fmt[-1])

    lines_fmt.append('</table>')

    return lines_fmt
#===============================================================
#
#===============================================================
def format_content_img(
    lines_raw: list, dir_img_this: str, dirName: str, toBeUpdated: bool
) -> None:

    proc = sys._getframe().f_code.co_name

    #url_img_parent = dir_img_this.replace(const.dir_page, const.url_page)
    url_img_parent = dir_img_this.replace(const.dir_page_base, const.url_page_base)

    lines_fmt = []
    info_photos = []

    line_this = ''
    for iLine, line in enumerate(lines_raw):
        if len(line) == 0:
            continue
        elif line.strip()[0] == '"':
            raise Exception(
                f'Invalid format of line @ {iLine+1}\n'+
                line
            )

        line_this += line.strip()

        if line.strip()[-1] == ',':
            continue
        else:
            line = line_this
            line_this = ''

        #print('[{}] line: {}'.format(proc, line))
        #-------------------------------------------------------
        # Divide by double quotes
        #-------------------------------------------------------
        loc0 = 0
        locs = [-1]
        while '"' in line[loc0:]:
            loc = line[loc0:].index('"') + loc0
            if '\\"' in line[loc0:]:
                loc_escape = line[loc0:].index('\\"') + loc0
                #print('[{}] loc: {}, loc_escape: {}'.format(proc, loc, loc_escape))
                if loc_escape != loc-1:
                    locs.append(loc)
            else:
                locs.append(loc)
            loc0 = loc + 1

            if loc0 == len(line)-1:
                locs.append(loc0)
                break
        #-------------------------------------------------------
        # Read keys and values
        #-------------------------------------------------------
        url = None
        url_drive = None
        fid = None
        cls = None
        ext_drive = None
        caption = None

        key = None
        is_first = True
        for loc0, loc1 in zip(locs[:-1], locs[1:]):
            content = line[loc0+1:loc1].strip()
            #print('[{}] content: {}'.format(proc, content))

            if key is None:
                if content[0] == ',':
                    if is_first:
                        raise Exception(
                            f'@ line {iLine+1}; Comma is at the head of the line.'\
                            f'{line}'
                        )
                    content = content[1:].strip()
                is_first = False

                found = False
                for key in [const.img_kw_url, const.img_kw_drv, const.img_kw_fid,
                            const.img_kw_cls, const.img_kw_ext, const.img_kw_cpt]:
                    if key in content:
                        if content.index(key) == 0:
                            found = True
                            break

                if not found:
                    print('*** {} ***'.format(proc))
                    print('Key was not found in line @ {}:'.format(iLine+1))
                    print('{}'.format(line))
                    print('Content: {}'.format(content))
                    quit()

                if content.replace(key,'').strip()[0] != '=':
                    print('*** {} ***'.format(proc))
                    print('Invalid format of line @ {}:'.format(iLine+1))
                    print('{}'.format(line))
                    print('Content: {}'.format(content))
                    print('Key: {}'.format(key))
                    quit()

                continue

            val = content
            print('[{}] key: {}'.format(proc, key))

            if key == const.img_kw_url:
                if url is not None or url_drive is not None:
                    print('*** {} ***'.format(proc))
                    print(('Key "{}" was found but "url" and "url_drive" were already specified'\
                           ' @ line {}')\
                          .format(key, iLine+1))
                    print('Line: {}'.format(line))
                    quit()
                url = val.replace('${img}', url_img_parent)

            elif key == const.img_kw_drv:
                if url is not None or url_drive is not None:
                    print('*** {} ***'.format(proc))
                    print(('Key "{}" was found but "url" and "url_drive" were already specified'\
                           ' @ line {}')\
                          .format(key, iLine+1))
                    print('Line: {}'.format(line))
                    quit()
                url_drive = val

            elif key == const.img_kw_fid:
                if fid is not None:
                    print('*** {} ***'.format(proc))
                    print('Key "{}" was found but already specified.'.format(key))
                    print('Line: {}'.format(line))
                    quit()
                fid = val

            elif key == const.img_kw_cls:
                if cls is not None:
                    print('*** {} ***'.format(proc))
                    print('Key "{}" was found but already specified.'.format(key))
                    print('Line: {}'.format(line))
                    quit()
                cls = val

            elif key == const.img_kw_ext:
                if ext_drive is not None:
                    print('*** {} ***'.format(proc))
                    print('Key "{}" was found but already specified.'.format(key))
                    print('Line: {}'.format(line))
                    quit()
                ext_drive = val

                if ext_drive not in const.img_exts:
                    print('*** {} ***'.format(proc))
                    print('Invalid extension of image in drive: {}'.format(ext_drive))
                    print('Line: {}'.format(line))
                    quit()

            elif key == const.img_kw_cpt:
                caption = val

            else:
                print('*** {} ***'.format(proc))
                print('Invalid key: {}'.format(key))
                print('Line: {}'.format(line))
                quit()

            # Reset.
            key = None
        #-------------------------------------------------------
        # Format lines
        #-------------------------------------------------------
        if url is None and url_drive is None:
            print('*** {} ***'.format(proc))
            print('Neither url or url_drive was not specified:')
            print(line)
            quit()

        if cls is None:
            if dirName == const.category_Photos:
                cls = const.img_cls_mw100
            else:
                cls = const.img_cls_mw50

        if url is not None:
            lines_fmt.append(fmt.img_src.format(cls=cls, url=url, src=url))

        elif url_drive is not None:
            if ext_drive is None:
                ext_drive = const.img_ext_drive_default
            line_fmt, info_photo = get_image_from_drive(
                cls, url_drive, fid, ext_drive, dir_img_this,
                dirName, toBeUpdated,
            )
            lines_fmt.append(line_fmt)
            info_photos.append(info_photo)

        if caption is not None:
            lines_fmt.append(fmt.img_caption.format(\
                             caption=format_content_inlines(caption,iLine)))

    return lines_fmt, info_photos
#===============================================================
#
#===============================================================
def format_content_body_main(
    path_raw: str, comp: list, dirName: str, toBeUpdated: bool
) -> (list, list):

    proc = sys._getframe().f_code.co_name
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    def remove_inline_mathjax(line):
        contents_mathjax = []
        loc_mathjax_right = 0
        while '\\(' in line[loc_mathjax_right:]:
            if '\\\\(' in line[loc_mathjax_right:]:
                loc_mathjax_left_cancel = line[loc_mathjax_right:].index('\\\\(') + loc_mathjax_right
            else:
                loc_mathjax_left_cancel = 0
            loc_mathjax_left  = line[loc_mathjax_right:].index('\\(') + loc_mathjax_right
            loc_mathjax_right = line[loc_mathjax_right:].index('\\)') + loc_mathjax_right

            if loc_mathjax_left_cancel == loc_mathjax_left - 1:
                loc_mathjax_right = loc_mathjax_left_cancel + 3
                continue

            contents_mathjax.append(line[loc_mathjax_left+2:loc_mathjax_right])
            line = line[:loc_mathjax_left] + mathjax_empty + line[loc_mathjax_right+2:]
            loc_mathjax_right = loc_mathjax_left + len(mathjax_empty)

        return line, contents_mathjax

    def insert_inline_mathjax(line, contents_mathjax):
        if len(contents_mathjax) == 0:
            return line

        for content in contents_mathjax:
            line = line.replace('\(\)','\('+content+'\)',1)

        return line
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    def get_words_replace(line, iLine):
        proc = sys._getframe().f_code.co_name

        words = line.strip().split()

        if len(words) != 2:
            raise Exception(
              'Invalid num. of comps. @ line {}\n'.format(iLine)+
              line.strip())

        return words
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    def replace_words(line, block=''):
        proc = sys._getframe().f_code.co_name

        if len(replaced.replaced) == 0:
            return line

        if rplc not in line:
            return line

        if block == const.blockName_math:
            if kw.inline_tag in line:
                loc0_tag = line.index(kw.inline_tag)
                loc1_tag = line[loc0_tag:].index('}') + loc0_tag

                tag = line[loc0_tag+len(kw.inline_tag)+1:loc1_tag+1]
                #print('[{}] loc_tag: {}, loc1_tag: {}'.format(proc, loc0_tag, loc1_tag))
                #print('[{}] tag: {}'.format(proc, tag))

                tag_new = replace_words_core(tag)
                line = line[:loc0_tag+len(kw.inline_tag)+1] + tag_new + line[loc1_tag+1:]

        else:
            line = replace_words_core(line)

        return line

    def replace_words_core(line):
        proc = sys._getframe().f_code.co_name

        while rplc in line:
            #print('[{}] {}'.format(proc, line))
            loc0_rplc = line.index(rplc)
            loc0 = loc0_rplc + len(rplc)
            depth = 1
            while depth > 0:
                if '{' in line[loc0:]:
                    loc_pl = line[loc0:].index('{') + loc0
                else:
                    loc_pl = len(line)
                if '}' in line[loc0:]:
                    loc_pr = line[loc0:].index('}') + loc0
                else:
                    raise Exception(
                      f'Parenthesis for "{rplc}" is not closed')
                if loc_pl < loc_pr:
                    depth += 1
                    loc0 = loc_pl + 1
                else:
                    depth -= 1
                #print('[{}] depth: {} loc_pl: {} loc_pr: {}'.format(proc, depth, loc_pl, loc_pr))
            loc1_rplc = loc_pr
            #print('[{}] rplc loc0: {}, loc1: {}'.format(proc, loc0_rplc, loc1_rplc))
            content_old = line[loc0_rplc+len(rplc):loc1_rplc]

            found = False
            for chunk in replaced.replaced:
                if content_old == chunk[0]:
                    content_new = chunk[1]
                    found = True
                    break
            if not found:
                raise Exception(
                  f'Keyword "{content_old}" not found in the list for replacement.\n'+
                  'Line:\n'+
                  line)
            #print('[{}] old: {}'.format(proc, content_old))
            #print('[{}] new: {}'.format(proc, content_new))
            
            line = line[:loc0_rplc] + content_new + line[loc1_rplc+1:]
        return line
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    def replace_punctuation_marks(line):
        line = line.replace('。', '．').replace('、', '，')
        return line
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    #print('[{}] dirName: {}'.format(proc, dirName))

    lines_fmt = []
    info_photos = []

    dir_raw_contents = get_dir_raw_contents(dirName)
    #[removed]
    #dir_src_this = get_dir_src_this(path_raw, dir_raw_contents, dirName)
    dir_img_this = get_dir_img_this(path_raw, dir_raw_contents, dirName)

    #[removed]
    #if not os.path.isdir(dir_src_this):
    #    print('[{}] mkdir -p {}'.format(proc, dir_src_this))
    #    os.makedirs(dir_src_this)

    if not os.path.isdir(dir_img_this):
        print('[{}] mkdir -p {}'.format(proc, dir_img_this))
        os.makedirs(dir_img_this)

    mathjax_empty = '/w{\(\)}'
    rplc = '/' + const.inline_replace + '{'

    lines_lastUpdate = []
    lines_src = []
    lines_img = []
    lines_table = []
    lines_math = []

    depth = 1
    blockName = None
    blockNames = []
    blockStatus = None

    flag_block_src_end = False
    flag_block_math_end = False
    flag_nobr_closed = True

    refStatus_prev = None

    lines_fmt.append("<!-- Contents -->")
    lines_fmt.append("<ul class='contentBox'>")

    nLinesInBlock = 0

    print('[{}] Formatting {}'.format(proc, path_raw))
    lines_raw = open(path_raw,'r').readlines()

    for iLine, line in enumerate(lines_raw):
        line = line.rstrip()
        #-------------------------------------------------------
        # Get block name and update status
        #-------------------------------------------------------
        comps = line.strip().split()

        if len(comps) >= 2 and comps[0] == '##':

            # Block ends
            if comps[1][-1] == '/':
                #print(line, comps)
                check_block_end(iLine, blockName, comps[1][:-1])
                blockName = comps[1][:-1]
                blockStatus = const.blockStatus_end
                #print('[{}] Block "{}" closed @ line {}'.format(proc, blockName,iLine+1))

            # Block begins
            else:
                if blockStatus in [const.blockStatus_in, const.blockStatus_begin]:
                    check_block_begin(iLine, blockName, comps[1])
                blockName = comps[1]
                blockStatus = const.blockStatus_begin
                #print('[{}] Block "{}" opened @ line {}'.format(proc, blockName,iLine+1))

                if blockName == const.blockName_src:
                    if len(comps) > 4:
                        raise Exception(
                            f'Too many components @ line {iLine}:\n'
                            f'{str(comps)}'
                        )
                    src_language = comps[2] if len(comps) >= 3 else None
                    ext_language = comps[3] if len(comps) >= 4 else None

                elif blockName == const.blockName_table:
                    table_head = False
                    table_nLines_format_cell = 0
                    table_margin = None
                    if len(comps) > 2:
                        for comp in comps[2:]:
                            if comp == const.table_opt_head:
                                table_head = True
                            elif comp.split('=')[0] == const.table_opt_format_cell:
                                table_nLines_format_cell = int(comp.split('=')[1])
                            else:
                                raise Exception(
                                  'Invalid option of table: {}'.format(comp))
        else:
            if len(line) > 0:
                if blockName != const.blockName_src:
                    if line[0] == '#': continue
        #-------------------------------------------------------
        # Format lines and add to the list
        #-------------------------------------------------------
        if blockStatus is None:
            continue

        #print('[{}] block Name: {}, Status: {}'.format(proc, blockName, blockStatus))
        #-------------------------------------------------------
        # Case: Block begins
        if blockStatus == const.blockStatus_begin:
            nLinesInBlock = 0

            if blockName in const.blockNames:
                if blockName == const.blockName_ref:
                    lines_fmt.append("</ul>")
                    lines_fmt.append("")
                    lines_fmt.append("<!-- References -->")
                    lines_fmt.append("<ul class='contentBox'>")
                    lines_fmt.append("<div class='index'>References</div>")

                depth += 1
                lines_fmt.append("<div class='{}'>".format(blockName))
                blockNames.append(blockName)

            blockStatus = const.blockStatus_in
        #-------------------------------------------------------
        # Case: Block ends and new block begins
        elif blockStatus == const.blockStatus_end:
            if flag_block_math_end:
                s = '</nobr></div>'  # put nobr on the head of the new line
                flag_nobr_closed = True
                flag_block_math_end = False
            else:
                s = ''

            nLinesInBlock = 0
            if blockName in const.blockNames:
                lines_fmt.append(s + '</div>')
                del blockNames[-1]
                depth -= 1

            elif blockName in const.blockNames_special:
                if blockName == const.blockName_lastUpdate:
                    lines_fmt += format_content_lastUpdate(lines_lastUpdate)
                    lines_lastUpdate = []

                elif blockName == const.blockName_src:
                    lines_fmt += [s + format_content_src(lines_src, src_language, ext_language)]
                    lines_src = []
                    flag_block_src_end = True

                elif blockName == const.blockName_table:
                    lines_table = format_content_table(
                                    lines_table, iLine-len(lines_table), 
                                    table_head, table_nLines_format_cell)
                    lines_table[0] = s + lines_table[0]
                    lines_fmt += lines_table
                    lines_table = []

                elif blockName == const.blockName_img:
                    lines_img, info_photos_add \
                      = format_content_img(lines_img, dir_img_this, dirName, toBeUpdated)
                    lines_img[0] = s + lines_img[0]
                    lines_fmt += lines_img
                    info_photos.append(info_photos_add)
                    lines_img = []

                elif blockName == const.blockName_math:
                    lines_math[0] = s + '<div class=\'mathjax\'><nobr>' + lines_math[0]
                    lines_fmt += lines_math
                    lines_math = []
                    flag_block_math_end = True
                    flag_nobr_closed = False

            if len(blockNames) > 0:
                blockName = blockNames[-1]
                blockStatus = const.blockStatus_in
            else:
                blockName = None
                blockStatus = None
        #-------------------------------------------------------
        # Case: Block continues
        elif blockStatus == const.blockStatus_in:

            if blockName is None:
                raise Exception('Block name is empty.')

            elif blockName in const.blockNames:

                nLinesInBlock += 1

                if blockName == const.blockName_index:
                    if nLinesInBlock > 1:
                        lines_fmt[-1] += '<br>'
                    line, contents_mathjax = remove_inline_mathjax(line)
                    line = replace_words(line, blockName)
                    line = format_content_inlines(line, iLine)
                    line = insert_inline_mathjax(line, contents_mathjax)
                    lines_fmt.append(line)

                elif blockName == const.blockName_contents:
                    if flag_block_math_end:
                        s = '</nobr></div>'
                        flag_nobr_closed = True
                        flag_block_math_end = False
                    else:
                        s = ''

                    line, contents_mathjax = remove_inline_mathjax(line)
                    line = replace_words(line, blockName)
                    line = replace_punctuation_marks(line)
                    line = format_content_inlines(line, iLine)
                    line = insert_inline_mathjax(line, contents_mathjax)

                    # Ignore one empty line after source block
                    if flag_block_src_end:
                        lines_fmt[-1] += s + line
                    else:
                        lines_fmt.append(s + line)
                    flag_block_src_end = False

                elif blockName == const.blockName_ref:

                    if len(line) == 0:
                        continue

                    # Title
                    elif refStatus_prev == const.refStatus_link or refStatus_prev is None:
                        if refStatus_prev is not None:
                            lines_fmt.append('')
                        lines_fmt.append(format_content_inlines(line, iLine))
                        refStatus_prev = const.refStatus_title

                    # Link
                    elif refStatus_prev == const.refStatus_title:
                        if line.strip() == '(None)':
                            lines_fmt.append('')
                        else:
                            lines_fmt.append(get_line_ref_link(line, line))
                        refStatus_prev = const.refStatus_link

                else:
                    raise Exception(f'Invalid block name: {blockName}')

            elif blockName in const.blockNames_special:
                if blockName == const.blockName_lastUpdate:
                    lines_lastUpdate.append(line)

                elif blockName == const.blockName_img:
                    line = replace_words(line, blockName)
                    lines_img.append(line)

                elif blockName == const.blockName_src:
                    lines_src.append(line)

                elif blockName == const.blockName_table:
                    line, contents_mathjax = remove_inline_mathjax(line)
                    line = replace_words(line, blockName)
                    line = replace_punctuation_marks(line)
                    line = format_content_inlines(line, iLine)
                    line = insert_inline_mathjax(line, contents_mathjax)
                    lines_table.append(line)

                elif blockName == const.blockName_math:
                    line = replace_words(line, blockName)
                    lines_math.append(line)

                elif blockName == const.blockName_replace:
                    if len(line) == 0: continue
                    replaced.replaced.append(get_words_replace(line, iLine))


        if flag_block_math_end and flag_nobr_closed:
            flag_block_math_end = False

    lines_fmt.append("</ul>")

    depth -= 1

    return lines_fmt, info_photos
#===============================================================
#
#===============================================================
def format_content(dirName, path_raw, comp, toBeUpdated):
    lines = []
    lines += format_page_head(comp[kw.title_index])
    lines += format_page_body_tag_begin()
    lines += format_page_body_title(comp[kw.title])
    lines += format_page_body_route(dirName, comp[kw.route])
    lines_body, info_photos = format_content_body_main(path_raw, comp, dirName, toBeUpdated)
    lines += lines_body
    lines += format_page_body_tag_end()

    return lines, info_photos
#===============================================================
#
#===============================================================
def format_content_Photos_FY(title, comps):
    proc = sys._getframe().f_code.co_name
    #-----------------------------------------------------------
    #
    #-----------------------------------------------------------
    print('[{}] {}'.format(proc, title))

    lines = []
    lines += format_page_head(comps[0][kw.title])
    lines += format_page_body_tag_begin()
    lines += format_page_body_title(comps[0][kw.title])
    lines += format_page_body_route(dirName, comps[0][kw.route])

    lines.append("  <!-- Contents -->")
    lines.append("  <ul class='contentBox'>")
    lines.append("    <div class='{}'>".format(const.blockName_contents))

    for comp in comps:
        if comp[kw.isfile]:
            lines.append(fmt.photos_index.format(
                         url=comp[kw.path_page].replace(const.dir_top,const.url),
                         title=comp[kw.title_index]))
            lines += format_index_body_main_photos_tmb(comp[kw.info_photos])
            lines.append('')

    lines.append("    </div>")
    lines.append("  </ul>")
    lines += format_page_body_tag_end()

    return lines
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def format_index_body_main(comps: list):
    proc = sys._getframe().f_code.co_name

    print('----------------------------------------------------------------')
    print('Making index page')

    lines_fmt = []

    lines_fmt.append("<!-- Contents -->")
    lines_fmt.append("<ul class='indexBox'>")
    lines_fmt.append("<nobr>")
    lines_fmt.append("<div class='parent-contents'>")

    iPage = -1
    n_depth0 = 0

    for comp in comps:
        comp[kw.tree] = ''

    for i, comp in enumerate(comps[:-1]):
        print(f'  Looking "{comp[kw.title_index]}"')
        loc_tree_head = comp[kw.depth]*4+2

        idx_comp_child_youngest = None
        for j, comp_below in enumerate(comps[i+1:]):
            if comp_below[kw.depth] == comp[kw.depth]+1:
                idx_comp_child_youngest = j + i + 1
            elif comp_below[kw.depth] <= comp[kw.depth]:
                break
        if idx_comp_child_youngest is not None:
            print(f'    child_youngest: {comps[idx_comp_child_youngest][kw.title]}')

        for j, comp_below in enumerate(comps[i+1:]):
            if comp_below[kw.depth] == comp[kw.depth]+1:
                comp_below[kw.tree] += ' ├─ '
                if j == idx_comp_child_youngest:
                    for comp_below in comps[idx_comp_child_youngest+1:]:
                        comp_below += '&nbsp;'
                    break
            elif comp_below[kw.depth] <= comp[kw.depth]:
                break
            elif comp_below[kw.depth] > comp[kw.depth]:
                comps[j+i+1][kw.tree] += ' │  '

        if idx_comp_child_youngest is not None:

            # Replace bottom branch
            tree = comps[idx_comp_child_youngest][kw.tree]
            if tree[-4:] == ' ├─ ':
                comps[idx_comp_child_youngest][kw.tree] = tree[:len(tree)-len(' ├─ ')] + ' └─ '
            else:
                comps[idx_comp_child_youngest][kw.tree] = tree[:len(tree)] + ' └─ '

            # Remove isolated branch
            if idx_comp_child_youngest < len(comps):
                for comp_below in comps[idx_comp_child_youngest+1:]:
                    if comp_below[kw.depth] <= comp[kw.depth]:
                        break
                    tree = comp_below[kw.tree]
                    comp_below[kw.tree] = comp_below[kw.tree][:len(tree)-len(' │  ')] + '&nbsp;'*8

    for comp in comps:
        if comp[kw.depth] == 0:
            if n_depth0 > 0:
                lines_fmt.append('')
            n_depth0 += 1

        if comp[kw.isfile]:
            iPage += 1
            lines_fmt.append(fmt.parent_content_url.format(
                             tree=comp[kw.tree],
                             url=comp[kw.path_page].replace(const.dir_top,const.url),
                             title=comp[kw.title_index]))
        elif comp[kw.depth] == 0:
            lines_fmt.append(fmt.parent_content_top.format(
                             tree='',
                             title=comp[kw.title_index]))
        else:
            lines_fmt.append(fmt.parent_content_nourl.format(
                             tree=comp[kw.tree],
                             title=comp[kw.title_index]))

    lines_fmt.append("</div>")
    lines_fmt.append("</nobr>")
    lines_fmt.append("</ul>")

    return lines_fmt
#===============================================================
#
#===============================================================
def format_index_body_main_photos(comps):
    proc = sys._getframe().f_code.co_name

    lines_fmt = []

    lines_fmt.append("<!-- Contents -->")
    lines_fmt.append("<ul class='contentBox'>")
    lines_fmt.append("<div class='contents'>")

    for comp in comps:
        if comp[kw.isfile]:
            lines_fmt.append(fmt.photos_index.format(
                             url=comp[kw.path_page].replace(const.dir_top,const.url),
                             title=comp[kw.title_index]))
            lines_fmt += format_index_body_main_photos_tmb(comp[kw.info_photos])
            lines_fmt.append('')

    lines_fmt.append("</div>")
    lines_fmt.append("</ul>")

    return lines_fmt
#===============================================================
#
#===============================================================
def format_index_body_main_photos_tmb(info_photos_page):
    proc = sys._getframe().f_code.co_name

    lines_fmt = []

    width_tmb_total = 0.0
    widths_tmb, paths_img_raw, paths_img_tmb = [], [], []

    for info_photos in info_photos_page:
        for i, info in enumerate(info_photos):
            #print(info)
            width_tmb = round(const.img_tmb_width_base / info[kw.aspect_tmb])
            width_tmb_total += width_tmb

            widths_tmb.append(width_tmb)
            paths_img_raw.append(info[kw.path_raw])
            paths_img_tmb.append(info[kw.path_tmb])

            #print('  width: {}, total: {}'.format(width_tmb, width_tmb_total))
            if width_tmb_total >= const.img_tmb_width_total_ulim \
                  and width_tmb_total > const.img_tmb_width_total_llim:
                #print('  Reached to the upper limit.')
                #-----------------------------------------------
                # Adjust widths
                #-----------------------------------------------
                width_tmb_total_ulim_raw\
                      = const.img_tmb_width_total_ulim - const.img_tmb_leftMargin*len(widths_tmb)
                coef = width_tmb_total_ulim_raw / width_tmb_total
                width_tmb_total = 0.0
                for i in range(len(widths_tmb[:-1])):
                    widths_tmb[i] = int(round(widths_tmb[i]*coef))
                    width_tmb_total += widths_tmb[i] + const.img_tmb_leftMargin
                widths_tmb[-1] = int(const.img_tmb_width_total_ulim - width_tmb_total)

                line_fmt = ''
                for width_tmb, path_img_raw, path_img_tmb \
                      in zip(widths_tmb, paths_img_raw, paths_img_tmb):
                    line_fmt += fmt.img_tmb.format(
                                cls='thumbnail',
                                url=path_img_raw.replace(const.dir_top, const.url),
                                src=path_img_tmb.replace(const.dir_top, const.url),
                                width=width_tmb)
                lines_fmt.append(line_fmt)

                width_tmb_total = 0.0
                widths_tmb, paths_img_raw, paths_img_tmb = [], [], []

    if len(widths_tmb) > 0:
        line_fmt = ''
        for width_tmb, path_img_raw, path_img_tmb \
              in zip(widths_tmb, paths_img_raw, paths_img_tmb):
            line_fmt += fmt.img_tmb.format(
                        cls='thumbnail',
                        url=path_img_raw.replace(const.dir_top, const.url),
                        src=path_img_tmb.replace(const.dir_top, const.url),
                        width=int(width_tmb))
        lines_fmt.append(line_fmt)

    return lines_fmt
#===============================================================
#
#===============================================================
def format_index(comps: list, dirName: str):
    proc = sys._getframe().f_code.co_name

    title = const.dirNames[const.dirNames.index(dirName)]

    lines = []
    lines += format_page_head(title)
    lines += format_page_body_tag_begin()
    lines += format_page_body_title(title)
    lines += format_page_body_route(dirName, [])
    lines += format_index_body_main(comps)
    lines += format_page_body_tag_end()

    return lines
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def conv_toppage():
    f_in = 'index.html'
    f_out = f'index{const.ext_platform}.html'
    print('----------------------------------------------------------------')
    print(f'Converting {f_in} to {f_out}')

    wf = open(f_out, 'w')
    for line in open(f_in, 'r').readlines():
        is_found = False
        for dirName in const.dirNames:
            if f'page/{dirName}/' in line:
                is_found = True
                break

        if is_found:
            line = line.replace(f'page/{dirName}/', f'page{const.ext_platform}/{dirName}/')

        wf.write(line)
    wf.close()
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def read_index(dirName):
    proc = sys._getframe().f_code.co_name

    f_contents_list = fmt.f_contents_list.format(dirName=dirName)

    route = []
    comps = []
    depth_prev = -1
    print(f'[{proc}] Reading {f_contents_list.replace(const.dir_top+"/","")}')

    for iLine, line in enumerate(open(f_contents_list,'r').readlines()):
        print(line.rstrip())


    for iLine, line in enumerate(open(f_contents_list,'r').readlines()):
        print(line.rstrip())

        # Skip empty line
        if len(line.strip()) == 0: continue

        # Skip comment
        if line.strip()[0] == '#': continue

        line = line.rstrip()

        # Get depth
        depth = 0
        while const.indent_contents_list in line:
            if line.index(const.indent_contents_list) == 0:
                depth += 1
                line = line[len(const.indent_contents_list):]
        if depth > 0:
            if depth > depth_prev+1:
                raise Exception(
                  f'depth > depth_prev+1\n'+\
                  f'depth     : {depth}\n'+\
                  f'depth_prev: {depth_prev}\n'+\
                  line.rstrip())
        depth_prev = depth

        comp = line.strip().split('|')

        if len(comp) not in [2, 3]:
            raise Exception('Invalid number of components.\n'+line.rstrip())

        # Get info.
        title_in = comp[0].strip()
        path     = comp[1].strip()

        title = format_content_inlines(title_in, iLine)
        title_index = format_content_inlines(title_in, iLine, True)

        # Judge if path is file or directory
        file_raw = ''
        if const.ext_raw in path and len(path) > len(const.ext_raw):
            if path[-len(const.ext_raw):] == const.ext_raw:
                file_raw = path
                if '/' in file_raw:
                    file_raw = os.path.basename(path)

        # Get directory
        if file_raw == '':
            dir_path = path
        else:
            if '/' in path:
                dir_path = os.path.dirname(path)
            else:
                dir_path = ''
        if dirName == const.category_Photos:
            if depth == 0:
                dir_path = title

        link_org = None
        link_dst = None
        if len(comp) == 3:
            for opt in [s.strip() for s in comp[2:]]:
                if is_on_head(opt, const.str_contents_list_org):
                    link_org = opt[len(const.str_contents_list_org):]
                elif is_on_head(opt, const.str_contents_list_dst):
                    link_dst = opt[len(const.str_contents_list_dst):]
                else:
                    raise Exception('Invalid pattern of option.\n'+line)
            print(f'[{proc}]  {link_org} -> {link_dst}')

        if depth+1 > len(route):
            route.append('')
        #print(depth, len(route))
        route[depth] = title

        isfile = True
        if file_raw == '':
            isfile = False
        if link_org is not None:
            isfile = True

        comps.append({
            kw.depth      : depth,
            kw.title      : title,
            kw.title_index: title_index,
            kw.path       : path,
            kw.isfile     : isfile,
            kw.dir_path   : dir_path,
            kw.file_raw   : file_raw,
            kw.route      : route[:depth],
            kw.link_org   : link_org,
            kw.link_dst   : link_dst,
        })

    return comps
#===============================================================
#
#===============================================================
def make_all(dirName, overwrite):
    proc = sys._getframe().f_code.co_name

    paths = [None] * const.maxPathDepth
    comps = read_index(dirName)
    #-----------------------------------------------------------
    # Write the content pages
    #-----------------------------------------------------------
    for comp in comps:
        print('----------------------------------------------------------------')
        print('depth: {}'.format(comp[kw.depth]))
        print('path : {}'.format(comp[kw.path]))
        print('title: {}'.format(comp[kw.title]))
        print('dir_path: {}'.format(comp[kw.dir_path]))
        print('file_raw: {}'.format(comp[kw.file_raw]))
        print('link_org: {}'.format(comp[kw.link_org]))
        #-------------------------------------------------------
        # Get directory
        #-------------------------------------------------------
        depth = comp[kw.depth]
        paths[depth] = comp[kw.dir_path]
        dir_this = f'{const.dir_raw}/{dirName}/{const.dirName_contents}'
        for p in paths[:depth+1]:
            dir_this = os.path.join(dir_this,p)

        print(f'[{proc}] Directory: {dir_this.replace(const.dir_top+"/","")}')
        #-------------------------------------------------------
        # Case: Linked by other page
        if comp[kw.link_org] is not None:
            path_page_this = os.path.join(dir_this.replace(const.dir_raw,const.dir_page),
                                          comp[kw.file_raw].replace(const.ext_raw,const.ext_html))
            comp[kw.path_page] = path_page_this

            path_link_org = os.path.join(const.dir_page,comp[kw.link_org])
            if os.path.isfile(path_page_this):
                os.remove(path_page_this)
            os.symlink(path_link_org, path_page_this)
            print(f'[{proc}]  <- {path_link_org.replace(const.dir_top+"/","")}')
        #-------------------------------------------------------
        # Case: Directory
        elif not comp[kw.isfile] :
            dir_page_this = dir_this.replace(const.dir_raw, const.dir_page)
            if not os.path.isdir(dir_page_this):
                print(f'[{proc}] mkdir -p {dir_page_this}')
                os.makedirs(dir_page_this)
            comp[kw.path_page] = None
        #-------------------------------------------------------
        # Case: Page
        else:
            #dir_src_this = dir_this.replace(const.dir_raw,const.dir_page,1)\
            #                       .replace(const.dirName_contents,const.dirName_src,1)
            #dir_img_this = dir_this.replace(const.dir_raw,const.dir_page_base,1)\
            #                       .replace(const.dirName_contents,const.dirName_img,1)
            #print('[{}] dir_src_this: {}'.format(proc, dir_src_this))
            #print(f'[{proc}] dir_img_this: {dir_img_this}')
            #for d in [dir_src_this,dir_img_this]:
            #    if not os.path.isdir(d):
            #        print('[{}] mkdir -p {}'.format(proc, d))
            #        os.makedirs(d)

            path_raw_this = os.path.join(dir_this, comp[kw.file_raw])
            path_page_this = os.path.join(dir_this.replace(const.dir_raw,const.dir_page),
                                          comp[kw.file_raw].replace(const.ext_raw,const.ext_html))
            comp[kw.path_page] = path_page_this
            print(f'[{proc}] path_page_this: {path_page_this}')

            # Skip if thumbnail page of Photos
            if dirName == const.category_Photos and comp[kw.depth] == 0:
                continue

            # Skip if the file is latest version
            toBeUpdated = True
            if not overwrite:
                if os.path.isfile(path_page_this):
                    if os.stat(path_raw_this).st_mtime < os.stat(path_page_this).st_mtime:
                        if dirName == const.category_Photos:
                            toBeUpdated = False
                        else:
                            print('File is latest version. Not updated.')
                            continue

            # Format lines
            lines_fmt, info_photos = format_content(dirName, path_raw_this, comp, toBeUpdated)
            comp[kw.info_photos] = info_photos

            # Make the directory
            dir_this = os.path.dirname(path_page_this)
            if not os.path.isdir(dir_this):
                print(f'[{proc}] mkdir -p {dir_this}')
                os.makedirs(dir_this)

            # Write html file
            wf = open(path_page_this,'w')
            for line in lines_fmt:
                wf.write(line+'\n')
            wf.close()
            print(f'[{proc}] Saved {path_page_this.replace(const.dir_top+"/","")}')

            # Make a link
            if comp[kw.link_dst] is not None:
                path_link = os.path.join(dir_page_this, comp[kw.link_dst]+const.ext_html)
                print(f'[{proc}] -> {path_link.replace(const.dir_top+"/","")}')
                if os.path.isfile(path_link):
                    os.remove(path_link)
                os.symlink(path_page_this, path_link)
    #-----------------------------------------------------------
    # Make pages of photo thumbnails
    #-----------------------------------------------------------
    if dirName == const.category_Photos:
        ii_comp = [i for i, comp in enumerate(comps) if comp[kw.depth]==0] + [len(comps)]
        for i0_comp, i1_comp in zip(ii_comp[:-1], ii_comp[1:]):
            comp0 = comps[i0_comp]
            path_page_this = os.path.join(const.dir_page, 
                              '{}/{}/{}/{}'.format(
                                dirName, 
                                const.dirName_contents, 
                                comp0[kw.dir_path], 
                                comp0[kw.file_raw].replace(const.ext_raw,const.ext_html)))
            #print('dir: {}'.format(path_page_this))
            title = comp0[kw.title]
            lines_fmt = format_content_Photos_FY(title, comps[i0_comp+1:i1_comp])

            wf = open(path_page_this,'w')
            for line in lines_fmt:
                wf.write(line+'\n')
            wf.close()
            print(f'[{proc}] Saved {path_page_this.replace(const.dir_top+"/","")}')
    #-----------------------------------------------------------
    # Make index page
    #-----------------------------------------------------------
    path_index = fmt.path_index.format(dirName=dirName)
    lines_fmt = format_index(comps, dirName)

    wf = open(path_index, 'w')
    for line in lines_fmt:
        wf.write(line+'\n')
    wf.close()
    print(f'Saved {path_index.replace(const.dir_top+"/","")}')
    #-----------------------------------------------------------
    # Convert index.html corresponding to the platform
    #-----------------------------------------------------------
    if const.platform != const.platform_github:
        conv_toppage()
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
def prep_vimStyle():
    vimStyle = {}
    for language in const.extension.keys():
        vimStyle[language] = {}

        f_css = get_f_css_src(language)
        if not os.path.isfile(f_css):
            continue

        for line in open(f_css, 'r').readlines():
            className = line.strip().split()[0][1:]
            style = line[len(className)+1:].strip()
            vimStyle[language][className] = style
            print(className, style)

    return vimStyle
#===============================================================
#
#===============================================================
def prep_vimStyle_notfound():
    vimStyle_notfound = {}
    for language in const.extension.keys():
        vimStyle_notfound[language] = {}

    return vimStyle_notfound
#===============================================================
#
#===============================================================
def report_vimStyle_notfound():
    for language in vimStyle_notfound.keys():
        if len(vimStyle_notfound[language]) == 0: continue
        print(f'language: {language}')
        for className, style in vimStyle_notfound[language].items():
            print(f'.{className} {style}')
#===============================================================
#
#===============================================================
#
#
#
#
#
#===============================================================
#
#===============================================================
class Const():
    platform_github = 'github'
    platform_local = 'local'
    platforms = [
        platform_github,
        platform_local,
    ]

    dir_top = os.getcwd()

    dirName_contents = 'contents'
    dirName_src = 'src'
    dirName_img = 'img'

    ext_raw  = '.src'
    ext_html = '.html'

    category_Python   = 'Python'
    category_Fortran  = 'Fortran'
    category_C        = 'C'
    category_Linux    = 'Linux'
    category_Works    = 'Works'
    category_Products = 'Products'
    category_Photos   = 'Photos'
    category_Others   = 'Others'
    category_Privates = 'Privates'
    category_tmp      = 'tmp'

    dirNames = [
      category_Python,
      category_Fortran, 
      category_C, 
      category_Linux, 
      category_Works,
      category_Products,
      category_Photos,
      category_Others,
      category_Privates,
      category_tmp,
    ]

    extension = dict(
      fortran = 'f90',
      python = 'py',
      c = 'c',
      html = 'html',
      bash = 'sh',
      json = 'json',
      yaml = 'yaml',
      plaintext = 'txt',
    )

    blockName_index = 'index'
    blockName_contents = 'contents'
    blockName_ref = 'ref'
    blockName_lastUpdate = 'lastUpdate'
    blockName_src = 'src'
    blockName_img = 'img'
    blockName_table = 'table'
    blockName_math = 'math'
    blockName_replace = 'replace'

    blockNames = [
      blockName_index, 
      blockName_contents, 
      blockName_ref,
    ]
    blockNames_special = [
      blockName_lastUpdate, 
      blockName_src, 
      blockName_img, 
      blockName_table,
      blockName_math,
      blockName_replace,
    ]

    blockStatus_begin = 'begin'
    blockStatus_end   = 'end'
    blockStatus_in    = 'in'

    str_line_continue = '\\'

    indent_contents_list = '  '
    str_contents_list_org = 'org='
    str_contents_list_dst = 'dst='

    # リンクが無い場合（書籍など）はリンクを「(None)」とする。
    refStatus_title = 'title'
    refStatus_link  = 'link'
    ref_link_none = '(None)'

    table_opt_head        = '-head'
    table_opt_format_cell = '-format'
    table_fmt_miss  = '-'
    table_tag_width = 'width'
    table_tag_align = 'align'

    table_tag_wrap  = 'wrap'
    table_tag_class = 'class'

    img_cls_mw50  = 'mw50'
    img_cls_mw100 = 'mw100'
    img_ext_drive_default = 'jpg'
    img_exts = ['jpg', 'png', 'PNG']
    img_kw_url = 'url'
    img_kw_drv = 'drv'
    img_kw_fid = 'fid'
    img_kw_cls = 'cls'
    img_kw_cpt = 'cpt'
    img_kw_ext = 'ext'

    img_tmb_width_base = 20.0
    img_tmb_width_total_ulim = 98.0
    img_tmb_width_total_llim = 65.0
    img_tmb_leftMargin = 1  # %; corresponds to css

    maxPathDepth = 10

    inline_replace = 'r'

    def load_config(self, conf):
        print('load config')
        self.url = conf['url']
        self.style_css = conf['style_css']

        self.platform = conf['platform']
        if self.platform == self.platform_github:
            self.ext_platform = ''
        elif self.platform == self.platform_local:
            self.ext_platform = '_local'
        else:
            raise Exception(
                f'Invalid input of `conf["platform"]`: {conf["platform"]}\n'
                f'Select from {self.platforms}.'
            )

        self.dir_raw = f'{self.dir_top}/raw'
        self.dir_page_base = f'{self.dir_top}/page'
        self.url_page_base = f'{self.url}/page'
        self.dir_page = f'{self.dir_top}/page{self.ext_platform}'
        self.url_page = f'{self.url}/page{self.ext_platform}'


class Keyword():
    depth = 'depth'
    title = 'title'
    title_index = 'title_index'
    link_org = 'link_org'
    link_dst = 'link_dst'
    path = 'path'
    dir_path = 'dir_path'
    file_raw = 'file_raw'
    route = 'route'
    isfile = 'isfile'
    path_raw = 'path_raw'
    path_tmb = 'path_tmb'
    aspect_tmb = 'aspect_tmb'
    path_page = 'path_page'
    info_photos = 'info_photos'
    tree = 'tree'

    parenth = 'parenth'
    tag = 'tag'
    cls = 'class'

    inline_typ = 'typ'
    inline_tag = 'tag'
    inline_nam = 'nam'
    inline_cls = 'cls'
    inline_is_double = 'is_double'

kw = Keyword()


class Format():
    def __init__(self, const: Const):
        self.f_contents_list = f'{const.dir_raw}/{{dirName}}/index.txt'
        self.dir_raw_contents = f'{const.dir_raw}/{{dirName}}/{const.dirName_contents}/'

        self.path_index = f'{const.dir_page}/{{dirName}}/index.html'

        self.dir_img = f'{const.dir_page}/{{dirName}}/{const.dirName_img}/'

        self.url_page_img = f'{const.url_page}/{{dirName}}/{const.dirName_img}/'

        self.inlines = '{line0}{content}{line1}'

        self.parent_content_top   = '{tree}<span class=\'fs\'>{title}</span>'
        self.parent_content_nourl = '{tree}<span class=\'fs\'>{title}</span>'
        self.parent_content_url   = '{tree}<span class=\'fs\'><a href="{url}">{title}</a></span>'

        self.photos_index = '+ <a href="{url}"><span class=\'photos-index\'>{title}</span></a>'

        self.img_title = '<span class=\'img-title\'>{title}</span>'
        self.img_caption = '<span class=\'img-caption\'>{caption}</span>'
        self.img_src = '<a href="{url}"><img class=\'{cls}\' src="{src}"></a>'
        self.img_tmb = '<a href="{url}"><img class=\'{cls}\' src="{src}" width=\'{width}%\'></a>'


class Replaced():
    replaced = []

#===============================================================
#
#===============================================================
const = Const()

parser = argparse.ArgumentParser()
parser.add_argument('dirName', type=str, choices=const.dirNames + ['all'])
parser.add_argument('--conf', default='conf/local.json')
parser.add_argument('-w', '--overwrite', action='store_true')

args = parser.parse_args()

dirName_ = args.dirName
overwrite = args.overwrite

conf = json.load(open(args.conf, 'r'))

const.load_config(conf)

fmt = Format(const)

replaced = Replaced()

inlines = mklist_inlines()

vimStyle = prep_vimStyle()
vimStyle_notfound = prep_vimStyle_notfound()

if dirName_ == 'all':
    for dirName_this in const.dirNames:
        make_all(dirName_this, overwrite)
else:
    make_all(dirName_, overwrite)

report_vimStyle_notfound()
