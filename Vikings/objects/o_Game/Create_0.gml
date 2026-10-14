// Which viking listens to the keys: o_Bjorn or o_Kaj
active = o_Bjorn;

// Move the camera towards the active viking.
// amount: 1 = jump there at once, 0.1 = a tenth of the way (smooth)
function MoveCamera(amount)
{
    if (!instance_exists(active))
    {
        return;
    }

    var cam = view_camera[0];
    var w = camera_get_view_width(cam);
    var h = camera_get_view_height(cam);

    // Where the camera wants to be: the viking in the middle, but not outside the room
    var target_x = clamp(active.x - w / 2, 0, room_width - w);
    var target_y = clamp(active.y - h / 2, 0, room_height - h);

    var new_x = lerp(camera_get_view_x(cam), target_x, amount);
    var new_y = lerp(camera_get_view_y(cam), target_y, amount);
    camera_set_view_pos(cam, new_x, new_y);
}
