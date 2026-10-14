// is_down is set in the room editor (Variables).
// Make the ladder longer with "Scale Y" in the room editor.
function Toggle()
{
    is_down = !is_down;
    audio_play_sound(snd_Door, 1, false);
}
