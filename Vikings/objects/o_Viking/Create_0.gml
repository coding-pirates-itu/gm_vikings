// Speeds, in pixels per step
walk_speed = 3;
climb_speed = 2;
grav = 1;          // gravity: how much faster we fall every step
vsp = 0;           // vertical speed: < 0 up, > 0 down
facing = 1;        // 1 = right, -1 = left

// Sprites, the children (o_Bjorn, o_Kaj) set their own
sprite_idle = sprite_index;
sprite_walk = sprite_index;
sprite_climb = sprite_index;
sprite_air = sprite_index;

function Die()
{
    instance_create_layer(x, bbox_top + 16, "Instances", o_Poof);
    audio_play_sound(snd_Hit, 1, false);

    // Restart the room in 1 second
    o_Game.alarm[0] = game_get_speed(gamespeed_fps);
    instance_destroy();
}

// Is this viking safe from an arrow or a slime?
// Only Bjorn's shield protects, see o_Bjorn.
function IsProtectedFrom(thing)
{
    return false;
}
