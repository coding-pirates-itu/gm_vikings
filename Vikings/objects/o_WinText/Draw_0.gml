// Big Bjorn (this instance) and big Kaj
draw_self();
draw_sprite_ext(s_KajIdle, image_index, x + 160, y, 4, 4, 0, c_white, 1);

draw_set_halign(fa_center);
draw_set_valign(fa_middle);

draw_set_font(fnt_Win);
draw_set_colour(c_yellow);
draw_text(room_width / 2, y + 80, "You win!");

draw_set_font(fnt_Hud);
draw_set_colour(c_white);
draw_text(room_width / 2, y + 170, "Press Enter to play again");
