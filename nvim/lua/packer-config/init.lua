local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath("data") .. "/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
	PACKER_BOOTSTRAP = fn.system({
		"git",
		"clone",
		"--depth",
		"1",
		"https://github.com/wbthomason/packer.nvim",
		install_path,
	})
	print("Installing packer close and reopen Neovim...")
	vim.cmd([[packadd packer.nvim]])
end

-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerSync
  augroup end
]])

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
	return
end

-- Have packer use a popup window
packer.init({
	display = {
		open_fn = function()
			return require("packer.util").float({ border = "rounded" })
		end,
	},
})

return require("packer").startup(function()
	use("wbthomason/packer.nvim")
	use("nvim-tree/nvim-tree.lua")
	use("nvim-tree/nvim-web-devicons")
	use("rcarriga/nvim-notify") -- notify
	use("nvim-lualine/lualine.nvim")
	use("romgrk/barbar.nvim")
	use("jose-elias-alvarez/null-ls.nvim")
	use("sunjon/shade.nvim")
	use("lukas-reineke/indent-blankline.nvim")
	-- ColorScheme
	use("tanvirtin/monokai.nvim")
	use("EdenEast/nightfox.nvim")

	-- Telescope
	use("nvim-telescope/telescope.nvim")
	use("nvim-lua/plenary.nvim")
	use("nvim-telescope/telescope-github.nvim")

	-- Tree sitter
	use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" })
	use("nvim-treesitter/nvim-treesitter-refactor")
	use("nvim-treesitter/playground")
	use("p00f/nvim-ts-rainbow")
	use("windwp/nvim-autopairs")
	use("windwp/nvim-ts-autotag")

	-- LSP plugins
	use("neovim/nvim-lspconfig")
	use("hrsh7th/nvim-cmp") -- Autocompletion plugin
	use("hrsh7th/cmp-nvim-lsp") -- LSP source for nvim-cmp
	use("saadparwaiz1/cmp_luasnip") -- Snippets source for nvim-cmp
	use("L3MON4D3/LuaSnip") -- Snippets plugin
	use("onsails/lspkind.nvim") --vscode like icon
	use("williamboman/nvim-lsp-installer") -- manage language server
end)
-- disable netrw at the very start of your init.lua (strongly advised)
