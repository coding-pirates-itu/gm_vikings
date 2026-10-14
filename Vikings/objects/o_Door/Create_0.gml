// is_open is set in the room editor (Variables)
image_speed = 0;

function Toggle()
{
    is_open = !is_open;
    audio_play_sound(snd_Door, 1, false);
}
