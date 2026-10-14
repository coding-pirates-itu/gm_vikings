// is_on is set in the room editor (Variables).
// Make the laser longer with "Scale Y" in the room editor.
function Toggle()
{
    is_on = !is_on;
    audio_play_sound(snd_Door, 1, false);
}
