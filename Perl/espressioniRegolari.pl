#!/usr/bin/perl

# un espressio regolare è racchiusa tra due '/'

$testo = "Oggi è una brutta giornata";
# il modificatore g fa in modo che controla tutta la stringa, e non si ferma alla prima occorrenza
# di matching con l'espressione regolare
# il modificatore i disattiva il case sensitive
if ($testo =~ /brut/i) {
    print "Pattern verificato"
} else {
    print "Pattern non verificato"
}

print "\n";

# funzioni avanzate
# eseguire comandi shell
# 1 modo
@es = `ls -al`;
print $_ for @es;

#2 modo
@output = qx{ls -ls};
print $_ for @output;

# ---
# sorting hash
%studenti = (
    ale => 1234,
    marco => 3645,
    gianni => 954395
);
print "\nspazio\n";

# sorting per chiavi
for (sort{$a cmp $b} keys %studenti) {
    print "$_ --> $studenti{$_}\n";
}

# sorting per elemento
for (sort{$studenti{$a} cmp $studenti{$b}} keys %studenti) {
    print "$_ --> $studenti{$_}\n";
}

# sort{$a cmp $b} ordine a-z
# sort{$b cmp $a} ordine z-a
# sort{$a <=> $b} le chiavi vengono trasformati in numero e ordinate in ordine crescente
# sort{$a <=> $b} le chiavi vengono trasformati in numero e ordinate in ordine decrescente


# a parita di valore, viene ordinata la chiave
for (sort{$studenti{$a} cmp $studenti{$b} || $a cmp $b} keys %studenti) {
    print "$_ --> $studenti{$_}\n";
}

# splitting di una stringa
$stringa = "ciao:mi:chiamo:marco";
@dati = split(/:/, $stringa);
print "I dati sono @dati\n"