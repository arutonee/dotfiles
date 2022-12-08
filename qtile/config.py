from os.path import expanduser, exists
import toml
import subprocess

THEME_DIR = "~/.config/qtile/themes/"
THEME_NAME = "hope"

# min of (width, height)
MIN_OF_WH = 1080


if not exists(expanduser(THEME_DIR + THEME_NAME + "/theme.toml")):
    THEME_NAME = "default"

THEME = toml.load(expanduser(THEME_DIR + THEME_NAME + "/theme.toml"))


from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Screen
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    Key([mod], "c", lazy.spawn("dunstctl close-all")),
    Key([mod], "v", lazy.spawn("dunstctl history-pop")),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "d", lazy.spawn(
        "rofi -show drun -config " + expanduser(THEME_DIR + THEME_NAME + "/cfg.rasi")
        )),
    Key([mod], "Return", lazy.spawn("kitty --config " + expanduser(THEME_DIR + THEME_NAME + "/kitty.conf")), desc="Launch terminal"),
    # Screenshot
    Key([mod], "x", lazy.spawn("scrot -s -f '/tmp/scsh.png' -e 'xclip -selection clipboard -target image/png -i $f && rm $f'")),
    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    KeyChord([mod, "shift"], "e", [
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod, "shift"], "l", lazy.spawn(
            "i3lock -k --indicator --radius " + str(int(MIN_OF_WH/3)) + " --ring-width 2 -c "+THEME["bar"]["background-color"][1:]+"aa" + \
            " --inside-color=00000000 --ring-color=00000000 --line-color=00000000" + \
            " --insidever-color=00000000 --ringver-color=00000000" + \
            " --insidewrong-color=00000000 --ringwrong-color="+THEME["tags"]["urgent"][1:] + \
            " --keyhl-color="+THEME["tags"]["active"]+" --bshl-color="+THEME["tags"]["inactive"][1:] + \
            " --separator-color=00000000" + \
            " --verif-color="+THEME["bar"]["text"][1:] + \
            " --wrong-color="+THEME["bar"]["text"][1:] + \
            " --modif-color="+THEME["bar"]["text"][1:] + \
            " --layout-color="+THEME["bar"]["text"][1:] + \
            " --time-color="+THEME["bar"]["text"][1:] + \
            " --date-color="+THEME["bar"]["text"][1:] + \
            " --time-str=\"%H:%M:%S\"" + \
            " --date-str=\"%Y-%m-%d %A\"" + \
            " --verif-text=\"...\"" + \
            " --wrong-text=\"X\"" + \
            " --keylayout 0" + \
            " --noinput-text=\"X\"" + \
            " --lock-text=\"Locking...\"" + \
            " --lockfailed-text=\"Couldn't lock.\"" + \
            " --no-modkey-text" + \
            " --time-font='fantasque sans mono'" + \
            " --date-font='fantasque sans mono'" + \
            " --layout-font='fantasque sans mono'" + \
            " --verif-font='fantasque sans mono'" + \
            " --wrong-font='fantasque sans mono'" + \
            " --pass-volume-keys --pass-screen-keys"
        ))
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
    # layout.Max(),
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
                # widget.CurrentLayout(),
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
                widget.Volume(foreground=THEME["bar"]["text"]),
                widget.Clock(format="%Y-%m-%d %A %H:%M:%S", foreground=THEME["bar"]["text"]),
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
#     float_rules=[
#         # # Run the utility of `xprop` to see the wm class and name of an X client.
#         # *layout.Floating.default_float_rules,
#         # Match(wm_class="confirmreset"),  # gitk
#         # Match(wm_class="makebranch"),  # gitk
#         # Match(wm_class="maketag"),  # gitk
#         # Match(wm_class="ssh-askpass"),  # ssh-askpass
#         # Match(title="branchdialog"),  # gitk
#         # Match(title="pinentry"),  # GPG key password entry
#     ]
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
        subprocess.call(["bash", home + "/.config/qtile/autostart.sh", str(THEME["border"]["round"]), THEME_NAME])
    else:
        for screen in screens:
            screen.cmd_set_wallpaper(expanduser("~/.config/qtile/none.png"), 'fill')
        subprocess.call(["bash", home + "/.config/qtile/autostart.sh", str(THEME["border"]["round"]), THEME_NAME, 'a'])
