#!/usr/bin/perl

#lettura di un file
open($fh, "<", "file1.txt") || die "Impossibile aprire il file";

#prima modalita di lettura -- poco efficiente, carica tutto il file subito
# quando si usano le parentesi angolari il contenuto si "svuota" dal puntatore al file
# quindi se lo devi usare più volte, bisogna metterlo in un array ed usare quello al posto
# del file handle
@array = <$fh>;
print "$_\n" for @array;

#seconda modalita di lettura -- più efficiente poichè carica una linea per volta in memoria
while($line = <$fh>){
    print "$line\n";
}

close $fh;

#scrittura di un file
open($fh2, ">", "file1.txt") || die $1;
print $fh2 "Stringa da stampare";

#chiusura file
close $fh;