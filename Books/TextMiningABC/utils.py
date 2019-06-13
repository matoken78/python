# 日本語フォントの適用
import matplotlib as mpl
from pathlib import Path
import shutil

def adapt_japanese_font(plt):
    dest_font_path = Path(mpl.matplotlib_fname()).parent / 'fonts' / 'ttf' / 'ipaexg.ttf'
    source_font_path = Path(__file__).parent / 'font' / 'ipaexg.ttf'
    shutil.copy(str(source_font_path), str(dest_font_path))

    config_dir = Path(mpl.get_configdir())
    for f in config_dir.glob('**/*'):
        if f.is_file():
            f.unlink()
        else:
            f.rmdir()
    plt.rcParams['font.family'] = 'IPAexGothic'