#!/usr/bin/perl

$file = shift if $#ARGV >= 0;

unless ($file) {
    @ls = qx{ls /usr/include};
    sort @ls;
    for (@ls) {
        chomp;
        print "$_\n" if $_ =~ /.h/;
    }
} else {
    @cat = qx{cat /usr/include/$file};
    @risultati = ();
    $flag = 1;
    $temp = "";
    for (@cat) {
        chomp;
        if ($_ =~ /\/\*(.*)\*\//) {
            # print "Ho trovato il commento completo:\n\t$1\n";
            push @risultati, $1;
        } elsif ($flag == 1 && $_ =~ /\/\*/ && $_ !~ /\*\//) {
            $_ =~ s/\/\* //;
            $temp = $_;
            $flag = 0;
            # print "Ho trovato il commento parziale iniziale:\n\t$temp\n";
        } elsif ($flag == 0 && $_ =~ /\*\//) {
            $flag = 1;
            $_ =~ s/\*\///;
            $temp = $temp.$_;
            # print "Ho trovato il commento parziale finale:\n\t$_\n";
            # print "Commento completo:\n\t$temp\n";
            push @risultati, $temp;
            $temp = "";
        } elsif ($flag == 0 && $_ !~ /\/\*/ && $_ !~ /\*\//) {
            # print "Ho trovato parte interna del commento parziale\n\t$_\n";
            $temp = $temp.$_;
        }
    }

    print "$_\n\n" for (@risultati);
}