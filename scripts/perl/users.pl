#!/usr/bin/env perl

# p5-JSON-RPC-1.06_1   Perl implementation of JSON-RPC 1.1 protocol
# https://www.freshports.org/devel/p5-JSON-RPC/

use 5.010;
use strict;
use warnings;
use JSON::RPC::Legacy::Client;
use Data::Dumper;

# Authenticate yourself
my $client = new JSON::RPC::Legacy::Client;
my $url = 'http://localhost/zabbix/api_jsonrpc.php';
my $authID;
my $response;

my $json = {
jsonrpc => "2.0",
method => "user.login",
params => {
user => "Admin",
password => "zabbix"
},
id => 1
};

$response = $client->call($url, $json);

# Check if response was successful
die "Authentication failed\n" unless $response->content->{'result'};

$authID = $response->content->{'result'};
print "Authentication successful. Auth ID: " . $authID . "\n";

# Get list of all hosts using authID

$json = {
jsonrpc=> '2.0',
method => 'user.get',
params =>
{
output => ['userid', 'alias', 'name', 'surname'],# get only user id and user name
sortfield => 'userid',        # sort by host userid
},
id => 2,
auth => "$authID",
};
$response = $client->call($url, $json);

# Check if response was successful
die "user.get failed\n" unless $response->content->{result};

print "List of users\n-----------------------------\n";
foreach my $user (@{$response->content->{result}}) {
print "User ID: ".$user->{userid}." Alias: ".$user->{alias}." Name: ".$user->{name}." Surname: ".$user->{surname}."\n";
}

# EOF
