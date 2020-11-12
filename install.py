import os
import shutil
import platform

print('\n')

# install the neovim package
if platform.system() == 'Linux':
  pass

elif platform.system() == 'Darwin':
  pass

elif platform.system() == 'Windows':
  pass

# read the init.vim file and change it for the operating system and user
init_text = []
with open('init.vim', 'r') as init_file:
  for line in init_file:
    init_text.append(line)

# set the new path for the plugins on the disk
home_path = os.path.expanduser('~')
vim_location = os.path.join(home_path, '.neovim')
new_plugin_location = os.path.join(vim_location, 'plugged')

# create the new location for the vim plugins in the init script
init_text[0] = f"call plug#begin('{new_plugin_location}')\n"
print(init_text[0])

# make all of the text one string
out_text = ''
for line in init_text:
  out_text += line

# rewrite the file with the new header
with open('new_init.vim', 'w') as init_file:
  init_file.write(out_text)

# move the file to its proper location
folder_list = os.listdir(home_path.__str__())

if platform.system() == 'Linux':
  base_path = os.path.join(home_path, '.config/nvim')
  if '.config' in folder_list:
    subfolder_path = os.path.join(home_path, '.config')
    subfolder_list = os.listdir(subfolder_path.__str__())
    if 'nvim' in subfolder_list:
      init_path = os.path.join(base_path, 'init.vim')
      shutil.copy('new_init.vim', init_path.__str__())

      # install the vim plug vimscript
      os.system(f'curl -fLo {home_path.__str__()}/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')

    else:
      neovim_path = os.path.join(home_path, '.config/nvim')
      os.mkdir(neovim_path.__str__())

      init_path = os.path.join(base_path, 'init.vim')
      shutil.copy('new_init.vim', init_path.__str__())

      # install the vim plug vimscript
      os.system(f'curl -fLo {home_path.__str__()}/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')

  else:
    os.makedirs(base_path)

    init_path = os.path.join(base_path, 'init.vim')
    shutil.copy('new_init.vim', init_path.__str__())

    # install the vim plug vimscript
    os.system(f'curl -fLo {home_path.__str__()}/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')

elif platform.system() == 'Darwin':
  pass

elif platform.system() == 'Windows':
  pass

else:
  raise ValueError('The os that you are using was not programed.')

os.remove('new_init.vim')