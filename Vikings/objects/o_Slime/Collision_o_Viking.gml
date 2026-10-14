if (other.IsProtectedFrom(id))
{
    // Bumped into Bjorn's shield: crawl away
    dir = other.facing;
    x += dir * 4;
}
else
{
    other.Die();
}
