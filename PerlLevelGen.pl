#!/usr/bin/perl
#use warnings;

# \@coords_1, \@_coords2   ->   returns hash object (not reference)
sub generate_room
	{
	my @coords_1 = @{$_[0]};
	my @coords_2 = @{$_[1]};

	#print("@coords_2 \n");

	my @xarr = sort({ $a <=> $b } ($coords_1[0],$coords_2[0]));
	my @yarr = sort({ $a <=> $b } ($coords_1[1],$coords_2[1]));

	my @c_1 = ($xarr[0],$yarr[0]);
	my @c_2 = ($xarr[1],$yarr[1]);

	#print("@c_1 @c_2 \n");

	my @b_1 = ($xarr[0]-1,$yarr[0]-1);
	my @b_2 = ($xarr[0]+1,$yarr[0]+1);

	my @center = (($c_1[0]-$c_1[0])/2.0,($c_1[1]-$c_1[1])/2.0);

	my $area = abs(($c_2[0]-$c_1[0])*($c_2[1]-$c_1[1]));

	#print("$area \n");
	my %reff = ("coords_1"=>\@c_1,"coords_2"=>\@c_2,"boundry_1"=>\@b_1,"boundry_2"=>\@b_2, "area"=>$area,"center"=>\@center);

	#print("@{$reff{coords_1}} \n");

	return %reff;
	}

=begin comment
@c1 = (0,0);
@c2 = (5,5);
%room = generate_room(\@c1,\@c2);
	print("@{$room{boundry_1}} \n");
=cut

# \@coords_1, \@coords_2, \@other_coords_1, \@other_coords_2 ,where coords_1 are both smaller than _2. only takes coords, not boundry - put it in manually to achieve the collision check.
sub check_collision
	{
	my @c_1 = @{$_[0]};
	my @c_2 = @{$_[1]};
	my @o_1 = @{$_[2]};
	my @o_2 = @{$_[3]};

	#print("@c_1 @c_2 @o_1 @o_2 \n");

	if( $c_1[0] <= $o_2[0] and $c_2[0] >= $o_1[0] and $c_1[1] <= $o_2[1] and $c_2[1] >= $o_1[1] )
		{
		return 1;
		}
	else
		{
		return 0;
		}
	}

#same as above, but takes in: %room_1, %room_2
sub check_room_collision
	{
	my $rr1 = $_[0];
	my $rr2 = $_[1];

	my %r_1 = %$rr1;
	my %r_2 = %$rr2;

	my @keyos = keys(%r_1);
	my @keyos2 = keys(%r_2);

	my $c_1 = $r_1{coords_1};
	my $c_2 = $r_1{coords_2};

	my $c_3 = $r_2{coords_1};
	my $c_4 = $r_2{coords_2};



	return check_collision($c_1,$c_2,$c_3,$c_4);
	}

=begin comment

@c_1 = (0,0);
@c_2 = (5,5);
%room1 = generate_room(\@c_1,\@c_2);

@c_3 = (5,5);
@c_4 = (8,8);
%room2 = generate_room(\@c_3,\@c_4);

#print("@{$room1{coords_1}} \n");

$val = check_collision(\@c_1,\@c_2,\@c_3,\@c_4);
print("$val");
$ref1 = \%room1;
$ref2 = \%room2;
$val2 = check_room_collision($ref1,$ref2);
print("$val2");
=cut

#generates list of possibly colliding rooms.
# /@size, $target_area = 0 to 1, jako część całego area
sub generate_any_rooms
	{
	my @size = @{$_[0]};
	my $area_part = $_[1];

	my $total_area = $size[0] * $size[1];
	my $target_area = int($total_area * $area_part);
	my $covered_area = 0;

	my @room_list = ();

	while($covered_area < $target_area)
		{
		print("$covered_area \n");
		my $newx1 = int(rand($size[0]));
		my $newx2 = int(rand($size[0]));
		my $newy1 = int(rand($size[1]));
		my $newy2 = int(rand($size[1]));

		my @coords_1 = ($newx1,$newy1);
		my @coords_2 = ($newx2,$newy2);

		%new_room = generate_room(\@coords_1,\@coords_2);
		$new_area = $new_room{"area"};
		$covered_area += $new_area;
		print(" added area $new_area \n");
		push(@room_list,\%new_room);
		}

	return @room_list;
	}

#@size = (10,40);
#generate_any_rooms(\@size,0.5);

# /@size, $target_area = 0 to 1, jako część całego area
sub generate_non_colliding_rooms
	{
	my @size = @{$_[0]};
	my $area_part = $_[1];

	my $total_area = $size[0] * $size[1];
	my $target_area = int($total_area * $area_part);
	my $covered_area = 0;

	my @room_list = ();

	while($covered_area < $target_area)
		{
		print("$covered_area \n");
		my $newx1 = int(rand($size[0]));
		my $newx2 = int(rand($size[0]));
		my $newy1 = int(rand($size[1]));
		my $newy2 = int(rand($size[1]));

		my @coords_1 = ($newx1,$newy1);
		my @coords_2 = ($newx2,$newy2);

		%new_room = generate_room(\@coords_1,\@coords_2);
		$passes = 1;
		$new_room_ref = \%new_room;


		foreach $room (@room_list)
			{
			if(check_room_collision($room,$new_room_ref))
				{
				$passes = 0;
				}
			}
		if($passes == 1)
			{
			$new_area = $new_room{"area"};
			$covered_area += $new_area;
			print(" added area $new_area \n");
			push(@room_list,\%new_room);
			}
		}

	return @room_list;
	}

#@size = (10,40);
#generate_non_colliding_rooms(\@size,0.5);

# /@size, $target_area = 0 to 1, jako część całego area
sub generate_colliding_rooms
	{
	my @size = @{$_[0]};
	my $area_part = $_[1];

	my $total_area = $size[0] * $size[1];
	my $target_area = int($total_area * $area_part);
	my $covered_area = 0;

	my @room_list = ();
	my $passes = 1;

	my $block = generate_block(\@size,".");
	#print("$$block \n");

	while($covered_area < $target_area)
		{
		#print("passes: $passes covered area: $covered_area / $target_area \n");

		my $area = 100;
		my $new_room_ref = {};
		my %new_room = ();
		while($area > 50)
			{
			my $newx1 = int(rand($size[0]-13)+1);
			my $newx2 = int(rand(12))+$newx1;
			my $newy1 = int(rand($size[1]-7)+1);
			my $newy2 = int(rand(6))+$newy1;

			my @coords_1 = ($newx1,$newy1);
			my @coords_2 = ($newx2,$newy2);

			%new_room = generate_room(\@coords_1,\@coords_2);

			$new_room_ref = \%new_room;

			$area = $new_room{'area'};
			}

		foreach $room (@room_list)
			{
			if(check_room_collision($room,$new_room_ref))
				{
				$passes = 1;
				}
			}

		if($passes == 1)
			{
			$block = print_room_on_block($new_room_ref,$block,\@size);
			$covered_area = ($$block =~ tr/' '//);

			#my $covered_area += $new_area;
			#print(" added area $covered_area \n");
			push(@room_list,\%new_room);

			}

			#print_block($block,$size);

			$passes = 0;
		}

	return @room_list;
	}



#\@size, $character returns \$block
sub generate_block
	{
	my @size = @{$_[0]};
	my $x = $size[0];
	my $y = $size[1];
	my $char = $_[1];
	#print("hello? @size  $x $y $char \n ");
	my $out = $char x ($x * $y);
	#print("$out ");
	return \$out
	}

# \$block, \@size
sub print_block
	{
	my @size = @{$_[1]};
	my $block = ${$_[0]};

	my $x = $size[0];
	my $y = $size[1];
	#print(" $x $y \n");

	for($i = 0; $i<$y; $i++)
		{
		$a = $i*$x;
		$b = ($i*$x)+$x;

		#print(" $a $b \n");
		print(substr($block,$i*$x,$x));
		print("\n");
		}
	}

#@size = (10,20);
#$sref = \@size;
#$block_ref = generate_block($sref,".");

#print(" $$block_ref \n");

#print_block($block_ref,\@size);

# \@size, \@coords  returns $coord_int
sub block_coord
	{
	my @size = @{$_[0]};
	my @coords = @{$_[1]};

	return ($size[0] * $coords[1]) + $coords[0];
	}
#\$block, \@size, \@coords, $character
sub set_in_block
	{
	my $block = ${$_[0]};
	my @size = @{$_[1]};
	my @coords = @{$_[2]};
	my $character = $_[3];

	my $block_coord = block_coord(\@size,\@coords);

	#print(" $block_coord \n");

	substr($block,$block_coord,1) =$character ;
	return \$block;
	}

=begin comment
@size = (10,20);
$sref = \@size;
$block_ref = generate_block($sref,".");
print_block($block_ref, $sref);
$newblock = set_in_block($block_ref,$sref,[5,2],"W");
print_block($newblock, $sref);
=cut


# \%room, \$block, \@size   returns \$printed_block
sub print_room_on_block
	{
	my %room = %{$_[0]};
	my $block = $_[1];
	my @size = @{$_[2]};

	my @coords1 = @{$room{"coords_1"}};
	my @coords2 = @{$room{"coords_2"}};

	#print("@coords1 @coords2 \n");
	#print(($coords1[0]..$coords2[0]));

	foreach $x(($coords1[0]..$coords2[0]))
		{
		foreach $y(($coords1[1]..$coords2[1]))
			{
			my @new_coords = ($x,$y);
			$block = set_in_block($block,\@size,\@new_coords," ");
			}
		}
	return $block;
	}

=begin comment
$size = [80,30];
@room_list = generate_colliding_rooms($size,0.6);
$block = generate_block($size,".");
#print_block($block,$size);
print("---\n");
foreach $room(@room_list)
	{
	$block = print_room_on_block($room,$block,$size);
	}
print_block($block,$size);
=cut
#TODO: 1. generator niekoludujących pokojów
# 2. generator wycinanych pokojów, celowo kolidujących.




#this function is what counts

# \@size returns \$bloc
sub generate_text_room
	{
	my @size = @{$_[0]};

	my @room_list = generate_colliding_rooms(\@size,0.6);
	my $block = generate_block(\@size,".");

	foreach $room(@room_list)
		{
		$block = print_room_on_block($room,$block,\@size);
		}

	return $block;
	}

#$block = generate_text_room([80,32]);
#print_block($block);






# mangler - does inserting all objects.

# \$block, \@size returns \@coord_list <listę wolnych miejsc>
sub block_to_list_of_coords
	{
	my $block = $_[0];
	my @size = @{$_[1]};
	my @coord_list = ();

	my @out_list = ();

	for($i=0; $i<$size[1]; $i++)
		{
		for($j=0; $j<$size[0]; $j++)
			{
			my @coords = ($j,$i);
			#print("coords @coords \n");
			my $block_coor = block_coord(\@size,\@coords);

			my $lenn = length($$block);
			#print("block coord $block_coor total $lenn \n");
			#print("$$block \n");

			my $char = substr($$block, $block_coor, 1);

			if($char eq " ")
				{
				my $passed = "$j" . "_" . "$i";
				push(@out_list,$passed);
				}
			}
		}
	return \@out_list;
	}

=begin
@size = (80,32);
$block = generate_text_room(\@size);
#print_block($block,[80,32]);

$out_list_ref = block_to_list_of_coords($block,[80,32]);
foreach $elem(@{$out_list_ref})
	{
	print("$elem \n");
	}
=cut

# $coord_string  -> @(x,y)
sub str_c_to_arr
	{
	my $input = $_[0];

	my @out_list = split(/_/,$input);
	@out_list = (int($out_list[0]),int($out_list[1]));
	return @out_list;
	}

# \$block \@string_coord_list \@object_size $char \@size  --> \@(\$block, \@string_coord_list)
sub generate_fielded_object
	{
	my $block_ref = $_[0];
	my @str_coord_list = @{$_[1]};
	my @obj_size = @{$_[2]};
	my $char = $_[3];
	my @size = @{$_[4]};



	while(1==1)
		{
		#print("@str_coord_list \n");

		my $random_index = rand(@str_coord_list);
		my @coords = str_c_to_arr($str_coord_list[$random_index]);

		my @str_potential_targets = ();
		for($i=0; $i<$obj_size[1]; $i++ )
			{
			for($j=0; $j<$obj_size[0]; $j++ )
				{
				my $x = $j+$coords[0];
				my $y = $i+$coords[1];
				my $passed = "$x" . "_" . "$y";
				push(@str_potential_targets,$passed);
				}
			}
		#print("potential targets @str_potential_targets \n");

		my @index_list = ();
		my $flag = 1;
		foreach $target(@str_potential_targets)
			{
			#print("checkin: $target \n");
			$flag = 0;
			for($i=0; $i<scalar(@str_coord_list); $i++ )
				{
				if($str_coord_list[$i] eq $target)
					{
					#print("$str_coord_list[$i] \n");
					push(@index_list,$i);
					$flag = 1;
					last;
					}
				}
			#print("flag $flag \n");
			if($flag == 0)
				{

				last;
				}
			}

		if($flag == 1)
			{
			my @target_coords = ($coords[0]+int($obj_size[0]/2),$coords[1]+int($obj_size[1]/2));
			#print("target coord:  @target_coords \n");

			my $block_ref = set_in_block($block_ref,\@size,\@target_coords,$char);

			@index_list = sort { $a <=> $b } @index_list;
			@index_list = reverse(@index_list);
			foreach $index(@index_list)
				{
				splice(@str_coord_list,$index,1);
				}
			return (\@str_coord_list,$block_ref);
			}

		}

	}

=begin co
@size = (80,32);
$block = generate_text_room(\@size);
#print_block($block,[80,32]);
$coord_list_ref = block_to_list_of_coords($block,\@size);

print(scalar(@$coord_list_ref));
print("\n");

@out = generate_fielded_object($block,$coord_list_ref,[10,10],"p",\@size);
$coord_list_ref = $out[0];

print(scalar(@$coord_list_ref));
print("\n");

$nblock = $out[1];
print_block($nblock,\@size);
=cut


# \@size $depth
sub generate_actors_to_room
	{
	my @size = @{$_[0]};
	my $depth = $_[1];

	my $block = generate_text_room(\@size);
	my $coord_list_ref = block_to_list_of_coords($block,\@size);

	#player
	my @out = generate_fielded_object($block,$coord_list_ref,[13,13],"p",\@size);
	my $block = $out[1];
	my $coord_list_ref = $out[0];

	#exit
	my @out = generate_fielded_object($block,$coord_list_ref,[3,3],"e",\@size);
	my $block = $out[1];
	my $coord_list_ref = $out[0];

	#others:
	my $danger_level = $depth * 2;
	my $weapon_num = 3;
	my $health_level = 3+int($depth/4);

	#print("$danger_level $weapon_num $health_level \n");

	my @baddie_dict = ("x","x","x","X","X","C","C","C","A","M");
	my @baddie_danger_dict = (1,1,1,2,2,3,3,3,5,8);

	while($danger_level > 0)
		{
		while(1==1)
			{
			$new_index = rand(@baddie_dict);
			$new_baddie = $baddie_dict[$new_index];
			$new_danger_level = $baddie_danger_dict[$new_index];

			if($new_danger_level <= $danger_level)
				{
				last;
				}
			}
		$danger_level -= $new_danger_level;

		my @out = generate_fielded_object($block,$coord_list_ref,[1,1],$new_baddie,\@size);
		$block = $out[1];
		$coord_list_ref = $out[0];
		}

	for(my $i=0;$i<$health_level;$i++)
		{
		my @out = generate_fielded_object($block,$coord_list_ref,[1,1],"+",\@size);
		#print("health $i $health_level \n");
		$block = $out[1];
		$coord_list_ref = $out[0];
		}

	@weapon_list = ("m","g","s","r");

	for(my $i=0;$i<$weapon_num;$i++)
		{

		my $random_weapon = @weapon_list[rand(@weapon_list)];
		#print("$random_weapon $i $weapon_num \n");

		my @out = generate_fielded_object($block,$coord_list_ref,[1,1],$random_weapon,\@size);
		$block = $out[1];
		$coord_list_ref = $out[0];
		}

	return $block;
	}




# \$block \@size  -> (\@player_coords, \@list_of_references to ($str,$x,$y) of actors);
sub translate_to_python
	{
	my $block = ${$_[0]};
	my @size = @{$_[1]};

	my $len = length($block);

	my @actor_ref_list = ();
	my @player_coords =();
	my %actor_dict = ("."=>"w","e"=>"we", "x"=>"bm","X"=>"bM","C"=>"bc","A"=>"ba","M"=>"bmo", "+"=>"p+","m"=>"pm","s"=>"ps","g"=>"pg","r"=>"pr");


	for($i=0;$i<$len;$i++)
		{
		$tblock = $block;
		my $char = substr($tblock, $i, 1);
		my $x = $i % $size[0];
		my $y = int(($i - $x) / $size[0]);
		if($char eq "p" )
			{
			@player_coords = ($x,$y);
			}
		elsif($char ne " ")
			{
			my @new_actor = ($actor_dict{$char},$x,$y);
			#print("$char \n");
			#print("new actor: @new_actor \n");
			push(@actor_ref_list,\@new_actor);
			}
		}

	return(\@player_coords,\@actor_ref_list)
	}
=begin
@size = (80,32);
$block = generate_actors_to_room(\@size,5);
@outo = translate_to_python($block,\@size);
@actors = @{$outo[1]};
#foreach $actor_ref(@actors)
#	{
#	print("@$actor_ref \n");
#	}
=cut

# \@size \$filename \$weapon $health $depth
sub generate_level_write
	{
	my @size = @{$_[0]};
	my $filename = ${$_[1]};
	my $weapon = ${$_[2]};
	my $health = $_[3];
	my $depth = $_[4];

	my $block = generate_actors_to_room(\@size,$depth);
	my @outo = translate_to_python($block,\@size);

	my @actors = @{$outo[1]};
	my @player_coords = @{$outo[0]};

	open(my $fh, '>', $filename);

	print ($fh "\@property\n");
	my $x = $size[0];
	my $y = $size[1]+5; #!!!!!!!!
	print ($fh "size_x $x\n");
	print ($fh "size_y $y\n");
	print ($fh "depth $depth\n");

	print ($fh "\@player\n");
	my $px = $player_coords[0];
	my $py = $player_coords[1];
	print ($fh "x $px\n");
	print ($fh "y $py\n");
	print ($fh "weapon $weapon\n");
	print ($fh "health $health\n");

	print ($fh "\@actor\n");
	foreach $actor_ref(@actors)
		{
		my @arro = @{$actor_ref};
		my $actor_str = @arro[0];
		my $actor_x = @arro[1];
		my $actor_y = @arro[2];
		print ($fh "$actor_str $actor_x $actor_y\n");
		}

	close $fh;
	}
=begin
@size = (80,27);
$filename = "last_level.txt";
$weapon = "m";
$health = 3;
$depth = 2;
generate_level_write(\@size,\$filename,\$weapon,$health,$depth);
=cut

my ($xsize, $ysize, $filename, $weapon, $health, $depth) = @ARGV;

if($xsize eq "-h" )
{
print("This script is not ment to be executed on it's own - it is launched by GameLauncher.py. \nIt will now quit \n");
exit 0;
}

@size = ($xsize,$ysize);
generate_level_write(\@size,\$filename,\$weapon,$health,$depth);
