#!/usr/bin/perl

$file_format = shift || die "Manca la lista dei formati di file da filtrare";
$path = shift or $path = './';
die "Troppi argomenti passati" if $#ARGV >= 0;

$file_format =~ s/--formats=//;
$file_format =~ tr/,/|/;

@files = qx{du -ka "$path"};

%hash_map = ();

for (@files) {
    chomp;
    $hash_map{$2} += $1 if $_ =~ m/^(\d+).+\.($file_format)/;
    $sum += $1;
}

$sum = 0;
foreach (sort {%hash_map{$b} <=> %hash_map{$a} || $a cmp $b } keys %hash_map) {
    print "Estensione: $_\t\t$hash_map{$_}Kb\n";
    $sum += $hash_map{$_};
}

open($fh, ">", 'du.out') || die $!;
print $fh "Totale occupazione disco della carrtella $path: $sum Kb\n";
close $fh;