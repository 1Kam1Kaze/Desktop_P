return {
  "akinsho/toggleterm.nvim",
  config = function()
    require("toggleterm").setup({
      open_mapping = [[<c-ñ>]], -- Ctrl + ñ
      size = 20, -- Tamaño del terminal flotante
      direction = "float", -- Terminal flotante
      start_in_insert = true, -- Comienza en modo insertar
      persist_size = true, -- Mantén el tamaño entre sesiones
    })
  end,
}
