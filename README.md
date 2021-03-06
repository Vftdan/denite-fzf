About
-----

The `denite-fzf` plugin allows you to use [fzf](https://github.com/junegunn/fzf) as a matcher and/or sorter for [Denite](https://github.com/Shougo/denite.nvim) in [Neovim](https://neovim.io/) or [Vim](https://www.vim.org/).
It is based on a [plugin](https://github.com/blankname/denite_fzf_matcher) by [blankname](https://github.com/blankname), which did not work for me.

After installation, you configure Denite to use fzf as a default matcher for all sources.
```
call denite#custom#source('_', 'matchers', ['matcher/fzf'])
call denite#custom#source('_', 'sorters', ['sorter/fzf'])
```

Installation
------------

The plugin depends on [Denite](https://github.com/Shougo/denite.nvim) by [Shougo](https://github.com/Shougo).
You need to install it in order to use this plugin.

### Plug
```
Plug 'Shougo/denite.nvim'
Plug 'Vftdan/denite-fzf'
```
### Vundle
```
Plugin 'Shougo/denite.nvim'
Plugin 'Vftdan/denite-fzf'
```
### NeoBundle
```
NeoBundle 'Shougo/denite.nvim'
NeoBundle 'Vftdan/denite-fzf'
```
