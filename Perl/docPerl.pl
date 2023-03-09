#!/usr/bin/perl

# use warnings;

print "ciao\n";

my $variabile_scalare = "Ciao";
my @array = (23, 42, 69);
my %array_associativo = (
    1 => "A",
    2 => "B"
);

#Stringhe
my $name = 'Stringa';
my $reminder = 'lab 21' . 'lun';

# print $reminder;

my $name = undef; # non necessario
my $rank; # assegnata ad undef

my @fibonacci = (1, 2, 3, 4, 5, "ciao"); # lista multi tipo
print $#fibonacci."\n"; # ritorno l ultimo indice, in pratica la size della lista

#aggiunta di elemnti alla lista
my @meals;
push @meals, ('hamburgers', "savuzizza", "patate_mbacchiuse");
print "@meals\n";

# eliminazione ultimo elemento dall array
pop @meals;
print "@meals\n";

#inserimento in testa
unshift @meals, ("scarola", "piparieddi");
print "@meals\n";

#eliminazione in testa
shift @meals;
print "@meals\n";

#aggiunta di un elemento ad un hash
my %hash = (
    Francesco => "patate",
    Giovanni => "savuzzizza"
);
print %hash;
print "\n";
$hash{Alessio} = 'Piparieddi';
print %hash; 
print "\n";

#esempi di context
my $zip_code = 87024;
my $city_zip = 'Fuscaldo, CS ' . $zip_code;
print $city_zip . "\n";

# -- 
my $call_sign = 'KBMIZ';
# aggiorna la var e ritorna un nuovo valore
my $next_sign = ++$call_sign;
print "next: $next_sign\n";
print "call: $call_sign\n";
# ritorna il vecchio valore e poi aggiorna
my $curr_sign = $call_sign++;

my @gatti = ('a','b','c');

my $first_cat = $gatti[0];
print "firstcat: $first_cat\n";

#assegnamento scalare
my $num_gatti = @gatti;
print "numgatti: $num_gatti\n";

#concatenzazione di string
print 'Posseggo '.@gatti." gatti!\n"

# trovare gli elementi univoci in una lista
my %uniq;
my @uniques = keys %uniq;