# Vikings — plan and progress

A simple "Lost Vikings"-like puzzle platformer in GameMaker, made for teaching children.
Same complexity as the other example games (`gm_boulder_dash`, `gm_farm_builder`, …):
few objects, short events, plain GML.

## Design decisions (answers from the teacher)

| Question | Answer |
|----------|--------|
| View | Side view platformer with gravity. |
| Control | One viking at a time, `Tab` switches. |
| Bjorn's shield | Always in front: blocks arrows and slimes from the side he faces. |
| Getting hit | Any hit restarts the level. |
| Jumping | Only Kaj jumps. |
| Up and down | Ladders for both. A ladder can be rolled up — then nobody can climb it until a button or plate rolls it down. |
| Buttons | Wall **button**: each push toggles. Floor **plate**: works only while a viking stands on it. |
| Linking | By instance: a button / plate has a `target` variable set in the room editor (e.g. `door_1`). |
| Stones | Kaj throws stones. They only push wall buttons (not plates), nothing else. |
| Slime | Patrols left/right. Bumping into Bjorn's shield turns it around; any other touch kills. |
| Size | 2 levels + win room. A level is won when **both** vikings stand in the exit. |
| Proportions (correction) | A normal room (storey) is 1.5–2× Bjorn's height; Kaj jumps about 2.1× Bjorn's height. |
| Camera (correction) | Follows the active viking; after `Tab` it glides (pans) to the other one. |

## Rules

- Grid of 32×32 px cells for building levels, but vikings move pixel by pixel (walk, fall, climb).
- Sizes: Bjorn is 48 px tall. A storey is 3 cells = 96 px (2× Bjorn), doors and the space above a ledge are 2 cells (1.3×).
  Kaj's jump is 105 px (2.2× Bjorn) — enough for a 3-cell ledge. (With whole-pixel speeds the choices are 91 px = 1.9× or 105 px = 2.2×.)
- Camera: shows 640×360 px of the room, zoomed 2× to a 1280×720 window, so the vikings look big.
  `o_Game.MoveCamera()` moves it 10 % of the way to the active viking every step — this follows the viking and pans after `Tab`.
- **Bjorn**: big, slow, can't jump, shield always in front.
- **Kaj**: small, jumps, throws one stone at a time (flies in an arc).
- **Button** (on a wall): a viking standing at it presses `E`, or a stone hits it → toggles its target.
- **Plate** (on the floor): target toggles when a viking steps on it and again when the viking steps off.
- Devices — every one has a `Toggle()` function:
  - **Door**: closed = solid, open = can walk through.
  - **Trapdoor**: a door lying in the floor (child of door). Open = vikings fall into the spikes below.
  - **Laser**: vertical beam from the ceiling; on = deadly.
  - **Ladder**: rolled down = climbable, rolled up = only a roll at the top.
- **Arrow hole** in a wall shoots an arrow every 1.5 s. Arrows stop at walls and doors and at Bjorn's shield.
- **Slime** crawls left/right, turns at walls and edges.
- **Spikes** at the bottom of pits are deadly.

## Controls

| Key | Action |
|-----|--------|
| ← → | walk |
| ↑ ↓ | climb a ladder |
| `Space` | Kaj: jump |
| `F` | Kaj: throw a stone |
| `E` | push the button you stand at |
| `Tab` | switch viking |
| `R` | restart the level |

## Resources

### Sprites (own pixel art, made by `tools/make_art.py`)

| Sprite | Size | Frames | Origin |
|--------|------|--------|--------|
| `s_BjornIdle`, `s_BjornWalk`, `s_BjornClimb` | 40×48 | 2 / 4 / 2 | bottom centre |
| `s_KajIdle`, `s_KajWalk`, `s_KajClimb`, `s_KajJump` | 32×36 | 2 / 4 / 2 / 1 | bottom centre |
| `s_Stone` | 12×12 | 1 | centre |
| `s_Wall` | 32×32 | 1 | top left |
| `s_Button` | 32×32 | 2 (off / on) | top left |
| `s_Plate` | 32×32 | 2 (up / down) | top left |
| `s_Door` | 32×64 | 2 (closed / open) | top left |
| `s_Trapdoor` | 32×32 | 2 (closed / open) | top left |
| `s_Ladder`, `s_LadderRolled` | 32×32 | 1 | top left |
| `s_Laser` | 32×32 | 3 (flicker, stretched in the room) | top left |
| `s_LaserEmitter` | 32×32 | 1 | top left |
| `s_ArrowHole` | 32×32 | 1 | centre (flip with x-scale) |
| `s_Arrow` | 24×6 | 1 | centre |
| `s_Slime` | 32×24 | 4 | bottom centre |
| `s_Spikes` | 32×32 | 1 | top left |
| `s_Exit` | 64×64 | 2 | top left |
| `s_Marker` | 16×12 | 2 | arrow over the active viking |
| `s_Poof` | 48×48 | 6 | centre — a viking was hit |

### Sounds (sfxr, https://sfxr.me — public domain, made by `tools/make_sfx.js`)

`snd_Jump`, `snd_Throw`, `snd_Click` (button / plate), `snd_Door` (any device toggles),
`snd_Arrow` (shot), `snd_Block` (shield), `snd_Hit` (viking is hit), `snd_Win` (level done).

### Objects

| Object | Parent | Events | Purpose |
|--------|--------|--------|---------|
| `o_Game` | — | Create, Room Start, Step, Key press Tab, Key press R, Alarm 0, Draw GUI | who is active, camera, restart, help text |
| `o_Viking` | — | Create, Step, Key press E, Draw | walking, gravity, ladders, dangers, `Die()`, `IsProtectedFrom()` |
| `o_Bjorn` | `o_Viking` | Create | slower, shield: overrides `IsProtectedFrom()` |
| `o_Kaj` | `o_Viking` | Create, Key press Space, Key press F | jump, throw |
| `o_Stone` | — | Create, Step, Collision `o_Button` | flies in an arc |
| `o_Wall` | — | — | solid |
| `o_Button` | — | Create | `Push()` toggles `target` |
| `o_Plate` | — | Create, Step | toggles `target` on step on / off |
| `o_Door` | — | Create, Step | `Toggle()`, solid while closed |
| `o_Trapdoor` | `o_Door` | — | same as door, other sprite |
| `o_Laser` | — | Create, Draw | `Toggle()`, deadly while on |
| `o_Ladder` | — | Create, Draw | `Toggle()`, climbable while down |
| `o_ArrowHole` | — | Create, Alarm 0 | shoots arrows |
| `o_Arrow` | — | Step, Collision `o_Viking` | flies, blocked by shield |
| `o_Slime` | — | Create, Step, Collision `o_Viking` | patrols |
| `o_Spikes` | — | — | deadly |
| `o_Exit` | — | Step | both vikings inside → next room |
| `o_Poof` | — | Animation End | effect |
| `o_WinText` | — | Draw, Key press Enter | win screen |

Script `Grid`: `#macro TILE 32`.

Variable Definitions (set in the room editor):
`o_Button.target`, `o_Plate.target` (Expression, the name of an instance in the room),
`o_Door.is_open`, `o_Laser.is_on`, `o_Ladder.is_down` (Boolean, starting state).

Stretched instances (scaled in the room editor): ladders and lasers (`Scale Y` = length in cells).

### Rooms

1280×704 (40×22 cells). Viewport 0: camera 640×360, port 1280×720, moved by `o_Game` (no "Object following").

| Room | Teaches |
|------|---------|
| `rm_Level1` | switching vikings, button → door, arrows vs. shield, stone → button behind spikes, Kaj's high jump, plate → ladder |
| `rm_Level2` | trapdoors over spikes, lasers, slime vs. shield, everything together |
| `rm_Win` | "You win!" |

## Lessons (1.5 hours each)

1. Project, `s_Wall` / `o_Wall` (solid), room with 32×32 grid. `o_Viking` with gravity, walking and the "move pixel by pixel" loop.
2. `o_Bjorn` and `o_Kaj` as children, `o_Game` switches with Tab, marker, camera that follows (`MoveCamera`). Kaj jumps. Ladders (always down).
3. Devices: `o_Door` with `Toggle()`, `o_Button` with `target`, then `o_Plate`. Ladder rolled up/down. Exit.
4. Kaj throws stones that push buttons. Arrow holes, arrows, `Die()` and restart, Bjorn's shield (`IsProtectedFrom`).
5. Trapdoors (child of door) and spikes, lasers, slime. Sounds. Second level, win room.

## Levels

Written as text maps (`W` wall, `S` spikes, `<` arrow hole, `M` slime, `B`/`K` vikings, `E` exit, letters for devices)
and converted to rooms by a script. From now on edit them in the room editor.
Instance names must be unique in the whole project, so they start with the level: `l1_door_1`, `l2_laser_2`, …
Pictures: `docs/level1.png`, `docs/level2.png`. Solutions are in the README.

Checked with a small calculation: Kaj's jump is 105 px (the ledge is 96 px). The stone (6, −5, gravity 0.25) stays under a
3-cell ceiling and hits the level 1 button from cells 19–21 (behind Bjorn) and the level 2 button from cells 16–19.

| Level 1 | Level 2 |
|---------|---------|
| storey A: `l1_button_door` → `l1_door_1`, arrow hole | storey A: `l2_button_door` → `l2_door_1`, slime |
| `l1_button_ladder` behind spikes (stone) → `l1_ladder_1` (rolled up) | `l2_button_laser_1` → `l2_laser_1` |
| storey B: corridor, `l1_ladder_2` | storey B: `l2_button_trapdoor` → `l2_trapdoor_1` (open, over spikes), `l2_ladder_2` |
| storey C: 3-cell ledge, `l1_plate_ladder` → `l1_ladder_3` (rolled up), exit | storey C: `l2_button_laser_2` behind the big laser (stone), exit |

## Progress

- [x] Questions answered, plan written
- [x] Graphics — own pixel art, `tools/make_art.py`
- [x] Sounds — sfxr (jsfxr), `tools/make_sfx.js`
- [x] Project, objects, code (format, options and fonts as in Farm Builder)
- [x] Levels
- [x] README with lessons and solutions
- [x] Commit and push
- [x] Correction: bigger vikings (storey = 2× Bjorn), Kaj jumps ~2× Bjorn, camera follows and pans
- [ ] Open in GameMaker and play-test both levels (no GameMaker in the build environment)

## Notes

- A viking climbing a ladder is moved to the ladder's middle, so Bjorn fits through the hole in the floor.
- Ladders stick out one cell above the floor they lead to, so the vikings can step off at the top.
- Two toggles on one target cancel each other (e.g. a plate and a button on the same door) — keep one switch per target.
