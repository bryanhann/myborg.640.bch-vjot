function GetFirstWordOnLine()
     let save_pos = getpos(".")
     normal ^
     let w = expand("<cword>") 
     call setpos(".", save_pos)
     return w
endfunction

function PlayJot()
    let stamp = GetFirstWordOnLine()
    let file = stamp . ".ws852.mp3"
    execute "!vjot-play-name " . file . " &"
    " silent execute "!vjot-play-name " . file . " &"
    " silent execute "!safe-afplay " . file . " &"
    " #silent execute "!./vjot.play " . file . " &"
endfunction

map  <Tab>      :call PlayJot()<CR>:redraw!<CR>
imap <Tab> <ESC>:call PlayJot()<CR>:redraw!<CR>i
