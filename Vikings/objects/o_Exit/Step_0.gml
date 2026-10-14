// Both vikings must be inside the exit
if (place_meeting(x, y, o_Bjorn) && place_meeting(x, y, o_Kaj))
{
    audio_play_sound(snd_Win, 1, false);
    room_goto_next();
}
