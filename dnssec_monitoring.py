# Script de Verificação de Expiração DNSSEC
# Autor: Rodrigo Brito - rbritodo@akamai.com
# Data: July, 2023
# Repo: 

import sys
import datetime
import dns.query
import dns.resolver
from dateutil.parser import parse as date_parse
import time

def check_zone_expiration(zones, minimum_reporting=None):
    resolver = dns.resolver.Resolver()
    count = 0

    for zone in zones:
        try:
            q = dns.message.make_query(zone, dns.rdatatype.RRSIG)
            response = dns.query.tcp(q, resolver.nameservers[0])
            rrsig_rrset = response.answer[0]

            for rrsig_record in rrsig_rrset:
                expiration_date = datetime.datetime.utcfromtimestamp(rrsig_record.expiration).strftime('%Y-%m-%d %H:%M:%S')
                delta = date_parse(expiration_date) - datetime.datetime.now()

                if minimum_reporting is None or delta.total_seconds() <= minimum_reporting:
                    count += 1
                    print(f"{zone:<22.22s} will expire in {delta}")

        except dns.resolver.NXDOMAIN:
            print(f"Failed to query for RRSIGs for '{zone}'")
            print("This can happen because the authoritative server for the zone")
            print("or the local resolver doesn't support querying for RRSIGs")
        
        except ConnectionRefusedError as e:
            print(f"Connection refused error occurred: {e}")
            print(f"If you are using Akamai SIA, disable it to test it locally. Failure to retrieve DNS '{zone}'")

    if minimum_reporting is None and count > 0:
        sys.exit(1)

# Specify the zones for which you want to check expiration
zones = ["akamai.com"]

# Specify the minimum reporting time (in seconds) if desired
minimum_reporting = None

# Check zone expiration
check_zone_expiration(zones, minimum_reporting)

while True:
    # Check zone expiration
    check_zone_expiration(zones, minimum_reporting)

    # Pause for 1 minute
    time.sleep(60)
