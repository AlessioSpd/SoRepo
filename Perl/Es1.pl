#!/usr/bin/perl

use Scalar::Util qw(looks_like_number);
my $num1 = <STDIN>;
my $num2 = <STDIN>;

if (looks_like_number($num1) && looks_like_number($num2)){
    print "somma: ".somma($num1+$num2)." diff: ".differenza($num1-$num2)."\n";
}

# con subroutine
sub somma {
    ($first, $second) = @_;
    my $res = $first + $second;
}

sub differenza {
    ($first, $second) = @_;
    my $res = $first - $second;
}

print "\n Inserisci un arry di numeri, per terminare -1\n";

$input = <STDIN>;
@array = ();

while ($input != -1) {
    push @array, $input;
    $input = <STDIN>;
}

print "Hai inserito ". ($#array + 1) . " elementi\n";

$sum = 0;

for(@array) { $sum += $_ }

print "La somma degli elementi è ".$sum."\n";