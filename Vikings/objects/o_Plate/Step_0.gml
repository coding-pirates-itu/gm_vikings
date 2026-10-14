// Toggle the target when a viking steps on the plate, and again when it steps off
var someone_on_me = place_meeting(x, y, o_Viking);

if (someone_on_me != pressed)
{
    pressed = someone_on_me;
    image_index = pressed;
    audio_play_sound(snd_Click, 1, false);
    target.Toggle();
}
