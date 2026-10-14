draw_self();

// Arrow above the active viking
if (o_Game.active == object_index)
{
    draw_sprite(s_Marker, current_time div 250, x, bbox_top - 6);
}
