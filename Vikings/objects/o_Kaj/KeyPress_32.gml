// Space = jump, only from the ground
if (o_Game.active != object_index)
{
    exit;
}

if (!place_free(x, y + 1))
{
    vsp = -jump_speed;
    audio_play_sound(snd_Jump, 1, false);
}
