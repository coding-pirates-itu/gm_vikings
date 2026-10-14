var arrow = instance_create_layer(x + image_xscale * TILE, y, "Instances", o_Arrow);
arrow.hspeed = 6 * image_xscale;
arrow.image_xscale = image_xscale;
audio_play_sound(snd_Arrow, 1, false);

alarm[0] = shoot_delay;
