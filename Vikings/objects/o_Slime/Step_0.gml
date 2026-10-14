// Turn around at walls and at edges
if (!place_free(x + dir * crawl_speed, y) || place_free(x + dir * 16, y + 1))
{
    dir = -dir;
}

x += dir * crawl_speed;
