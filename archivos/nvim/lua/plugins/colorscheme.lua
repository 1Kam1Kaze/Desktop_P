return {
  -- import colorschemes
  { "catppuccin/nvim", name = "catppuccin", lazy = false, opts = { flavour = "mocha" } },
  { "EdenEast/nightfox.nvim", name = "nightfox", lazy = false },
  { "diegoulloao/neofusion.nvim", name = "neofusion", lazy = false },
  { "bluz71/vim-moonfly-colors", name = "moonfly", lazy = false },
  { "shaunsingh/moonlight.nvim", name = "moonlight", lazy = false },
  { "ntk148v/vim-horizon", name = "horizon", lazy = false },
  { "navarasu/onedark.nvim", name = "onedark", lazy = false },

  {
    "LazyVim/LazyVim",
    opts = { -- options of colorscheme
      colorscheme = "onedark",
      -- Lua
    },
  },
}
