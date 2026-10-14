// Hit a wall or a closed door: gone
if (!place_free(x, y))
{
    instance_destroy();
}
