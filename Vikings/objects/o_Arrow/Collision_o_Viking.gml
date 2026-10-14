if (other.IsProtectedFrom(id))
{
    audio_play_sound(snd_Block, 1, false);
}
else
{
    other.Die();
}
instance_destroy();
