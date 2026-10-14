// target is set in the room editor (double-click the instance -> Variables),
// for example door_1. It must have a Toggle() function.
is_on = false;
image_speed = 0;

function Push()
{
    is_on = !is_on;
    image_index = is_on;
    audio_play_sound(snd_Click, 1, false);
    target.Toggle();
}
