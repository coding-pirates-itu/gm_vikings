// F = throw a stone, only one at a time
if (o_Game.active != object_index || instance_exists(o_Stone))
{
    exit;
}

var stone = instance_create_layer(x + facing * 10, y - 24, "Instances", o_Stone);
stone.hspeed = 6 * facing;
stone.vspeed = -6;
stone.gravity = 0.25;
audio_play_sound(snd_Throw, 1, false);
