return {
  "folke/todo-comments.nvim",
  dependencies = { "nvim-lua/plenary.nvim" },
  opts = {
    signs = true, -- Mostrar iconos en la columna de signos
    sign_priority = 8, -- Prioridad de los signos
    -- Keywords reconocidos como comentarios todo
    keywords = {
      DANGER = { icon = " ", color = "danger" },
      FIX = { icon = " ", color = "fix", alt = { "FIXME", "BUG", "FIXIT" } },
      INFO = { icon = " ", color = "info" },
      TEST = { icon = "⏲ ", color = "test", alt = { "TESTING", "PASSED", "FAILED" } },
      WARNING = { icon = " ", color = "warning" }, -- Añadí el color específico para WARNING
    },
    gui_style = {
      fg = "NONE", -- Sin color para el texto
      bg = "NONE", -- Sin fondo de color
    },
    merge_keywords = true, -- Si es verdadero, fusiona los keywords personalizados con los predeterminados
    highlight = {
      multiline = true, -- Habilitar comentarios multilinea
      multiline_pattern = "^.", -- Patrón para comentarios multilinea
      multiline_context = 10, -- Líneas adicionales que se reevaluarán cuando se cambie una línea
      before = "", -- "fg" o "bg" o vacío
      keyword = "fg", -- "fg", "bg", "wide", "wide_bg", "wide_fg" o vacío
      after = "fg", -- "fg" o "bg" o vacío
      pattern = [[.*<(KEYWORDS)\s*]], -- Patrón de expresión regular para coincidir
      comments_only = true, -- Solo resaltar las palabras clave dentro de los comentarios
      max_line_len = 400, -- Ignorar líneas más largas que esto
      exclude = {}, -- Lista de tipos de archivos a excluir
    },
    colors = {
      fix = { "DiagnosticFix", "#FFFFFF" }, -- FIX con color blanco
      danger = { "#DC2626" }, -- DANGER ahora en rojo tomate
      warning = { "#FF4500" }, -- WARNING ahora en un naranja más oscuro
      info = { "DiagnosticInfo", "#2563EB" }, -- TODO en azul
      test = { "#FF00FF" }, -- TEST en color rosa
    },
    search = {
      command = "rg", -- Usar ripgrep para la búsqueda
      args = {
        "--color=never",
        "--no-heading",
        "--with-filename",
        "--line-number",
        "--column",
      },
      pattern = [[\b(KEYWORDS)\b]], -- Patrón ajustado para buscar las palabras clave sin los dos puntos ":"
    },
  },
}
