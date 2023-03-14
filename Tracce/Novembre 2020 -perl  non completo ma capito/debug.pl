#!/usr/bin/perl
# wlp4s0

sub ifconfig {
    $device = shift;
    # eseguo il comando shell e mi salvo il risultato all'interno di una variabile
    # non un array, cosi mi viene piu semplice cercare con le regex
    $res = qx{ifconfig $device};
    $res =~ m/inet\s((?:\d{1,3}\.){3}\d{1,3})/;
    return $1;       
}

sub arp {
    @res = qx{arp -n};
    %arp_map = ();

    foreach (@res) {
        m/^((?:\d{1,3}\.){3}\d{1,3})/;
        chomp($1);
        next if ($1 eq "");
        $arp_map{$1} = 0;
    }
    
    return %arp_map;
}

$device = shift || die "É obbligatorio almeno un operatore";
die "Troppi parametri bro" if $#ARGV >= 0;

$myIp = ifconfig($device);
print "Local Ip = $myIp\n";

%ip_hash = arp();

foreach (keys %ip_hash){
    print "$_ -- $ip_hash{$_}\n";
}

print "\n";

@netstat = qx{netstat -tupan};

for (@netstat) {
    chomp;
    @splitted = split(" ", $_);
    @ip = split(":", $splitted[3]);
    next if (@ip[0] eq "");

    for $ip (keys %ip_hash) {
        if ($ip eq @ip[0] &&)
    }

    %ip_hash{@ip[0]}++ if ( exists($ip_hash{@ip[0]}) $splitted[5] eq "ESTABLISHED");
}