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