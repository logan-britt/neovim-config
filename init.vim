call plug#begin()
  " handel the usage of the file explorer 
  Plug 'ryanoasis/vim-devicons'
  Plug 'scrooloose/nerdtree', {'on' : 'NERDTreeToggle'}
  
  " set up the plugins for searching the file system for files
  Plug 'junegunn/fzf', {'dir': '~/.fzf', 'do': './install --all'}
  Plug 'junegunn/fzf.vim'

  " set up the auto compleate
  Plug 'neoclide/coc.nvim'
call plug#end()

" set up the tabs and the spacing
set smartindent
set tabstop=2
set shiftwidth=2
set expandtab

" set up the coc python settings
python.jediEnabled:false
