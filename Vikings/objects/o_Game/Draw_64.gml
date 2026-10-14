draw_set_font(fnt_Hud);
draw_set_halign(fa_left);
draw_set_valign(fa_top);

if (active == o_Bjorn)
{
    draw_set_colour(c_red);
    draw_text(16, 8, "Bjorn");
}
else
{
    draw_set_colour(c_lime);
    draw_text(16, 8, "Kaj");
}

draw_set_colour(c_white);
draw_text_transformed(140, 18, "Tab: switch   E: push button   Kaj: Space = jump, F = throw   R: restart", 0.5, 0.5, 0);
