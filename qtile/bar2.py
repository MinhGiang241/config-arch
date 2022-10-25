from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.prompt import Prompt
from libqtile.widget.clock import Clock

from colors import gruvbox
from unicodes import left_half_circle, right_half_circle

bar = Bar([
    Spacer(length=10),
    left_half_circle(gruvbox['yellow']),
    CurrentLayout(
        background=gruvbox['yellow'],
    ),
    right_half_circle(gruvbox['yellow']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['dark-blue'],
        show_zero=True
    ),
    right_half_circle(gruvbox['dark-blue']),

    Spacer(length=10),

    left_half_circle(gruvbox['cyan']),
    Net(
        background=gruvbox['cyan'],
    ),
    right_half_circle(gruvbox['cyan']),

    Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    WindowName(foreground=gruvbox['fg']),

    Spacer(length=20),


    Prompt(background=gruvbox['dark-yellow']),



    Spacer(length=40),



    left_half_circle(gruvbox['bg']),
    GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_half_circle(gruvbox['bg']),

    Spacer(length=100),

    Systray(
        padding=15,
        # background='#00000000'
    ),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-cyan']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    right_half_circle(gruvbox['dark-cyan']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    Clock(
        format=' %d-%m-%Y %a %I:%M %p',
        background=gruvbox['dark-blue']
    ),
    right_half_circle(gruvbox['dark-blue']),

    Spacer(length=10),
    left_half_circle(gruvbox['dark-red']),
    QuickExit(background=gruvbox['dark-red']),
    right_half_circle(gruvbox['dark-red']),
    Spacer(length=10),

],
    margin=[10, 10, 5, 10],
    background=gruvbox['bg'],
    opacity=1,
    size=25,
)
