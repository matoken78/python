1. msys2-x86_64-20190524.exe ���C���X�g�[��
2. mysys �R�}���h�v�����v�g�ŉ��L�����s
  pacman -Syu
  pacman -S mingw64/mingw-w64-x86_64-cairo
3. ���z���ŉ��L�����s
   ��python3.7�ȊO�̏ꍇ�ɂ͉��L���T��
     https://www.lfd.uci.edu/~gohlke/pythonlibs/
  py -m pip install pycairo-1.19.1-cp37-cp37m-win_amd64.whl
  py -m pip install python_igraph-0.7.1.post6-cp37-cp37m-win_amd64.whl
4. igraph �̃t�H���g��ύX����
  venv\Lib\site-packages\igraph\drawing\graph.py
  context.select_font_face �̑�������ύX