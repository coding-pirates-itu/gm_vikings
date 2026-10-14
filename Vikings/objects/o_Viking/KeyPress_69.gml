// E = push the button we stand at
if (o_Game.active != object_index)
{
    exit;
}

var button = instance_place(x, y, o_Button);
if (button != noone)
{
    button.Push();
}
