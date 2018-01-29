#!/usr/bin/perl
use warnings;
# This will print "Hello, World"
#print("Hello, world\n");

sub print_arr() {
  my (@arr) = @_;
  foreach $elem (@arr) {
    print "  $elem\n";
  }
}

# create an integer array using the range operator
@arr1 = qw/cheese pepperoni veggie/;

@arr2 = @arr1;

push @arr1, 'works';

print "array1:\n";
&print_arr(@arr1);

print "\narray2:\n";
&print_arr(@arr2);

print("----\n");
