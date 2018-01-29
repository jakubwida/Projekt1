#!/usr/bin/perl
use warnings;

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
# \%room, \$block, \@size   returns \$printed_block
sub print_empty_room_on_block
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
		my @new_coords = ($x,$coords1[1]);
		$block = set_in_block($block,\@size,\@new_coords,"R");
		my @new_coords = ($x,$coords2[1]);
		$block = set_in_block($block,\@size,\@new_coords,"R");
		}

	foreach $y(($coords1[1]..$coords2[1]))
		{
		my @new_coords = ($coords1[0],$y);
		$block = set_in_block($block,\@size,\@new_coords,"R");
		my @new_coords = ($coords2[0],$y);
		$block = set_in_block($block,\@size,\@new_coords,"R");
		}

	my @choicearray = (0,1,2,3);
	my $randomwall = $choicearray[rand @choicearray];


	if($randomwall == 0)
		{
		foreach $x((($coords1[0]+1)..$coords2[0]-1))
			{
			my @new_coords = ($x,$coords1[1]);
			$block = set_in_block($block,\@size,\@new_coords," ");
			}
		}
	elsif($randomwall == 1)
		{
		foreach $x((($coords1[0]+1)..($coords2[0]-1)))
			{
			my @new_coords = ($x,$coords2[1]);
			$block = set_in_block($block,\@size,\@new_coords," ");
			}
		}
	elsif($randomwall == 2)
		{
		foreach $y((($coords1[1]+1)..($coords2[1]-1)))
			{
			my @new_coords = ($coords1[0],$y);
			$block = set_in_block($block,\@size,\@new_coords," ");
			}
		}
	elsif($randomwall == 3)
		{
		foreach $y((($coords1[1]+1)..($coords2[1]-1)))
			{
			my @new_coords = ($coords2[0],$y);
			$block = set_in_block($block,\@size,\@new_coords," ");
			}
		}


	return $block;
	}
=cut

=begin comment
%room = generate_room([5,5],[7,15]);
$block = generate_block([20,30]," ");
$block1 = print_room_on_block(\%room,$block,[20,30]);
print_block($block1,[20,30]);

$block2 = print_empty_room_on_block(\%room,$block,[20,30]);
print_block($block2,[20,30]);
=cut

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

#TODO:
#inserter of actors. however simple it may be.
#plan is to use block_to_list_of_coords to create list of all free coords.
#choose at random from it and remove neighbors that dont work as intended
