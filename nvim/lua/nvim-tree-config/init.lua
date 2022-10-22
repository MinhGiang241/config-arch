-- disable netrw at the very start of your init.lua (strongly advised)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

require'nvim-tree'.setup {
  diagnostics={enable=true},
  view = {
    adaptive_size=true,
    
  },
  renderer={group_empty=true},
  filters={dotfiles=true}
}
