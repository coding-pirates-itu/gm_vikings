// Only the active viking listens to the keys
var move = 0;
var climb = 0;
if (o_Game.active == object_index)
{
    move = keyboard_check(vk_right) - keyboard_check(vk_left);
    climb = keyboard_check(vk_down) - keyboard_check(vk_up);
}

if (move != 0)
{
    facing = move;
    image_xscale = facing;
}

// On a ladder there is no gravity: up and down keys climb
var ladder = instance_place(x, y, o_Ladder);
var on_ladder = (ladder != noone && ladder.is_down);

if (on_ladder)
{
    vsp = climb * climb_speed;

    // Climbing: stand in the middle of the ladder, so we fit through the hole
    if (climb != 0)
    {
        x = ladder.x + TILE / 2;
    }
}
else
{
    vsp = min(vsp + grav, 10);
}

// Walk pixel by pixel, stop in front of solid things
repeat (walk_speed * abs(move))
{
    if (place_free(x + move, y))
    {
        x += move;
    }
}

// Fall (or jump, or climb) pixel by pixel
repeat (abs(vsp))
{
    if (place_free(x, y + sign(vsp)))
    {
        y += sign(vsp);
    }
    else
    {
        vsp = 0;
    }
}

// Choose the picture
if (on_ladder && climb != 0)
{
    sprite_index = sprite_climb;
}
else if (!on_ladder && place_free(x, y + 1))
{
    sprite_index = sprite_air;
}
else if (move != 0)
{
    sprite_index = sprite_walk;
}
else
{
    sprite_index = sprite_idle;
}

// Dangers
if (place_meeting(x, y, o_Spikes))
{
    Die();
    exit;
}

var laser = instance_place(x, y, o_Laser);
if (laser != noone && laser.is_on)
{
    Die();
    exit;
}
