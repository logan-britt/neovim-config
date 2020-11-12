import os
import shutil
import platform

home_path = os.path.expanduser('~')

if platform.system() == 'Linux':
  neovim_path = os.path.join(home_path, '.config')
  neovim_plugin_path = os.path.join(home_path, '.neovim')

  folder_list = os.listdir(neovim_path.__str__())
  if 'nvim' in folder_list:
    remove_path = os.path.join(neovim_path, 'nvim')
    shutil.rmtree(remove_path.__str__())
    shutil.rmtree(neovim_plugin_path.__str__())

  else:
    raise RuntimeError('Neovim was not installed.')

elif platform.system() == 'Darwin':
  pass

elif platform.system() == 'Windows':
  pass