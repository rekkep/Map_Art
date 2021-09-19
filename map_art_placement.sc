place_map_art() -> (
    global_blocks = read_file('block_placement', 'json');  //load blocks from json
    global_coordinates = read_file('coordinates', 'json'); //load coordinates from json
    global_i = 0;
    global_y = 128;
    place_block() -> ( //places blocks at every coordinat
        set(global_x, global_y, global_z, str(global_blocks:global_i));
        water() -> ( //suportblocks for water (no water spilling)
            //set(global_x, global_y - 1, global_z, 'glass');
            set(global_x + 1, global_y, global_z, 'glass');
            set(global_x, global_y, global_z + 1, 'glass');
            if(global_coordinates:(global_i-1) == 1, set(global_x, global_y, global_z-1, 'glass'));
            if(global_coordinates:(global_i) == -1, set(global_x, global_y-1, global_z, 'glass'));
            if(global_z == -64, set(global_x, global_y, -65, 'glass'))
            );
        //scan(-64,0,-64,64,255,64,set(_,'air'));
        if(global_blocks:global_i == 'glow_lichen[down=true]', set(global_x, global_y, global_z, 'cobblestone'));   //suportblock for lichen
        if(global_blocks:global_i == 'cobblestone_stairs[facing=west,waterlogged=true]', water()); //supportblock for water
        global_y += global_coordinates:global_i;
        global_i += 1;
        if(global_z == 63, global_y = 128);
    );
    //first z -64 to 64 then x+1 and z -64 to 64 until its at 64|64
    c_for(global_x = -64, global_x < 64, global_x += 1, c_for(global_z = -64, global_z < 64, global_z += 1, place_block()));
);
fill_air() -> (
    //fills area with air
    b = block('air'); scan(0,0,0,(-64),255,(-64),set(_,b))
)
