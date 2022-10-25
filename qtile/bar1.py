from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.prompt import Prompt

from unicodes import right_arrow, left_arrow
from colors import gruvbox

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_arrow(gruvbox['magenta'], gruvbox['bg']),
    CurrentLayout(
        background=gruvbox['magenta'],
        foreground=gruvbox['white']
    ),
    right_arrow(gruvbox['bg0'], gruvbox['magenta']),

    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['bg0'],
        foreground=gruvbox['white'],
        show_zero=True,
    ),

    right_arrow(gruvbox['bg'], gruvbox['bg0']),
    WindowName(foreground=gruvbox['fg']),

    left_arrow(gruvbox['bg'], gruvbox['dark-yellow']),
    Prompt(background=gruvbox['dark-yellow']),


    left_arrow(gruvbox['dark-yellow'], gruvbox['dark-green']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-green'],
        foreground=gruvbox['white']
    ),

    left_arrow(gruvbox['dark-green'], gruvbox['cyan']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['cyan'],
        foreground=gruvbox['white']
    ),

    left_arrow(gruvbox['cyan'], gruvbox['dark-blue']),
    Net(
        background=gruvbox['dark-blue'],
        foreground=gruvbox['white']
    ),

    left_arrow(gruvbox['dark-blue'], gruvbox['dark-magenta']),
    Clock(
        background=gruvbox['dark-magenta'],
        foreground=gruvbox['white'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['dark-magenta'], gruvbox['dark-red']),
    QuickExit(background=gruvbox['dark-red']),
    left_arrow(gruvbox['dark-red'], gruvbox['fg0']),
    Systray(
        background=gruvbox['fg0']
    ),

    Spacer(length=20, background=gruvbox['fg0'])
], background=gruvbox['bg'], size=26, margin=9)
