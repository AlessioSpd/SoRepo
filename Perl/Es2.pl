#!/usr/bin/perl
use 5.010;
no warnings 'experimental';

%rubrica = ();
$ris = 0;

while($ris != 5) {
	print "Scegli un'opzione:\n1.Aggiungi contatto\n2.Elimina Contatto\n3.Cerca contatto\n4.Mostra rubrica\n5.Esci\n";
	$ris = <STDIN>;
	
	given ($ris) {
		when($_ == 1) {
			print "Inserisci i dati del nuovo contatto:\nNome completo: ";
			$nomeContatto = <STDIN>;
			print "Numero di telefono: ";
			$numeroContatto = <STDIN>;
			chomp($nomeContatto);
			chomp($numeroContatto);
			$rubrica{$nomeContatto} = $numeroContatto;
			print "\n";
		}
		
		when ($_ == 2) {
			$cont = 0;
			print "\nLista dei contatti:\n---------------\n";
			for my $it (keys %rubrica) {
				print ++$cont." - Nome: ".$it." - Numero: ".$rubrica{$it}."\n";
			}
			print "---------------\nScegli il numero associato al contatto che vuoi eliminare: ";
			$input = <STDIN>;
			if ($input > 0 && $input <= $cont) {
				$cont = 0;
				for my $it (keys %rubrica) {
					if(++$cont == $input) {
						delete($rubrica{$it});
						print "Contatto eliminato\n";
					}
				}
			} else {
				print "Indice non valido\n";
			}
		}
		
		when ($_ == 4) {
			print "\n---------------\n";
			for my $it (keys %rubrica) {
				print "Nome: ".$it." - Numero: ".$rubrica{$it}."\n";
			}
			print "---------------\n\n";
		}
	}
}
