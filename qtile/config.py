from os.path import expanduser, exists
import toml
import subprocess

THEME_DIR = "~/.config/qtile/themes/"
THEME_NAME = "default"

if not exists(expanduser(THEME_DIR + THEME_NAME + "/theme.toml")):
    THEME_NAME = "default"

THEME = toml.load(expanduser(THEME_DIR + THEME_NAME + "/theme.toml"))


from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

TERMFG = THEME["terminal"]["foreground"]
TERMBG = THEME["terminal"]["background"]

TERMBLACK = THEME["terminal"]["black"]
TERMRED = THEME["terminal"]["red"]
TERMGREEN = THEME["terminal"]["green"]
TERMYELLOW = THEME["terminal"]["yellow"]
TERMBLUE = THEME["terminal"]["blue"]
TERMMAGENTA = THEME["terminal"]["magenta"]
TERMCYAN = THEME["terminal"]["cyan"]
TERMWHITE = THEME["terminal"]["white"]

TERMBBLACK = THEME["terminal"]["bright_black"]
TERMBRED = THEME["terminal"]["bright_red"]
TERMBGREEN = THEME["terminal"]["bright_green"]
TERMBYELLOW = THEME["terminal"]["bright_yellow"]
TERMBBLUE = THEME["terminal"]["bright_blue"]
TERMBMAGENTA = THEME["terminal"]["bright_magenta"]
TERMBCYAN = THEME["terminal"]["bright_cyan"]
TERMBWHITE = THEME["terminal"]["bright_white"]

keys = [
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "d", lazy.spawn(
        "rofi -show drun -config " + expanduser(THEME_DIR + THEME_NAME + "/cfg.rasi")
        )),
    Key([mod], "Return", lazy.spawn("alacritty" + \
        f" -o \"colors.primary.foreground='{TERMFG}'\"" + \
        f" -o \"colors.primary.background='{TERMBG}'\"" + \
        f" -o \"colors.normal.black='{TERMBLACK}'\"" + \
        f" -o \"colors.normal.red='{TERMRED}'\"" + \
        f" -o \"colors.normal.green='{TERMGREEN}'\"" + \
        f" -o \"colors.normal.yellow='{TERMYELLOW}'\"" + \
        f" -o \"colors.normal.blue='{TERMBLUE}'\"" + \
        f" -o \"colors.normal.magenta='{TERMMAGENTA}'\"" + \
        f" -o \"colors.normal.cyan='{TERMCYAN}'\"" + \
        f" -o \"colors.normal.white='{TERMWHITE}'\"" + \
        f" -o \"colors.bright.black='{TERMBBLACK}'\"" + \
        f" -o \"colors.bright.red='{TERMBRED}'\"" + \
        f" -o \"colors.bright.green='{TERMBGREEN}'\"" + \
        f" -o \"colors.bright.yellow='{TERMBYELLOW}'\"" + \
        f" -o \"colors.bright.blue='{TERMBBLUE}'\"" + \
        f" -o \"colors.bright.magenta='{TERMBMAGENTA}'\"" + \
        f" -o \"colors.bright.cyan='{TERMBCYAN}'\"" + \
        f" -o \"colors.bright.white='{TERMBWHITE}'\""
    ), desc="Launch terminal"),
    # Screenshot
    Key([mod], "x", lazy.spawn("scrot -s -f '/tmp/scsh.png' -e 'xclip -selection clipboard -target image/png -i $f && rm $f'")),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    # Toggle between different layouts as defined below
    Key([mod], "Space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    KeyChord([mod, "shift"], "e", [
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile")
    ], name="Power"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=THEME["border"]["focused"],
        border_normal=THEME["border"]["unfocused"],
        border_width=THEME["border"]["width"],
        margin=THEME["border"]["gap"]
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=THEME["fonts"]["family"],
    fontsize=THEME["fonts"]["size"],
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method=THEME["tags"]["highlight_method"],
                    borderwidth=THEME["tags"]["width"],
                    disable_drag=True,
                    active=THEME["tags"]["active"],
                    inactive=THEME["tags"]["inactive"],
                    this_current_screen_border=THEME["tags"]["current_color"],
                    block_highlight_text_color=THEME["tags"]["current_font_color"],
                    urgent_border=THEME["tags"]["urgent"],
                    urgent_text=THEME["tags"]["urgent_font_color"]
                ),
                widget.Prompt(),
                widget.Spacer(),
                # widget.WindowName(),
                widget.Chord(foreground=THEME["bar"]["chord"]),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Volume(),
                widget.Clock(format="%Y-%m-%d %a %H:%M:%S"),
                # widget.QuickExit(),
            ],
            int(THEME["fonts"]["size"] * THEME["bar"]["vertical_padding"]),
            background=THEME["bar"]["background-color"],
            margin=[0] + [THEME["border"]["gap"]] * 3
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        # Match(wm_class="confirmreset"),  # gitk
        # Match(wm_class="makebranch"),  # gitk
        # Match(wm_class="maketag"),  # gitk
        # Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(title="branchdialog"),  # gitk
        # Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

BG_TYPE = THEME["background"]["type"]

@hook.subscribe.startup
def startup():
    home = expanduser("~")
    if BG_TYPE != "gif":
        for screen in screens:
            screen.cmd_set_wallpaper(expanduser(THEME_DIR + THEME_NAME + "/background." + BG_TYPE), 'fill')
        subprocess.call(["bash", home + "/.config/qtile/autostart.sh", str(THEME["border"]["round"])])
    else:
        for screen in screens:
            screen.cmd_set_wallpaper(expanduser("~/.config/qtile/none.png"), 'fill')
        subprocess.call(["bash", home + "/.config/qtile/autostart.sh", str(THEME["border"]["round"]), THEME_NAME])
