event_inherited();

walk_speed = 2;    // Bjorn is big and slow

sprite_idle = s_BjornIdle;
sprite_walk = s_BjornWalk;
sprite_climb = s_BjornClimb;
sprite_air = s_BjornIdle;

// The shield protects from everything on the side Bjorn looks at
function IsProtectedFrom(thing)
{
    return sign(thing.x - x) == facing;
}
