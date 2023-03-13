#!/usr/bin/perl

$ingredienti = shift || die "Serve almeno un ingrediente";

print qx{ls ./CartellaRicette};

