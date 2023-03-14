#!/usr/bin/perl

sub cercaNelFile {
    $nome_file = shift;
    $cartella = shift;
    $contatore = shift;
    %hash_scelta = %{$_[0]};
    @ingredienti = @{$_[1]};

    open($fh, "<", $cartella."/".$nome_file) || die "Impossibile aprire il file";
    
    $nome_file =~ s/.txt//;
    # print "Entrato con nome file = $nome_file\n";
    while ($riga = <$fh>) {
        chomp($riga);
        next if $riga =~ /Ingredienti/;
        last if $riga =~ /Preparazione/;
        for my $ingrediente (@ingredienti) { 
            if ($riga =~ /$ingrediente/) {
                print "$contatore -> $nome_file: $riga\n";
                $hash_scelta{$contatore} = $nome_file;
                $contatore += 1;
            }
        }
    }

    close $fh;
}

sub stampa_procedimento {
    $cartella = shift;
    $nome_file = shift;
    $flag = 0;
    
    print"\n";
    
    open($fh, "<", $cartella."/".$nome_file.".txt") || die "Impossibile aprire il file proc";
    while (<$fh>) {
        $flag = 1 if($_ =~ /Preparazione/);
        print $_ unless ($flag == 0);
    }

    print"\n";
    close $fh;
}

$cartella = "./CartellaRicette";
$ingrediente = shift || die "Almeno un argomento";
push @ingredienti, $ingrediente;

while ($#ARGV >= 0) {
    $ingrediente = shift;
    push @ingredienti, $ingrediente;
}

@ricette = qx{ls $cartella};
chomp for (@ricette);
$contatore = 1;
%hash_scelta = ();
cercaNelFile($_, $cartella, $contatore, \%hash_scelta, \@ingredienti) for (@ricette);

for (keys %hash_scelta) {
    print "chiave = $_ -- valore = $hash_scelta{$_}\n";
}

print "Scegli la ricetta di cui vedere il procedimento: ";
$risposta = <STDIN>;
unless ($risponta <= 0 || $risposta > $contatore || $risposta cmp "END") {
    chomp($risposta);
    stampa_procedimento($cartella, $hash_scelta{$risposta});
}
