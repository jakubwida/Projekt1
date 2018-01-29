#!/usr/bin/perl
use warnings;

# @size
sub generate_block
	{
	local @size = @_;
	@outarr = ();
	for ($i=0;$i<$size[1];$i++)
		{
		for ($j=0;$j<$size[0];$j++)
			{
			push(@outarr,"w");
			}
		}
	return @outarr;
	}


# \@size \@block
sub print_block
	{
	local $size = @{$_[0]};
	local @arr = @{$_[1]};
	#print("$size @arr \n");
	local $counter = 0;

	foreach my $x (@arr)
		{
		$counter += 1;
		print("$x");
		if($counter == $size[0])
			{
			print("\n");
			$counter = 0;
			}
		}
	}



# \@size, \@block, \@set_coords, $char
sub set_in_block
	{
	local @size = @{$_[0]};
	local @arr = @{$_[1]};
	local @coords = @{$_[2]};
	local $elem = $_[3];
	if (($coords[0] >= 0) and ($coords[0] < $size[0]) and ($coords[1] >= 0) and ($coords[1] < $size[1]))
		{
		local $x = $coords[0] + $coords[1] * $size[0];
		@arr[$x] = $elem;
		}
	return @arr;
	}


# \@size, \@block, \@set_coords
sub get_in_block
	{
	local @size = @{$_[0]};
	local @arr = @{$_[1]};
	local @coords = @{$_[2]};
	local $elem = $_[3];
	if (($coords[0] >= 0) and ($coords[0] < $size[0]) and ($coords[1] >= 0) and ($coords[1] < $size[1]))
		{
		local $x = $coords[0] + $coords[1] * $size[0];
		return $arr[$x];
		}
	return "0";
	}

=begin comment
@size = (5,10);
@arr = generate_block(@size);
print_block(\@size,\@arr);
@coords = (1,2);
@arr = set_in_block(\@size,\@arr,\@coords,"5");
print_block(\@size,\@arr);
print(get_in_block(\@size,\@arr,\@coords));
=cut

#will need an overhaul to add multi-step

# \@size, \@block, \@current_coords // returns \@block, \@current_coords
sub walk_randomly
	{
	local @size = @{$_[0]};
	local @arr = @{$_[1]};
	local @curr_coords = @{$_[2]};
	local $is_updown = $_[3];
	local @possible_transp = ([1,0],[-1,0]);
	if( $is_updown == 1)
		{
		@possible_transp = ([1,0],[-1,0]);
		$is_updown =0;
		}
	else
		{
		@possible_transp = ([0,1],[0,-1]);
		$is_updown =1;
		}
	local @transpos = @{$possible_transp[rand @possible_transp]};

	local @possible_step_len = (1,2,4,6,6,8,12,12,18,24,32);
	local $step_len = $possible_step_len[rand @possible_step_len];
	#print("len $step_len coords @curr_coords \n");

	local $out = 0;
	local $counter = 0;

	while($out == 0 or $counter == 8)
		{
		$counter +=1;
		local @transpos = @{$possible_transp[rand @possible_transp]};
		local @possible_coords = ($curr_coords[0]+$transpos[0]*$step_len,$curr_coords[1]+$transpos[1]*$step_len);
		local $possible_target = get_in_block(\@size,\@arr,\@possible_coords);
		if (($possible_target ne " ") and ($possible_target ne "-1"))
			{
			$out = 1;
			}
		}

	for(my $i =0; $i<$step_len;$i++)
		{

			local @new_coords = ($curr_coords[0]+$transpos[0],$curr_coords[1]+$transpos[1]);
			local $target = get_in_block(\@size,\@arr,\@new_coords);
			if($target ne -1)
				{
				@arr = set_in_block(\@size,\@arr,\@new_coords," ");
				@curr_coords = @new_coords;
				#print("--\n");
				#print_block(\@size,\@arr);
				}
			else
				{
				$i = $step_len;
				}

		}
	return((\@arr,\@curr_coords,$is_updown))
	}

=begin comment
@size = (80,30);
@arr = generate_block(@size);
@curr_coords = (3,3);
print_block(\@size,\@arr);
print(" --- \n");
$updown = 1;
for(my $i=0;$i<100;$i++)
	{
	@out = walk_randomly(\@size,\@arr,\@curr_coords,$updown);
	@arr = @{@out[0]};
	@curr_coords = @{@out[1]};
	$updown = @{@out[2]};
	}

print_block(\@size,\@arr);

=cut
