my $i = 0;
until($i >= scalar @array) {
	print $i, ": ", $array[$i];
	$i++;
}