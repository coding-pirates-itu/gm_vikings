if (is_down)
{
    // One ladder piece for every cell
    for (var i = 0; i < image_yscale; i++)
    {
        draw_sprite(s_Ladder, 0, x, y + i * TILE);
    }
}
else
{
    // Rolled up at the top
    draw_sprite(s_LadderRolled, 0, x, y);
}
